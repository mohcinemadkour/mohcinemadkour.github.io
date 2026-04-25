---
layout: page
title: teaching
permalink: /teaching/
description: Courses, workshops, and educational content on AI, machine learning, and data science.
nav: true
nav_order: 4
---

<div class="teaching">

I'm passionate about making advanced AI concepts accessible. My teaching spans university-level instruction, professional bootcamps, online courses, and mentorship programs.

---

## Online Courses

{% assign sorted_teachings = site.teachings | where: "category", "online" | sort: "importance" %}
{% for teaching in sorted_teachings %}
<div class="card mt-3">
  <div class="p-3">
    <h4 class="card-title"><a href="{{ teaching.url | prepend: site.baseurl }}">{{ teaching.title }}</a></h4>
    <h6 class="card-subtitle mb-2 text-muted">{{ teaching.platform }} &middot; {{ teaching.year }}</h6>
    <p class="card-text">{{ teaching.description }}</p>
    {% if teaching.link %}
    <a href="{{ teaching.link }}" class="btn btn-sm btn-outline-primary" target="_blank">View Course</a>
    {% endif %}
  </div>
</div>
{% endfor %}

---

## University & Bootcamp Teaching

{% assign sorted_teachings = site.teachings | where: "category", "university" | sort: "importance" %}
{% for teaching in sorted_teachings %}
<div class="card mt-3">
  <div class="p-3">
    <h4 class="card-title"><a href="{{ teaching.url | prepend: site.baseurl }}">{{ teaching.title }}</a></h4>
    <h6 class="card-subtitle mb-2 text-muted">{{ teaching.institution }} &middot; {{ teaching.year }}</h6>
    <p class="card-text">{{ teaching.description }}</p>
  </div>
</div>
{% endfor %}

---

## Mentorship

I mentor early-career ML engineers through **SharpestMinds** and other programs. Topics include production ML, career strategy, and research-to-industry transition.

</div>
