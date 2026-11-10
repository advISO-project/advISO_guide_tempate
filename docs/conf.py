# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

guide_name = 'advISO Bioinformatics Validation Guide'
copyright = '2026, licensed under CC BY-NC-SA 4.0'
author = 'advISO'

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_design',
    'sphinx_tabs.tabs',
    'sphinx.ext.ifconfig'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']


# -- Custom substitutions ----------------------------------------------------

# These let you use |version|, |release|, and |guide_name| in your .rst files
rst_epilog = f"""
.. |release| replace:: {release}
.. |version| replace:: {version}
.. |guide_name| replace:: {guide_name}
"""

# Use dynamic date for |today|
today_fmt = "%Y-%m-%d"


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# Path for static files
html_static_path = ['source/_static']

html_css_files = [
    'custom.css',
]

# Path to the logo
html_logo = 'source/_static/logo.png'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'collapse_navigation': False,
    "navigation_depth": 3,
}

# -- Options for EPUB output -------------------------------------------------

epub_show_urls = 'footnote'


# -- Custom configuration variables ------------------------------------------
def setup(app):
    app.add_config_value('under_development', False, 'env')

under_development = True  # Set to True if the guide is under development, False otherwise

