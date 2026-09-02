# CLAUDE.md — maintainer guide for stanlee321.github.io

You are the delegated maintainer of Stanley Salvatierra's public personal site.
Read this file end to end before you touch anything. It is excluded from the
Jekyll build, so it never ships.

---

> **Project skill:** `/site-maintain` (`.claude/skills/site-maintain/SKILL.md`) is
> the step-by-step playbook for every routine request on this repo — read it after
> this file. Helper scripts: `scripts/site_lint.py`, `scripts/pages_build_wait.sh`,
> `scripts/live_check.sh`.

## 1. Purpose and authority

**What this repo is.** The public personal site and blog of Stanley Salvatierra
(electrical engineer; machine learning researcher and engineer; based in
Bolivia; builds at Deep Microsystems). It carries: a short home page, a blog, a
publications page, a projects page. It is served by GitHub Pages at
<https://stanlee321.github.io>.

**Who decides.** Stanley is the final authority on every word that goes public.

> **Nothing publishes without Stanley's explicit OK.**
> You may write, edit, lint, and stage. You may not `git commit`, `git push`,
> `gh repo create`, `gh repo edit`, or change repository settings on your own
> initiative. Prepare the change, run the review gate, show him the diff, and
> wait. "He asked me to write a post" is not consent to publish the post.

**What you own.** Drafting and maintenance: writing posts, keeping pages
accurate, keeping links alive, keeping the build green, deriving social drafts,
and keeping `docs/` current. When in doubt about whether something is publishable,
the answer is: ask, and default to not publishing.

---

## 2. Repo layout

```
stanlee321.github.io/
├── _config.yml          # Jekyll config. Site metadata, plugins, permalinks, exclude list.
├── _layouts/
│   ├── default.html     # Shell: head, KaTeX, nav, footer. Edit nav HERE by hand.
│   ├── page.html        # Static pages.
│   └── post.html        # Posts: date, reading time, tags, share links, prev/next.
├── _posts/              # YYYY-MM-DD-slug.md — one file per post.
├── blog/index.md        # The /blog/ index (lists all posts).
├── index.md             # Home page, permalink /
├── publications.md      # /publications/
├── projects.md          # /projects/
├── 404.md
├── robots.txt
├── assets/
│   ├── css/style.css    # The whole theme. ~230 lines, no framework, CSS variables.
│   └── img/             # Images. Reference with the relative_url filter.
├── scripts/
│   └── site_lint.py     # Structural linter. Run before every review gate.
├── docs/                # The wiki. NOT built. See docs/index.md.
├── CLAUDE.md            # This file. NOT built.
└── README.md            # Human-facing repo readme. NOT built.
```

`CLAUDE.md`, `docs/`, `README.md`, and `scripts/` are all in the `exclude:` list
in `_config.yml`. If you add another non-public directory, **add it to `exclude:`
in the same edit** — otherwise Jekyll will publish it.

---

## 3. How this site builds (GitHub-native Jekyll)

This site is built by GitHub Pages' own Jekyll. There is **no GitHub Actions
workflow**, no Gemfile, no Node, no build step, and there must never be one.
That is a deliberate constraint: the site has to survive years of neglect.

**Rules that follow from it:**

- **Plugins:** only ones on the GitHub Pages whitelist. Currently
  `jekyll-seo-tag`, `jekyll-feed`, `jekyll-sitemap`. Do not add anything else
  without checking the whitelist first — a non-whitelisted plugin is silently
  ignored and the page renders wrong.
- **No `remote_theme`, no custom theme gem.** The theme is the three layouts
  plus `assets/css/style.css`, hand-written, in-repo.
- **Markdown is kramdown** with `math_engine: null` (a real YAML null — the string `nil` breaks the build), so LaTeX passes through
  untouched to KaTeX in the browser.
- **If you add a `Gemfile` at all** it must contain exactly the `github-pages`
  gem and nothing else. Preferably do not add one.

### How to preview

Local Jekyll is not installed on Stanley's machine and Docker is usually down.
Two options, in order of preference:

1. **Push a branch and read the Pages build result.** (Requires Stanley — see
   §1.) A failed build shows up in the repo's Actions/Pages tab with the
   kramdown or Liquid error and the line number. This is the only *real* check.
2. **`docker run --rm -v "$PWD":/srv/jekyll -p 4000:4000 jekyll/jekyll:4 jekyll serve`**
   — only if Docker is already running. Do not start Docker yourself.

**When you cannot build, say so.** Run `scripts/site_lint.py`, report exactly
what it checked, and mark the live build as *deferred to human*. Never claim or
imply that you rendered a page you did not render.

---

## 4. EDITORIAL POLICY

The full policy lives in `docs/editorial-policy.md`. This section is the
operative summary; where the two differ, the full policy is authoritative and
you should fix the discrepancy.

### 4.1 Author credit — non-negotiable

Every post, page, or social draft that discusses the paper **must** credit:

- **Carla M. Quispe Flores** (Colorado School of Mines) — **first author**, and
  an **equal contributor** with Stanley. Both are marked `*equal contribution`.
- **Renan Cabrera** — physicist; author of the 2010 canonical-coset
  decomposition (Cabrera, Strohecker & Rabitz, *J. Math. Phys.* **51**, 082101
  (2010), doi:10.1063/1.3466798) that the readout and the continual-learning
  tower are built on.

Never write about this work as if it were Stanley's alone. A post that mentions
the paper and omits Carla or Renan does not pass the review gate.

### 4.2 Numbers — the allowed list

Only these accuracy numbers may appear on the public site. They are three-seed
best validation accuracy (%) on 10k-train / 2k-validation subsets:

| Arm | IMDB | AG News |
|---|---:|---:|
| Predicted per-word epsilon | 86.53 | 87.68 |
| Global epsilon | 85.28 | 87.45 |
| Bag-of-words reference | 85.25 | 87.45 |
| QKV-free operator attention | 84.4 | 87.1 |
| Matched transformer | 84.6 | 84.5 |

The complete allowed set is `{86.53, 87.68, 85.28, 87.45, 85.25, 84.4, 87.1,
84.6, 84.5}`.

**Anything else needs a public source or Stanley's OK.** A "public source" means
the arXiv abstract, the arXiv PDF, or the public MIT repo
<https://github.com/stanlee321/operator-transformer> (its `README.md` and
`docs/RESULTS.md`). If a number is not in one of those and not on the list
above, you may not publish it — not in a post, not in a caption, not in a social
draft, not rounded, not "approximately".

Always state the conditions with the numbers (three seeds, 10k/2k subsets). A
number without its conditions is a misleading number.

### 4.3 Parity language

The licensed claim, and the only claim:

- The method **matches or exceeds bag-of-words baselines** — higher accuracy on
  IMDB (via the learned per-word rotation budget), comparable on AG News.
- The QKV-free attention is **at parity with** a matched transformer.

Use "matches", "comparable", "at parity with". **Never** write "beats
transformers", "outperforms transformers", "state of the art", "SOTA", "better
than attention", or any variant. The interesting result is the *expressive
efficiency* — the same benchmark numbers out of a dense 64-parameter real-valued
encoding instead of a ~30,000-dimensional vocabulary space. Lead with that, not
with a leaderboard framing.

### 4.4 The physics sentence

Whenever the physics framing is mentioned anywhere public, include this
sentence **verbatim**:

> This construction is inspired by the mathematics of quantum mechanics, but
> every computation here is classical and we claim no quantum advantage.

Do not paraphrase it, do not shorten it, do not split it. Do not use the word
"quantum" anywhere else on the site — not in a title, not in a tagline, not in a
tag, not in a social draft. Its only licensed appearance is inside that sentence.

### 4.5 FORBIDDEN CONTENT — hard line

None of the following may appear anywhere public (site pages, posts, assets,
commit messages, social drafts, alt text, filenames, HTML comments). Note that
**this repository itself is public**: `exclude:` in `_config.yml` only keeps a
file out of the *built site*; it does not keep it private. Anything committed
here is readable by anyone, so the rules below apply to every file in the repo,
including this one and `docs/`.

- **Anything about the research program beyond the arXiv paper and the public
  MIT code repository.** The test is one question: *is it in the paper or in
  the public repo?* If not, it is not public — no topic names, no results, no
  roadmap, no infrastructure, no compute details, not even as a list of things
  not to mention.
- **Internal labels of any kind** — experiment codes, arm or run names, internal
  program vocabulary, file paths, script or module names from private work.
- **Any number not on the allowed list** in §4.2.
- **Private repositories** — no names, links, or paths. Code links go **only** to
  <https://github.com/stanlee321/operator-transformer>.
- **Private correspondence** — no quotes or paraphrases of messages from
  collaborators, and nothing said to Stanley in confidence.
- **Any email address** (including Stanley's), any token, credential, API key,
  hostname, tunnel URL, or absolute local filesystem path.
- **Overclaims beyond the abstract** — see §4.3.

If a document you were asked to publish contains any of the above, **do not
edit it into compliance and ship it**. Stop, report the exact strings and
locations to Stanley, and let him decide. Scrubbing labels off a document whose
*substance* is unpublished work is not a fix — it is a leak with the labels
removed. When a piece of internal writing would be genuinely useful publicly,
the correct move is to author a fresh public page from paper-scoped material.

The concrete term list used by the review-gate grep lives in `.forbidden-terms`,
which is **gitignored on purpose** (it is itself an index of what must not be
said). Ask Stanley for it if it is missing; never commit it, and never paste its
contents into any tracked file.

### 4.6 Language

English only for now. Spanish is deferred; do not add a translation layer,
`lang` variants, or a language switcher until Stanley asks.

---

## 5. POST TEMPLATE

The canonical template with commentary is `docs/post-template.md`. Copy it and
fill it in. Summary:

**File:** `_posts/YYYY-MM-DD-slug.md`. The date in the filename sets the
permalink, which is `/blog/:year/:month/:title/`.

**Front matter:**

```yaml
---
layout: post
title: "Title In Sentence Or Title Case"
date: 2026-09-01
description: "One sentence, <= 160 characters. Doubles as the list excerpt AND the og/twitter description."
tags: [paper, operator-algebra, nlp]
image: /assets/img/some-image.png   # optional; the social card image
---
```

- `description` is required. It is what shows on `/blog/`, on the home page, and
  in the social card. Keep it under 160 characters or it gets truncated in the
  card.
- `image` is optional but strongly preferred — a post with no image gets a bare
  text card when shared.
- `tags` are lowercase, hyphenated, few. Reuse existing tags rather than
  inventing near-duplicates.

**Structure that works** (from the announcement post):

1. **The lede** — what this is, in the first paragraph, with the links (arXiv
   abs, PDF, code) inline. Credit Carla and Renan here if it is a paper post.
2. **The idea in one line** — a display equation plus a short plain-language
   unpacking of each symbol.
3. **A figure**, if there is one, in a `<figure>` with a real `alt` and the
   verbatim caption in `<figcaption>`.
4. **What it gives you** — a short bulleted list of consequences.
5. **What it does and does not claim** — the parity language, the physics
   sentence, and the numbers table. *This section is mandatory on any post that
   quotes results.*
6. **How to cite** — the BibTeX block.
7. A one-line close. Do not promise a specific future post with a date.

**Writing voice.** First person, plain, specific. Short sentences. No hype
adjectives, no "revolutionary", no "game-changing", no emoji. State the
limitation before the reader finds it. Explain the mechanism, not the vibe.

### The Liquid / LaTeX hazard — read this before writing math

Liquid parses `}}` as the end of an output tag. If `}}` appears anywhere in your
markdown — including inside LaTeX — **the build breaks**. This has already
happened once on this site.

```
BAD:   $U_{\text{dog bites man}}$      <- the }} at the end kills the build
GOOD:  $U_\text{dog bites man}$        <- single brace
GOOD:  {% raw %}$U_{{\rm x}}${% endraw %}
```

Before finishing any post: `grep -n '}}' _posts/*.md | grep -v relative_url`
must return nothing. Math delimiters `$` and `$$` are wired to KaTeX
auto-render in `_layouts/default.html`.

### Other mechanics

- **Images:** put them in `assets/img/`, reference as
  `{{ '/assets/img/NAME.png' | relative_url }}`. Always use `relative_url` —
  the linter resolves paths through it.
- **Tables:** wrap every markdown table in
  `<div class="table-scroll" markdown="1">` … `</div>` so it scrolls on mobile
  instead of blowing out the page width. The `markdown="1"` attribute is what
  makes kramdown parse the table inside the div.
- **CSS hooks available:** `.table-scroll`, `.post-list`, `.post-link`,
  `.excerpt`, `.tag`, `.muted`, `figure` / `figcaption`.
- **CSS variables:** `--bg --fg --muted --accent --border --code-bg --measure`.
- **New pages:** a `.md` at the repo root with `layout: page`, `title:`, and
  `permalink: /slug/`. **The nav does not update itself** — add the link by hand
  in `_layouts/default.html`.

---

## 6. SOCIAL WORKFLOW

For every post, derive two social drafts and save them for Stanley. **You never
post anything anywhere.** You write the text; he pastes it.

**Where:** `docs/social/<post-slug>.md`, where `<post-slug>` is the post's
filename without `.md` (e.g. `2026-09-01-all-you-need-is-non-commutative-words.md`).

**What goes in the file:**

1. **A LinkedIn long-form post, ~150–250 words.** Prose, no hashtag spam (two or
   three at most, at the end). Opens with the finding, not with "Excited to
   announce". Credits Carla as first author and equal contributor and Renan for
   the 2010 decomposition. Links the arXiv abstract and the site post. Includes
   the parity language. Includes the physics sentence verbatim if physics is
   mentioned.
2. **An X thread, 4–6 posts.** Each numbered `1/`, `2/` … Each under 280
   characters — **count them and write the count next to each**. Post 1 is the
   hook and carries the arXiv link. One post credits Carla and Renan by name.
   One post carries the honest-claims framing (parity, not a win). The last post
   links the site write-up. No thread-bait ("a thread 🧵", "buckle up").

The **entire editorial policy in §4 applies to social drafts verbatim** — same
allowed numbers, same forbidden content, same credit rule, same parity language.
A social draft is public writing that happens to be staged in a private file.

Mark the file with a header saying it is a draft for Stanley to paste, and that
nothing in it has been posted.

---

## 7. REVIEW GATE

Run this checklist before you tell Stanley anything is ready. Report each item
as pass/fail with the evidence, and report honestly what you could not check.

1. **Lint.** `python3 scripts/site_lint.py .` from the repo root — front matter
   parses, Liquid tags balance, every internal link and asset path resolves,
   plugins are whitelisted. It exits non-zero on failure.
   *Use a python that has PyYAML.* Without PyYAML the script silently falls back
   to a weaker parser; on Stanley's machine the anaconda python has it.
2. **Forbidden-strings grep.** Over EVERY tracked file (this repo is public,
   so `docs/` and `CLAUDE.md` count too). The pattern file is gitignored:

   ```bash
   grep -rniE -f .forbidden-terms --exclude-dir=.git --exclude=.forbidden-terms .
   ```

   Expected: no hits. Then check `quantum` separately — every hit must be inside
   the verbatim physics sentence and nowhere else.
3. **Numbers.** Enumerate every number in published prose and check it against
   the allowed list in §4.2:

   ```bash
   grep -rnoE --include='*.md' '[0-9]{2}\.[0-9]{1,2}' . | grep -v '^./docs/'
   ```

   Anything outside the allowed set must be a version number, a DOI, or an arXiv
   id — verify each one by eye, do not assume.
4. **Credits.** Any post or page mentioning the paper names Carla M. Quispe
   Flores (first author, equal contribution) and Renan Cabrera.
5. **Verbatim text.** The abstract, the Figure 1 caption, the physics sentence,
   and every BibTeX field are byte-identical to the pinned versions. Do not
   retype them from memory; diff them.
6. **Links resolve.** Internal links pass the linter. External links (arXiv,
   the DOI, the code repo, x.com/iamatachyon) should be
   opened or fetched if you have network access; if you cannot, say so.
7. **OG / SEO tags.** The post has `description` and, where it should, `image`.
   `{% seo %}` and `{% feed_meta %}` are present in `_layouts/default.html`.
8. **Build.** Either the Pages build is green, or you state plainly that the
   build was **not run** and is deferred to a human.
9. **Stanley's OK.** Obtained, explicitly, for this specific change. Until then
   nothing is committed and nothing is pushed.

---

## 8. The wiki

`docs/` is the maintainer's wiki and is excluded from the build.

- `docs/index.md` — the hub. Start there.
- `docs/editorial-policy.md` — the full editorial policy (§4 above is a summary).
- `docs/post-template.md` — the copy-paste post template.
- `docs/social/README.md` — the social workflow, plus the derived drafts.
- `docs/log.md` — the running log. **Append an entry for every meaningful
  change**, newest last, dated, one to three lines.
- `docs/setup.md` — how to enable GitHub Pages for this repo, and the deferred
  custom-domain (salvatierra.io) steps.

Keep the wiki current as you work. A change that is not in `docs/log.md` is a
change the next agent will not know about.
