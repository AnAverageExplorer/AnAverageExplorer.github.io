---
layout: default
title: An Average Explorer
---

<div class="grid">
  <div class="grid-sizer"></div>
  {% for photo in site.static_files %}
    {% if photo.path contains 'gallery_light' %}
      {% assign full_res = photo.path | replace: 'gallery_light', 'gallery' %}
      <div class="grid-item">
        <a href="{{ full_res }}" class="glightbox" data-gallery="gallery">
          <img src="{{ photo.path }}" alt="" loading="lazy" decoding="async">
        </a>
      </div>
    {% endif %}
  {% endfor %}
</div>



