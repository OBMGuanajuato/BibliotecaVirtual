---
title: Olimpiada Mexicana de Matemáticas
urlname: omm
logo-title: ../assets/img/Logo-omm.png
layout: home
---

  <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
  {% for item in site.nacionales_omm reversed%}
      <div class="col">
        <div class="card h-100 mb-3">
          <a
            href="{{ item.file | relative_url }}"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              height="150px"
              style="object-fit: contain;"
              class="card-img-top border-bottom bg-white"
              src="{{ item.thumbnail | relative_url}}"
              alt="Nacional {{ item.year }}">
          </a>
          <div class="card-body">
            <a
              href="{{ item.file | relative_url }}"
              target="_blank"
              class="card-link"
              rel="noopener noreferrer"
            >Nacional {{ item.year }}</a>
          </div>
        </div>
      </div>
  {% endfor %}
  </div>
