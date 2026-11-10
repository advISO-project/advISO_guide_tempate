# Configuration file for the Sphinx documentation builder.
#
# ============================================================================
# GUIDE SETTINGS — edit these to configure your guide
# ============================================================================

## To do: Update guide name, author, copyright, release, version, and github_repo to match your guide.
guide_name = 'advISO Bioinformatics Validation Guide'
author = 'advISO'
copyright = '2026, licensed under CC BY-NC-SA 4.0'
release = '0.1'
version = '0.1.0'

## To do: Set under_development to True if the guide is still under development, or False if it is ready for release. This controls whether the "under development" message is displayed on the index page.
under_development = True

# Set the GitHub repository URL for the guide. This is used to generate links to the guide's source code and issues on GitHub.
github_repo = 'https://github.com/advISO-project/advISO_validation_guide'

html_logo = 'source/_static/logo.png'


# ============================================================================
# Everything below here is Sphinx plumbing — you shouldn't need to change it.
# ============================================================================

project = guide_name

# -- Extensions --------------------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx_design',
    'sphinx_tabs.tabs',
]

# -- Substitutions -----------------------------------------------------------

rst_epilog = f"""
.. |release| replace:: {release}
.. |version| replace:: {version}
.. |guide_name| replace:: {guide_name}
.. |github_repo| replace:: {github_repo}
"""

today_fmt = "%Y-%m-%d"

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

# -- Custom config values ----------------------------------------------------

def setup(app):
    app.add_config_value('under_development', False, 'env')
