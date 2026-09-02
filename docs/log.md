# Log

Running record of what has happened to this site. Newest **last**. One to three
lines per entry, dated. Append an entry for every meaningful change — a change
that is not logged is a change the next maintainer will not know about.

Not built (`docs/` is excluded).

---

## 2026-09-01 — Site created

Scaffolded the GitHub-native Jekyll site from scratch at `stanlee321.github.io`.
`git init -b main`, **nothing committed** — publishing is Stanley's call.

**Stack.** No GitHub Actions, no Gemfile, no Node, no build step. kramdown with
`math_engine: null` (a YAML null — the string `nil` breaks kramdown); KaTeX 0.16.9 from cdnjs renders math client-side. Plugins
limited to the GitHub Pages whitelist: `jekyll-seo-tag`, `jekyll-feed`,
`jekyll-sitemap`. Hand-written theme — three layouts plus `assets/css/style.css`
(~230 lines, no framework, CSS-variable light/dark, 720px measure).

**Shipped.** Pages `/` (home), `/blog/`, `/publications/`, `/projects/`,
`/404.html`, plus `robots.txt`. One post: the paper announcement, dated
2026-09-01, at `/blog/2026/09/all-you-need-is-non-commutative-words/`. Figure 1
copied to `assets/img/main_model.png`.

**Governance added.** `CLAUDE.md` (maintainer guide), this wiki
(`docs/index.md`, `editorial-policy.md`, `post-template.md`, `social/`,
`log.md`, `setup.md`), `README.md`, and `scripts/site_lint.py`. All five paths
are in the `exclude:` list in `_config.yml` so none of them ship.

**Social drafts** derived for the announcement post into
`docs/social/2026-09-01-all-you-need-is-non-commutative-words.md` — a LinkedIn
long-form and a 6-post X thread. Nothing posted; they are for Stanley to paste.

### Decisions worth remembering

- **The internal coset explainer was withheld.** It was staged for publication
  and then not shipped: it contains internal experiment codes, internal arm
  names, preregistration framing for unrun experiments, internal program
  vocabulary, and a private attribution. Scrubbing the labels would not have
  fixed it, because that framing is the document's spine. If a public coset
  explainer is wanted, it must be **authored fresh from paper-scoped material**.
  See `editorial-policy.md` §6.6.
- **`}}` broke the build once**, inside LaTeX (`$U_{\text{...}}$`). Liquid reads
  `}}` as an output tag. Rewritten to single-brace form. This is now a standing
  hazard note in `CLAUDE.md` §5 and `post-template.md` §4.
- **`publications.md` carries no numbers and no figure.** Both live in the post
  instead. Deliberate, so there is one place where results are stated with their
  conditions.
- The announcement post was originally dated 2026-08-29 to match the arXiv
  listing, then moved to 2026-09-01. The 08-29 permalink never went public, so
  nothing links it.

### Open at the end of the day

- LinkedIn: no URL yet. The placeholder was REMOVED from `_config.yml`,
  `index.md`, and the profile README rather than shipped; add `linkedin_url`
  and the bullets back when Stanley supplies it.
- Deep Microsystems: the company site does not resolve (DNS), so it is named
  but not linked anywhere. Re-link when it is live.
- `projects.md` is a three-line placeholder; a curated list is owed.
- One post only, so `/blog/` is a one-item list and post prev/next nav renders
  empty.
- **No Jekyll build has ever been run.** Local Jekyll is not installed and
  Docker was down. Verification to date is structural only — the linter, the
  forbidden-strings grep, byte-diffs of the verbatim texts. The first real build
  will be GitHub's. See `setup.md`.
- Nothing committed, no remote configured. A human must commit, point the repo,
  and enable Pages.

## 2026-09-01 — Hand-back after the adversarial audit (FIX_NEEDED → fixed)

Five audit lenses ran over the build. Fixed by hand in the main thread:

- **`math_engine: nil` → `null`.** Ruby's YAML reads `nil` as the string
  `"nil"`, which kramdown rejects; would have failed the first Pages build.
  `scripts/site_lint.py` now checks option VALUES (typed null / known engine),
  and its markdown-image regex was broadened so `![]({{ ... | relative_url }})`
  is checked.
- **Governance files were an itemized index of unpublished work.** This repo is
  public, so `exclude:` does not make a file private. §4.5 of `CLAUDE.md` and
  §6.1–6.3 of the editorial policy were rewritten as categorical rules (the
  one-question test) with no topic list; the review-gate term regex moved to
  `.forbidden-terms`, which is gitignored. `setup.md` no longer says
  `git add -A`.
- **One invented sentence** about who did what on the paper was deleted from the
  announcement post. Only pinned, sourced facts remain.
- Provenance wording softened ("the raw logs the result tables are rebuilt
  from"); the post's table note says the bag-of-words row is the paper's
  reference baseline. Math blocks got an overflow rule in the CSS.
- Gates re-run clean: lint PASS (0 errors); the term sweep over ALL files finds
  only policy phrasings; `quantum` appears only in the verbatim sentence and in
  policy text.

## 2026-09-01 — Published + first build fix

Repo `stanlee321/stanlee321.github.io` created (public), Pages enabled from
`main` root; first build succeeded (40 s). Live check: all pages 200, excluded
files 404, og/twitter tags present. One rendering defect found in the live
post: kramdown emits block math as `\[ … \]` (and inline as `\( … \)`) when
`math_engine` is null, and the KaTeX auto-render config only listed `$`
delimiters, so the pipeline formula showed raw TeX. Fixed by adding the
`\[ \]` and `\( \)` delimiters in `_layouts/default.html`.
