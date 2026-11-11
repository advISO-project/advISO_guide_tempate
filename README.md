# advISO Guide Template

A Sphinx documentation template for creating advISO-branded guides, hosted on Read the Docs. Each guide in the advISO series is built from a fork of this repository.

## Quick start

1. **Fork this repository** on GitHub.

2. **Rename** the forked repo to match your guide (e.g. `advISO_validation_guide`).

3. **Edit the guide settings** at the top of [`docs/conf.py`](docs/conf.py). These are the only values you need to change to brand your guide:

   | Setting | Description | Example |
   |---|---|---|
   | `guide_name` | Full title shown in the browser tab and index page | `'advISO Validation Guide'` |
   | `guide_subtitle` | Short name that appears on the logo and buttons | `'Validation Guide'` |
   | `sidebar_color` | Hex colour for the sidebar and button backgrounds | `'#5C9AD0'` |
   | `github_repo` | URL of your GitHub repository | `'https://github.com/advISO-project/advISO_validation_guide'` |
   | `author` | Author name for metadata | `'advISO'` |
   | `copyright` | Copyright line | `'2026, licensed under CC BY-NC-SA 4.0'` |
   | `release` / `version` | Guide version numbers | `'1.0'` / `'1.0.0'` |
   | `under_development` | Show the "under development" banner on the index page | `True` or `False` |

4. **Update the content**:

   | File | Purpose |
   |---|---|
   | `docs/intro.md` | Introduction section included on the index page |
   | `docs/toc.md` | Table of contents — add your pages here |
   | `docs/pages/example_page.md` | A sample content page — rename or replace with your own |

5. **Connect to Read the Docs.** Import the new repository on [readthedocs.org](https://readthedocs.org). The included `.readthedocs.yml` handles the build configuration automatically.

## How it works

### Auto-generated assets

The logo, buttons, and sidebar CSS are generated automatically at build time from the settings in `conf.py` — you never need to edit these files by hand.

| Asset | Generated from | Output |
|---|---|---|
| Sidebar logo | `base/logo_base.png` + `guide_subtitle` | `images/logo.png` |
| Horizontal button | `base/button_base.png` + `guide_subtitle` + `sidebar_color` | `brand/button_horizontal.png` |
| Website banner (16:9) | `base/logo_base_16x9.png` + `guide_subtitle` + `sidebar_color` | `brand/button_website.png` |
| Sidebar CSS | `sidebar_color` | `custom.css` |

The generation scripts are in `docs/_scripts/`. The base images in `docs/_static/base/` are shared across all guides and should not be modified.

Generated files are listed in `.gitignore` — they are rebuilt on every Sphinx run and should not be committed.

### Project structure

```
docs/
├── conf.py                  # Guide settings and Sphinx configuration
├── index.md                 # Index page
├── intro.md                 # Introduction (edit this)
├── toc.md                   # Table of contents (add your pages here)
├── requirements.txt         # Python dependencies for Read the Docs
│
├── pages/                   # Content pages — add your guide pages here
│   └── example_page.md
│
├── _includes/               # Shared fragments (do not edit)
│   ├── guide_series.md
│   └── project_partners.md
│
├── _brand_assets/           # Brand assets page (hidden, accessible via direct URL)
│   └── brand_assets.md
│
├── _scripts/                # Build-time asset generation
│   ├── generate_logo.py
│   └── generate_buttons.py
│
├── _static/
│   ├── base/                # Template base images (do not modify)
│   │   ├── button_base.png
│   │   ├── logo_base.png
│   │   └── logo_base_16x9.png
│   ├── brand/               # Generated brand assets (gitignored)
│   │   ├── button_horizontal.png
│   │   └── button_website.png
│   ├── images/              # Content images
│   │   ├── logo.png         # Generated sidebar logo (gitignored)
│   │   ├── guide_series_button_horizontal.png
│   │   └── partner_logos.png
│   └── custom.css           # Generated sidebar CSS (gitignored)
```

### Writing content

Pages are written in Markdown using [MyST](https://myst-parser.readthedocs.io/en/latest/), which adds Sphinx directives to standard Markdown. The template includes several Sphinx extensions:

- **MyST Parser** — write Markdown instead of reStructuredText
- **sphinx-design** — grids, cards, tabs, badges
- **sphinx-tabs** — tabbed content blocks
- **sphinx.ext.ifconfig** — conditional content (used for the "under development" banner)

To add a new page, create a `.md` file in `docs/pages/` and add it to the `toctree` in `docs/_includes/toc.md`.

## Building locally

```bash
cd docs
pip install -r requirements.txt
make html
```

The built site will be in `docs/_build/html/`. Open `index.html` to preview.

## Brand assets page

A hidden page at `_brand_assets/brand_assets.html` in the built docs shows all generated assets for review. It is not linked from the navigation — share the direct URL with anyone who needs the logos.

## License

This project is licensed under CC BY-NC-SA 4.0. See [LICENSE.md](LICENSE.md) for details.
