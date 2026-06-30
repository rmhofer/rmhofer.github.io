---
layout: default
title: Code & Demos
permalink: /code/
---

<div class="section" id="code">
    <h3 class="scrollable-content-header">Code &amp; Demos</h3>

    <p style="margin-bottom: 20px;">A collection of interactive demos and code from my research &mdash; things you can try in the browser, and repositories accompanying papers.</p>

    <ul class="publication-list">
      {% for item in site.data.demos %}
        <li class="paper">
          <strong>{{ item.title }}</strong>
          {% if item.demo %}<a href="{{ item.demo }}" class="paper-icon" target="_blank" rel="noopener" title="Live demo" aria-label="Live demo"><i class="fas fa-play"></i></a>{% endif %}
          {% if item.repo %}<a href="{{ item.repo }}" class="paper-icon" target="_blank" rel="noopener" title="Code repository" aria-label="Code repository"><i class="fab fa-github"></i></a>{% endif %}
          {% if item.link %}<a href="{{ item.link }}" class="paper-icon" target="_blank" rel="noopener" title="Link" aria-label="Link"><i class="fas fa-up-right-from-square"></i></a>{% endif %}
          {% if item.description %}<div class="venue" style="display: block; margin-top: 2px;">{{ item.description }}</div>{% endif %}
        </li>
      {% endfor %}
    </ul>
</div>
