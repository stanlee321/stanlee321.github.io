---
layout: page
title: Publications
permalink: /publications/
---

## All You Need Is Non-Commutative Words

Carla M. Quispe Flores\*, Stanley Salvatierra\*, Renan Cabrera
<span class="muted">\*equal contribution</span>

arXiv:2608.29314 [cs.CL], 2026 — listed 29 Aug 2026.

[Abstract](https://arxiv.org/abs/2608.29314) · [PDF](https://arxiv.org/pdf/2608.29314) · [Code (MIT)](https://github.com/stanlee321/operator-transformer)

### Abstract

> We represent lexical tokens as unitary matrices and encode each sentence as their ordered product. The noncommutativity of matrix product captures word order without positional encodings (PEs). The same algebra yields several capabilities, including antisymmetric self-attention that requires no query, key, or value projections, and the parallel composition of variable-length text chunks at a reduced attention cost. Furthermore, it provides a canonical-coset readout layer that intrinsically encodes all true unitary degrees of freedom compactly, while supporting continual learning through nested group extensions that enlarge the operator space with each new task while preserving prior representations exactly. Across standard text-classification benchmarks, the method matches or exceeds bag-of-words baselines. Achieving higher accuracy on IMDB and comparable performance on AG News. Notably, this is accomplished by replacing the conventional ~30,000-dimensional vocabulary space with a dense, 64-parameter real-valued encoding, highlighting the expressive efficiency of our parameterization.

This construction is inspired by the mathematics of quantum mechanics, but every computation here is classical and we claim no quantum advantage.

### Cite

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

### Reference this work builds on

R. Cabrera, T. Strohecker and H. Rabitz, *The canonical coset decomposition of unitary matrices through Householder transformations*, **J. Math. Phys. 51**, 082101 (2010), [doi:10.1063/1.3466798](https://doi.org/10.1063/1.3466798).
