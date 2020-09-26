---
layout: hackbar-menu
title: Hackbars
permalink: "/hackbars/"
---

# {{ page.title }}

{% for hackbar in site.hackbars %}
  {% if hackbar.layout == 'hackbar' %}
  * [{{ hackbar.title }}](..{{ hackbar.url }}) by {{ hackbar.author }}
  {% endif %}
{% endfor %}
