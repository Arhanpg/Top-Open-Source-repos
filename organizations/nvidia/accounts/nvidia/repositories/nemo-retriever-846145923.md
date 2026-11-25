# NVIDIA/NeMo-Retriever

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/NeMo-Retriever](https://github.com/NVIDIA/NeMo-Retriever)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/NeMo-Retriever/blob/main/README.md)
- README blob SHA: 5e507495c39c5358f5a58d2450e156c06af873dd
- README bytes captured: 14705
- README truncated at capture limit: False
- Repository ID: 846145923
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NeMo Retriever Library is a scalable, performance-oriented document content and metadata extraction microservice. NeMo Retriever Library uses specialized NVIDIA NIM microservices to find, contextualize, and extract text, tables, charts and images that you can use in downstream generative applications.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:18:35+00:00

### Short excerpt (up to 300 words)

> SPDX-FileCopyrightText: Copyright (c) 2024, NeMo Retriever Extraction doesn't

### README headings

- NeMo Retriever Library
- Typical Use
- ingestion tasks are chainable and defined lazily
- ingestor.ingest() actually executes the pipeline
- page 1 raw text:
- markdown formatted table from the first page
- a chart from the first page
- markdown formatting for full pages or documents:
- per-page markdown is keyed by page number
- full document markdown is a single string (or None if empty)
- Query Ingested Content
- you can also submit a list with retriever.queries([...])
- Documentation Resources
- Notices
- Third Party License Notice:
- Security Considerations

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> SPDX-FileCopyrightText: Copyright (c) 2024,

### Limitations and security: Security Considerations

> NeMo Retriever Extraction doesn't

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 7,483,306 |
| JavaScript | 54,461 |
| Go Template | 34,500 |
| Jinja | 33,598 |
| Shell | 13,137 |
| Dockerfile | 12,060 |
| Standard ML | 9,174 |
| HTML | 8,034 |
| Jupyter Notebook | 5,030 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- .devcontainer/Dockerfile (capture: captured)
- docs/Makefile (capture: captured)
- docs/requirements.txt (capture: captured) — dependency clues: autodoc_pydantic, make, mike, mkdocs, mkdocs-gen-files, mkdocs-include-dir-to-nav, mkdocs-jupyter, mkdocs-literate-nav, mkdocs-macros-plugin, mkdocs-material, mkdocs-minify-plugin, mkdocs-redirects, mkdocs-site-urls, mkdocstrings, myst-parser, nvidia-sphinx-theme, pymdown-extensions, sphinx, sphinx-markdown-builder, sphinx-rtd-theme
- nemo_retriever/pyproject.toml (capture: captured) — dependency clues: accelerate, addict, albumentations, backoff, build, cairosvg, click, datasets, debugpy, duckdb, easydict, einops, fastapi, fastmcp, ffmpeg-python, filelock, flashinfer-python, fsspec, httpx, huggingface-hub
- retrieval-bench/pyproject.toml (capture: captured) — dependency clues: Pillow, PyStemmer, aiofiles, bm25s, datasets, jinja2, litellm, pydantic, pytest, python-dotenv, pytrec_eval, rich, ruff, torch, torchvision, transformers, typer, vidore-benchmark

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3015
- Forks at capture: 364
- Last updated: 2026-11-22T03:56:19Z
- Last pushed: 2026-11-21T03:12:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/NeMo-Retriever)
- [README](https://github.com/NVIDIA/NeMo-Retriever/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/NeMo-Retriever/issues)
- [Releases](https://github.com/NVIDIA/NeMo-Retriever/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
