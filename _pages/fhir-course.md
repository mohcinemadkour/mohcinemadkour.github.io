---
layout: none
title: "HL7 FHIR Integration for Clinical AI — Udemy Course"
permalink: /fhir-course/
description: Build production-grade clinical data pipelines from raw HL7 v2 hospital feeds through FHIR R4 APIs, Mirth Connect, Epic, and AI inference.
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HL7 FHIR Integration for Clinical AI — Udemy Course</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Mono:ital,wght@0,400;0,500;1,400&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --navy:   #0a1628;
    --navy2:  #112240;
    --teal:   #0d9488;
    --teal2:  #14b8a6;
    --teal3:  #99f6e4;
    --blue:   #3b82f6;
    --blue2:  #93c5fd;
    --amber:  #f59e0b;
    --amber2: #fde68a;
    --coral:  #f97316;
    --white:  #f8fafc;
    --muted:  #94a3b8;
    --border: rgba(255,255,255,0.08);
  }

_, _::before, \*::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
font-family: 'DM Sans', sans-serif;
background: var(--navy);
color: var(--white);
line-height: 1.6;
overflow-x: hidden;
}

/_ ── NOISE TEXTURE OVERLAY ── _/
body::before {
content: '';
position: fixed; inset: 0;
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
opacity: 0.03;
pointer-events: none;
z-index: 0;
}

/_ ── GLOW BLOBS ── _/
.blob {
position: fixed;
border-radius: 50%;
filter: blur(120px);
pointer-events: none;
z-index: 0;
}
.blob-1 { width: 500px; height: 500px; background: rgba(13,148,136,0.18); top: -100px; right: -100px; }
.blob-2 { width: 400px; height: 400px; background: rgba(59,130,246,0.12); bottom: 200px; left: -100px; }
.blob-3 { width: 300px; height: 300px; background: rgba(249,115,22,0.08); top: 50%; left: 50%; transform: translate(-50%,-50%); }

/_ ── LAYOUT ── _/
.container { max-width: 900px; margin: 0 auto; padding: 0 28px; position: relative; z-index: 1; }

section { padding: 80px 0; }

/_ ── HERO ── _/
.hero {
min-height: 100vh;
display: flex;
align-items: center;
padding: 80px 0 60px;
position: relative;
}

.hero-eyebrow {
display: inline-flex; align-items: center; gap: 8px;
font-family: 'DM Mono', monospace;
font-size: 11px; letter-spacing: .15em; text-transform: uppercase;
color: var(--teal2);
border: 1px solid rgba(20,184,166,0.3);
padding: 6px 14px; border-radius: 100px;
margin-bottom: 32px;
animation: fadeUp .6s ease both;
}
.hero-eyebrow::before {
content: '';
width: 6px; height: 6px; border-radius: 50%;
background: var(--teal2);
animation: pulse 2s ease infinite;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.4;transform:scale(.8)} }

.hero-title {
font-family: 'Syne', sans-serif;
font-size: clamp(36px, 6vw, 72px);
font-weight: 800;
line-height: 1.05;
letter-spacing: -.02em;
margin-bottom: 12px;
animation: fadeUp .6s .1s ease both;
}

.hero-title .accent { color: var(--teal2); }
.hero-title .line2 { display: block; color: var(--muted); font-weight: 400; font-size: .55em; letter-spacing: 0; margin-top: 6px; }

.hero-sub {
font-size: 18px; color: var(--muted); max-width: 580px;
line-height: 1.7; margin-bottom: 40px;
font-weight: 300;
animation: fadeUp .6s .2s ease both;
}

.hero-cta {
display: flex; align-items: center; gap: 16px; flex-wrap: wrap;
animation: fadeUp .6s .3s ease both;
}

.btn-primary {
display: inline-flex; align-items: center; gap: 8px;
background: var(--teal);
color: #fff; font-family: 'Syne', sans-serif; font-weight: 600;
font-size: 15px; padding: 14px 28px; border-radius: 8px;
text-decoration: none; border: none; cursor: pointer;
transition: background .2s, transform .15s;
position: relative; overflow: hidden;
}
.btn-primary::after {
content: ''; position: absolute; inset: 0;
background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, transparent 60%);
}
.btn-primary:hover { background: var(--teal2); transform: translateY(-1px); }
.btn-primary svg { width: 16px; height: 16px; }

.btn-ghost {
display: inline-flex; align-items: center; gap: 6px;
color: var(--muted); font-size: 14px;
text-decoration: none; border: none; background: none; cursor: pointer;
transition: color .2s;
}
.btn-ghost:hover { color: var(--white); }

.hero-stats {
display: flex; gap: 32px; flex-wrap: wrap;
margin-top: 56px; padding-top: 40px;
border-top: 1px solid var(--border);
animation: fadeUp .6s .4s ease both;
}
.stat-item { display: flex; flex-direction: column; gap: 4px; }
.stat-num {
font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 700;
color: var(--white);
}
.stat-num span { color: var(--teal2); }
.stat-label { font-size: 12px; color: var(--muted); letter-spacing: .04em; }

/_ ── PIPELINE BAR ── _/
.pipeline-bar {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 12px;
padding: 24px 28px;
display: flex; align-items: center; gap: 0;
flex-wrap: wrap;
overflow: hidden;
position: relative;
}
.pipeline-bar::before {
content: '';
position: absolute; top: 0; left: 0; right: 0; height: 2px;
background: linear-gradient(90deg, var(--teal), var(--blue), var(--amber), var(--coral));
}
.pipe-node {
display: flex; flex-direction: column; align-items: center; gap: 4px;
padding: 6px 16px;
font-family: 'DM Mono', monospace; font-size: 12px;
}
.pipe-node .label { color: var(--muted); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; }
.pipe-node .value { color: var(--white); font-weight: 500; }
.pipe-arrow { color: var(--border); font-size: 18px; padding: 0 4px; }

/_ ── SECTION HEADERS ── _/
.section-tag {
font-family: 'DM Mono', monospace;
font-size: 11px; letter-spacing: .15em; text-transform: uppercase;
color: var(--teal2); margin-bottom: 12px;
}
.section-title {
font-family: 'Syne', sans-serif;
font-size: clamp(28px, 4vw, 44px);
font-weight: 700; line-height: 1.1;
letter-spacing: -.02em;
margin-bottom: 16px;
}
.section-desc { font-size: 17px; color: var(--muted); max-width: 580px; font-weight: 300; line-height: 1.7; }

/_ ── PURPOSE ── _/
.purpose-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
gap: 16px; margin-top: 48px;
}
.purpose-card {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 12px;
padding: 24px;
position: relative; overflow: hidden;
transition: border-color .2s, transform .2s;
}
.purpose-card:hover { border-color: rgba(20,184,166,0.4); transform: translateY(-2px); }
.purpose-card::before {
content: '';
position: absolute; top: 0; left: 0; right: 0; height: 2px;
background: var(--card-accent, var(--teal));
opacity: 0; transition: opacity .2s;
}
.purpose-card:hover::before { opacity: 1; }
.card-icon {
width: 40px; height: 40px; border-radius: 8px;
display: flex; align-items: center; justify-content: center;
font-size: 18px; margin-bottom: 14px;
background: var(--card-bg, rgba(13,148,136,0.12));
}
.card-title { font-family: 'Syne', sans-serif; font-weight: 600; font-size: 16px; margin-bottom: 8px; }
.card-desc { font-size: 14px; color: var(--muted); line-height: 1.6; }

/_ ── FOR WHO ── _/
.audience-section { background: linear-gradient(135deg, rgba(17,34,64,0.8), rgba(10,22,40,0.95)); }

.audience-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 48px; }

.audience-item {
display: flex; align-items: flex-start; gap: 14px;
padding: 18px 20px;
background: rgba(255,255,255,0.03);
border: 1px solid var(--border);
border-radius: 10px;
transition: background .2s;
}
.audience-item:hover { background: rgba(255,255,255,0.05); }
.audience-check {
width: 22px; height: 22px; border-radius: 50%;
background: rgba(13,148,136,0.15);
border: 1px solid rgba(20,184,166,0.4);
display: flex; align-items: center; justify-content: center;
flex-shrink: 0; margin-top: 1px;
font-size: 11px; color: var(--teal2);
}
.audience-text { font-size: 14px; color: var(--white); line-height: 1.5; }

.prereq-box {
margin-top: 40px;
background: rgba(59,130,246,0.06);
border: 1px solid rgba(59,130,246,0.2);
border-radius: 12px;
padding: 24px 28px;
}
.prereq-title { font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 600; color: var(--blue2); margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }
.prereq-list { display: flex; flex-wrap: wrap; gap: 8px; }
.prereq-tag {
font-family: 'DM Mono', monospace; font-size: 12px;
padding: 5px 12px; border-radius: 6px;
background: rgba(59,130,246,0.1);
border: 1px solid rgba(59,130,246,0.2);
color: var(--blue2);
}

/_ ── CURRICULUM ── _/
.module-list { display: flex; flex-direction: column; gap: 12px; margin-top: 48px; }

.module-item {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 12px;
overflow: hidden;
transition: border-color .2s;
}
.module-item:hover { border-color: rgba(255,255,255,0.15); }

.module-header {
display: flex; align-items: center; gap: 16px;
padding: 20px 24px;
}
.module-num {
font-family: 'DM Mono', monospace;
font-size: 11px; font-weight: 500;
color: var(--muted);
width: 28px; flex-shrink: 0;
}
.module-accent {
width: 4px; height: 36px; border-radius: 2px; flex-shrink: 0;
background: var(--m-color, var(--teal));
}
.module-info { flex: 1; }
.module-title { font-family: 'Syne', sans-serif; font-weight: 600; font-size: 15px; margin-bottom: 3px; }
.module-meta { display: flex; gap: 14px; align-items: center; }
.module-duration { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--muted); }
.module-tags { display: flex; gap: 6px; }
.mtag {
font-size: 11px; padding: 2px 8px; border-radius: 4px;
font-family: 'DM Mono', monospace;
background: rgba(255,255,255,0.05); color: var(--muted);
}
.module-lessons {
padding: 0 24px 20px 68px;
display: flex; flex-wrap: wrap; gap: 8px;
}
.lesson-pill {
font-size: 12px; padding: 4px 10px; border-radius: 6px;
background: rgba(255,255,255,0.04);
border: 1px solid rgba(255,255,255,0.06);
color: var(--muted);
transition: color .15s, border-color .15s;
}
.module-item:hover .lesson-pill { color: rgba(255,255,255,0.7); border-color: rgba(255,255,255,0.1); }

/_ ── WHAT YOU BUILD ── _/
.build-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 48px; }

.build-card {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 14px;
padding: 28px 24px;
position: relative; overflow: hidden;
}
.build-num {
font-family: 'Syne', sans-serif; font-size: 64px; font-weight: 800;
color: rgba(255,255,255,0.04);
position: absolute; top: 8px; right: 16px; line-height: 1;
pointer-events: none;
}
.build-icon { font-size: 28px; margin-bottom: 16px; }
.build-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 17px; margin-bottom: 10px; }
.build-desc { font-size: 13px; color: var(--muted); line-height: 1.65; }

/_ ── STACK ── _/
.stack-section { padding: 60px 0; }
.stack-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 36px; }
.stack-item {
display: flex; align-items: center; gap: 8px;
padding: 10px 16px; border-radius: 8px;
background: rgba(255,255,255,0.04);
border: 1px solid rgba(255,255,255,0.08);
font-family: 'DM Mono', monospace; font-size: 13px; color: var(--white);
transition: background .2s, border-color .2s;
}
.stack-item:hover { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.15); }
.stack-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }

/_ ── CODE SNIPPET ── _/
.code-preview {
background: #0d1117;
border: 1px solid rgba(255,255,255,0.1);
border-radius: 12px; overflow: hidden;
margin-top: 48px;
}
.code-bar {
display: flex; align-items: center; gap: 8px;
padding: 12px 16px;
background: rgba(255,255,255,0.04);
border-bottom: 1px solid rgba(255,255,255,0.06);
}
.code-dot { width: 10px; height: 10px; border-radius: 50%; }
.code-filename { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--muted); margin-left: 8px; }
.code-body { padding: 20px 24px; font-family: 'DM Mono', monospace; font-size: 13px; line-height: 1.75; overflow-x: auto; }
.c-comment { color: #6b737d; font-style: italic; }
.c-kw { color: #ff7b72; }
.c-str { color: #a5d6ff; }
.c-fn { color: #d2a8ff; }
.c-val { color: #ffa657; }
.c-obj { color: #79c0ff; }
.c-plain { color: #e6edf3; }

/_ ── INSTRUCTOR ── _/
.instructor-card {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 16px;
padding: 36px;
display: flex; gap: 32px; align-items: flex-start;
flex-wrap: wrap;
margin-top: 48px;
position: relative; overflow: hidden;
}
.instructor-card::after {
content: '';
position: absolute; top: 0; right: 0;
width: 300px; height: 300px;
background: radial-gradient(circle at top right, rgba(13,148,136,0.08), transparent 70%);
pointer-events: none;
}
.instructor-avatar {
width: 80px; height: 80px; border-radius: 50%; flex-shrink: 0;
background: linear-gradient(135deg, var(--teal), var(--blue));
display: flex; align-items: center; justify-content: center;
font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800;
color: #fff;
border: 3px solid rgba(20,184,166,0.3);
}
.instructor-info { flex: 1; min-width: 220px; }
.instructor-name { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700; margin-bottom: 4px; }
.instructor-title { font-size: 14px; color: var(--teal2); margin-bottom: 14px; }
.instructor-bio { font-size: 14px; color: var(--muted); line-height: 1.7; margin-bottom: 16px; }
.instructor-creds { display: flex; flex-wrap: wrap; gap: 8px; }
.cred-badge {
font-size: 12px; padding: 4px 12px; border-radius: 6px;
background: rgba(255,255,255,0.05);
border: 1px solid rgba(255,255,255,0.1);
color: var(--muted);
}

/_ ── CONCLUSION / CTA ── _/
.cta-section {
text-align: center;
padding: 100px 0;
position: relative;
}
.cta-section::before {
content: '';
position: absolute; top: 0; left: 50%; transform: translateX(-50%);
width: 1px; height: 80px;
background: linear-gradient(to bottom, transparent, var(--border));
}
.cta-label {
font-family: 'DM Mono', monospace; font-size: 11px;
letter-spacing: .15em; text-transform: uppercase;
color: var(--amber); margin-bottom: 20px;
}
.cta-title {
font-family: 'Syne', sans-serif;
font-size: clamp(32px, 5vw, 56px);
font-weight: 800; line-height: 1.1;
letter-spacing: -.02em;
margin-bottom: 20px;
}
.cta-title em { color: var(--teal2); font-style: normal; }
.cta-desc { font-size: 17px; color: var(--muted); max-width: 520px; margin: 0 auto 40px; line-height: 1.7; font-weight: 300; }
.cta-pricing {
display: inline-flex; align-items: center; gap: 16px;
background: rgba(245,158,11,0.08);
border: 1px solid rgba(245,158,11,0.2);
border-radius: 12px; padding: 16px 28px;
margin-bottom: 32px;
}
.price-launch { font-family: 'Syne', sans-serif; font-size: 36px; font-weight: 800; color: var(--amber); }
.price-meta { text-align: left; }
.price-list { font-size: 13px; color: var(--muted); text-decoration: line-through; }
.price-tag { font-size: 12px; color: var(--amber2); font-family: 'DM Mono', monospace; }

.cta-btn {
display: inline-flex; align-items: center; gap: 10px;
background: var(--teal); color: #fff;
font-family: 'Syne', sans-serif; font-weight: 700; font-size: 17px;
padding: 18px 40px; border-radius: 10px;
text-decoration: none; border: none; cursor: pointer;
transition: background .2s, transform .15s, box-shadow .2s;
box-shadow: 0 0 40px rgba(13,148,136,0.3);
}
.cta-btn:hover {
background: var(--teal2);
transform: translateY(-2px);
box-shadow: 0 0 60px rgba(20,184,166,0.4);
}
.cta-fine { font-size: 12px; color: var(--muted); margin-top: 20px; font-family: 'DM Mono', monospace; }

/_ ── DIVIDER ── _/
.divider {
border: none;
height: 1px;
background: var(--border);
margin: 0;
}

/_ ── ANIMATIONS ── _/
@keyframes fadeUp {
from { opacity: 0; transform: translateY(20px); }
to { opacity: 1; transform: translateY(0); }
}

.reveal {
opacity: 0; transform: translateY(24px);
transition: opacity .6s ease, transform .6s ease;
}
.reveal.visible { opacity: 1; transform: translateY(0); }

/_ ── FOOTER ── _/
.footer {
padding: 32px 0;
border-top: 1px solid var(--border);
display: flex; justify-content: space-between; align-items: center;
flex-wrap: wrap; gap: 12px;
font-size: 13px; color: var(--muted);
}
.footer a { color: var(--teal2); text-decoration: none; }
.footer a:hover { color: var(--teal3); }

/_ ── RESPONSIVE ── _/
@media (max-width: 600px) {
section { padding: 60px 0; }
.hero { padding: 60px 0 40px; }
.module-lessons { padding-left: 24px; }
.instructor-card { padding: 24px; }
}
</style>

</head>
<body>

<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="blob blob-3"></div>

<!-- ── HERO ── -->
<section class="hero">
  <div class="container">
    <div class="hero-eyebrow">Now on Udemy &nbsp;·&nbsp; New course 2025</div>

    <h1 class="hero-title">
      HL7 &amp; FHIR Integration<br>
      <span class="accent">for Clinical AI</span>
      <span class="line2">A Practitioner's Guide · Mirth Connect · Epic</span>
    </h1>

    <p class="hero-sub">
      Build production-grade clinical data pipelines from raw HL7 v2 hospital feeds through FHIR R4 APIs, Mirth Connect channels, Epic EHR connectivity, and live AI inference — with every concept backed by real hospital deployments.
    </p>

    <div class="hero-cta">
      <a href="https://udemy.com" class="btn-primary" target="_blank">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        Enroll now — $19.99
      </a>
      <a href="#curriculum" class="btn-ghost">View curriculum ↓</a>
    </div>

    <div class="hero-stats">
      <div class="stat-item">
        <div class="stat-num">8<span>×</span></div>
        <div class="stat-label">Modules</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">45<span>+</span></div>
        <div class="stat-label">Lessons</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">12<span>+</span></div>
        <div class="stat-label">Hands-on labs</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">14<span>h</span></div>
        <div class="stat-label">Total content</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">$0</div>
        <div class="stat-label">Lab tool cost</div>
      </div>
    </div>

    <!-- pipeline -->
    <div class="pipeline-bar" style="margin-top:48px">
      <div class="pipe-node"><span class="label">Source</span><span class="value">Epic EHR</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Protocol</span><span class="value">HL7 v2</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Engine</span><span class="value">Mirth Connect</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Standard</span><span class="value">FHIR R4</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Inference</span><span class="value">AI Model</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Feedback</span><span class="value">CDS Hooks</span></div>
    </div>

  </div>
</section>

<hr class="divider">

<!-- ── PURPOSE ── -->
<section>
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Purpose</p>
      <h2 class="section-title">Why this course exists</h2>
      <p class="section-desc">Clinical AI fails at the integration layer — not the model layer. This course fixes that gap by teaching the exact data engineering stack that connects hospital systems to inference engines.</p>
    </div>

    <div class="purpose-grid">
      <div class="purpose-card reveal" style="--card-accent:var(--teal);--card-bg:rgba(13,148,136,0.1)">
        <div class="card-icon">🏥</div>
        <div class="card-title">Real-world, not theoretical</div>
        <div class="card-desc">Every concept is grounded in production deployments at major academic medical centers — including the MySurgeryRisk platform at UF Shands Hospital.</div>
      </div>
      <div class="purpose-card reveal" style="--card-accent:var(--blue);--card-bg:rgba(59,130,246,0.1)">
        <div class="card-icon">⚡</div>
        <div class="card-title">End-to-end pipeline mastery</div>
        <div class="card-desc">From raw HL7 v2 byte streams to CDS Hooks alert cards inside Epic — you will own the full stack, not just isolated pieces.</div>
      </div>
      <div class="purpose-card reveal" style="--card-accent:var(--amber);--card-bg:rgba(245,158,11,0.1)">
        <div class="card-icon">🆓</div>
        <div class="card-title">Zero tool cost to learn</div>
        <div class="card-desc">Mirth Connect Community Edition, Epic FHIR public sandbox, HAPI FHIR Server, and HAPI TestPanel are all free. No hospital system access required.</div>
      </div>
      <div class="purpose-card reveal" style="--card-accent:var(--coral);--card-bg:rgba(249,115,22,0.1)">
        <div class="card-icon">🤖</div>
        <div class="card-title">AI-first integration design</div>
        <div class="card-desc">Every architectural decision — trigger events, channel filters, FHIR query patterns — is made with downstream AI inference in mind, not just data movement.</div>
      </div>
    </div>

  </div>
</section>

<hr class="divider">

<!-- ── FOR WHO ── -->
<section>
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Who is this for</p>
      <h2 class="section-title">Built for practitioners,<br>not observers</h2>
      <p class="section-desc">This is a hands-on engineering course. If you write code and want to build or extend clinical AI systems, you belong here.</p>
    </div>

    <div class="audience-list">
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>ML engineers &amp; AI architects</strong> working in healthcare or moving into the space who need to understand how clinical data actually flows.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Software engineers</strong> tasked with Epic or EHR integration projects who need to understand HL7, FHIR, and Mirth from first principles.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Clinical informaticists</strong> and health IT professionals who want to add AI/ML integration capability to their existing domain expertise.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Researchers building clinical AI models</strong> who need to understand how production hospital data is structured, ingested, and governed.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Developers from other domains</strong> — fintech, IoT, enterprise software — making a deliberate move into health tech.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Biomedical informatics students</strong> and postdocs who want production-level engineering skills alongside their academic training.</div>
      </div>
    </div>

    <div class="prereq-box reveal">
      <div class="prereq-title">
        <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        Prerequisites — you need these coming in
      </div>
      <div class="prereq-list">
        <span class="prereq-tag">Python (intermediate)</span>
        <span class="prereq-tag">REST APIs &amp; JSON</span>
        <span class="prereq-tag">Basic OAuth concepts</span>
        <span class="prereq-tag">Command-line comfort</span>
        <span class="prereq-tag">Docker basics (M8)</span>
      </div>
    </div>

  </div>
</section>

<hr class="divider">

<!-- ── CODE PREVIEW ── -->
<section style="padding:60px 0">
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Sample content</p>
      <h2 class="section-title">Real code, real patterns</h2>
      <p class="section-desc">Every lab produces working code you can deploy. Here's a taste of what you'll build in Module 3.</p>
    </div>
    <div class="code-preview reveal">
      <div class="code-bar">
        <div class="code-dot" style="background:#ff5f57"></div>
        <div class="code-dot" style="background:#febc2e"></div>
        <div class="code-dot" style="background:#28c840"></div>
        <div class="code-filename">mirth_transformer.js &nbsp;·&nbsp; Module 3 — Mirth Connect</div>
      </div>
      <div class="code-body">
<span class="c-comment">// HL7 v2 OBX → FHIR R4 Observation — Mirth destination transformer</span>
<span class="c-plain">
</span><span class="c-kw">var</span> <span class="c-plain">mrn   = </span><span class="c-obj">msg</span><span class="c-plain">['PID']['PID.3']['PID.3.1'].toString();
</span><span class="c-kw">var</span> <span class="c-plain">loinc = </span><span class="c-obj">msg</span><span class="c-plain">['OBX'][0]['OBX.3']['OBX.3.1'].toString();
</span><span class="c-kw">var</span> <span class="c-plain">val   = parseFloat(</span><span class="c-obj">msg</span><span class="c-plain">['OBX'][0]['OBX.5']['OBX.5.1'].toString());
</span><span class="c-kw">var</span> <span class="c-plain">flag  = </span><span class="c-obj">msg</span><span class="c-plain">['OBX'][0]['OBX.8']['OBX.8.1'].toString();
</span><span class="c-plain">
</span><span class="c-kw">var</span> <span class="c-plain">fhir = {
  resourceType: </span><span class="c-str">'Observation'</span><span class="c-plain">,
  status:       </span><span class="c-str">'final'</span><span class="c-plain">,
  subject:      { reference: </span><span class="c-str">'Patient?identifier=urn:epic:mrn|'</span><span class="c-plain"> + mrn },
  code:         { coding: [{ system: </span><span class="c-str">'http://loinc.org'</span><span class="c-plain">, code: loinc }] },
  valueQuantity:{ value: val, unit: </span><span class="c-str">'mg/dL'</span><span class="c-plain"> },
  interpretation: flag ? [{ coding: [{ code: flag }] }] : </span><span class="c-kw">undefined</span>
<span class="c-plain">};
</span><span class="c-plain">
</span><span class="c-fn">channelMap</span><span class="c-plain">.put(</span><span class="c-str">'fhirPayload'</span><span class="c-plain">, JSON.stringify(fhir));
</span><span class="c-comment">// → Destination: HTTP POST to HAPI FHIR server /fhir/r4/Observation</span>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ── CURRICULUM ── -->
<section id="curriculum">
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Curriculum</p>
      <h2 class="section-title">8 modules, end to end</h2>
      <p class="section-desc">Structured from fundamentals to production — each module builds on the last, culminating in a fully deployed clinical AI pipeline.</p>
    </div>

    <div class="module-list">

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M1</div>
          <div class="module-accent" style="--m-color:#0d9488"></div>
          <div class="module-info">
            <div class="module-title">Foundation: HL7 v2 Messaging Deep Dive</div>
            <div class="module-meta">
              <div class="module-duration">~90 min</div>
              <div class="module-tags"><span class="mtag">7 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">MSH / PID / OBX segments</span>
          <span class="lesson-pill">ADT trigger events</span>
          <span class="lesson-pill">MLLP transport</span>
          <span class="lesson-pill">HAPI TestPanel lab</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M2</div>
          <div class="module-accent" style="--m-color:#3b82f6"></div>
          <div class="module-info">
            <div class="module-title">FHIR R4 for Clinical AI Practitioners</div>
            <div class="module-meta">
              <div class="module-duration">~110 min</div>
              <div class="module-tags"><span class="mtag">9 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Patient / Observation / Condition</span>
          <span class="lesson-pill">$lastn operation</span>
          <span class="lesson-pill">Bulk Data $export</span>
          <span class="lesson-pill">Epic sandbox queries</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M3</div>
          <div class="module-accent" style="--m-color:#14b8a6"></div>
          <div class="module-info">
            <div class="module-title">Mirth Connect: Channel Engineering</div>
            <div class="module-meta">
              <div class="module-duration">~130 min</div>
              <div class="module-tags"><span class="mtag">10 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">JS transformers</span>
          <span class="lesson-pill">Content-based routing</span>
          <span class="lesson-pill">Dead-letter queues</span>
          <span class="lesson-pill">CI/CD via Mirth REST API</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M4</div>
          <div class="module-accent" style="--m-color:#8b5cf6"></div>
          <div class="module-info">
            <div class="module-title">Epic Integration: SMART on FHIR &amp; Interconnect</div>
            <div class="module-meta">
              <div class="module-duration">~120 min</div>
              <div class="module-tags"><span class="mtag">9 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">SMART OAuth 2.0 flows</span>
          <span class="lesson-pill">JWT client assertion</span>
          <span class="lesson-pill">CDS Hooks cards</span>
          <span class="lesson-pill">App Orchard registration</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M5</div>
          <div class="module-accent" style="--m-color:#f59e0b"></div>
          <div class="module-info">
            <div class="module-title">FHIR Feature Extraction for AI Models</div>
            <div class="module-meta">
              <div class="module-duration">~100 min</div>
              <div class="module-tags"><span class="mtag">8 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Time-series lab features</span>
          <span class="lesson-pill">Charlson / Elixhauser scoring</span>
          <span class="lesson-pill">FHIR feature store</span>
          <span class="lesson-pill">Missing data imputation</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M6</div>
          <div class="module-accent" style="--m-color:#f97316"></div>
          <div class="module-info">
            <div class="module-title">Clinical AI Inference &amp; CDS Hooks</div>
            <div class="module-meta">
              <div class="module-duration">~120 min</div>
              <div class="module-tags"><span class="mtag">8 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">FastAPI inference service</span>
          <span class="lesson-pill">FHIR RiskAssessment write-back</span>
          <span class="lesson-pill">ADT trigger → model loop</span>
          <span class="lesson-pill">Alert fatigue strategy</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M7</div>
          <div class="module-accent" style="--m-color:#06b6d4"></div>
          <div class="module-info">
            <div class="module-title">NLP on Clinical Notes via DocumentReference</div>
            <div class="module-meta">
              <div class="module-duration">~90 min</div>
              <div class="module-tags"><span class="mtag">8 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">scispaCy entity extraction</span>
          <span class="lesson-pill">SDOH from free text</span>
          <span class="lesson-pill">LLM note summarization</span>
          <span class="lesson-pill">FHIR write-back of NLP output</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M8</div>
          <div class="module-accent" style="--m-color:#ef4444"></div>
          <div class="module-info">
            <div class="module-title">Production, Compliance &amp; MLOps</div>
            <div class="module-meta">
              <div class="module-duration">~100 min</div>
              <div class="module-tags"><span class="mtag">9 lessons</span><span class="mtag">1 lab</span><span class="mtag">case study</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">HIPAA Safe Harbor de-ID</span>
          <span class="lesson-pill">MLflow model registry</span>
          <span class="lesson-pill">Evidently AI monitoring</span>
          <span class="lesson-pill">MySurgeryRisk case study</span>
          <span class="lesson-pill">FDA SaMD landscape</span>
        </div>
      </div>

    </div>

  </div>
</section>

<hr class="divider">

<!-- ── WHAT YOU BUILD ── -->
<section>
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Capstone projects</p>
      <h2 class="section-title">Three production systems<br>you will build</h2>
      <p class="section-desc">Labs are not toy exercises. Each produces a deployable artifact you can show, extend, and put in a portfolio.</p>
    </div>

    <div class="build-grid">
      <div class="build-card reveal">
        <div class="build-num">01</div>
        <div class="build-icon">🔌</div>
        <div class="build-title">HL7 → FHIR Integration Channel</div>
        <div class="build-desc">A fully working Mirth Connect channel that receives Epic HL7 v2 ADT and ORU feeds, transforms them to FHIR R4 Observation and Patient resources, and POSTs them to a local HAPI FHIR server with audit logging.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">02</div>
        <div class="build-icon">🧠</div>
        <div class="build-title">Real-Time Sepsis Risk Pipeline</div>
        <div class="build-desc">Mirth ADT trigger → FHIR feature extraction → XGBoost inference → CDS Hooks alert card surfaced inside a simulated Epic clinician workflow, with FHIR RiskAssessment write-back and MLflow tracking.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">03</div>
        <div class="build-icon">📄</div>
        <div class="build-title">Clinical NLP Pipeline</div>
        <div class="build-desc">A pipeline that retrieves H&amp;P notes via FHIR DocumentReference, extracts medications, diagnoses, and social determinants using scispaCy, and writes structured FHIR Observations back to the server.</div>
      </div>
    </div>

  </div>
</section>

<hr class="divider">

<!-- ── STACK ── -->
<section class="stack-section">
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Technology stack</p>
      <h2 class="section-title">Every tool is free</h2>
    </div>
    <div class="stack-grid reveal">
      <div class="stack-item"><div class="stack-dot" style="background:var(--teal)"></div>Mirth Connect CE</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--blue)"></div>FHIR R4 (Epic sandbox)</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--teal2)"></div>HAPI FHIR Server</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--blue2)"></div>HAPI TestPanel</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--amber)"></div>FastAPI</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--coral)"></div>XGBoost / scikit-learn</div>
      <div class="stack-item"><div class="stack-dot" style="background:#a78bfa"></div>scispaCy</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--teal)"></div>MLflow</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--blue)"></div>Evidently AI</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--amber2)"></div>PostgreSQL / Redis</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--muted)"></div>Docker</div>
      <div class="stack-item"><div class="stack-dot" style="background:#f472b6"></div>CDS Hooks</div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ── INSTRUCTOR ── -->
<section>
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Instructor</p>
      <h2 class="section-title">Built by someone who<br>shipped it in production</h2>
    </div>

    <div class="instructor-card reveal">
      <div class="instructor-avatar">MM</div>
      <div class="instructor-info">
        <div class="instructor-name">Mohcine Madkour, PhD</div>
        <div class="instructor-title">Senior AI/ML Engineer &amp; Architect · Biomedical Informatics</div>
        <div class="instructor-bio">
          I have spent the last decade building AI systems that run on real hospital data — from the MySurgeryRisk surgical risk prediction platform at UF Shands, to predictive maintenance systems at Intuitive Surgical, to connected diagnostics at Cummins. I have written the Mirth transformers, debugged the HL7 feeds, navigated Epic interface team relationships, and shipped models that touched patient care. This course teaches what I wish existed when I started.
        </div>
        <div class="instructor-creds">
          <span class="cred-badge">PhD Computer Science</span>
          <span class="cred-badge">Postdoc · UTHealth Houston</span>
          <span class="cred-badge">Intuitive Surgical</span>
          <span class="cred-badge">Cummins</span>
          <span class="cred-badge">UF Shands · MySurgeryRisk</span>
          <span class="cred-badge">AI/ML Boot Camp Instructor</span>
        </div>
      </div>
    </div>

  </div>
</section>

<hr class="divider">

<!-- ── CONCLUSION / CTA ── -->
<section class="cta-section">
  <div class="container">
    <div class="cta-label reveal">Launch offer — limited time</div>
    <h2 class="cta-title reveal">
      Stop guessing how<br><em>clinical data actually flows</em>
    </h2>
    <p class="cta-desc reveal">
      In 14 hours you will go from "what is an OBX segment" to deploying a FHIR-native AI inference service that surfaces risk scores inside Epic. All tools are free. All labs produce real, deployable code.
    </p>

    <div class="cta-pricing reveal">
      <div class="price-launch">$19.99</div>
      <div class="price-meta">
        <div class="price-list">List price $129.99</div>
        <div class="price-tag">Launch discount · limited seats</div>
      </div>
    </div>

    <br>

    <a href="https://udemy.com" class="cta-btn reveal" target="_blank">
      Enroll on Udemy
      <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
    </a>

    <div class="cta-fine reveal">30-day Udemy money-back guarantee · lifetime access · certificate of completion</div>

  </div>
</section>

<!-- ── FOOTER ── -->
<div class="container">
  <div class="footer">
    <span>© 2025 Mohcine Madkour, PhD — <a href="{{ site.baseurl }}/">mohcinemadkour.com</a></span>
    <span style="font-family:'DM Mono',monospace;font-size:11px">HL7 · FHIR R4 · Mirth Connect · Epic · Clinical AI</span>
  </div>
</div>

<script>
  // Intersection observer for .reveal elements
  const obs = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        setTimeout(() => e.target.classList.add('visible'), i * 60);
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
</script>
</body>
</html>
