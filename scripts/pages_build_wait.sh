#!/usr/bin/env bash
# Wait for the latest GitHub Pages build of this repo and report its result.
# Usage: scripts/pages_build_wait.sh [expected-commit-sha-prefix] [max-seconds]
# Exit 0 on "built", 1 on "errored", 2 on timeout. Needs `gh` authenticated.
set -u
REPO="${PAGES_REPO:-stanlee321/stanlee321.github.io}"
WANT="${1:-}"; MAX="${2:-420}"; t=0
while [ "$t" -lt "$MAX" ]; do
  j=$(gh api "repos/$REPO/pages/builds/latest" 2>/dev/null) || { sleep 10; t=$((t+10)); continue; }
  st=$(printf '%s' "$j" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d.get("status"))')
  sha=$(printf '%s' "$j" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d.get("commit") or "")')
  if [ -n "$WANT" ] && [ "${sha#"$WANT"}" = "$sha" ]; then sleep 10; t=$((t+10)); continue; fi
  case "$st" in
    built)   printf '%s' "$j" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(f"BUILT commit={d[\"commit\"]} duration={d[\"duration\"]}ms")'; exit 0;;
    errored) printf '%s' "$j" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(f"ERRORED commit={d[\"commit\"]} error={(d.get(\"error\") or {}).get(\"message\")}")'; exit 1;;
  esac
  sleep 10; t=$((t+10))
done
echo "TIMEOUT after ${MAX}s (last status: ${st:-none})"; exit 2
