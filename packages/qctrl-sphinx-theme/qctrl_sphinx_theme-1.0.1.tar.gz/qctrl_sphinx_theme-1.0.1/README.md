# Q-CTRL Sphinx Theme

The Q-CTRL Sphinx Theme is a very opinionated [Sphinx](https://www.sphinx-doc.org/) theme intended for use with public [Q-CTRL Documentation](https://docs.q-ctrl.com/) websites such as the [Q-CTRL Python package](https://docs.q-ctrl.com/boulder-opal/references/qctrl/).

## Installation

```shell
pip install qctrl-sphinx-theme
```

## Usage

1. Add `qctrl-sphinx-theme` as a dev dependency in `pyproject.toml`.
```toml
[tool.poetry.dev-dependencies]
qctrl-sphinx-theme = "~1.0.0"
```
1. Add the following to `docs/conf.py` (this sets the Q-CTRL Sphinx Theme as the theme for your documentation):
  ```python
  html_theme = "qctrl_sphinx_theme"
  ```
1. Update (or create) the `html_theme_options` dictionary in `docs/conf.py` using `qctrlsphinxtheme.get_html_theme_options` (this checks each DocSearch and Segment theme option for an available environment variable and, if one exists, sets it). For example:

To update an `html_theme_options` dictionary:

  ```python
  from qctrlsphinxtheme import get_html_theme_options
  html_theme_options.update(get_html_theme_options())
  ```

To create a `html_theme_options` dictionary:

  ```python
  from qctrlsphinxtheme import get_html_theme_options
  html_theme_options = get_html_theme_options()
  ```
