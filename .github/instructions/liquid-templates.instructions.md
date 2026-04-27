---
applyTo: "**/*.liquid"
---

# Liquid Templates Instructions

## Liquid Template Basics

This al-folio repository uses Liquid templating extensively. When modifying `.liquid` files:

### Key Directories

- `_includes/` – Reusable template components (imported with `{% include %}`)
- `_layouts/` – Page layout templates (specified in frontmatter with `layout: name`)

### Common Liquid Tags in al-folio

- `{% include filename.liquid %}` – Includes template component
- `{% for item in collection %}...{% endfor %}` – Loops
- `{% if condition %}...{% endif %}` – Conditionals
- `{{ variable }}` – Output variable
- `{% assign var = value %}` – Assign variable
- `{% capture %}...{% endcapture %}` – Capture output to variable
- `| date: format` – Date formatting
- `| where: "key", "value"` – Collection filtering
- `| slugify` – Convert to URL-safe slug
- `| relative_url` – Prepend site.baseurl to URLs
- `| absolute_url` – Prepend site.url + site.baseurl to URLs (full absolute path)

### Commonly Used Liquid Filters in al-folio

These filters appear throughout al-folio templates and scripts:

**URL/Path Filters:**

- `{{ page.url | relative_url }}` – Returns URL relative to baseurl (e.g., `/my-site/about/` if baseurl is `/my-site`)
- `{{ page.url | absolute_url }}` – Returns full absolute URL (e.g., `https://example.com/my-site/about/`)
- Use `relative_url` for internal links; use `absolute_url` for RSS, emails, social sharing

**String Filters:**

- `{{ title | slugify }}` – Convert "My Cool Title" → "my-cool-title" (for IDs, URLs)
- `{{ title | escape }}` – Escape HTML special characters (use in JSON, HTML attributes)
- `{{ content | strip_html }}` – Remove HTML tags (useful for previews)
- `{{ content | truncatewords: 20 }}` – Limit to 20 words with ellipsis

**Date Filters:**

- `{{ date | date: "%Y-%m-%d" }}` – Format: "2023-12-25"
- `{{ date | date: "%B %d, %Y" }}` – Format: "December 25, 2023"
- `{{ date | date: "%d %b %Y" }}` – Format: "25 Dec 2023"

**Collection Filters:**

- `{{ site.posts | where: "category", "blog" }}` – Filter posts by category
- `{{ site.projects | where: "featured", true }}` – Get only featured projects
- `{{ pages | size }}` – Count items in collection

**Whitespace Control in Liquid:**

- `{{ variable }}` – Renders with surrounding whitespace preserved
- `{{- variable -}}` – Strips whitespace before and after (hyphens remove spaces)
- `{%- if condition -%}` – Use in `.liquid.js` files to prevent extra newlines in generated JSON
- Critical in `.liquid.js` files where extra whitespace corrupts JavaScript/JSON structure

### Important al-folio Liquid Components

- `_includes/citation.liquid` – Bibliography entry rendering
- `_includes/distill_scripts.liquid` – Distill.pub specific scripts
- `_includes/footer.liquid` – Site footer
- `_includes/head.liquid` – Page <head> section
- `_includes/header.liquid` – Site header/navigation
- `_includes/projects.liquid` – Project display
- `_includes/scripts.liquid` – Global scripts
- `_includes/selected_papers.liquid` – Featured publications display

### Prettier Formatting for Liquid

Prettier with `@shopify/prettier-plugin-liquid` enforces formatting:

- Single quotes around strings in Liquid tags
- Consistent spacing
- Indentation with 2 spaces
- Run `npx prettier . --write` before committing

## Common Modification Patterns

### Modifying Site Header/Navigation

- Edit `_includes/header.liquid`
- Add links to navigation array in `_config.yml` (see yaml-configuration.instructions.md)
- Test by viewing site in browser: `docker compose up` → http://localhost:8080

### Adding a New Component Include

1. Create new file in `_includes/mycomponent.liquid`
2. Use Liquid syntax for conditionals, loops, and variable output
3. Call it from templates: `{% include mycomponent.liquid %}`
4. Test: `docker compose up`

### Adjusting Styling with Liquid

- Some SCSS variables can be controlled via Liquid logic
- Avoid mixing complex Liquid with CSS; keep templates focused

## Validation Before Committing

**Always run these checks:**

1. **Prettier format check:**

   ```bash
   npx prettier _includes/ _layouts/ --check
   npx prettier . --write  # Fix formatting
   ```

2. **Build test:**

   ```bash
   docker compose down
   docker compose up
   # Wait 30 seconds, check for errors in output
   # No "Unknown tag" messages should appear
   ```

3. **Visual verification:**
   - Open http://localhost:8080
   - Check that your changes rendered correctly
   - Verify no broken layout or missing content

## Trust These Instructions

When working with Liquid templates:

- Use `_includes/` and `_layouts/` as reference for syntax patterns
- Follow existing formatting in files (Prettier will enforce consistency)
- Always test locally before pushing (build must succeed)
- For configuration changes, see yaml-configuration.instructions.md
- Only search for additional details if error messages reference unfamiliar Liquid tags or Jekyll concepts
