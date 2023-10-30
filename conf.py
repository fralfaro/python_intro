###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
author = "Francisco Alfaro"
comments_config = {"hypothesis": False, "utterances": False}
copyright = "2023"
exclude_patterns = [
    "**.ipynb_checkpoints",
    "**.pytest_cache",
    ".DS_Store",
    "Thumbs.db",
    "_build",
    "tools",
]
extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "jupyter_book",
    "sphinx_thebe",
    "sphinx_comments",
    "sphinx_external_toc",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_book_theme",
    "sphinxcontrib.bibtex",
    "sphinx_jupyterbook_latex",
]
external_toc_exclude_missing = True
external_toc_path = "_toc.yml"
html_baseurl = ""
html_favicon = "docs/img/icons/ccr_favicon.png"
html_logo = "docs/img/icons/icon.png"
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_theme_options = {
    "search_bar_text": "Search this book...",
    "launch_buttons": {
        "notebook_interface": "classic",
        "binderhub_url": "",
        "jupyterhub_url": "",
        "thebe": False,
        #"colab_url": "https://colab.research.google.com",
    },
    "path_to_docs": "",
    "repository_url": "https://github.com/ampl/mo-book.ampl.com",
    "repository_branch": "dev",
    "extra_footer": "",
    "home_page_in_toc": True,
    "announcement": "",
    "analytics": {"google_analytics_id": "G-TB617QHPDG"},
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
}
html_title = "Educación en Cuatro Dimensiones"
#latex_engine = "pdflatex"
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]
myst_url_schemes = ["mailto", "http", "https"]
nb_execution_allow_errors = False
nb_execution_cache_path = ""
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = "off"
nb_execution_timeout = 30
nb_output_stderr = "show"
numfig = True
pygments_style = "sphinx"
suppress_warnings = ["myst.domains"]
use_jupyterbook_latex = True
use_multitoc_numbering = True
latex_elements = {
    "extraclassoptions": "oneside",  # do not leave empty pages
    "tableofcontents": "\\sphinxtableofcontents",
}
