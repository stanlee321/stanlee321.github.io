# Social drafts — All You Need Is Non-Commutative Words

Source post: `_posts/2026-09-01-all-you-need-is-non-commutative-words.md` — <https://stanlee321.github.io/blog/2026/09/all-you-need-is-non-commutative-words/>
Status: DRAFT. Nothing here has been posted. For Stanley to paste.

Checked against `../editorial-policy.md`: credits present (Carla first author and
equal contributor, Renan for the 2010 decomposition); parity language only; the
physics sentence verbatim in the LinkedIn draft; every number on the allowed
list; no forbidden content; code link goes to the public MIT repo only.

---

## LinkedIn — long form (Stanley's post, 2026-09-02, complements Carla's and Renan's)

Attach the cover figure (assets/img/sentence_path.png) as the image. Tag Carla and Renan with LinkedIn mentions.

Our paper is on arXiv: "All You Need Is Non-Commutative Words", with Carla M. Quispe Flores (co-first author) and Renan Cabrera, whose 2010 work on the canonical coset decomposition of unitary matrices is the mathematical foundation we built on.

The idea fits in one picture. Each word is a rotation in a different plane. A sentence applies those rotations in order. Rotations don't commute, so "not bad, quite good" and "not good, quite bad" trace different paths and end in different places, even though a bag-of-words model sees the same four words. The label is simply read off where you ended. No positional encodings, because the order is the path.

What the same algebra gives without extra machinery: self-attention with no query, key, or value projections, parallel composition of long documents in chunks, and continual learning that preserves earlier tasks exactly instead of approximately.

What it does not claim: on standard text classification we match bag-of-words baselines, higher on IMDB and comparable on AG News, while replacing a ~30,000-dimensional vocabulary space with 64 numbers per word. The construction is inspired by the mathematics of quantum mechanics, but every computation is classical and we claim no quantum advantage.

The engineer's part of the story: the whole experimental program ran on a desk machine and one workstation, from Bolivia, with a small team. The code is public under MIT, with the raw logs every table is rebuilt from, so anyone can check us.

Paper: https://arxiv.org/abs/2608.29314
Code: https://github.com/stanlee321/operator-transformer
Write-up: https://stanlee321.github.io/blog/2026/09/all-you-need-is-non-commutative-words/

#MachineLearning #NLP #GroupTheory #Bolivia

(~290 words)

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
