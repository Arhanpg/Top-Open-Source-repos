# microsoft/amplifier-module-resolution

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/amplifier-module-resolution](https://github.com/microsoft/amplifier-module-resolution)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/amplifier-module-resolution/blob/main/README.md)
- README blob SHA: fd1789fb7a2de548280e13373a628ef1a5e8a860
- README bytes captured: 22437
- README truncated at capture limit: False
- Repository ID: 1086094820
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Reference implementation for a module resolution library for the Amplifier project

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:36:23+00:00

### Short excerpt (up to 300 words)

> curl -LsSf https://astral.sh/uv/install.sh | **→ See Technical Specification uv sync --dev

### README headings

- amplifier-module-resolution
- Documentation
- Installation
- Install uv first (required for GitSource and recommended for all Python work)
- From PyPI (when published)
- From git (development)
- For local development
- Or using uv sync for development with dependencies
- Quick Start
- Set up settings provider for overrides
- Create standard resolver
- Resolve module to source
- Uses 5-layer resolution: env → workspace → settings → profile → package
- Resolve module path
- What This Library Provides
- Important: Why This Is a Library (Not Kernel)
- Standard 5-Layer Resolution
- Environment override takes highest precedence
- Or use workspace for local development
- Source Types
- FileSource
- Absolute path
- Relative path (resolved to absolute)
- URI format
- Resolve to module path (validates exists and is directory)
- GitSource
- From URI (note: subdirectory requires "subdirectory=" prefix)
- Or construct directly
- For module resolution: resolve to cached path
- For collection installation: install to specific directory

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install uv first (required for GitSource and recommended for all Python work)

> curl -LsSf https://astral.sh/uv/install.sh |

### Architecture and design: Design Philosophy

> **→ See Technical Specification

### Technology and requirements: Or using uv sync for development with dependencies

> uv sync --dev

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 63,122 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: pytest, pytest-asyncio, pytest-cov

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 4
- Forks at capture: 5
- Last updated: 2026-08-27T10:58:59Z
- Last pushed: 2026-01-12T14:58:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/amplifier-module-resolution)
- [README](https://github.com/microsoft/amplifier-module-resolution/blob/main/README.md)
- [Issues](https://github.com/microsoft/amplifier-module-resolution/issues)
- [Releases](https://github.com/microsoft/amplifier-module-resolution/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
