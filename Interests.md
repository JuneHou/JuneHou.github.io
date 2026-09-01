---
layout: page
title: Interests
featured_image: /assets/images/pages/about.jpg
---

<style>
  .interest-section { margin-bottom: 3.5rem; }
  .interest-section h2 {
    border-bottom: 1px solid #eee;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
    font-size: 1.5rem;
  }
  .interest-blurb { margin-bottom: 1.5rem; }

  /* Justified rows: flex-basis and flex-grow are both proportional to each photo's
     aspect ratio, so every item in a row lands on the same height with no cropping. */
  .jg {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .jg-item {
    margin: 0;
    min-width: 0;
    flex-grow: var(--ar);
    flex-basis: calc(var(--ar) * 150px);
  }
  .jg-item a { display: block; line-height: 0; }
  .jg-item img {
    display: block;
    width: 100%;
    height: auto;
    background: #f9f9fb;
    transition: opacity .2s;
  }
  .jg-item a:hover img { opacity: .85; }
  /* Absorbs the slack on the final row so its photos keep their natural size
     instead of stretching to fill the width. */
  .jg::after { content: ''; flex-grow: 1000000; }

  .jg-empty {
    color: #a1a1a7;
    font-style: italic;
  }

  /* Break the galleries out of the 720px text column, matching the width the theme's
     own #wide images use (see _sass/_media-queries.scss). */
  @media only screen and (min-width: 785px) {
    .jg { margin-left: calc(360px - 47vw); margin-right: calc(360px - 47vw); }
  }
  @media only screen and (min-width: 1141px) {
    .jg { margin-left: -180px; margin-right: -180px; }
  }
  @media only screen and (max-width: 600px) {
    .jg-item { flex-basis: calc(var(--ar) * 110px); }
  }

  /* Lightbox */
  .lb {
    position: fixed;
    inset: 0;
    z-index: 999;
    background: rgba(20, 20, 24, .94);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 4vh 4vw;
  }
  .lb[hidden] { display: none; }
  .lb figure { margin: 0; text-align: center; max-height: 92vh; }
  .lb img {
    max-width: 100%;
    max-height: 84vh;
    width: auto;
    height: auto;
    display: block;
    margin: 0 auto;
  }
  .lb figcaption {
    color: #d8d8d8;
    font-size: 15px;
    font-style: italic;
    line-height: 1.5;
    margin-top: 1rem;
  }
  .lb button {
    position: absolute;
    background: none;
    border: 0;
    color: #fff;
    cursor: pointer;
    font-size: 34px;
    line-height: 1;
    padding: 12px 18px;
    height: auto;
    opacity: .7;
  }
  .lb button:hover, .lb button:focus { opacity: 1; background: none; }
  .lb-close { top: 8px; right: 8px; }
  .lb-prev  { left: 4px;  top: 50%; transform: translateY(-50%); }
  .lb-next  { right: 4px; top: 50%; transform: translateY(-50%); }
  @media only screen and (max-width: 600px) {
    .lb-prev, .lb-next { font-size: 28px; padding: 10px 12px; }
  }
</style>

{% for section in site.data.interests.sections %}
<div class="interest-section" id="{{ section.id }}">
  <h2>{{ section.title }}</h2>

  {% if section.blurb %}
  <p class="interest-blurb">{{ section.blurb }}</p>
  {% endif %}

  {% if section.photos and section.photos.size > 0 %}
  <div class="jg">
    {% for photo in section.photos %}
    {% assign base = '/assets/images/interests/' | append: section.id %}
    <figure class="jg-item" style="--ar: {{ photo.ar | default: 1.5 }}">
      <a href="{{ site.baseurl }}{{ base }}/full/{{ photo.file }}"
         data-caption="{{ photo.caption | escape }}"
         data-alt="{{ photo.alt | escape }}">
        <img src="{{ site.baseurl }}{{ base }}/thumb/{{ photo.file }}"
             width="{{ photo.w }}" height="{{ photo.h }}"
             alt="{{ photo.alt }}" loading="lazy">
      </a>
    </figure>
    {% endfor %}
  </div>
  {% else %}
  <p class="jg-empty">Photos coming soon.</p>
  {% endif %}
</div>
{% endfor %}

<div class="lb" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button class="lb-close" type="button" aria-label="Close">&times;</button>
  <button class="lb-prev"  type="button" aria-label="Previous photo">&lsaquo;</button>
  <button class="lb-next"  type="button" aria-label="Next photo">&rsaquo;</button>
  <figure>
    <img id="lb-img" src="" alt="">
    <figcaption id="lb-cap"></figcaption>
  </figure>
</div>

<script>
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.jg-item > a'));
  if (!links.length) return;

  var box = document.getElementById('lightbox'),
      img = document.getElementById('lb-img'),
      cap = document.getElementById('lb-cap'),
      current = 0,
      lastFocus = null;

  function show(i) {
    current = (i + links.length) % links.length;   // wrap at both ends
    var a = links[current];
    img.src = a.getAttribute('href');
    img.alt = a.getAttribute('data-alt') || '';
    var text = a.getAttribute('data-caption') || '';
    cap.textContent = text;
    cap.style.display = text ? '' : 'none';
  }

  function open(i, trigger) {
    lastFocus = trigger;
    show(i);
    box.hidden = false;
    document.body.style.overflow = 'hidden';       // stop the page scrolling behind
    box.querySelector('.lb-close').focus();
  }

  function close() {
    box.hidden = true;
    img.src = '';
    document.body.style.overflow = '';
    if (lastFocus) lastFocus.focus();
  }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); open(i, a); });
  });

  box.querySelector('.lb-close').addEventListener('click', close);
  box.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
  box.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
  box.addEventListener('click', function (e) { if (e.target === box) close(); });

  document.addEventListener('keydown', function (e) {
    if (box.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(current - 1);
    else if (e.key === 'ArrowRight') show(current + 1);
  });
})();
</script>
