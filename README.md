# Portfolio

Live site: https://aryanmishra-dev.github.io

## Stack
Static HTML + CSS + Vanilla JS. No build tools. Hosted on GitHub Pages.

## Structure
- `css/` — component stylesheets, imported via css/main.css
- `js/` — ES modules, entry point is js/main.js
- `assets/` — images and resume PDF
- `components/` — HTML reference snippets for adding new content

## Dynamic features
- GitHub stats: fetched live via GitHub REST API (js/stats.js)
- Contact form: Formspree endpoint (replace YOUR_FORM_ID in index.html)

## Adding a new project
1. Copy the template from components/project-cards.html
2. Paste into index.html inside .projects-grid
3. Update title, description, metrics, stack tags, and links
4. Set data-category to: nlp | mlops | data | web

## Performance targets
- Lighthouse Performance ≥ 95
- Lighthouse Accessibility ≥ 95
- Lighthouse SEO = 100
- Total page weight < 500KB
