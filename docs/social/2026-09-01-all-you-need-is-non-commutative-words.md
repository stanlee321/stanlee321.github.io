# Social drafts — All You Need Is Non-Commutative Words

Source post: `_posts/2026-09-01-all-you-need-is-non-commutative-words.md` — <https://stanlee321.github.io/blog/2026/09/all-you-need-is-non-commutative-words/>
Status: DRAFT. Nothing here has been posted. For Stanley to paste.

Checked against `../editorial-policy.md`: credits present (Carla first author and
equal contributor, Renan for the 2010 decomposition); parity language only; the
physics sentence verbatim in the LinkedIn draft; every number on the allowed
list; no forbidden content; code link goes to the public MIT repo only.

---

## LinkedIn — long form

**Word count: 246** (body, excluding the link lines and hashtags).

---

Our paper is on arXiv: *All You Need Is Non-Commutative Words*.

The idea is small. Represent each word as a unitary matrix, and represent a
sentence as the ordered product of its words' matrices. Matrix multiplication
does not commute, so the product for "dog bites man" is not the product for "man
bites dog" — word order is carried by the algebra itself. There is no positional
encoding in the model, because there is nothing left for one to do.

The same algebra hands you things that normally need their own machinery:
self-attention with no query, key, or value projections; parallel composition of
variable-length chunks at reduced attention cost; a canonical-coset readout; and
continual learning by nested group extension, which enlarges the operator space
for a new task while preserving the earlier task's representations exactly.

On standard text-classification benchmarks the method matches bag-of-words
baselines — higher on IMDB through a learned per-word rotation budget,
comparable on AG News — and the QKV-free attention sits at parity with a matched
transformer. The result worth attention is the cost: a conventional
~30,000-dimensional vocabulary space replaced by a dense, 64-parameter
real-valued encoding.

This construction is inspired by the mathematics of quantum mechanics, but every
computation here is classical and we claim no quantum advantage.

Joint work with Carla M. Quispe Flores (Colorado School of Mines), first author
and my equal contributor, and Renan Cabrera, whose 2010 canonical-coset
decomposition of unitary matrices is the foundation the readout is built on.

Paper: https://arxiv.org/abs/2608.29314
Write-up: https://stanlee321.github.io/blog/2026/09/all-you-need-is-non-commutative-words/
Code (MIT): https://github.com/stanlee321/operator-transformer

#MachineLearning #NLP #Research

---

## X — thread of 6

**Every post counted below. All under 280.**

---

**1/** — 260 characters

```
1/ New paper: All You Need Is Non-Commutative Words.

Represent every word as a unitary matrix. Represent a sentence as the ordered product of its words.

Matrix product doesn't commute, so word order falls out of the algebra.

https://arxiv.org/abs/2608.29314
```

---

**2/** — 217 characters

```
2/ "dog bites man" and "man bites dog" are different products of the same three matrices.

That's the whole mechanism for word order. No positional encoding anywhere in the model — there is nothing left for one to do.
```

---

**3/** — 267 characters

```
3/ The same algebra gives you, for free:

- self-attention with no Q, K or V projections
- parallel composition of variable-length chunks at reduced cost
- a canonical-coset readout
- continual learning that enlarges the operator space and preserves old tasks exactly
```

---

**4/** — 273 characters

```
4/ Honest about what it does: on standard text-classification benchmarks it matches bag-of-words baselines, higher on IMDB via a learned per-word rotation budget, and the QKV-free attention is at parity with a matched transformer.

Parity, not a win. The cost is the story.
```

---

**5/** — 205 characters

```
5/ That cost: a ~30,000-dimensional vocabulary space replaced by a dense 64-parameter real-valued encoding.

Same benchmark numbers, far smaller parameterization. That expressive efficiency is the finding.
```

---

**6/** — 269 characters

```
6/ With Carla M. Quispe Flores (Colorado School of Mines), first author and equal contributor, and Renan Cabrera, whose 2010 canonical-coset decomposition this is built on.

Full write-up: https://stanlee321.github.io/blog/2026/09/all-you-need-is-non-commutative-words/
```

---

## Notes for Stanley

- The X thread deliberately does not use the word "quantum" at all, so the
  verbatim physics sentence is not required there. If you add any physics
  framing to a post, the sentence has to come with it — it will not fit in 280
  characters alongside anything else, so it would need its own post in the
  thread.
- The character counts above were measured on the literal text, URLs included at
  their full length. X counts every URL as 23 characters regardless of length
  (t.co wrapping), so the real counts for posts 1 and 6 are lower than shown.
  Measuring literally is the conservative direction.
- The credit originally sat in the same post as the write-up link and came to 318
  characters, over the limit. It is now split: post 5 carries the efficiency
  point, post 6 carries the credits and the link.
