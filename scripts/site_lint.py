#!/usr/bin/env python3
"""Structural lint for a GitHub-Pages-native Jekyll site.

(a) parse every front matter block as YAML
(b) check {% %} / {{ }} balance in every .html/.md
(c) list every relative link/asset referenced and confirm the file exists
(d) confirm _config.yml plugins are a subset of the GitHub Pages whitelist
"""
import os, re, sys, json

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
ROOT = os.path.abspath(ROOT)

try:
    import yaml
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

GH_PAGES_PLUGINS = {
    "jekyll-coffeescript", "jekyll-default-layout", "jekyll-gist",
    "jekyll-github-metadata", "jekyll-optional-front-matter", "jekyll-paginate",
    "jekyll-readme-index", "jekyll-titles-from-headings", "jekyll-relative-links",
    "jekyll-seo-tag", "jekyll-feed", "jekyll-sitemap", "jekyll-avatar",
    "jekyll-mentions", "jekyll-redirect-from", "jemoji",
}

errors, warnings, notes = [], [], []

def rel(p): return os.path.relpath(p, ROOT)

# ---------- collect files ----------
SKIP_DIRS = {".git", "_site", ".jekyll-cache", ".sass-cache", "scratch", "node_modules", ".claude"}

# Honour _config.yml's `exclude:` list. Files Jekyll does not build must not be
# linted as if they were site content -- CLAUDE.md and docs/ deliberately quote
# forbidden Liquid (`}}`) and placeholder asset paths in order to document them.
EXCLUDED_DIRS, EXCLUDED_FILES = set(), set()
_cfg_path = os.path.join(ROOT, "_config.yml")
if os.path.exists(_cfg_path):
    _raw = open(_cfg_path, encoding="utf-8").read()
    _m = re.search(r"^exclude:\s*$((?:\n[ \t]*-[ \t]*.*)+)", _raw, re.M)
    if _m:
        for _line in _m.group(1).strip().splitlines():
            _e = _line.strip().lstrip("-").strip().strip('"').strip("'")
            if not _e:
                continue
            if _e.endswith("/"):
                EXCLUDED_DIRS.add(_e.rstrip("/"))
            else:
                EXCLUDED_FILES.add(_e)

def is_excluded(path):
    r = rel(path).replace(os.sep, "/")
    if r in EXCLUDED_FILES:
        return True
    return any(r == d or r.startswith(d + "/") for d in EXCLUDED_DIRS)

files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames
                   if d not in SKIP_DIRS
                   and not is_excluded(os.path.join(dirpath, d))]
    for fn in filenames:
        p = os.path.join(dirpath, fn)
        if is_excluded(p):
            continue
        files.append(p)

content_files = [f for f in files if f.endswith((".md", ".html"))]

# ---------- strict fallback front-matter parser ----------
def strict_parse(block, where):
    """Very small strict YAML subset check: key: value / nested / list items."""
    ok = True
    for i, line in enumerate(block.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            continue
        if stripped in (">-", "|", ">"):
            continue
        if re.match(r"^[A-Za-z0-9_.\-\"']+\s*:(\s|$)", stripped):
            continue
        # continuation of a folded scalar
        if line.startswith(("  ", "\t")):
            continue
        errors.append(f"[front-matter] {where}:{i}: unparseable line: {stripped!r}")
        ok = False
    return ok

# ---------- (a) front matter ----------
fm_count = 0
for f in content_files:
    with open(f, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    if not text.startswith("---"):
        notes.append(f"[front-matter] {rel(f)}: no front matter (static file, not processed by Jekyll)")
        continue
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not m:
        errors.append(f"[front-matter] {rel(f)}: opening '---' with no closing '---'")
        continue
    fm_count += 1
    block = m.group(1)
    if HAVE_YAML:
        try:
            data = yaml.safe_load(block)
            if data is not None and not isinstance(data, dict):
                errors.append(f"[front-matter] {rel(f)}: front matter is not a mapping ({type(data).__name__})")
        except Exception as e:
            errors.append(f"[front-matter] {rel(f)}: YAML error: {e}")
    else:
        strict_parse(block, rel(f))

# ---------- (b) liquid balance ----------
def liquid_balance(text, where):
    local = []
    # raw delimiter counts
    if text.count("{%") != text.count("%}"):
        local.append(f"[liquid] {where}: unbalanced tag delimiters {{% ={text.count('{%')} %}} ={text.count('%}')}")
    # {{ }} — count non-overlapping
    if text.count("{{") != text.count("}}"):
        local.append(f"[liquid] {where}: unbalanced output delimiters {{{{ ={text.count('{{')} }}}} ={text.count('}}')}")
    # block tag nesting
    BLOCKS = {"if": "endif", "unless": "endunless", "for": "endfor",
              "case": "endcase", "capture": "endcapture", "raw": "endraw",
              "comment": "endcomment", "tablerow": "endtablerow", "highlight": "endhighlight"}
    ENDS = set(BLOCKS.values())
    stack = []
    for m in re.finditer(r"\{%-?\s*(\w+)", text):
        tag = m.group(1)
        if tag in BLOCKS:
            stack.append((tag, m.start()))
        elif tag in ENDS:
            if not stack:
                local.append(f"[liquid] {where}: stray '{tag}' with no opening block")
            else:
                open_tag, _ = stack.pop()
                if BLOCKS[open_tag] != tag:
                    local.append(f"[liquid] {where}: '{tag}' closes '{open_tag}' (expected '{BLOCKS[open_tag]}')")
    for open_tag, pos in stack:
        line = text[:pos].count("\n") + 1
        local.append(f"[liquid] {where}:{line}: unclosed '{{% {open_tag} %}}'")
    return local

for f in content_files:
    with open(f, encoding="utf-8", errors="replace") as fh:
        errors.extend(liquid_balance(fh.read(), rel(f)))

# ---------- (c) relative links / assets ----------
# Known Jekyll-generated outputs that exist only after a build.
GENERATED = {"/feed.xml", "/sitemap.xml", "/robots.txt", "/404.html"}
# Pages declared via permalink front matter.
permalinks = {}
for f in content_files:
    with open(f, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        continue
    pm = re.search(r"^permalink:\s*(.+?)\s*$", m.group(1), re.M)
    if pm:
        permalinks[pm.group(1).strip().strip('"\'')] = rel(f)

link_rows = []
# href/src attributes, and markdown links
patterns = [
    r'(?:href|src)\s*=\s*"([^"]+)"',
    r'(?:href|src)\s*=\s*\'([^\']+)\'',
    r'\]\(\s*([^)]+?)\s*\)',
]
for f in content_files:
    with open(f, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    seen = set()
    for pat in patterns:
        for m in re.finditer(pat, text):
            raw = m.group(1).strip()
            if raw in seen:
                continue
            seen.add(raw)
            if re.match(r"^(https?:|mailto:|data:|#|//|\{\{\s*site\.(url|linkedin))", raw):
                continue
            # Liquid-wrapped internal path: {{ '/x' | relative_url }}
            lm = re.match(r"^\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*(relative_url|absolute_url)", raw)
            if lm:
                target = lm.group(1)
            elif raw.startswith("{{") or raw.startswith("{%"):
                continue  # dynamic (post.url etc.) — cannot resolve statically
            else:
                target = raw
            target = target.split("#")[0].split("?")[0]
            if not target:
                continue
            status = None
            if not target.startswith("/"):
                status = "SKIP(relative-to-page)"
            elif target in GENERATED:
                status = "OK(jekyll-generated)"
            elif target in permalinks:
                status = f"OK(permalink -> {permalinks[target]})"
            else:
                fs = os.path.join(ROOT, target.lstrip("/"))
                if os.path.exists(fs):
                    status = "OK(file)"
                elif os.path.exists(fs.rstrip("/") + ".md") or os.path.exists(fs.rstrip("/") + ".html"):
                    status = "OK(file)"
                else:
                    status = "MISSING"
                    errors.append(f"[link] {rel(f)}: '{target}' does not resolve to a file or permalink")
            link_rows.append((rel(f), target, status))

# ---------- (d) plugins whitelist ----------
cfg_path = os.path.join(ROOT, "_config.yml")
cfg = None
if not os.path.exists(cfg_path):
    errors.append("[config] _config.yml is missing")
else:
    with open(cfg_path, encoding="utf-8") as fh:
        cfg_text = fh.read()
    if HAVE_YAML:
        try:
            cfg = yaml.safe_load(cfg_text)
        except Exception as e:
            errors.append(f"[config] _config.yml YAML error: {e}")
    plugins = []
    if isinstance(cfg, dict):
        plugins = cfg.get("plugins") or cfg.get("gems") or []
    else:
        m = re.search(r"^plugins:\s*\n((?:\s*-\s*\S+\n?)+)", cfg_text, re.M)
        if m:
            plugins = [l.strip("- \n") for l in m.group(1).splitlines() if l.strip()]
    for p in plugins:
        if p not in GH_PAGES_PLUGINS:
            errors.append(f"[config] plugin '{p}' is NOT on the GitHub Pages whitelist")
    notes.append(f"[config] plugins declared: {plugins}")
    if isinstance(cfg, dict):
        for key in ("title", "url", "baseurl", "markdown", "permalink"):
            if key not in cfg:
                warnings.append(f"[config] missing recommended key '{key}'")
        km = (cfg.get("kramdown") or {}) if isinstance(cfg, dict) else {}
        me = km.get("math_engine", None)
        if isinstance(me, str) and me.strip().lower() in ("nil", "none", "null", "true", "false"):
            errors.append(f"[config] kramdown.math_engine is the STRING {me!r} — use a real YAML null (null / ~ / empty), not a Ruby-ism")
        elif me not in (None, "mathjax", "katex", "sskatex", "mathjaxnode", "itex2mml", "ritex"):
            errors.append(f"[config] kramdown.math_engine {me!r} is not a known engine")
        if km.get("input") not in (None, "GFM", "kramdown", "markdown"):
            errors.append(f"[config] kramdown.input {km.get('input')!r} is not a known parser")
        if cfg.get("markdown") != "kramdown":
            errors.append(f"[config] markdown must be 'kramdown' for GitHub Pages, got {cfg.get('markdown')!r}")

# ---------- report ----------
print("=" * 72)
print(f"SITE LINT  {ROOT}")
print(f"PyYAML: {'yes (real YAML parse)' if HAVE_YAML else 'NO (strict fallback parser)'}")
print("=" * 72)

print(f"\n(a) FRONT MATTER — {fm_count} block(s) parsed")
for n in notes:
    if n.startswith("[front-matter]"):
        print("    " + n)

print(f"\n(b) LIQUID BALANCE — {len(content_files)} .md/.html file(s) checked")
liq = [e for e in errors if e.startswith("[liquid]")]
print("    " + ("no imbalance found" if not liq else f"{len(liq)} problem(s)"))
for e in liq:
    print("    " + e)

print(f"\n(c) INTERNAL LINKS / ASSETS — {len(link_rows)} reference(s)")
for src, target, status in sorted(link_rows):
    flag = "!!" if status == "MISSING" else "  "
    print(f"  {flag} {src:24s} {target:44s} {status}")

print("\n(d) PLUGINS vs GITHUB PAGES WHITELIST")
for n in notes:
    if n.startswith("[config]"):
        print("    " + n)
cfg_err = [e for e in errors if e.startswith("[config]")]
print("    " + ("all declared plugins are whitelisted" if not cfg_err else f"{len(cfg_err)} problem(s)"))
for e in cfg_err:
    print("    " + e)

print("\n" + "=" * 72)
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings:
        print("  - " + w)
print(f"ERRORS: {len(errors)}")
for e in errors:
    print("  - " + e)
print("RESULT:", "PASS" if not errors else "FAIL")
print("=" * 72)
sys.exit(1 if errors else 0)
