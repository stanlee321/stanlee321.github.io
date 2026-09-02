# Site wiki — stanlee321.github.io

The maintainer's hub for this repo. **Not built** — `docs/` is in the `exclude:`
list in `_config.yml`, so nothing here ships to the public site.

Start with `../CLAUDE.md` (the maintainer-agent guide). This wiki holds the
long-form versions of what that file summarizes.

---

## What this site is

The public personal site and blog of **Stanley Salvatierra** — electrical
engineer, machine learning researcher and engineer, based in Bolivia; builds at
Deep Microsystems. Served by GitHub Pages at
<https://stanlee321.github.io>.

**Stanley is the final authority on everything public. Nothing publishes without
his explicit OK.**

---

## Read order

1. **`../CLAUDE.md`** — the operating guide: authority, layout, build rules,
   editorial policy summary, post template, social workflow, review gate.
2. **`editorial-policy.md`** — the full policy. Author credit, the allowed
   numbers, parity language, the physics sentence, the forbidden-content list.
   **This is the document that binds every piece of public writing.**
3. **`post-template.md`** — copy this to start a post.
4. **`social/README.md`** — how post → LinkedIn draft + X thread works, and
   where the drafts live.
5. **`log.md`** — what has happened to this site, newest last.
6. **`setup.md`** — enabling GitHub Pages; the deferred custom domain.

---

## The stack, in one paragraph

GitHub-native Jekyll. No GitHub Actions, no Gemfile, no Node, no build step.
Markdown is kramdown with `math_engine: nil`; math renders client-side via KaTeX
loaded in `_layouts/default.html`. Plugins are limited to the GitHub Pages
whitelist — currently `jekyll-seo-tag`, `jekyll-feed`, `jekyll-sitemap`. The
theme is hand-written: three layouts plus `assets/css/style.css` (~230 lines, no
framework, CSS-variable light/dark). The constraint is deliberate: this site
should still build in five years with nobody maintaining a toolchain.

---

## Current state

- Pages: `/` (home), `/blog/`, `/publications/`, `/projects/`, `/404.html`.
- Posts: one — the paper announcement, `2026-09-01-all-you-need-is-non-commutative-words`.
- The paper: *All You Need Is Non-Commutative Words*, Carla M. Quispe Flores\*,
  Stanley Salvatierra\*, Renan Cabrera (\*equal contribution).
  arXiv:2608.29314 [cs.CL], listed 29 Aug 2026.
  Code (MIT): <https://github.com/stanlee321/operator-transformer>.

## Known open items

- `linkedin_url` in `_config.yml` is the literal placeholder `TODO-LINKEDIN-URL`,
  and `index.md` renders it as visible text. It must be replaced before or
  immediately after launch.
- `projects.md` is a placeholder; a real curated list is owed.
- The site has one post, so `/blog/` is a one-item list and post prev/next nav
  renders empty.
- No Jekyll build has ever been run locally (no local Jekyll, Docker down). The
  first real build will be the GitHub Pages build. See `setup.md`.
- Custom domain `salvatierra.io` is deferred; steps are written down in
  `setup.md`.

## Standing hazards

- **`}}` in markdown breaks the build.** Liquid reads it as an output tag. This
  has already bitten this repo once, in LaTeX. See the hazard section in
  `../CLAUDE.md` §5.
- **A new non-public directory must be added to `exclude:` in the same edit**,
  or Jekyll publishes it.
- **A non-whitelisted plugin fails silently** — the page just renders wrong.
