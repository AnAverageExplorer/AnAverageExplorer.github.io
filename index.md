---
layout: default
title: An Average Explorer
---

<style>
  .grid-item {
    position: relative;
    overflow: hidden;
    aspect-ratio: attr(data-ratio);
  }

  .grid-overlay {
    position: absolute;
    bottom: 10px;
    left: 10px;
    color: white;
    padding: 10px 12px;
    background: rgba(0, 0, 0, 0.55);
    border-radius: 4px;
    font-size: 0.85rem;
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: 2;
  }

  .grid-item:hover .grid-overlay {
    opacity: 1;
  }

  .hover-filter {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.25);
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: 1;
    pointer-events: none;
  }

  .grid-item:hover .hover-filter {
    opacity: 1;
  }

  .grid-overlay strong {
    display: block;
    font-size: 1rem;
    margin-bottom: 2px;
  }
</style>

<div class="grid">
  <div class="grid-sizer"></div>

  {% for image in site.image_info %}
    {% if image.display %}
      {% assign filename_base = image.filename | split: '.' | first %}
      {% assign light_webp = '/assets/images/gallery_light/' | append: filename_base | append: '.webp' %}
      {% assign full_src = '/assets/images/gallery/' | append: image.filename %}

      <div class="grid-item" style="aspect-ratio: {{ image.ratio }}">
        {% if image.project %}
          {% assign slug = image.project | slugify %}
          {% assign project_data = site.projects | where: "title", image.project | first %}
          <a href="/projects/{{ slug }}/" style="position: relative; display: block;">
            <picture>
              <source srcset="{{ light_webp }}" type="image/webp">
              <img src="{{ light_webp }}" alt="{{ image.description | default: image.title }}" loading="lazy" decoding="async">
            </picture>
            <span class="hover-filter"></span>
            <div class="grid-overlay">
              <strong>{{ image.project }}</strong>
              {% if project_data.tags %}{{ project_data.tags[0] }}{% endif %}
            </div>
          </a>
        {% else %}
          <a href="{{ full_src }}" class="glightbox" data-gallery="gallery">
            <picture>
              <source srcset="{{ light_webp }}" type="image/webp">
              <img src="{{ light_webp }}" alt="{{ image.description | default: image.title }}" loading="lazy" decoding="async">
            </picture>
          </a>
        {% endif %}
      </div>
    {% endif %}
  {% endfor %}

</div>
