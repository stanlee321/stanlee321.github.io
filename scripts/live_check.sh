#!/usr/bin/env bash
# Smoke-check the LIVE site: public pages must be 200, excluded files must be 404,
# the newest post must carry social-card tags, and no forbidden term may be served.
# Usage: scripts/live_check.sh [base-url]     (default https://stanlee321.github.io)
set -u
BASE="${1:-https://stanlee321.github.io}"; fail=0
code() { curl -sS -o /dev/null -w '%{http_code}' -m 20 "$1"; }
for u in / /blog/ /publications/ /projects/ /feed.xml /sitemap.xml /404.html; do
  c=$(code "$BASE$u"); [ "$c" = 200 ] || { echo "FAIL $u -> $c"; fail=1; }; echo "ok   $u -> $c"
done
for u in /CLAUDE.md /README.md /docs/index.md /scripts/site_lint.py /.claude/skills/site-maintain/SKILL.md /.forbidden-terms; do
  c=$(code "$BASE$u"); [ "$c" = 404 ] || { echo "FAIL (must be 404) $u -> $c"; fail=1; }; echo "ok   $u -> $c (excluded)"
done
# newest post from the local _posts/ dir -> its permalink /blog/YYYY/MM/slug/
newest=$(ls _posts/*.md 2>/dev/null | sort | tail -1)
if [ -n "$newest" ]; then
  b=$(basename "$newest" .md); y=${b:0:4}; m=${b:5:2}; slug=${b:11}
  url="$BASE/blog/$y/$m/$slug/"; c=$(code "$url"); echo "post $url -> $c"; [ "$c" = 200 ] || fail=1
  html=$(curl -sS -m 20 "$url")
  for tag in 'property="og:title"' 'property="og:image"' 'property="og:description"' 'name="twitter:card"'; do
    printf '%s' "$html" | grep -q "$tag" && echo "ok   $tag" || { echo "FAIL missing $tag"; fail=1; }
  done
  if [ -f .forbidden-terms ]; then
    hits=$(printf '%s' "$html" | grep -ciE -f .forbidden-terms || true)
    [ "$hits" = 0 ] && echo "ok   no forbidden terms served" || { echo "FAIL forbidden terms served: $hits line(s)"; fail=1; }
  else
    echo "warn .forbidden-terms missing — served-content sweep skipped (ask Stanley for the file)"
  fi
fi
[ $fail = 0 ] && echo "LIVE CHECK PASS" || echo "LIVE CHECK FAIL"; exit $fail
