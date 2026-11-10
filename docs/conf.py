# Configuration file for the Sphinx documentation builder.
import os
import sys
from datetime import date

#
# ============================================================================
# GUIDE SETTINGS — edit these to configure your guide
# ============================================================================

## To do: Update guide name, author, copyright, release, version, and github_repo to match your guide.
guide_name = 'advISO Guide Template'
author = 'advISO'
copyright = '2026, licensed under CC BY-NC-SA 4.0'
release = '0.1'
version = '0.1.0'

## To do: Set under_development to True if the guide is still under development, or False if it is ready for release. This controls whether the "under development" message is displayed on the index page.
under_development = True

## To do: Set the guide subtitle that appears on the logo (e.g. "Validation Guide", "SOP Guide").
guide_subtitle = 'Guide Template'

## To do: Set the sidebar background colour (hex).
sidebar_color = '#5C9AD0'

# To do: Set the GitHub repository URL for the guide. This is used to generate links to the guide's source code and issues on GitHub.
github_repo = 'https://github.com/advISO-project/advISO_guide_template'

html_logo = 'source/_static/logo.png'


# ============================================================================
# Everything below here is Sphinx plumbing — you shouldn't need to change it.
# ============================================================================

project = guide_name

exclude_patterns = [
    '_build',
    'source/intro.md',
    'source/guide_series.md',
    'source/project_partners.md',
    'source/toc.md',
]

# -- Extensions --------------------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx_design',
    'sphinx_tabs.tabs',
]

# -- MyST (Markdown) configuration ------------------------------------------

myst_enable_extensions = [
    'colon_fence',
    'substitution',
]

today_fmt = "%Y-%m-%d"

myst_substitutions = {
    'guide_name': guide_name,
    'release': release,
    'version': version,
    'github_repo': github_repo,
    'github_issues_link': f'[GitHub repository]({github_repo}/issues)',
    'today_date': date.today().strftime(today_fmt),
}

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['source/_static']

html_css_files = [
    'custom.css',
]

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'collapse_navigation': False,
    'navigation_depth': 3,
}

# -- EPUB output -------------------------------------------------------------

epub_show_urls = 'footnote'

# -- Build-time asset generation ---------------------------------------------

sys.path.insert(0, os.path.dirname(__file__))
from generate_logo import generate_logo
generate_logo(guide_subtitle)

_css_path = os.path.join(os.path.dirname(__file__), 'source', '_static', 'custom.css')
with open(_css_path, 'w') as _f:
    _f.write(f""".wy-side-nav-search,
.wy-nav-top {{
    background: {sidebar_color};
}}

.guide-button {{
  border-radius: 12px;
  box-shadow: 0 2px 6px rgba(0,0,0,.15);
  transition: transform .15s, box-shadow .15s;
}}
.guide-button:hover {{
  transform: translateY(-3px);
  box-shadow: 0 6px 14px rgba(0,0,0,.25);
}}
""")

# -- Custom config values ----------------------------------------------------

def setup(app):
    app.add_config_value('under_development', False, 'env')
