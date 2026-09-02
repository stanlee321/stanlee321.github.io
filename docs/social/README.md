# Social drafts

**Nothing in this directory has been posted anywhere. Nothing in it will be.**

These are drafts for Stanley to read, edit, and paste himself. The maintainer
agent writes the text; Stanley decides whether it goes out and pushes the
button. Not built — `docs/` is excluded from the Jekyll build.

---

## The workflow

For every published post, derive two drafts and save them in one file:

```
docs/social/<post-slug>.md
```

where `<post-slug>` is the post's filename without the `.md` extension — e.g.
`_posts/2026-09-01-all-you-need-is-non-commutative-words.md` becomes
`docs/social/2026-09-01-all-you-need-is-non-commutative-words.md`.

Do this **after** the post passes the review gate, not before. If the post
changes, the drafts change with it.

---

## What goes in the file

### 1. A LinkedIn long-form post, ~150–250 words

- Prose, not a bulleted list. LinkedIn's first two lines are the hook that
  shows before "see more" — put the finding there.
- **Do not** open with "Excited to announce" or "Thrilled to share". Open with
  what the thing is.
- Credits **Carla M. Quispe Flores** as first author and equal contributor, and
  **Renan Cabrera** for the 2010 canonical-coset decomposition.
- Links the **arXiv abstract** and the **site post**.
- Carries the parity language — matches bag-of-words, exceeds on IMDB via the
  learned per-word rotation budget, at parity with a matched transformer.
- Carries the **physics sentence verbatim** if physics is mentioned.
- Two or three hashtags at the end, at most. No hashtag spam.

### 2. An X thread, 4–6 posts

- Number them `1/`, `2/`, … `n/`.
- **Each post must be under 280 characters, and you write the count next to
  each one.** Count it; do not estimate.
- Post 1 is the hook and carries the arXiv link.
- One post credits Carla and Renan by name.
- One post carries the honest-claims framing — parity, not a win.
- The last post links the site write-up.
- No thread-bait: no "a thread 🧵", no "buckle up", no "you won't believe".
- No emoji.

---

## The policy applies here in full

`../editorial-policy.md` binds these drafts exactly as it binds the site itself.
A social draft is public writing that happens to be staged in a private file,
and it is the format where compression pressure is highest — which is precisely
where the credit rule and the parity language get dropped by accident.

Specifically, in a social draft you still may not:

- omit Carla or Renan,
- publish a number outside the allowed list in `../editorial-policy.md` §2.1,
- say "beats transformers", "SOTA", or any superlative,
- use the word "quantum" outside the verbatim physics sentence,
- mention any unpublished follow-up work, experiment code, or arm name,
- link or name the private repository.

---

## File header convention

Start every draft file with:

```markdown
# Social drafts — <post title>

Source post: `_posts/<slug>.md` — <https://stanlee321.github.io/blog/YYYY/MM/slug/>
Status: DRAFT. Nothing here has been posted. For Stanley to paste.
```
