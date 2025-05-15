---
layout: default
title: An Average Explorer
---

<div class="homepage-grid">
  <div class="grid">
    <div class="grid-sizer"></div>

    {% for image in site.image_info %}
      {% if image.display %}
        {% assign filename_base = image.filename | split: '.' | first %}
        {% assign light_webp = '/assets/images/gallery_light/' | append: filename_base | append: '.webp' %}
        {% assign first_tag = image.tags | first | downcase %}

        <div class="grid-item" style="aspect-ratio: {{ image.ratio }}">
          {% if image.project %}
            {% assign slug = image.project | slugify %}
            {% assign project_data = site.projects | where: "title", image.project | first %}
            <a href="/projects/{{ slug }}/" class="grid-link">
              <picture>
                <source srcset="{{ light_webp }}" type="image/webp">
                <img src="{{ light_webp }}" alt="{{ image.description | default: image.title }}" loading="lazy" decoding="async">
              </picture>
              <span class="hover-filter"></span>
              <div class="grid-overlay">
                <strong>{{ image.project }}</strong>
                {% if project_data.tags %}
                  {{ project_data.tags[0] }}
                {% endif %}
              </div>
            </a>
          {% else %}
            <a href="/gallery/?tags={{ first_tag | uri_escape }}" class="grid-link">
              <picture>
                <source srcset="{{ light_webp }}" type="image/webp">
                <img src="{{ light_webp }}" alt="{{ image.description | default: image.title }}" loading="lazy" decoding="async">
              </picture>
              <span class="hover-filter"></span>
              <div class="grid-overlay">
                <strong>#{{ first_tag | capitalize }}</strong>
              </div>
            </a>
          {% endif %}
        </div>
      {% endif %}
    {% endfor %}
  </div>
</div>
