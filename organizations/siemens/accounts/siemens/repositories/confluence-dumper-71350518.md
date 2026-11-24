# siemens/confluence-dumper

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/confluence-dumper](https://github.com/siemens/confluence-dumper)
- Default branch: master
- README: [Open upstream README](https://github.com/siemens/confluence-dumper/blob/master/README.rst)
- README blob SHA: 412653dc4c4130924a50a7bb6f0f964d37fbc671
- Repository ID: 71350518
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Tool to export Confluence spaces and pages recursively via its API

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:54+00:00

### Short excerpt (up to 100 words)

> ============== How to install ============== *************************** Configure virtualenvwrapper *************************** For convenience you should use `virtualenvwrapper <http://virtualenvwrapper.readthedocs.io/en/latest/>`_:: sudo pip install virtualenvwrapper Add three lines to /etc/environment or another shell startup file:: export WORKON_HOME=$HOME/.virtualenvs export PROJECT_HOME=$HOME/python_dev source /usr/share/virtualenvwrapper/virtualenvwrapper.sh Create a new virtual environment:: mkvirtualenv confluence_dumper_venv Enter the virtual environment:: workon confluence_dumper_venv *************************** Configure confluence dumper *************************** Install dependencies:: pip install -r requirements.txt Copy confluence settings:: cd confluence_dumper cp settings.sample.py settings.py Please personalize the ``settings.py`` on your own according to your confluence instance. ========== How to use ========== Don't forget to switch to the virtual environment because of the installed dependencies:: workon confluence_dumper_venv

### README headings

- No headings captured

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 31,841 |
| HTML | 182 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: lxml, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 212
- Forks at capture: 69
- Last updated: 2026-06-22T18:45:38Z
- Last pushed: 2023-05-12T22:50:39Z
- Topics: confluence, dump, offline, python, rest-client

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/confluence-dumper)
- [README](https://github.com/siemens/confluence-dumper/blob/master/README.rst)
- [Issues](https://github.com/siemens/confluence-dumper/issues)
- [Releases](https://github.com/siemens/confluence-dumper/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
