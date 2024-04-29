---
title: Olimpiada Mexicana de Matemáticas para Educación Básica
urlname: ommeb
logo-title: ../assets/img/Logo-ommeb.png
layout: home
---

{% for edition in site.data.ediciones_ommeb reversed %}
<div class="row">
	<div class="col mb-3">
	<h2 class="text-center">{{edition.year}}</h2>
  <h3>Individual</h3>
    <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
    {% for item in site.nacionales_ommeb %}
    {% if item.year == edition.year and item.mode == "Individual"%}
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
                alt="Nacional {{ item.year }} {{item.mode}}">
            </a>
            <div class="card-body">
              <a
                href="{{ item.file | relative_url }}"
                target="_blank"
                class="card-link"
                rel="noopener noreferrer"
              >Nacional {{ item.year }} Nivel {{item.level}} {{item.mode}}</a>
            </div>
          </div>
        </div>
      {% endif %}
    {% endfor %}
    </div>
    <h3>Equipos</h3>
    <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
    {% for item in site.nacionales_ommeb %}
    {% if item.year == edition.year and item.mode == "Equipos"%}
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
                alt="Nacional {{ item.year }} {{item.mode}}">
            </a>
            <div class="card-body">
              <a
                href="{{ item.file | relative_url }}"
                target="_blank"
                class="card-link"
                rel="noopener noreferrer"
              >Nacional {{ item.year }} Nivel {{item.level}} {{item.mode}}</a>
            </div>
          </div>
        </div>
      {% endif %}
    {% endfor %}
    </div>
  </div>
</div>
{% endfor %}