# MEdit - Previewing [M]arkup [Editor]

A simple text editor based on PyQt6/QScintilla with the following goals in mind:

- Auto-saves and tracks filesystem in order to make loading/saving obsolete
- Syntax highlighting for typical file formats
- Previewing markdown or representations in other file formats
- Support for local and remote images in Markdown/reST
- Decent nice looking interface for easily distractable people like me

As almost all of my projects, `medit` is in dangerous alpha state - use it with
care and don't believe anything written here.


## Installation

```sh
[<PYTHON> -m] pip[3] install [--upgrade] medit
```


## Usage

```sh
medit [<PATH>]  # will open medit in given directory or on given file
```


## Development & Contribution

```sh
pip3 install -U poetry pre-commit
git clone --recurse-submodules https://projects.om-office.de/frans/pocketrockit.git
cd pocketrockit
pre-commit install
# if you need a specific version of Python inside your dev environment
poetry env use ~/.pyenv/versions/3.10.4/bin/python3
poetry install
```

After modifications, this way a newly built wheel can be checked and installed:

```sh
poetry build
poetry run twine check dist/medit-0.0.5-py3-none-any.whl
python3 -m pip install --user --upgrade dist/medit-0.0.5-py3-none-any.whl
```

## My personal MLP (v1.0) goals

* [x] File to title
* [x] File viewer for Plain, Python, YAML, JSON, ..
* [x] Autosave
* [x] Manage word wrap in editor
* [x] include files
* [?] sort files by modification
* [ ] Autoload
* [ ] Search in files
* [ ] spell check
* [ ] add / remove / rename files
* [ ] support sequence diagrams mermaid
* [ ] Workdir/file history / Recent files
* [ ] Multi-File Undo/Redo
* [ ] Change into / step up current directory
* [ ] Zen mode
* [ ] Search/open files
* [ ] Preview for previewable only
* [ ] Hightlight todo.txt
* [ ] Notify external file changes
* [ ] (Re-)store zoom and fullscreen
* [ ] File ignore filter
* [ ] Icon / .desktop file
* [ ] Proper Qt style
* [ ] Show local images
* [ ] Show remote images
* [ ] Slim file / folder create / rename
* [ ] Proper View CSS selector
* [ ] View follows editor
* [ ] Links clickable
* [ ] Fix Links to support `(text)[url]` syntax


## Feature ideas

* [ ] Export to Pdf / Html / Docx ..
* [ ] Copy / paste images
* [ ] Drag & drop images
* [ ] Spell checker
* [ ] Script console with preview
* [ ] Preview rules (markdown->HTML, xml/json/yaml -> xml/json/yaml ..)


## Read

### Mermaid

* https://unpkg.com/browse/mermaid@8.1.0/dist/
* https://pypi.org/project/md-mermaid/
* https://github.com/oruelle/md_mermaid/issues/2


### Qt6

* https://github.com/5yutan5/PyQtDarkTheme


### QScintilla

* https://web.archive.org/web/20190604145031/https://qscintilla.com/prepare-image-hack/


### Markdown

* https://pypi.org/project/markdown-include/
* (Markdown Editor) https://github.com/jamiemcg/remarkable


### Styles / CSS

* https://thomasf.github.io/solarized-css/
* https://thomasf.github.io/solarized-css/solarized-light.css
* https://github.com/altercation/solarized
* https://github.com/sindresorhus/github-markdown-css
* https://python-markdown.github.io/extensions/code_hilite/#step-1-download-and-install-pygments
* https://github.com/richleland/pygments-css
* https://github.com/OzakIOne/markdown-github-dark
* https://github.com/sindresorhus/github-markdown-css
* https://markdowncss.github.io/
* https://github.com/markdowncss/retro
* https://mixu.net/markdown-styles/
* https://www.jsdelivr.com/package/npm/@naokim03/markdown-theme-solarized
