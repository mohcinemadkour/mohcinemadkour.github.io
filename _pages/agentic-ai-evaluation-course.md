---
layout: none
title: "Agentic AI Evaluation: Production-Ready Systems — Udemy Course"
permalink: /agentic-ai-evaluation-course/
description: Build automated evaluation pipelines for RAG and agentic AI systems using LangGraph, LangSmith, and RAGAS.
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agentic AI Evaluation: Production-Ready Systems — Udemy Course</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Mono:ital,wght@0,400;0,500;1,400&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --navy:   #0a1628;
    --navy2:  #112240;
    --purple: #7c3aed;
    --purple2:#a78bfa;
    --purple3:#ede9fe;
    --teal:   #0d9488;
    --teal2:  #14b8a6;
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

body::before {
content: '';
position: fixed; inset: 0;
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
opacity: 0.03;
pointer-events: none;
z-index: 0;
}

.blob { position: fixed; border-radius: 50%; filter: blur(120px); pointer-events: none; z-index: 0; }
.blob-1 { width: 500px; height: 500px; background: rgba(124,58,237,0.15); top: -100px; right: -100px; }
.blob-2 { width: 400px; height: 400px; background: rgba(13,148,136,0.10); bottom: 200px; left: -100px; }
.blob-3 { width: 300px; height: 300px; background: rgba(59,130,246,0.08); top: 50%; left: 50%; transform: translate(-50%,-50%); }

.container { max-width: 900px; margin: 0 auto; padding: 0 28px; position: relative; z-index: 1; }
section { padding: 80px 0; }

/_ ── HERO ── _/
.hero { min-height: 100vh; display: flex; align-items: center; padding: 80px 0 60px; position: relative; }

.hero-eyebrow {
display: inline-flex; align-items: center; gap: 8px;
font-family: 'DM Mono', monospace;
font-size: 11px; letter-spacing: .15em; text-transform: uppercase;
color: var(--purple2);
border: 1px solid rgba(167,139,250,0.3);
padding: 6px 14px; border-radius: 100px;
margin-bottom: 32px;
animation: fadeUp .6s ease both;
}
.hero-eyebrow::before {
content: '';
width: 6px; height: 6px; border-radius: 50%;
background: var(--purple2);
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
.hero-title .accent { color: var(--purple2); }
.hero-title .line2 { display: block; color: var(--muted); font-weight: 400; font-size: .55em; letter-spacing: 0; margin-top: 6px; }

.hero-sub {
font-size: 18px; color: var(--muted); max-width: 580px;
line-height: 1.7; margin-bottom: 40px; font-weight: 300;
animation: fadeUp .6s .2s ease both;
}

.hero-cta { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; animation: fadeUp .6s .3s ease both; }

.btn-primary {
display: inline-flex; align-items: center; gap: 8px;
background: var(--purple);
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
.btn-primary:hover { background: var(--purple2); transform: translateY(-1px); }
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
.stat-num { font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 700; color: var(--white); }
.stat-num span { color: var(--purple2); }
.stat-label { font-size: 12px; color: var(--muted); letter-spacing: .04em; }

/_ ── EVAL PYRAMID BAR ── _/
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
background: linear-gradient(90deg, var(--purple), var(--blue), var(--teal2), var(--amber), var(--coral));
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
.section-tag { font-family: 'DM Mono', monospace; font-size: 11px; letter-spacing: .15em; text-transform: uppercase; color: var(--purple2); margin-bottom: 12px; }
.section-title { font-family: 'Syne', sans-serif; font-size: clamp(28px, 4vw, 44px); font-weight: 700; line-height: 1.1; letter-spacing: -.02em; margin-bottom: 16px; }
.section-desc { font-size: 17px; color: var(--muted); max-width: 580px; font-weight: 300; line-height: 1.7; }

/_ ── PURPOSE ── _/
.purpose-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-top: 48px; }
.purpose-card {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 12px; padding: 24px;
position: relative; overflow: hidden;
transition: border-color .2s, transform .2s;
}
.purpose-card:hover { border-color: rgba(167,139,250,0.4); transform: translateY(-2px); }
.purpose-card::before {
content: '';
position: absolute; top: 0; left: 0; right: 0; height: 2px;
background: var(--card-accent, var(--purple));
opacity: 0; transition: opacity .2s;
}
.purpose-card:hover::before { opacity: 1; }
.card-icon { width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 18px; margin-bottom: 14px; background: var(--card-bg, rgba(124,58,237,0.12)); }
.card-title { font-family: 'Syne', sans-serif; font-weight: 600; font-size: 16px; margin-bottom: 8px; }
.card-desc { font-size: 14px; color: var(--muted); line-height: 1.6; }

/_ ── AUDIENCE ── _/
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
background: rgba(124,58,237,0.15);
border: 1px solid rgba(167,139,250,0.4);
display: flex; align-items: center; justify-content: center;
flex-shrink: 0; margin-top: 1px;
font-size: 11px; color: var(--purple2);
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
border-radius: 12px; overflow: hidden;
transition: border-color .2s;
}
.module-item:hover { border-color: rgba(255,255,255,0.15); }
.module-header { display: flex; align-items: center; gap: 16px; padding: 20px 24px; }
.module-num { font-family: 'DM Mono', monospace; font-size: 11px; font-weight: 500; color: var(--muted); width: 28px; flex-shrink: 0; }
.module-accent { width: 4px; height: 36px; border-radius: 2px; flex-shrink: 0; background: var(--m-color, var(--purple)); }
.module-info { flex: 1; }
.module-title { font-family: 'Syne', sans-serif; font-weight: 600; font-size: 15px; margin-bottom: 3px; }
.module-meta { display: flex; gap: 14px; align-items: center; }
.module-duration { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--muted); }
.module-tags { display: flex; gap: 6px; }
.mtag { font-size: 11px; padding: 2px 8px; border-radius: 4px; font-family: 'DM Mono', monospace; background: rgba(255,255,255,0.05); color: var(--muted); }
.module-lessons { padding: 0 24px 20px 68px; display: flex; flex-wrap: wrap; gap: 8px; }
.lesson-pill {
font-size: 12px; padding: 4px 10px; border-radius: 6px;
background: rgba(255,255,255,0.04);
border: 1px solid rgba(255,255,255,0.06);
color: var(--muted);
transition: color .15s, border-color .15s;
}
.module-item:hover .lesson-pill { color: rgba(255,255,255,0.7); border-color: rgba(255,255,255,0.1); }

/_ ── TRACK LABEL ── _/
.track-label {
font-family: 'DM Mono', monospace;
font-size: 11px; letter-spacing: .15em; text-transform: uppercase;
color: var(--muted);
padding: 8px 0 4px;
border-bottom: 1px solid var(--border);
margin-bottom: 12px;
display: flex; align-items: center; gap: 10px;
}
.track-label span { color: var(--purple2); }

/_ ── WHAT YOU BUILD ── _/
.build-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 48px; }
.build-card {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 14px; padding: 28px 24px;
position: relative; overflow: hidden;
}
.build-num { font-family: 'Syne', sans-serif; font-size: 64px; font-weight: 800; color: rgba(255,255,255,0.04); position: absolute; top: 8px; right: 16px; line-height: 1; pointer-events: none; }
.build-icon { font-size: 28px; margin-bottom: 16px; }
.build-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 17px; margin-bottom: 10px; }
.build-desc { font-size: 13px; color: var(--muted); line-height: 1.65; }

/_ ── CODE SNIPPET ── _/
.code-preview { background: #0d1117; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; overflow: hidden; margin-top: 48px; }
.code-bar { display: flex; align-items: center; gap: 8px; padding: 12px 16px; background: rgba(255,255,255,0.04); border-bottom: 1px solid rgba(255,255,255,0.06); }
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

/_ ── INSTRUCTOR ── _/
.instructor-card {
background: var(--navy2);
border: 1px solid var(--border);
border-radius: 16px; padding: 36px;
display: flex; gap: 32px; align-items: flex-start; flex-wrap: wrap;
margin-top: 48px; position: relative; overflow: hidden;
}
.instructor-card::after {
content: '';
position: absolute; top: 0; right: 0;
width: 300px; height: 300px;
background: radial-gradient(circle at top right, rgba(124,58,237,0.08), transparent 70%);
pointer-events: none;
}
.instructor-avatar {
width: 80px; height: 80px; border-radius: 50%; flex-shrink: 0;
background: linear-gradient(135deg, var(--purple), var(--blue));
display: flex; align-items: center; justify-content: center;
font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800; color: #fff;
border: 3px solid rgba(167,139,250,0.3);
}
.instructor-info { flex: 1; min-width: 220px; }
.instructor-name { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700; margin-bottom: 4px; }
.instructor-title { font-size: 14px; color: var(--purple2); margin-bottom: 14px; }
.instructor-bio { font-size: 14px; color: var(--muted); line-height: 1.7; margin-bottom: 16px; }
.instructor-creds { display: flex; flex-wrap: wrap; gap: 8px; }
.cred-badge { font-size: 12px; padding: 4px 12px; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: var(--muted); }

/_ ── CTA ── _/
.cta-section { text-align: center; padding: 100px 0; position: relative; }
.cta-section::before {
content: '';
position: absolute; top: 0; left: 50%; transform: translateX(-50%);
width: 1px; height: 80px;
background: linear-gradient(to bottom, transparent, var(--border));
}
.cta-label { font-family: 'DM Mono', monospace; font-size: 11px; letter-spacing: .15em; text-transform: uppercase; color: var(--amber); margin-bottom: 20px; }
.cta-title { font-family: 'Syne', sans-serif; font-size: clamp(32px, 5vw, 56px); font-weight: 800; line-height: 1.1; letter-spacing: -.02em; margin-bottom: 20px; }
.cta-title em { color: var(--purple2); font-style: normal; }
.cta-desc { font-size: 17px; color: var(--muted); max-width: 520px; margin: 0 auto 40px; line-height: 1.7; font-weight: 300; }
.cta-pricing {
display: inline-flex; align-items: center; gap: 16px;
background: rgba(245,158,11,0.08);
border: 1px solid rgba(245,158,11,0.2);
border-radius: 12px; padding: 16px 28px; margin-bottom: 32px;
}
.price-launch { font-family: 'Syne', sans-serif; font-size: 36px; font-weight: 800; color: var(--amber); }
.price-meta { text-align: left; }
.price-list { font-size: 13px; color: var(--muted); text-decoration: line-through; }
.price-tag { font-size: 12px; color: var(--amber2); font-family: 'DM Mono', monospace; }
.cta-btn {
display: inline-flex; align-items: center; gap: 10px;
background: var(--purple); color: #fff;
font-family: 'Syne', sans-serif; font-weight: 700; font-size: 17px;
padding: 18px 40px; border-radius: 10px;
text-decoration: none; border: none; cursor: pointer;
transition: background .2s, transform .15s, box-shadow .2s;
box-shadow: 0 0 40px rgba(124,58,237,0.3);
}
.cta-btn:hover { background: var(--purple2); transform: translateY(-2px); box-shadow: 0 0 60px rgba(167,139,250,0.4); }
.cta-fine { font-size: 12px; color: var(--muted); margin-top: 20px; font-family: 'DM Mono', monospace; }

/_ ── DIVIDER ── _/
.divider { border: none; height: 1px; background: var(--border); margin: 0; }

/_ ── ANIMATIONS ── _/
@keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.reveal { opacity: 0; transform: translateY(24px); transition: opacity .6s ease, transform .6s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }

/_ ── FOOTER ── _/
.footer {
padding: 32px 0;
border-top: 1px solid var(--border);
display: flex; justify-content: space-between; align-items: center;
flex-wrap: wrap; gap: 12px;
font-size: 13px; color: var(--muted);
}
.footer a { color: var(--purple2); text-decoration: none; }
.footer a:hover { color: var(--purple3); }

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
    <div class="hero-eyebrow">Coming to Udemy &nbsp;·&nbsp; New course 2026</div>

    <h1 class="hero-title">
      Agentic AI Evaluation<br>
      <span class="accent">Production-Ready Systems</span>
      <span class="line2">LangGraph · LangSmith · RAGAS · CI/CD Quality Gates</span>
    </h1>

    <p class="hero-sub">
      Move beyond "it works in the demo." Build automated, rigorous evaluation pipelines for your RAG and agentic AI systems — measuring retrieval quality, generation faithfulness, latency, and cost, all the way to GitHub Actions deployment gates.
    </p>

    <div class="hero-cta">
      <a href="https://udemy.com" class="btn-primary" target="_blank">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        Join the waitlist
      </a>
      <a href="#curriculum" class="btn-ghost">View curriculum ↓</a>
    </div>

    <div class="hero-stats">
      <div class="stat-item">
        <div class="stat-num">10<span>×</span></div>
        <div class="stat-label">Modules</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">2<span> tracks</span></div>
        <div class="stat-label">Core + Advanced</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">9<span>+</span></div>
        <div class="stat-label">Capstone deliverables</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">$0</div>
        <div class="stat-label">Tool licensing cost</div>
      </div>
    </div>

    <!-- eval pipeline bar -->
    <div class="pipeline-bar" style="margin-top:48px">
      <div class="pipe-node"><span class="label">System</span><span class="value">Agentic RAG</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Retrieval</span><span class="value">RAGAS Eval</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Generation</span><span class="value">LLM-as-Judge</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Tracing</span><span class="value">LangSmith</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Gate</span><span class="value">CI/CD Block</span></div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-node"><span class="label">Monitor</span><span class="value">Drift Alert</span></div>
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
      <p class="section-desc">Shipping an agentic AI system without evaluation infrastructure is like deploying a web service with no monitoring. You will not know when it breaks — until your users tell you.</p>
    </div>

    <div class="purpose-grid">
      <div class="purpose-card reveal" style="--card-accent:var(--purple);--card-bg:rgba(124,58,237,0.1)">
        <div class="card-icon">📉</div>
        <div class="card-title">Silent production failure</div>
        <div class="card-desc">Retrieval drifts, hallucinations slip through, costs balloon — all without a single error log. Evaluation infrastructure is the only way to catch this before users do.</div>
      </div>
      <div class="purpose-card reveal" style="--card-accent:var(--blue);--card-bg:rgba(59,130,246,0.1)">
        <div class="card-icon">🔬</div>
        <div class="card-title">Metrics that actually matter</div>
        <div class="card-desc">Beyond vibe checks and manual spot-testing — NDCG, Hit Rate@K, faithfulness, answer relevancy, and LLM-as-Judge scoring built into your CI pipeline.</div>
      </div>
      <div class="purpose-card reveal" style="--card-accent:var(--teal);--card-bg:rgba(13,148,136,0.1)">
        <div class="card-icon">🏗️</div>
        <div class="card-title">Production patterns, not toy demos</div>
        <div class="card-desc">Every module produces working, deployable artifacts — a retrieval evaluator, a CI quality gate, an embedding drift detector — that you can plug into a real system on day one.</div>
      </div>
      <div class="purpose-card reveal" style="--card-accent:var(--amber);--card-bg:rgba(245,158,11,0.1)">
        <div class="card-icon">🤖</div>
        <div class="card-title">Agentic and multi-hop ready</div>
        <div class="card-desc">Standard RAG evaluation is not enough. This course covers trajectory evaluation, tool call correctness, and consistency testing for multi-agent systems running in production.</div>
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
      <h2 class="section-title">Built for engineers<br>who ship to production</h2>
      <p class="section-desc">This is not an introduction to LLMs. It is an engineering course for practitioners who have already built agentic or RAG systems and need to make them measurably reliable.</p>
    </div>

    <div class="audience-list">
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>ML engineers &amp; AI architects</strong> maintaining RAG or agentic pipelines in production who need systematic quality measurement, not ad-hoc testing.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Senior developers</strong> who have shipped LLM-powered features and now need to instrument them for drift, hallucination, and cost visibility.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>AI architects</strong> designing evaluation strategies for enterprise agentic systems — including multi-agent orchestration with LangGraph.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Data scientists</strong> with Python and LLM API experience who want to move into production MLOps for AI systems beyond classical ML monitoring.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Healthcare and clinical AI engineers</strong> who need domain-specific evaluation rubrics — the M9 case study covers hallucination detection in a production clinical RAG system.</div>
      </div>
      <div class="audience-item reveal">
        <div class="audience-check">✓</div>
        <div class="audience-text"><strong>Platform and DevOps engineers</strong> who own CI/CD pipelines and need to understand what quality gates for AI systems should look like before implementing them.</div>
      </div>
    </div>

    <div class="prereq-box reveal">
      <div class="prereq-title">
        <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        Prerequisites — you need these coming in
      </div>
      <div class="prereq-list">
        <span class="prereq-tag">Python (intermediate)</span>
        <span class="prereq-tag">LLM API basics</span>
        <span class="prereq-tag">RAG fundamentals</span>
        <span class="prereq-tag">Git &amp; command line</span>
        <span class="prereq-tag">Docker basics (M8+)</span>
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
      <h2 class="section-title">Real evaluators, real code</h2>
      <p class="section-desc">Every module produces working code you can deploy. Here's a taste of the retrieval evaluator you will build in Module 3.</p>
    </div>
    <div class="code-preview reveal">
      <div class="code-bar">
        <div class="code-dot" style="background:#ff5f57"></div>
        <div class="code-dot" style="background:#febc2e"></div>
        <div class="code-dot" style="background:#28c840"></div>
        <div class="code-filename">retrieval_evaluator.py &nbsp;·&nbsp; Module 3 — Building Retrieval Evaluators</div>
      </div>
      <div class="code-body">
<span class="c-comment"># Evaluate retrieval quality with Hit Rate@K, MRR, and NDCG</span>
<span class="c-plain">
</span><span class="c-kw">from</span><span class="c-plain"> ragas.metrics </span><span class="c-kw">import</span><span class="c-plain"> </span><span class="c-obj">ContextPrecision</span><span class="c-plain">, </span><span class="c-obj">ContextRecall</span>
<span class="c-kw">from</span><span class="c-plain"> datasets </span><span class="c-kw">import</span><span class="c-plain"> </span><span class="c-obj">Dataset</span>
<span class="c-kw">import</span><span class="c-plain"> numpy </span><span class="c-kw">as</span><span class="c-plain"> np
</span><span class="c-plain">
</span><span class="c-kw">def</span> <span class="c-fn">ndcg_at_k</span><span class="c-plain">(retrieved_ids, relevant_ids, k=</span><span class="c-val">5</span><span class="c-plain">):
    </span><span class="c-str">"""Normalized Discounted Cumulative Gain @K"""</span>
<span class="c-plain">    hits = [</span><span class="c-val">1</span><span class="c-plain"> </span><span class="c-kw">if</span><span class="c-plain"> doc </span><span class="c-kw">in</span><span class="c-plain"> relevant_ids </span><span class="c-kw">else</span><span class="c-plain"> </span><span class="c-val">0</span><span class="c-plain">
            </span><span class="c-kw">for</span><span class="c-plain"> doc </span><span class="c-kw">in</span><span class="c-plain"> retrieved_ids[:k]]
    dcg  = sum(h / np.log2(i + </span><span class="c-val">2</span><span class="c-plain">) </span><span class="c-kw">for</span><span class="c-plain"> i, h </span><span class="c-kw">in</span><span class="c-plain"> enumerate(hits))
    idcg = sum(</span><span class="c-val">1</span><span class="c-plain"> / np.log2(i + </span><span class="c-val">2</span><span class="c-plain">) </span><span class="c-kw">for</span><span class="c-plain"> i </span><span class="c-kw">in</span><span class="c-plain"> range(min(len(relevant_ids), k)))
    </span><span class="c-kw">return</span><span class="c-plain"> dcg / idcg </span><span class="c-kw">if</span><span class="c-plain"> idcg </span><span class="c-kw">else</span><span class="c-plain"> </span><span class="c-val">0.0</span>
<span class="c-plain">
</span><span class="c-comment"># Run full eval against golden dataset</span>
<span class="c-plain">eval_data = </span><span class="c-obj">Dataset</span><span class="c-plain">.from_dict({
    </span><span class="c-str">"question"</span><span class="c-plain">:    golden_questions,
    </span><span class="c-str">"contexts"</span><span class="c-plain">:    retrieved_contexts,
    </span><span class="c-str">"ground_truth"</span><span class="c-plain">: reference_answers,
})
results = </span><span class="c-fn">evaluate</span><span class="c-plain">(eval_data, metrics=[</span><span class="c-obj">ContextPrecision</span><span class="c-plain">(), </span><span class="c-obj">ContextRecall</span><span class="c-plain">()])
</span><span class="c-comment"># → Publishes scores to LangSmith experiment dashboard</span>
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
      <h2 class="section-title">10 modules across two tracks</h2>
      <p class="section-desc">Track A builds the foundation — retrieval evaluation, generation scoring, and CI/CD gates. Track B extends into drift detection, cost optimization, multi-agent evaluation, and a healthcare case study.</p>
    </div>

    <div class="module-list">

      <div class="track-label reveal"><span>Track A</span> — Core Curriculum (Modules 1–5)</div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M1</div>
          <div class="module-accent" style="--m-color:#7c3aed"></div>
          <div class="module-info">
            <div class="module-title">Why Evaluation Matters</div>
            <div class="module-meta">
              <div class="module-duration">~60 min</div>
              <div class="module-tags"><span class="mtag">5 lessons</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">The evaluation problem in production</span>
          <span class="lesson-pill">The Evaluation Pyramid</span>
          <span class="lesson-pill">What "production-ready" actually means</span>
          <span class="lesson-pill">Course roadmap walkthrough</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M2</div>
          <div class="module-accent" style="--m-color:#3b82f6"></div>
          <div class="module-info">
            <div class="module-title">Metrics Demystified</div>
            <div class="module-meta">
              <div class="module-duration">~80 min</div>
              <div class="module-tags"><span class="mtag">6 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Retrieval vs generation metrics</span>
          <span class="lesson-pill">Precision, Recall, F1 for RAG</span>
          <span class="lesson-pill">LangSmith setup &amp; tracing</span>
          <span class="lesson-pill">First experiment run</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M3</div>
          <div class="module-accent" style="--m-color:#14b8a6"></div>
          <div class="module-info">
            <div class="module-title">Building Retrieval Evaluators</div>
            <div class="module-meta">
              <div class="module-duration">~100 min</div>
              <div class="module-tags"><span class="mtag">7 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Hit Rate@K</span>
          <span class="lesson-pill">MRR implementation</span>
          <span class="lesson-pill">NDCG from scratch</span>
          <span class="lesson-pill">RAGAS context precision &amp; recall</span>
          <span class="lesson-pill">Golden dataset construction</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M4</div>
          <div class="module-accent" style="--m-color:#f59e0b"></div>
          <div class="module-info">
            <div class="module-title">Generation Quality &amp; LLM-as-Judge</div>
            <div class="module-meta">
              <div class="module-duration">~110 min</div>
              <div class="module-tags"><span class="mtag">8 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">RAGAS faithfulness scoring</span>
          <span class="lesson-pill">Answer relevancy metric</span>
          <span class="lesson-pill">LLM-as-Judge pipeline design</span>
          <span class="lesson-pill">Bias mitigation strategies</span>
          <span class="lesson-pill">Human-in-the-loop calibration</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M5</div>
          <div class="module-accent" style="--m-color:#f97316"></div>
          <div class="module-info">
            <div class="module-title">CI/CD Quality Gates</div>
            <div class="module-meta">
              <div class="module-duration">~90 min</div>
              <div class="module-tags"><span class="mtag">7 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">GitHub Actions eval workflow</span>
          <span class="lesson-pill">Threshold configuration</span>
          <span class="lesson-pill">Blocking deployments on quality drop</span>
          <span class="lesson-pill">LangSmith experiment comparison</span>
        </div>
      </div>

      <div class="track-label reveal" style="margin-top:24px"><span>Track B</span> — Advanced Modules (Modules 6–10)</div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M6</div>
          <div class="module-accent" style="--m-color:#06b6d4"></div>
          <div class="module-info">
            <div class="module-title">Embedding Drift &amp; Re-indexing</div>
            <div class="module-meta">
              <div class="module-duration">~90 min</div>
              <div class="module-tags"><span class="mtag">6 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Cosine centroid drift detection</span>
          <span class="lesson-pill">Spearman correlation monitoring</span>
          <span class="lesson-pill">Chunk-level citation tracking</span>
          <span class="lesson-pill">Re-indexing strategy</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M7</div>
          <div class="module-accent" style="--m-color:#8b5cf6"></div>
          <div class="module-info">
            <div class="module-title">Latency &amp; Cost Optimization</div>
            <div class="module-meta">
              <div class="module-duration">~80 min</div>
              <div class="module-tags"><span class="mtag">6 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Pipeline profiling</span>
          <span class="lesson-pill">Cost-per-query analysis</span>
          <span class="lesson-pill">Latency vs quality tradeoff</span>
          <span class="lesson-pill">Caching strategies</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M8</div>
          <div class="module-accent" style="--m-color:#ec4899"></div>
          <div class="module-info">
            <div class="module-title">Multi-Agent Evaluation</div>
            <div class="module-meta">
              <div class="module-duration">~100 min</div>
              <div class="module-tags"><span class="mtag">7 lessons</span><span class="mtag">1 lab</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Trajectory evaluation</span>
          <span class="lesson-pill">Tool call correctness scoring</span>
          <span class="lesson-pill">Consistency testing across agents</span>
          <span class="lesson-pill">LangGraph tracing with LangSmith</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M9</div>
          <div class="module-accent" style="--m-color:#ef4444"></div>
          <div class="module-info">
            <div class="module-title">Healthcare RAG Case Study</div>
            <div class="module-meta">
              <div class="module-duration">~90 min</div>
              <div class="module-tags"><span class="mtag">6 lessons</span><span class="mtag">case study</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Clinical safety rubric design</span>
          <span class="lesson-pill">Hallucination caught in production</span>
          <span class="lesson-pill">Domain-specific eval patterns</span>
          <span class="lesson-pill">Regulatory &amp; compliance framing</span>
        </div>
      </div>

      <div class="module-item reveal">
        <div class="module-header">
          <div class="module-num">M10</div>
          <div class="module-accent" style="--m-color:#0d9488"></div>
          <div class="module-info">
            <div class="module-title">Capstone Project</div>
            <div class="module-meta">
              <div class="module-duration">~120 min</div>
              <div class="module-tags"><span class="mtag">9 deliverables</span><span class="mtag">portfolio</span></div>
            </div>
          </div>
        </div>
        <div class="module-lessons">
          <span class="lesson-pill">Build your own eval framework</span>
          <span class="lesson-pill">9-deliverable checklist</span>
          <span class="lesson-pill">LangSmith dashboard setup</span>
          <span class="lesson-pill">CI gate deployment</span>
          <span class="lesson-pill">Portfolio writeup</span>
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
      <p class="section-tag">Capstone deliverables</p>
      <h2 class="section-title">Seven production artifacts<br>you will build</h2>
      <p class="section-desc">Labs are not toy exercises. Each produces a deployable artifact you can extend, adapt, and put in a portfolio — or plug directly into a system you already run.</p>
    </div>

    <div class="build-grid">
      <div class="build-card reveal">
        <div class="build-num">01</div>
        <div class="build-icon">🔍</div>
        <div class="build-title">Retrieval Evaluator</div>
        <div class="build-desc">A working evaluator measuring Hit Rate@K, MRR, and NDCG against a golden dataset — publishable directly to a LangSmith experiment for tracking over time.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">02</div>
        <div class="build-icon">⚖️</div>
        <div class="build-title">LLM-as-Judge Pipeline</div>
        <div class="build-desc">An automated generation quality scorer that rates faithfulness and answer relevancy at scale — with calibration against human labels and bias mitigation built in.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">03</div>
        <div class="build-icon">🚦</div>
        <div class="build-title">CI/CD Quality Gate</div>
        <div class="build-desc">A GitHub Actions workflow that runs your eval suite on every PR and blocks deployment if retrieval or generation scores fall below configured thresholds.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">04</div>
        <div class="build-icon">📡</div>
        <div class="build-title">Embedding Drift Detector</div>
        <div class="build-desc">A monitor that tracks cosine centroid shift across your vector index over time and triggers re-indexing workflows when drift exceeds a configurable threshold.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">05</div>
        <div class="build-icon">🧩</div>
        <div class="build-title">Multi-Agent Trajectory Evaluator</div>
        <div class="build-desc">A LangGraph-native evaluator that scores agent trajectories for tool call correctness, step consistency, and final answer quality across multi-hop reasoning chains.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">06</div>
        <div class="build-icon">🏥</div>
        <div class="build-title">Clinical Safety Rubric</div>
        <div class="build-desc">A domain-specific evaluation rubric for healthcare RAG systems — covering hallucination risk tiers, clinical accuracy scoring, and the regulatory framing for AI-in-the-loop systems.</div>
      </div>
      <div class="build-card reveal">
        <div class="build-num">07</div>
        <div class="build-icon">📦</div>
        <div class="build-title">Full Eval Framework</div>
        <div class="build-desc">The capstone deliverable — a complete, modular evaluation framework integrating all prior artifacts, documented and packaged for deployment to any agentic AI system you own.</div>
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
      <h2 class="section-title">All open source, all free</h2>
    </div>
    <div class="stack-grid reveal">
      <div class="stack-item"><div class="stack-dot" style="background:var(--purple2)"></div>LangGraph</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--blue)"></div>LangSmith</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--teal2)"></div>RAGAS</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--blue2)"></div>LangChain</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--amber)"></div>ChromaDB</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--coral)"></div>Anthropic API</div>
      <div class="stack-item"><div class="stack-dot" style="background:#a78bfa"></div>OpenAI API</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--teal)"></div>GitHub Actions</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--blue)"></div>sentence-transformers</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--muted)"></div>Python 3.11+</div>
      <div class="stack-item"><div class="stack-dot" style="background:#f472b6"></div>TruLens</div>
      <div class="stack-item"><div class="stack-dot" style="background:var(--purple)"></div>Hugging Face</div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ── INSTRUCTOR ── -->
<section>
  <div class="container">
    <div class="reveal">
      <p class="section-tag">Instructor</p>
      <h2 class="section-title">Built by someone who<br>caught the failures in production</h2>
    </div>

    <div class="instructor-card reveal">
      <div class="instructor-avatar">MM</div>
      <div class="instructor-info">
        <div class="instructor-name">Mohcine Madkour, PhD</div>
        <div class="instructor-title">Senior AI/ML Engineer &amp; Architect · Biomedical Informatics</div>
        <div class="instructor-bio">
          I have spent a decade building AI systems that run on real data — from the Da Vinci surgical robotics RAG system at Intuitive Surgical, to predictive maintenance pipelines at Cummins ($700K annual savings), to surgical risk prediction at UF Shands (AUC 0.82–0.94). In every one of those systems, the hardest problems were evaluation problems: knowing when retrieval drifted, catching hallucinations before clinicians did, and proving to stakeholders that the system was improving, not just changing. This course is what I wish had existed when I was building those systems.
        </div>
        <div class="instructor-creds">
          <span class="cred-badge">PhD Computer Science</span>
          <span class="cred-badge">Postdoc · UTHealth Houston</span>
          <span class="cred-badge">Intuitive Surgical</span>
          <span class="cred-badge">Cummins · $700K savings</span>
          <span class="cred-badge">UF Shands · MySurgeryRisk</span>
          <span class="cred-badge">AI/ML Boot Camp Instructor</span>
          <span class="cred-badge">SharpestMinds Mentor</span>
        </div>
      </div>
    </div>

  </div>
</section>

<hr class="divider">

<!-- ── CONCLUSION / CTA ── -->
<section class="cta-section">
  <div class="container">
    <div class="cta-label reveal">Early access — launching 2026</div>
    <h2 class="cta-title reveal">
      Stop shipping agentic AI<br><em>without measuring it</em>
    </h2>
    <p class="cta-desc reveal">
      In 10 modules you will go from manual spot-testing to a fully automated evaluation pipeline — with retrieval metrics, LLM-as-Judge scoring, CI/CD gates, and drift detection running on every deployment. All tools are free. All labs produce deployable code.
    </p>

    <div class="cta-pricing reveal">
      <div class="price-launch">$19.99</div>
      <div class="price-meta">
        <div class="price-list">List price $129.99</div>
        <div class="price-tag">Launch discount · early access</div>
      </div>
    </div>

    <br>

    <a href="https://udemy.com" class="cta-btn reveal" target="_blank">
      Join the waitlist on Udemy
      <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
    </a>

    <div class="cta-fine reveal">30-day Udemy money-back guarantee · lifetime access · certificate of completion</div>

  </div>
</section>

<!-- ── FOOTER ── -->
<div class="container">
  <div class="footer">
    <span>© 2026 Mohcine Madkour, PhD — <a href="#">mohcinemadkour.com</a></span>
    <span style="font-family:'DM Mono',monospace;font-size:11px">LangGraph · LangSmith · RAGAS · Agentic AI · MLOps</span>
  </div>
</div>

<script>
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
