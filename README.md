# mohcinemadkour.github.io

Personal academic/professional website for Mohcine Madkour — Senior AI/ML Engineer & Architect.

Built with [Jekyll](https://jekyllrb.com/) and the [al-folio](https://github.com/alshedivat/al-folio) theme.

🌐 **Live site:** [https://mohcinemadkour.github.io](https://mohcinemadkour.github.io)

## Structure

| Directory                  | Content                                                   |
| -------------------------- | --------------------------------------------------------- |
| `_pages/`                  | Main nav pages: About, Writing, Projects, Teaching, Talks |
| `_projects/`               | Project entries (RAG PM, MySurgeryRisk, MLOps, CV, etc.)  |
| `_posts/`                  | Writing/blog articles                                     |
| `_teachings/`              | Courses and mentorship entries                            |
| `_talks/`                  | Conference and event presentations                        |
| `_news/`                   | Short announcements on the About page                     |
| `_bibliography/papers.bib` | Publications (BibTeX)                                     |
| `_data/cv.yml`             | CV data                                                   |
| `_data/socials.yml`        | Social links                                              |
| `assets/img/`              | Images (add `prof_pic.jpg` here)                          |

## Quick Start (Local)

```bash
# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve --livereload
# → http://localhost:4000
```

## Deployment

Push to `main` — GitHub Actions builds and deploys automatically via `.github/workflows/deploy.yml`.

**Prerequisites (one-time setup):**

1. Go to repo **Settings → Pages**
2. Set **Source** to `GitHub Actions`
3. Push — the workflow handles the rest

## Adding Content

### New Project

```bash
# Create _projects/8_myproject.md
# Required front matter:
---
layout: page
title: My Project
description: Short description shown on the card.
img: assets/img/projects/myproject.png
importance: 1
category: agentic-ai  # agentic-ai | healthcare-ai | computer-vision | mlops | industrial-iot
---
```

### New Blog Post

```bash
# Create _posts/YYYY-MM-DD-post-title.md
---
layout: post
title: "Post Title"
date: 2026-04-01
tags: [LangGraph, RAG, MLOps]
categories: writing
---
```

### New Talk

```bash
# Create _talks/YYYY_event_name.md
---
layout: page
title: "Talk Title"
event: Conference Name
location: City, State
date: 2026-03-31
type: Conference  # Conference | Workshop | Panel | Invited
slides: /assets/pdf/slides.pdf
video: https://youtube.com/...
---
```

## Customization

- **Profile photo:** Drop `prof_pic.jpg` into `assets/img/`
- **CV PDF:** Drop your CV PDF into `assets/pdf/` and update path in `_data/socials.yml`
- **Google Scholar ID:** Add to `_data/socials.yml` under `scholar_userid`
- **Google Analytics:** Add `G-XXXXXXXXXX` to `_config.yml` under `google_analytics`
