# NVIDIA/data-federation-mesh

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/data-federation-mesh](https://github.com/NVIDIA/data-federation-mesh)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/data-federation-mesh/blob/main/README.md)
- README blob SHA: c44cb9c01be205f176a9ab30b92838878331ccff
- README bytes captured: 7721
- README truncated at capture limit: False
- Repository ID: 1165929935
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Python-based framework designed to facilitate creation and orchestration of complex workflows processing data coming from various distributed sources, and streaming those data into applications.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T23:22:50+00:00

### Short excerpt (up to 300 words)

> SPDX-FileCopyrightText: Copyright (c) 2026 Core/common support Python 3.10–3.12; uv sync --all-packages

### README headings

- NVIDIA Data Federation Mesh
- Project Structure
- Quick Start
- Installation from PyPI
- Install core framework only
- Install weather adapters library (see warning below)
- Install weather adapters with AI model support (requires GPU, see below).
- Pick the extra(s) you need; combine them in one command to get several.
- Development Setup
- Install all workspace packages and their dependencies
- Install a single package (for example core only)
- Install with tutorial extras (adds ipywidgets, leafmap). Open the .ipynb
- tutorials with your own Jupyter frontend (JupyterLab / VS Code / etc.).
- Examples
- Overview
- NVIDIA Flare
- DFM Command Line Interface
- Contributors
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> SPDX-FileCopyrightText: Copyright (c) 2026

### Getting started and usage: Installation from PyPI

> Core/common support Python 3.10–3.12;

### Technology and requirements: Install all workspace packages and their dependencies

> uv sync --all-packages

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,031,397 |
| Jupyter Notebook | 2,719,105 |
| Jinja | 44,780 |
| Shell | 42,170 |
| Dockerfile | 3,512 |
| Go Template | 2,263 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: ipywidgets, leafmap, nv-dfm-lib-weather
- packages/nv-dfm-core/pyproject.toml (capture: captured) — dependency clues: appdirs, bottleneck, click, datamodel-code-generator, fsspec, gitpython, hypothesis, jinja2, nvflare, pandera, pooch, pydantic, pyproj, ruamel-yaml, scipy, sh, typing-extensions, universal-pathlib, xarray
- packages/nv-dfm-lib-common/pyproject.toml (capture: captured) — dependency clues: nv-dfm-core
- packages/nv-dfm-lib-weather/pyproject.toml (capture: captured) — dependency clues: cartopy, earth2studio, gcsfs, herbie-data, intake-esgf, metpy, netCDF4, nv-dfm-core, nv-dfm-lib-common, nvidia-physicsnemo, pillow, pytz, rioxarray, zarr
- tutorials/example-fed/pyproject.toml (capture: captured) — dependency clues: nv-dfm-core
- tutorials/startup-fed/{{cookiecutter.project_name}}/pyproject.toml (capture: captured) — dependency clues: nv-dfm-core

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 7
- Last updated: 2026-11-16T16:24:49Z
- Last pushed: 2026-11-17T11:48:53Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/data-federation-mesh)
- [README](https://github.com/NVIDIA/data-federation-mesh/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/data-federation-mesh/issues)
- [Releases](https://github.com/NVIDIA/data-federation-mesh/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
