# amazonlinux/amazon-linux-supportinfo

- Company: Amazon
- Account: amazonlinux
- Repository: https://github.com/amazonlinux/amazon-linux-supportinfo
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:28:43+00:00

## Project purpose

supportinfo is a Python library for parsing and querying Amazon Linux's package support metadata. It reads the support_info.xml documents Amazon Linux publishes and exposes the data through a typed Python API.

## Why this project is used

supportinfo is a Python library for parsing and querying Amazon Linux's package support metadata. It reads the support_info.xml documents Amazon Linux publishes and exposes the data through a typed Python API.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: lxml, xmlschema
- Build/package tools: Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/supportinfo/__init__.py, src/supportinfo/handler.py, src/supportinfo/schemas/__init__.py, setup.py

## Setup and usage

- Installation: The package is not yet on PyPI. Install from a checkout:
- Installation: pip install -e ".[test,dev]"

## Limitations and caveats

- Reporting security issues: Do **not** open a GitHub issue. Use AWS's
- Reporting security issues: vulnerability reporting page

## Evidence and provenance

- README: https://github.com/amazonlinux/amazon-linux-supportinfo/blob/main/README.md
- README SHA: a52d7809a041763b64dc36a481e134fc0812bd5a
- Manifests: Makefile, pyproject.toml, setup.py
- Sampled source files: src/supportinfo/__init__.py, src/supportinfo/handler.py, setup.py
- Git tree state: captured
- Evidence fingerprint: 6d95f43d5a435f4804f3981b0e514a346069b8d55647c87c85b7cb336d014890

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
