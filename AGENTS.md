# Agent Guidelines for al-folio

A simple, clean, and responsive Jekyll theme for academics. This document helps AI agents understand project conventions and work efficiently.

## Quick Links by Role

- **Are you a coding agent?** → Read [`.github/copilot-instructions.md`](.github/copilot-instructions.md) first (tech stack, build, CI/CD, common pitfalls & solutions)
- **Customizing the site?** → Use [`.github/agents/customize.agent.md`](.github/agents/customize.agent.md) for step-by-step guidance
- **Writing/updating documentation?** → Use [`.github/agents/docs.agent.md`](.github/agents/docs.agent.md) to keep docs in sync
- **Need setup/deployment help?** → [INSTALL.md](INSTALL.md)
- **Troubleshooting & FAQ?** → [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Customization & theming?** → [CUSTOMIZE.md](CUSTOMIZE.md)
- **Quick 5-min start?** → [QUICKSTART.md](QUICKSTART.md)

## Essential Commands

### Local Development (Docker)

The recommended approach is using Docker.

```bash
# Initial setup & start dev server
docker compose pull && docker compose up
# Site runs at http://localhost:8080

# Rebuild after changing dependencies or Dockerfile
docker compose up --build

# Stop containers and free port 8080
docker compose down
```

### Pre-Commit Checklist

Before every commit, you **must** run these steps:

1.  **Format Code:**
    ```bash
    # (First time only)
    npm install --save-dev prettier @shopify/prettier-plugin-liquid
    # Format all files
    npx prettier . --write
    ```
2.  **Build Locally & Verify:**

    ```bash
    # Rebuild the site
    docker compose up --build

    # Verify by visiting http://localhost:8080.
    # Check navigation, pages, images, and dark mode.
    ```

## Critical Configuration

When modifying `_config.yml`, these **must be updated together**:

- **Personal site:** `url: https://username.github.io` + `baseurl:` (empty)
- **Project site:** `url: https://username.github.io` + `baseurl: /repo-name/`
- **YAML errors:** Quote strings with special characters: `title: "My: Cool Site"`

## Project Organization

### Content Structure

- **`_pages/`** – Static pages (about, CV, publications, projects, etc.) – Layout: `page` or custom
- **`_posts/`** – Blog posts (format: `YYYY-MM-DD-hyphenated-title.md`) – Layout: `post`
- **`_projects/`** – Project showcase (format: `NUMBER_name.md`, e.g., `1_rag_project.md`) – Layout: `page`
- **`_news/`** – News announcements – Layout: `post`
- **`_teachings/`** – Courses and teaching – Layout: `page`
- **`_books/`** – Book reviews – Layout: `book-review`

### Project-Specific Conventions

- **Project importance:** Integer field (1, 2, 3...) – lower numbers = higher homepage prominence. **REQUIRED for display sorting**
- **Project categories:** Hardcoded values: `mlops`, `healthcare-ai`, `agentic-ai`, `computer-vision`, `industrial-iot` (used in layout filtering)
- **Frontmatter dates:** Must match `YYYY-MM-DD` format and match filename date (else Jekyll sorts by filename, not frontmatter)
- **Post slugification:** Filenames use hyphens; Jekyll converts to underscores in URLs – plan permalink accordingly

## Development Workflow

- **Git & Commits:** For commit message format and Git practices, see [.github/GIT_WORKFLOW.md](.github/GIT_WORKFLOW.md).
- **Code-Specific Instructions:** Consult the relevant instruction file for your code type.

| File Type                                     | Instruction File                                                                                |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Markdown content (`_posts/`, `_pages/`, etc.) | [markdown-content.instructions.md](.github/instructions/markdown-content.instructions.md)       |
| YAML config (`_config.yml`, `_data/`)         | [yaml-configuration.instructions.md](.github/instructions/yaml-configuration.instructions.md)   |
| BibTeX (`_bibliography/`)                     | [bibtex-bibliography.instructions.md](.github/instructions/bibtex-bibliography.instructions.md) |
| Liquid templates (`_includes/`, `_layouts/`)  | [liquid-templates.instructions.md](.github/instructions/liquid-templates.instructions.md)       |
| JavaScript (`_scripts/`)                      | [javascript-scripts.instructions.md](.github/instructions/javascript-scripts.instructions.md)   |

## Specialized Agent Workflows

### Customization Agent ([`.github/agents/customize.agent.md`](.github/agents/customize.agent.md))

- **Use when:** User needs step-by-step guidance on customizing their site (non-coders welcome)
- **Handles:** Configuration, content creation, theme customization, social media setup
- **Guidance:** Plain-language explanations, validates changes against current code

### Docs Agent ([`.github/agents/docs.agent.md`](.github/agents/docs.agent.md))

- **Use when:** Documentation needs updating (README, CUSTOMIZE.md, FAQ, TROUBLESHOOTING)
- **Handles:** Synchronizing docs with code changes, maintaining documentation quality
- **Guidance:** Links to existing docs, avoids duplication, preserves accuracy

## Common Issues & Silent Failures

For troubleshooting, see:

- [Common Pitfalls & Workarounds](.github/copilot-instructions.md#common-pitfalls--workarounds) in copilot-instructions.md
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed solutions
- [GitHub Issues](https://github.com/alshedivat/al-folio/issues) to search for your specific problem

### Known Silent Failures (Hard to Debug)

1. **"Zero vectors cannot be normalized"** – Occurs when blog post has minimal content and `related_posts: true`. Solution: Add real content to post or set `related_posts: false` in frontmatter.
2. **CSS/JS don't load after deploy** – Caused by mismatched `url` and `baseurl` in `_config.yml`. Clear browser cache or use private browsing to verify.
3. **Post sort order broken** – When post filename doesn't match `date:` frontmatter field, Jekyll silently uses filename date instead of frontmatter date.
4. **Feature flags scattered** – Both `_config.yml` (global) and frontmatter (per-post) control `related_posts`; dual control points confuse intended behavior.
