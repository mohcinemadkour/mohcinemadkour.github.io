---
layout: page
title: talks
permalink: /talks/
description: Conference talks, workshops, panels, and invited presentations on AI and machine learning.
nav: true
nav_order: 5
---

<div class="talks">

I speak at conferences, meetups, and workshops on topics including agentic AI systems, RAG architectures, MLOps, and healthcare AI. Feel free to reach out if you'd like me to speak at your event.

---

{% assign sorted_talks = site.talks | sort: "date" | reverse %}
{% for talk in sorted_talks %}

<div class="card mt-3">
  <div class="p-3">
    <div class="row">
      <div class="col-sm-9">
        <h4 class="card-title">
          {% if talk.slides %}
          <a href="{{ talk.slides }}" target="_blank">{{ talk.title }}</a>
          {% else %}
          {{ talk.title }}
          {% endif %}
        </h4>
        <h6 class="card-subtitle mb-2 text-muted">
          {{ talk.event }} &middot; {{ talk.location }} &middot; {{ talk.date | date: "%B %Y" }}
        </h6>
        <p class="card-text">{{ talk.description }}</p>
        <div class="mt-2">
          {% if talk.slides %}
          <a href="{{ talk.slides }}" class="btn btn-sm btn-outline-primary me-1" target="_blank">
            <i class="fas fa-file-powerpoint"></i> Slides
          </a>
          {% endif %}
          {% if talk.video %}
          <a href="{{ talk.video }}" class="btn btn-sm btn-outline-danger me-1" target="_blank">
            <i class="fas fa-video"></i> Video
          </a>
          {% endif %}
          {% if talk.poster %}
          <a href="{{ talk.poster }}" class="btn btn-sm btn-outline-success me-1" target="_blank">
            <i class="fas fa-image"></i> Poster
          </a>
          {% endif %}
        </div>
      </div>
      <div class="col-sm-3 text-right">
        <span class="badge rounded-pill" style="background-color: var(--global-theme-color);">
          {{ talk.type | default: "Talk" }}
        </span>
      </div>
    </div>
  </div>
</div>
{% endfor %}

{% if site.talks.size == 0 %}

<p class="text-muted">Talks and presentations coming soon. Check back shortly.</p>
{% endif %}

</div>
