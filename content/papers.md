<div class="section" id="papers">
<h3 class="scrollable-content-header">Papers</h3>

<div style="margin-bottom: 15px;">
(A more up-to-date list can be found on <a href="https://scholar.google.com/citations?hl=en&pli=1&user=9L864oYAAAAJ" target="_blank">Google Scholar</a>.)
</div>

{% assign sorted_papers = site.data.papers | sort: 'year' | reverse %}

<ul class="publication-list">
  {% for paper in sorted_papers %}
    <li class="paper">
      <strong>{{ paper.title }}</strong>.
      <span class="authors">{{ paper.authors }}</span>
      <span class="year">({{ paper.year }})</span>
      <span class="venue">{{ paper.details }}</span>
      {% if paper.link %}{% assign lk = paper.link | downcase %}{% if lk contains '.pdf' or lk contains '/pdf' %}
      <a href="{{ paper.link }}" class="paper-icon" target="_blank" title="PDF" aria-label="PDF"><i class="fas fa-file-pdf"></i></a>
      {% else %}
      <a href="{{ paper.link }}" class="paper-icon" target="_blank" title="View paper" aria-label="View paper"><i class="fas fa-up-right-from-square"></i></a>
      {% endif %}{% endif %}
    </li>
  {% endfor %}
</ul>

</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  let elements = document.querySelectorAll(".publication-list .paper .authors");
  elements.forEach(function(el) {
    el.innerHTML = el.innerHTML.replace(/M Hofer/g, '<span class="underline">M Hofer</span>');
  });
});
</script>