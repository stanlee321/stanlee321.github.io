# Post template

Copy the block in §2 into `_posts/YYYY-MM-DD-slug.md` and fill it in.
Not built — this file lives in `docs/`.

Before you write a word, read `editorial-policy.md`. Before you finish, run the
review gate in `../CLAUDE.md` §7.

---

## 1. Front matter fields

| Field | Required | Notes |
|---|---|---|
| `layout` | yes | Always `post`. |
| `title` | yes | In quotes. Title case. No emoji, no "quantum", no hype. |
| `date` | yes | `YYYY-MM-DD`. Must match the filename date, which sets the permalink. |
| `description` | yes | One sentence, **≤ 160 characters**. Used three ways: the excerpt on `/blog/`, the excerpt on the home page, and the `og:description` / twitter-card description. |
| `tags` | optional | Lowercase, hyphenated, few. Reuse existing tags — `paper`, `operator-algebra`, `nlp` — rather than inventing near-duplicates. |
| `image` | optional, preferred | `/assets/img/NAME.png`. The social-card image. A post without one gets a bare text card when shared. |

Permalink is `/blog/:year/:month/:title/` — set by `permalink:` in `_config.yml`.
Changing a post's filename date changes its URL and breaks any existing link.

---

## 2. The template

Copy from here down.

```markdown
---
layout: post
title: "Your Title Here"
date: 2026-09-01
description: "One sentence under 160 characters that says what this post is. Shows on the blog index and in the social card."
tags: [tag-one, tag-two]
image: /assets/img/your-image.png
---

Open with what this is, in the first paragraph, with the links inline. If this
is about the paper, credit **Carla M. Quispe Flores** (Colorado School of Mines,
first author and equal contributor) and **Renan Cabrera** (whose 2010
canonical-coset decomposition the readout is built on) right here — not in a
footer.

## The idea in one line

A display equation, then a short plain-language unpacking of every symbol in it.

$$ A \;\longrightarrow\; B \;\longrightarrow\; C $$

Then a paragraph that says what the equation means to someone who did not read
the paper. Name each symbol. Do not leave a variable unexplained.

<figure>
  <img src="{{ '/assets/img/your-image.png' | relative_url }}" alt="A real description of what the figure shows, for a reader who cannot see it.">
  <figcaption>The verbatim caption from the paper, if this is a paper figure.</figcaption>
</figure>

## What it gives you

- **A consequence.** One or two sentences on the mechanism, not the vibe.
- **Another consequence.** Same.
- **A third.** Keep the list short; four bullets is usually the ceiling.

This construction is inspired by the mathematics of quantum mechanics, but every
computation here is classical and we claim no quantum advantage.

## What it does and does not claim

Mandatory on any post that quotes results. Be precise, use the parity language
from the editorial policy, and state the limitation before the reader finds it.

Best validation accuracy (%), three seeds, on 10k-train / 2k-validation subsets:

<div class="table-scroll" markdown="1">

| Configuration | IMDB | AG News |
|---|---:|---:|
| Predicted per-word epsilon | 86.53 | 87.68 |
| Bag-of-words reference | 85.25 | 87.45 |

</div>

Then a sentence saying what the result actually is — the efficiency, the
mechanism — rather than letting the table imply a leaderboard win.

## How to cite

```bibtex
@article{quispeflores2026noncommutative,
  title   = {All You Need Is Non-Commutative Words},
  author  = {Quispe Flores, Carla M. and Salvatierra, Stanley and Cabrera, Renan},
  journal = {arXiv preprint arXiv:2608.29314},
  year    = {2026},
  eprint  = {2608.29314},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url     = {https://arxiv.org/abs/2608.29314}
}
```

One closing line. Do not promise a specific future post with a date.
```

---

## 3. Structure that works

From the announcement post, which is the reference implementation:

1. **Lede** — what this is, links inline, credits if it is a paper post.
2. **The idea in one line** — display equation, then the unpacking.
3. **Figure** — `<figure>` with a real `alt` and the verbatim caption.
4. **What it gives you** — short bulleted list of consequences.
5. **What it does and does not claim** — parity language, physics sentence,
   numbers table. Mandatory when results appear.
6. **How to cite** — BibTeX.
7. **Close** — one line.

---

## 4. Mechanics

### The Liquid / LaTeX hazard

Liquid parses `}}` as the end of an output tag. If `}}` appears anywhere in the
markdown — **including inside LaTeX** — the build breaks. This has already
happened once on this site.

```
BAD:   $U_{\text{dog bites man}}$      the trailing }} kills the build
GOOD:  $U_\text{dog bites man}$        single brace
GOOD:  {% raw %}$U_{{\rm x}}${% endraw %}
```

Check before finishing:

```bash
grep -n '}}' _posts/*.md | grep -v relative_url    # must return nothing
```

### Math

`$...$` inline, `$$...$$` display. KaTeX auto-render is wired up in
`_layouts/default.html`; kramdown is set to `math_engine: null` (a YAML null, never the string `nil`) so the LaTeX
passes through untouched. Nothing to configure per-post.

### Images

Put files in `assets/img/`. Reference them as:

```liquid
{{ '/assets/img/NAME.png' | relative_url }}
```

Always use `relative_url` — the linter resolves asset paths through it, and a
bare path will break if a baseurl is ever set. Every image needs a real `alt`.

### Tables

Wrap every markdown table:

```html
<div class="table-scroll" markdown="1">

| A | B |
|---|--:|
| 1 | 2 |

</div>
```

`markdown="1"` is what makes kramdown parse the table inside the div. The blank
lines around the table are required. `.table-scroll` gives it horizontal
overflow so it scrolls on mobile instead of blowing out the page width.

### CSS hooks

`.table-scroll`, `.post-list`, `.post-link`, `.excerpt`, `.tag`, `.muted`,
`figure` / `figcaption`.
CSS variables: `--bg --fg --muted --accent --border --code-bg --measure`.

### New pages (not posts)

A `.md` at the repo root with `layout: page`, `title:`, and `permalink: /slug/`.
**The nav does not update itself** — add the link by hand in
`_layouts/default.html`.

---

## 5. After the post

1. Derive the social drafts into `docs/social/<post-slug>.md` — a LinkedIn
   long-form of ~150–250 words and an X thread of 4–6 posts. See
   `social/README.md`. **You never post them.**
2. Append an entry to `log.md`.
3. Run the review gate in `../CLAUDE.md` §7.
4. Show Stanley the diff and wait for his explicit OK. Do not commit, do not
   push.
