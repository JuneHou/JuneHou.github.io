---
layout: page
title: Publications
---

<style>
  .pub-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 2.5rem;
  }
  .pub-image {
    flex-shrink: 0;
    margin-right: 1.5rem;
  }
  .pub-image img {
    width: 160px;
    height: auto;
    border: 1px solid #eee;
  }
  .pub-info {
    flex-grow: 1;
  }
  .pub-info h3 {
    margin-top: 0;
    margin-bottom: 0.25rem;
    font-size: 1.2rem;
  }
  .pub-info p {
    margin: 0.2rem 0;
    line-height: 1.5;
    color: #555;
  }
  .pub-links a {
    margin-right: 1rem;
    font-weight: bold;
  }
</style>

{% for pub in site.publications reversed %}
<div class="pub-item">
  <div class="pub-image">
    <img src="{{ site.baseurl }}/{{ pub.image }}" alt="Thumbnail for {{ pub.title }}">
  </div>
  <div class="pub-info">
    <h3>{{ pub.title }}</h3>
    <p>{{ pub.authors }}</p>
    <p><em>{{ pub.venue }}</em></p>
    <p class="pub-links">
      {% if pub.pdf %}
        <a href="{{ pub.pdf }}" target="_blank" rel="noopener noreferrer">[PDF]</a>
      {% endif %}
      {% if pub.code %}
        <a href="{{ pub.code }}" target="_blank" rel="noopener noreferrer">[Code]</a>
      {% endif %}
      </p>
  </div>
</div>
{% endfor %}