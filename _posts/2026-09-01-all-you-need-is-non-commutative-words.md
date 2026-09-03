---
layout: post
title: "All You Need Is Non-Commutative Words"
date: 2026-09-01
description: "Our paper is on arXiv: words as unitary matrices and sentences as their ordered product, so word order comes from the algebra instead of a positional encoding."
tags: [paper, operator-algebra, nlp]
image: /assets/img/sentence_path.png
---

Our paper is on arXiv: [**All You Need Is Non-Commutative Words**](https://arxiv.org/abs/2608.29314) — [abstract](https://arxiv.org/abs/2608.29314) · [PDF](https://arxiv.org/pdf/2608.29314) · [code (MIT)](https://github.com/stanlee321/operator-transformer). It is joint work with **Carla M. Quispe Flores** (Colorado School of Mines), who is first author and my equal contributor on it, and **Renan Cabrera**, whose 2010 canonical-coset decomposition of unitary matrices is the mathematical foundation the readout and the continual-learning tower are built on. arXiv:2608.29314 [cs.CL], listed 29 Aug 2026.

<figure>
<img src="/assets/img/sentence_path.png" alt="Words are rotations. A sentence is a path.">
<figcaption>Each word is a rotation in a different plane; a sentence applies them in order. The same words in a different order trace a different path and end somewhere else.</figcaption>
</figure>

## The idea in one line

Every token becomes a Hermitian generator, exponentiating that generator gives a unitary word operator, and a sentence is the ordered product of its word operators:

$$\text{token } w \;\longrightarrow\; H_w \;\longrightarrow\; U_w = \exp(i\,\varepsilon_w H_w) \;\longrightarrow\; P_L = U_L \cdots U_1 \;\longrightarrow\; \text{readout}$$

Each word $w$ carries a small set of real coordinates that assemble into a Hermitian generator $H_w$. The word operator is $U_w = \exp(i\,\varepsilon_w H_w)$, where $\varepsilon_w$ is a rotation budget — how far this particular word is allowed to turn the state. The document state is the ordered product $P_L = U_L \cdots U_1$, and a flattened readout plus a single linear head produces the label.

Matrix multiplication does not commute, so the product for *dog bites man* is not the product for *man bites dog*. Word order is carried by the algebra itself. There is no positional encoding anywhere in the model, because there is nothing left for one to do.

<figure>
  <img src="{{ '/assets/img/main_model.png' | relative_url }}" alt="Diagram of the model: each word becomes a unitary matrix, a sentence is their ordered product, and a flattened readout plus a linear head produces the label.">
  <figcaption>Capturing word order natively: every word is a unitary matrix, and a sentence is their ordered product; because these matrices do not commute, the resulting document state P_L carries word order without positional encoding (PE). A flattened readout and a single linear head then produce the label.</figcaption>
</figure>

## What the same algebra gives for free

The part I find most interesting is that once you commit to this representation, several things that normally need their own machinery fall out of the same algebra:

- **Self-attention with no Q, K, or V projections.** The antisymmetric score between two positions is read directly off their operators, so the three projection matrices that every attention block carries simply are not there.
- **Parallel composition of variable-length chunks.** Because a product of products is still a product, chunks of text compose in parallel, at a reduced attention cost.
- **A canonical-coset readout.** The document state has redundant coordinates when you flatten it naively. The coset chart encodes all the true unitary degrees of freedom compactly instead.
- **Exact continual learning by nested group extension.** A new task enlarges the operator space rather than overwriting it — $U(n) \subset U(n+k)$ — so the earlier task's representations are preserved exactly, not approximately.

This construction is inspired by the mathematics of quantum mechanics, but every computation here is classical and we claim no quantum advantage.

## What it does and does not claim

I want to be precise here, because this is the easiest thing in the world to oversell. Across standard text-classification benchmarks the method **matches** bag-of-words baselines; it achieves higher accuracy on IMDB, through the learned per-word rotation budget, and comparable performance on AG News. The QKV-free attention sits at parity with a matched transformer. That is the claim, and there is nothing beyond it.

Best validation accuracy (%), three-seed means, on 10k-train / 2k-validation subsets. The bag-of-words row is the reference baseline reported in the paper; the other rows are reconstructed from the raw logs in the public repository:

<div class="table-scroll" markdown="1">

| Configuration | IMDB | AG News |
|---|---:|---:|
| Predicted per-word epsilon | 86.53 | 87.68 |
| Global epsilon | 85.28 | 87.45 |
| Bag-of-words reference | 85.25 | 87.45 |
| QKV-free operator attention | 84.4 | 87.1 |
| Matched transformer | 84.6 | 84.5 |

</div>

The result worth attention is not the accuracy column but what it costs to get there. A conventional vocabulary space of roughly 30,000 dimensions is replaced by a dense, 64-parameter real-valued encoding — the same benchmark numbers out of a far smaller parameterization. That expressive efficiency is the finding.

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

The reproducibility code is at [github.com/stanlee321/operator-transformer](https://github.com/stanlee321/operator-transformer) under MIT: the model, the mathematical and parity tests, an entry point behind every table in the paper, and the curated raw logs. One command rebuilds every table from those logs, downloading nothing and training nothing.

More on each component in coming posts.
