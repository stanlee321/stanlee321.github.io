---
layout: page
title: Blog
permalink: /blog/
---

{% if site.posts.size == 0 %}
<p class="muted">No posts yet. The first one is on its way.</p>
{% else %}
<ul class="post-list">
{% for post in site.posts %}
  <li>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
    {% if post.description %}
    <p class="excerpt">{{ post.description }}</p>
    {% else %}
    <p class="excerpt">{{ post.excerpt | strip_html | truncate: 200 }}</p>
    {% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}
