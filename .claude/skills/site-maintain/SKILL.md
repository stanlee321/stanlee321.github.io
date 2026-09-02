---
name: site-maintain
description: Maintain and administer Stanley Salvatierra's public personal site + blog (stanlee321.github.io, GitHub-native Jekyll) and his GitHub profile README. Invoke with /site-maintain for any request over this repo — NEW-POST (write a post from a source + derive the LinkedIn/X drafts), UPDATE-PAGE (home/publications/projects), ADD-PUBLICATION, REVIEW (run the full pre-publish gate), PUBLISH (commit → push → wait for the Pages build → live check → screenshot), FIX-BUILD (diagnose a failed or wrong build), PROFILE-README (keep stanlee321/stanlee321 in sync), DOMAIN (the deferred salvatierra.io steps), and ORIENT (cold-start read order). Integrity-first — this repo is PUBLIC, only paper-scoped material ships, Carla and Renan are credited on every paper mention, and NOTHING is committed or pushed without Stanley's explicit OK.
---

# /site-maintain — operating the public site

Repo: `stanlee321/stanlee321.github.io` (PUBLIC). Live: <https://stanlee321.github.io>.
Profile README repo: `stanlee321/stanlee321` (PUBLIC; README.md + LICENSE only).
Stanley Salvatierra is the final authority. **Nothing publishes without his explicit
OK** — "publish", "push", "go" in his own words. Drafting, linting, and local commits
he asked for are fine; pushing is the gate.

## 0. ORIENT (do this first, every session)

Read in this order, chunked (≤300 lines per read; grep first):
1. `CLAUDE.md` — authority, layout, build rules, editorial policy summary, post
   template, social workflow, review gate.
2. `docs/editorial-policy.md` — the binding policy for every public sentence.
3. `docs/log.md` (tail) — what happened last; open items.
4. `docs/index.md` — current state + standing hazards.
Then `git status -sb` and `git log --oneline -5`. If `.forbidden-terms` is missing
(it is gitignored on purpose), ask Stanley for it before any REVIEW or PUBLISH.

## 1. The four rules that never bend

1. **Public-scope test.** Is it in the arXiv paper (arXiv:2608.29314) or the public
   MIT repo (github.com/stanlee321/operator-transformer)? If not, it is not public.
   This repo is public too: `exclude:` in `_config.yml` keeps a file out of the
   BUILT SITE, not out of the repo. Never commit an itemized list of what must not
   be said; the term regex lives only in gitignored `.forbidden-terms`.
2. **Credit.** Carla M. Quispe Flores (first author, equal contribution) and Renan
   Cabrera on every paper mention. Parity language: the method *matches*
   bag-of-words, exceeds it on IMDB only via the learned per-word epsilon. The
   only licensed "quantum" is the verbatim sentence in the policy.
3. **Only pinned facts.** Biography, affiliations, numbers: from `CLAUDE.md` §4.2 and
   the policy's pinned-facts section. No invented anecdotes about who did what.
4. **Propose, then act.** Show the diff or the draft; commit locally only if asked;
   push only on Stanley's OK. Social drafts go to `docs/social/` — never posted.

## 2. Playbooks

### NEW-POST
1. Source: what Stanley hands you (a paper section, a public repo doc, his notes).
   Run the public-scope test on the SOURCE before writing a word.
2. Copy `docs/post-template.md` → `_posts/YYYY-MM-DD-slug.md`. Front matter:
   `layout: post`, `title`, `date`, `description` (≤160 chars, becomes the social
   card), `tags`, `image` (absolute site path; the card image).
3. Math: `$...$` inline, `$$...$$` on its own line for display. **Never write `}}`**
   inside LaTeX (Liquid reads it as a tag) — use `} }` or restructure. kramdown
   emits block math as `\[ \]` and inline as `\( \)`; KaTeX in `_layouts/default.html`
   handles `$`, `$$`, `\[ \]`, `\( \)` — keep all four delimiters if you touch it.
4. Images → `assets/img/`; reference with `{{ '/assets/img/x.png' | relative_url }}`
   or a plain `<img src="/assets/img/x.png">`. Wide tables inside
   `<div class="table-scroll" markdown="1">`.
5. Derive social drafts → `docs/social/<slug>.md` per `docs/social/README.md`
   (LinkedIn 150–250 words + X thread 4–6 posts ≤280 chars each, counts written in).
6. REVIEW (below). Log it in `docs/log.md`. Hand Stanley the post path + drafts.

### UPDATE-PAGE / ADD-PUBLICATION
- Home = `index.md`; publications = `publications.md` (entry + BibTeX; keep the
  Cabrera 2010 reference line); projects = `projects.md` (placeholder until Stanley
  curates). New non-public directories MUST be added to `exclude:` in the same edit.
- New link targets: verify they resolve (`curl -sS -o /dev/null -w '%{http_code}'`).
  A dead site is named, not linked (Deep Microsystems is currently unlinked for this
  reason; LinkedIn has no URL yet — do not ship placeholders).

### REVIEW (the pre-publish gate; all five, every time)
```bash
python3 scripts/site_lint.py .                       # front matter, Liquid balance, links, plugins, config VALUES
grep -rniE -f .forbidden-terms --exclude-dir=.git --exclude=.forbidden-terms .   # ALL tracked files; policy phrasing only is acceptable
grep -rn -i quantum . --exclude-dir=.git | grep -v "claim no quantum advantage"  # hits must be policy text only
ruby -ryaml -e 'p YAML.load_file("_config.yml")'    # typed values (null is nil, not "nil")
git status --short                                   # only the files you meant; .forbidden-terms never staged
```
Then read the rendered markdown once as a reader: credit present, numbers on the
allowed list, no promises about future results, description + image in front matter.

### PUBLISH (only after Stanley's OK)
```bash
git add <explicit paths>            # never `git add -A`
git commit -m "<what changed>"      # add the attribution trailer your harness requires
git push
scripts/pages_build_wait.sh $(git rev-parse --short HEAD)   # BUILT / ERRORED / TIMEOUT
scripts/live_check.sh               # 200s, excluded 404s, og tags, served-content sweep
```
Then a headless screenshot for visual QA (macOS):
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1200,2400 --screenshot=<scratch>/page.png <url>`
Look at it. Raw TeX, overflow, missing figure, broken nav = FIX-BUILD. Append the
outcome to `docs/log.md` and push that too (or fold it into the next commit).

### FIX-BUILD
- Build ERRORED: `gh api repos/stanlee321/stanlee321.github.io/pages/builds/latest`
  shows the message. Usual causes: `}}` in markdown; a Ruby-ism in YAML (`nil`);
  a plugin off the whitelist; a layout name that does not exist.
- Build fine but page wrong: math raw → delimiters (see NEW-POST §3); page missing →
  front matter or `exclude:`; card missing → `description`/`image` front matter;
  private file served → it was never in `exclude:` (and re-check it should even be
  in the repo).
- Never disable a check to make it pass; fix the content.

### PROFILE-README
`stanlee321/stanlee321` holds only `README.md` + `LICENSE`. Keep its "Latest paper"
block and links in sync with `publications.md` and `index.md`. Same policy, same
review, same OK before push. Do not add badges that point to workflows (there are
none). Its stale `gh-pages` branch (2020 test blog) is Stanley's call to delete.

### DOMAIN (deferred)
`docs/setup.md` §4 has the `salvatierra.io` steps (DNS + `CNAME` file). Do nothing
until Stanley says so; then follow it exactly and verify HTTPS after propagation.

## 3. Hazards learned the hard way (keep this list honest, append when bitten)
- `math_engine: nil` in YAML is the STRING "nil" → kramdown rejects it → build fails.
  Use `null`. The lint now checks typed values.
- `exclude:` ≠ private. The maintainer docs once enumerated unpublished lines; the
  audit caught it before push. Categorical rules only; term list gitignored.
- One invented attribution sentence made it into a draft. Only pinned facts.
- kramdown block math renders as `\[ \]`; KaTeX must list those delimiters.
- Deleting Dependabot branches on the profile repo auto-closes their PRs and emails
  "won't notify again" — normal, not an error.

## 4. Where things are
```
_config.yml  _layouts/{default,page,post}.html  assets/css/style.css  assets/img/
index.md  blog/index.md  _posts/  publications.md  projects.md  404.md  robots.txt
CLAUDE.md  docs/{index,editorial-policy,post-template,setup,log}.md  docs/social/
scripts/{site_lint.py,pages_build_wait.sh,live_check.sh}   .claude/skills/site-maintain/
.forbidden-terms (gitignored)   _site/ .jekyll-cache/ (gitignored)
```
Jekyll ignores dot-directories, so `.claude/` never ships; keep it that way.
