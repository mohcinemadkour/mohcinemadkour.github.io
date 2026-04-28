---
layout: page
title: Teaching
permalink: /teaching/
description: Courses, workshops, and educational content on AI, machine learning, and data science.
nav: true
nav_order: 4
---

<div class="teaching">

I build courses that bridge the gap between AI research and real-world implementation. My courses are **hands-on, code-first, and designed for practitioners** — covering production RAG systems, agentic AI evaluation, clinical AI integration, and MLOps at scale.

---

## 2026 Course Launch

<div class="row text-center my-5">
  <div class="col-md-3">
    <div class="stat-box">
      <h3 class="stat-number">2</h3>
      <p class="stat-label">Courses Launching May 2026</p>
    </div>
  </div>
  <div class="col-md-3">
    <div class="stat-box">
      <h3 class="stat-number">60+</h3>
      <p class="stat-label">Hours of Content</p>
    </div>
  </div>
  <div class="col-md-3">
    <div class="stat-box">
      <h3 class="stat-number">18+</h3>
      <p class="stat-label">Modules</p>
    </div>
  </div>
  <div class="col-md-3">
    <div class="stat-box">
      <h3 class="stat-number">100+</h3>
      <p class="stat-label">Lessons & Labs</p>
    </div>
  </div>
</div>

---

## Online Courses on Udemy

{% assign udemy_courses = site.teachings | where: "category", "online" | where: "platform", "Udemy" | sort: "importance" %}
{% for teaching in udemy_courses %}

<div class="course-card mt-4 mb-4">
  <div class="course-header {% if teaching.importance == 1 %}course-primary{% else %}course-secondary{% endif %}">
    <div class="course-meta">
      <h4 class="course-title">{{ teaching.title }}</h4>
      <p class="course-platform">{{ teaching.platform }} &middot; {{ teaching.year }}</p>
    </div>
    <div class="course-stats">
      {% if teaching.modules %}
        <span class="badge">{{ teaching.modules }} Modules</span>
      {% endif %}
      {% if teaching.hours %}
        <span class="badge">{{ teaching.hours }} hrs</span>
      {% endif %}
      {% if teaching.labs %}
        <span class="badge">{{ teaching.labs }}+ Labs</span>
      {% endif %}
    </div>
  </div>
  
  <div class="course-body">
    <p class="course-description">{{ teaching.description }}</p>
    
    {% if teaching.what_youll_build %}
    <div class="what-youll-build">
      <h6 class="fw-bold">What You'll Build:</h6>
      <ul class="build-list">
        {% for item in teaching.what_youll_build %}
          <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
    
    <div class="course-footer">
      {% if teaching.link %}
        <a href="{{ teaching.link }}" class="btn btn-sm btn-primary" target="_blank">View on Udemy</a>
      {% endif %}
      {% if teaching.importance == 1 %}
        <a href="{{ site.baseurl }}/agentic-ai-evaluation-course/" class="btn btn-sm btn-outline-primary">Course Details</a>
      {% elsif teaching.importance == 2 %}
        <a href="{{ site.baseurl }}/fhir-course/" class="btn btn-sm btn-outline-primary">Course Details</a>
      {% endif %}
      {% if teaching.status %}
        <span class="course-status badge bg-info">{{ teaching.status }}</span>
      {% endif %}
    </div>
  </div>
</div>

{% endfor %}

---

## Mentorship & University Teaching

I also mentor early-career ML engineers through various programs. Topics include production ML, career strategy, and research-to-industry transition.

</div>

<style>
.stat-box {
  padding: 20px;
  border-radius: 8px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  margin-bottom: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  margin: 0;
}

.stat-label {
  font-size: 0.95rem;
  margin: 8px 0 0 0;
  opacity: 0.9;
}

.course-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s, box-shadow 0.2s;
  background: #ffffff;
}

.course-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

html[data-theme="dark"] .course-card {
  background: #1a1a2e;
  border-color: #333;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

html[data-theme="dark"] .course-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}

.course-header {
  padding: 20px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
}

.course-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.course-secondary {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.course-meta h4 {
  margin: 0 0 4px 0;
  font-size: 1.2rem;
}

.course-platform {
  margin: 0;
  font-size: 0.9rem;
  opacity: 0.9;
}

.course-stats {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: flex-end;
}

.badge {
  background: rgba(255, 255, 255, 0.3);
  color: white;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
}

.course-body {
  padding: 20px;
  background: #ffffff;
}

html[data-theme="dark"] .course-body {
  background: #1a1a2e;
}

.course-description {
  margin: 0 0 16px 0;
  color: #555;
  line-height: 1.6;
}

html[data-theme="dark"] .course-description {
  color: #d0d0d0;
}

.what-youll-build {
  background: #f8f9fa;
  padding: 12px 16px;
  border-radius: 6px;
  margin: 16px 0;
}

.what-youll-build h6 {
  margin: 0 0 8px 0;
  color: #333;
}

html[data-theme="dark"] .what-youll-build {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

html[data-theme="dark"] .what-youll-build h6 {
  color: #e0e0e0;
}

.build-list {
  margin: 0;
  padding-left: 20px;
  color: #666;
}

.build-list li {
  margin: 4px 0;
  font-size: 0.95rem;
}

html[data-theme="dark"] .build-list {
  color: #b0b0b0;
}

html[data-theme="dark"] .build-list li {
  color: #b0b0b0;
}

.course-footer {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-top: 16px;
}

.btn {
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 0.9rem;
  text-decoration: none;
  cursor: pointer;
  border: none;
  transition: background 0.2s, color 0.2s;
}

.btn-primary {
  background: #667eea;
  color: white;
}

.btn-primary:hover {
  background: #764ba2;
}

.btn-outline-primary {
  background: transparent;
  color: #667eea;
  border: 1px solid #667eea;
}

.btn-outline-primary:hover {
  background: rgba(102, 126, 234, 0.1);
  color: #764ba2;
  border-color: #764ba2;
}

html[data-theme="dark"] .btn-outline-primary {
  color: #7c9ceb;
  border-color: #7c9ceb;
}

html[data-theme="dark"] .btn-outline-primary:hover {
  background: rgba(124, 156, 235, 0.15);
  color: #9db5ff;
  border-color: #9db5ff;
}

.btn-sm {
  padding: 4px 10px;
  font-size: 0.85rem;
}

.course-status {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
}

@media (max-width: 768px) {
  .course-header {
    flex-direction: column;
  }
  
  .course-stats {
    justify-content: flex-start;
  }
  
  .stat-box {
    padding: 15px;
  }
  
  .stat-number {
    font-size: 2rem;
  }
}
</style>
