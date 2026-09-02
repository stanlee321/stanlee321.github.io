---
layout: page
title: Stanley Salvatierra
hide_title: true
permalink: /
---

# Stanley Salvatierra

I am an electrical engineer working as a machine learning researcher and engineer, based in Bolivia. I build ML systems at Deep Microsystems and spend my research time on a single question: what happens if you represent language with operator algebra instead of vectors.

## What I work on

- **Language as operator algebra.** Words as unitary matrices, sentences as their ordered, non-commutative products — so word order is carried by the algebra itself, without positional encodings.
- **ML systems engineering at Deep Microsystems.** Taking models from a research notebook to something that runs in production: PyTorch, Go, gRPC, Kubernetes, AWS.
- **Open-source reproducibility.** The code behind the paper is public, with the raw logs the result tables are rebuilt from.

## Latest

<ul class="post-list">
{% for post in site.posts limit: 3 %}
  <li>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
    {% if post.description %}<p class="excerpt">{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>

<p><a href="{{ '/blog/' | relative_url }}">All posts &rarr;</a></p>

## Links

- [GitHub](https://github.com/stanlee321)
- [X / Twitter](https://x.com/iamatachyon)
- [arXiv: All You Need Is Non-Commutative Words](https://arxiv.org/abs/2608.29314)

<p class="muted">Solve the problem of intelligence, solve everything else!</p>
