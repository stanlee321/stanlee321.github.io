# Editorial policy — stanlee321.github.io

**Status:** binding on every piece of public writing produced for or from this
repo — site pages, blog posts, image alt text and captions, `robots.txt`, commit
messages, and the social drafts in `docs/social/`.

**Not built.** This file lives in `docs/`, which is excluded from the Jekyll
build.

**Authority.** Stanley Salvatierra is the final authority. Nothing publishes
without his explicit OK. This policy tells you what you may draft; it never
substitutes for his approval on the specific text.

---

## 0. The one-sentence version

Publish only what is already public (the arXiv paper and the MIT repo), credit
Carla and Renan every time, claim parity and not victory, keep the physics
sentence verbatim, and when a document contains anything from the unpublished
program — stop and ask rather than editing it into shape.

---

## 1. Author credit

The paper is:

> **All You Need Is Non-Commutative Words**
> Carla M. Quispe Flores\*, Stanley Salvatierra\*, Renan Cabrera
> \*equal contribution
> arXiv:2608.29314 [cs.CL], listed 29 Aug 2026

**The rule.** Any public text that discusses this work names:

- **Carla M. Quispe Flores** (Colorado School of Mines) — **first author**, and
  **equal contributor** with Stanley. When authors are listed, the `*equal
  contribution` marker goes on both her name and Stanley's.
- **Renan Cabrera** — physicist, third author, and the author of the canonical
  coset decomposition the readout and continual-learning tower rest on:
  R. Cabrera, T. Strohecker and H. Rabitz, *The canonical coset decomposition of
  unitary matrices through Householder transformations*, **J. Math. Phys. 51**,
  082101 (2010), [doi:10.1063/1.3466798](https://doi.org/10.1063/1.3466798).

**This applies to social drafts too**, where the temptation to compress is
highest. A LinkedIn post or an X thread about the paper that does not name Carla
and Renan is not a compressed post; it is a wrong post.

**Never** frame the work as Stanley's solo project, and never use first-person
singular for a joint result ("I showed that…"). First person singular is fine
for Stanley's own reflections and framing; the results are "we" and "ours".

**Do not** invent affiliations, titles, or credentials beyond: Carla M. Quispe
Flores, Colorado School of Mines; Renan Cabrera, physicist.

---

## 2. Numbers

### 2.1 The allowed list

These are the only accuracy numbers that may appear publicly. They are
**three-seed best validation accuracy (%)**, on **10k-train / 2k-validation
subsets**, from the public repo's `docs/RESULTS.md`:

| Arm | IMDB | AG News |
|---|---:|---:|
| Predicted per-word epsilon | 86.53 | 87.68 |
| Global epsilon | 85.28 | 87.45 |
| Bag-of-words reference | 85.25 | 87.45 |
| QKV-free operator attention | 84.4 | 87.1 |
| Matched transformer | 84.6 | 84.5 |

The complete allowed set:

```
{86.53, 87.68, 85.28, 87.45, 85.25, 84.4, 87.1, 84.6, 84.5}
```

Also publishable, because they are in the abstract: the conventional
**~30,000-dimensional** vocabulary space, and the **64-parameter** real-valued
encoding that replaces it.

### 2.2 Anything else needs a public source or Stanley's OK

A **public source** is exactly one of:

- the arXiv abstract (verbatim text in §5),
- the arXiv PDF (<https://arxiv.org/pdf/2608.29314>),
- the public MIT repository <https://github.com/stanlee321/operator-transformer>
  — specifically its `README.md` and `docs/RESULTS.md`.

If a number is not on the allowed list and not in one of those, **it does not go
public**. This includes numbers that feel harmless: parameter counts, training
times, epoch counts, dataset sizes other than the 10k/2k subsets, speedups,
seeds, losses, deltas. Ask Stanley. He may know it is public; you may not assume.

### 2.3 How to state numbers

- **Always carry the conditions.** "86.53% on IMDB" without "three seeds, 10k
  train / 2k validation" is a misleading number. State the conditions in the
  table header, a caption, or the sentence.
- **Do not round, re-derive, or aggregate.** Do not compute an average of the
  allowed numbers, a delta between them, or a percentage improvement — a derived
  number is a new number and is not on the list.
- **Do not re-order the comparison to flatter.** Present the bag-of-words
  reference alongside the method every time results appear.

---

## 3. Claim discipline

### 3.1 The licensed claim

From the abstract: *"Across standard text-classification benchmarks, the method
matches or exceeds bag-of-words baselines. Achieving higher accuracy on IMDB and
comparable performance on AG News."*

In practice, the two things you may say:

- The method **matches** bag-of-words baselines, **exceeding** them on IMDB —
  and that exceedance comes specifically from the **learned per-word rotation
  budget** (per-word epsilon), not from the operator representation alone.
- The QKV-free attention is **at parity with** a matched transformer.

### 3.2 The framing that matters

The headline is **expressive efficiency**, not the leaderboard: the same
benchmark numbers out of a dense, 64-parameter real-valued encoding instead of a
~30,000-dimensional vocabulary space, and word order carried by the algebra with
no positional encoding at all. Lead with the mechanism and the cost. A post that
leads with a table is a post that invites the wrong comparison.

### 3.3 Banned phrasings

Never write, in any register, including social drafts:

- "beats transformers", "outperforms transformers", "better than attention"
- "state of the art", "SOTA", "new record", "breakthrough"
- "replaces the transformer", "the end of positional encodings"
- "quantum speedup", "quantum advantage", "quantum NLP", "quantum model"
- any superlative about the method's performance

Prefer: "matches", "comparable to", "at parity with", "without needing", "at a
reduced cost".

### 3.4 Say the limitation

Where results appear, the scope appears with them: text classification
benchmarks, subsets of 10k train / 2k validation, three seeds. Do not imply
results at scale, on generation, on other modalities, or on anything the paper
does not report.

---

## 4. The physics sentence

Whenever the physics framing is mentioned publicly, include this sentence,
**byte-for-byte**:

> This construction is inspired by the mathematics of quantum mechanics, but
> every computation here is classical and we claim no quantum advantage.

Rules:

- Verbatim. No paraphrase, no truncation, no splitting across paragraphs, no
  "(see the paper)".
- It is the **only** licensed appearance of the word "quantum" on this site.
  Not in a title, tagline, heading, tag, alt text, filename, or social hook.
- If you mention unitary matrices, Hermitian generators, the exponential map, or
  anything that reads as physics, the sentence belongs in that document.

---

## 5. Verbatim texts

Do not retype these from memory. Copy them, and diff before shipping.

### 5.1 Abstract

> We represent lexical tokens as unitary matrices and encode each sentence as
> their ordered product. The noncommutativity of matrix product captures word
> order without positional encodings (PEs). The same algebra yields several
> capabilities, including antisymmetric self-attention that requires no query,
> key, or value projections, and the parallel composition of variable-length
> text chunks at a reduced attention cost. Furthermore, it provides a
> canonical-coset readout layer that intrinsically encodes all true unitary
> degrees of freedom compactly, while supporting continual learning through
> nested group extensions that enlarge the operator space with each new task
> while preserving prior representations exactly. Across standard
> text-classification benchmarks, the method matches or exceeds bag-of-words
> baselines. Achieving higher accuracy on IMDB and comparable performance on AG
> News. Notably, this is accomplished by replacing the conventional
> ~30,000-dimensional vocabulary space with a dense, 64-parameter real-valued
> encoding, highlighting the expressive efficiency of our parameterization.

### 5.2 Figure 1 caption

> Capturing word order natively: every word is a unitary matrix, and a sentence
> is their ordered product; because these matrices do not commute, the resulting
> document state P_L carries word order without positional encoding (PE). A
> flattened readout and a single linear head then produce the label.

### 5.3 BibTeX

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

### 5.4 Links

- Abstract: <https://arxiv.org/abs/2608.29314>
- PDF: <https://arxiv.org/pdf/2608.29314>
- Code (MIT): <https://github.com/stanlee321/operator-transformer>
- GitHub: <https://github.com/stanlee321>
- X: <https://x.com/iamatachyon> (@iamatachyon)
- Deep Microsystems (company site currently offline — do not link until it resolves)
- Cabrera 2010 DOI: <https://doi.org/10.1063/1.3466798>

---

## 6. FORBIDDEN CONTENT

**This is a hard line, not a guideline.** None of the following appears in any
public artifact — page, post, asset, caption, alt text, filename, HTML comment,
commit message, or social draft.

### 6.1 Unpublished work

Nothing about the research program beyond the arXiv paper and the public MIT
code repository. **The test is: is it in the arXiv paper or the public repo? If
not, it is not public.** That covers topics, results, methods in progress,
plans, collaborators' unpublished ideas, and compute or infrastructure details.
This policy deliberately does not enumerate them: an itemized list of what must
not be said is itself a disclosure, and this repository is public.

### 6.2 Internal labels and vocabulary

No experiment codes, arm or run names, internal program vocabulary, or file,
script, and module names from private work. If a phrase would only make sense
to someone who has read the private notes, it does not go public.

### 6.3 Private repositories

No private repository is named, linked, or pathed publicly. **Code links go
only to <https://github.com/stanlee321/operator-transformer>.**

### 6.4 Private correspondence

No WhatsApp messages, no email quotes, no DMs, no paraphrases of private
conversations with Carla, Renan, or anyone else. Do not attribute an opinion,
reaction, or idea to a collaborator from a private channel — even a flattering
one. If a collaborator's view belongs in a post, Stanley gets it cleared with
them first.

### 6.5 Secrets and identifiers

No email addresses (including Stanley's own — the site publishes no email), no
tokens, credentials, or API keys, no hostnames, no tunnel URLs (ngrok or
otherwise), no absolute local filesystem paths (`/Users/...`), no internal IPs
or ports.

### 6.6 The rule when a document is dirty

If a document you were asked to publish contains forbidden content:

1. **Do not publish it.**
2. **Do not edit it into compliance and publish the result.** Scrubbing the
   labels off a document whose *substance* is unpublished work produces a leak
   with the labels removed. If the preregistration framing, the internal
   comparison structure, or the unrun-experiment scaffolding is the document's
   spine, renaming things does not fix it.
3. **Report** the exact strings and their locations to Stanley, and let him
   decide.
4. If the underlying idea is genuinely worth having publicly, the correct move
   is to **author a fresh public page from paper-scoped material** — not to
   sanitize the internal one.

This has already come up once: the internal coset explainer was staged and then
withheld for exactly these reasons. See `log.md`.

---

## 7. Style

- **Voice.** First person, plain, specific. Stanley's own voice for reflection;
  "we" for the paper's results.
- **Sentences.** Short. One idea each. Prefer the concrete noun to the abstract
  one.
- **No hype.** No "revolutionary", "game-changing", "insane", "wild", "🚀". No
  emoji anywhere on the site.
- **No AI tells.** No "delve", "leverage" as a verb, "in today's rapidly
  evolving landscape", "it's important to note that", or a bulleted list where a
  sentence would do. Do not open a post with a rhetorical question.
- **Explain the mechanism.** A reader should finish a post knowing how the thing
  works, not just that it exists.
- **Say the limitation before the reader finds it.** It is the cheapest
  credibility available.
- **Language: English only** for now. Spanish is deferred — no translation
  layer, no `lang` variants, no switcher until Stanley asks.

---

## 8. Facts of record

Use these; do not invent around them.

- **Person:** Stanley Salvatierra. Electrical engineer; machine learning
  researcher and engineer. Based in Bolivia.
- **Company:** Deep Microsystems (site currently offline; do not link).
- **GitHub motto (public):** "Solve the problem of intelligence, solve everything
  else!"
- **Public tech list:** PyTorch, Node, Go, gRPC, Kubernetes, Flutter/React, AWS.
- **LinkedIn:** URL unknown. The placeholder `TODO-LINKEDIN-URL` lives in exactly
  one config value, `linkedin_url` in `_config.yml`. Do not scatter it.
- **Email:** publish none.

---

## 9. The gate

Before anything is presented as ready, run the review gate in `../CLAUDE.md` §7:
lint, forbidden-strings grep, number audit, credit check, verbatim diff, link
check, OG tags, build status, and Stanley's explicit OK.

Report honestly what you verified and what you could not. Never claim a build
you did not run.
