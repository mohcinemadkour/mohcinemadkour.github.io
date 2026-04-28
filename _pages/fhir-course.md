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

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--navy);
    color: var(--white);
    line-height: 1.6;
    overflow-x: hidden;
  }

  /* ── NOISE TEXTURE OVERLAY ── */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
    opacity: 0.03;
    pointer-events: none;
    z-index: 0;
  }

  /* ── GLOW BLOBS ── */
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

  /* ── LAYOUT ── */
  .container { max-width: 900px; margin: 0 auto; padding: 0 28px; position: relative; z-index: 1; }

  section { padding: 80px 0; }

  /* ── HERO ── */
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

  /* ── PIPELINE BAR ── */
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

  /* ── SECTION HEADERS ── */
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

  /* ── PURPOSE ── */
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

  /* ── DIVIDER ── */
  .divider {
    border: none;
    height: 1px;
    background: var(--border);
    margin: 0;
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .reveal {
    opacity: 0; transform: translateY(24px);
    transition: opacity .6s ease, transform .6s ease;
  }
  .reveal.visible { opacity: 1; transform: translateY(0); }

  /* ── RESPONSIVE ── */
  @media (max-width: 600px) {
    section { padding: 60px 0; }
    .hero { padding: 60px 0 40px; }
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
    <div class="hero-eyebrow">Coming to Udemy · May 2026</div>

    <h1 class="hero-title">
      HL7 &amp; FHIR Integration<br>
      <span class="accent">for Clinical AI</span>
      <span class="line2">A Practitioner's Guide · Mirth Connect · Epic</span>
    </h1>

    <p class="hero-sub">
      Build production-grade clinical data pipelines from raw HL7 v2 hospital feeds through FHIR R4 APIs, Mirth Connect channels, Epic EHR connectivity, and live AI inference — with every concept backed by real hospital deployments.
    </p>

    <div class="hero-cta">
      <a href="https://www.udemy.com" class="btn-primary" target="_blank">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        Enroll on Udemy
      </a>
      <a href="#hero" class="btn-ghost">← Back to Teaching</a>
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
        <div class="card-desc">Every architectural decision — trigger events, channel filters, FHIR query patterns — is made with downstream AI inference in mind.</div>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<script>
const observerOptions = { threshold: 0.1 };
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Back link
document.querySelector('.btn-ghost').addEventListener('click', e => {
  e.preventDefault();
  window.location.href = '{{ site.baseurl }}/teaching/';
});
</script>

</body>
</html>
