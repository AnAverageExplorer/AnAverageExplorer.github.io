---
layout: gallery
title: Explore Photos
permalink: /gallery/
---

{% assign tag_string = "" %}
{% for image in site.image_info %}
  {% if image.tags %}
    {% for tag in image.tags %}
      {% assign clean_tag = tag | strip | downcase %}
      {% assign tag_string = tag_string | append: clean_tag | append: "||" %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign all_tags = tag_string | split: "||" %}
{% assign unique_tags = all_tags | uniq | sort %}
{% for tag in unique_tags %}
  {% assign count = 0 %}
  {% for t in all_tags %}
    {% if t == tag %}
      {% assign count = count | plus: 1 %}
    {% endif %}
  {% endfor %}
  <label>
    <input type="checkbox" name="tag" value="{{ tag }}">
    #{{ tag }} ({{ count }})
  </label>
{% endfor %}

