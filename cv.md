---
layout: page
title: cv
---

<style>
  .cv-actions {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 1.5rem;
  }
  .cv-updated {
    color: #888;
    font-size: 0.9rem;
    margin: 0;
  }
  /* Inline viewer: letter-page aspect ratio, full width of the content column. */
  .cv-embed {
    width: 100%;
    aspect-ratio: 8.5 / 11;
    border: 1px solid #e5e7e9;
    background: #f9f9fb;
  }
  .cv-fallback {
    display: none;
    border: 1px solid #e5e7e9;
    background: #f9f9fb;
    padding: 2rem 1.5rem;
    text-align: center;
  }
  .cv-fallback p {
    margin: 0 0 1.25rem;
    color: #535358;
  }
  /* Mobile browsers largely refuse to render inline PDFs, so swap in a download card. */
  @media (max-width: 700px) {
    .cv-embed { display: none; }
    .cv-fallback { display: block; }
  }
</style>

<div class="cv-actions">
  <p class="cv-updated">Last updated: August 2026</p>
  <a class="btn" href="{{ site.baseurl }}/assets/cv/Resume_JunHou.pdf" target="_blank" rel="noopener noreferrer">Download PDF</a>
</div>

<object class="cv-embed" data="{{ site.baseurl }}/assets/cv/Resume_JunHou.pdf" type="application/pdf">
  <div class="cv-fallback" style="display:block;">
    <p>Your browser can&rsquo;t display PDFs inline.</p>
    <a class="btn" href="{{ site.baseurl }}/assets/cv/Resume_JunHou.pdf" target="_blank" rel="noopener noreferrer">Download PDF</a>
  </div>
</object>

<div class="cv-fallback">
  <p>View my full CV as a PDF.</p>
  <a class="btn" href="{{ site.baseurl }}/assets/cv/Resume_JunHou.pdf" target="_blank" rel="noopener noreferrer">Download PDF</a>
</div>
