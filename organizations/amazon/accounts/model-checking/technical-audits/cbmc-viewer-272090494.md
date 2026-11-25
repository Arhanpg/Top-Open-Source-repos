# model-checking/cbmc-viewer

- Company: Amazon
- Account: model-checking
- Repository: https://github.com/model-checking/cbmc-viewer
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:14:54+00:00

## Project purpose

CBMC is a Bounded Model Checker for C. It can prove that (for computations of bounded depth) a C program exhibits no memory safe errors (no buffer overflows, no invalid pointers, etc), no undefined behaviors, and no failures of assertions in the code. CBMC Viewer is a tool that scans the output of CBMC and produces a browsable summary of its findings.

## Why this project is used

CBMC Viewer scans the output of CBMC and produces a browsable summary of its findings, making it easy to root cause the issues it finds.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Makefile, HTML, Shell, JavaScript, CSS, C
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/cbmc_viewer/__init__.py, src/cbmc_viewer/cbmc_viewer.py, src/cbmc_viewer/configt.py, src/cbmc_viewer/coveraget.py

## Setup and usage

- Installation: Most people should just follow the instructions on the
- Installation: Developers can install the package in Python "development mode" as follows.
- Installation: * Clone the repository and install dependencies with
- Installation: git clone https://github.com/awslabs/aws-viewer-for-cbmc.git cbmc-viewer
- Installation: apt install python3-pip python3-venv python3-jinja2 python3-voluptuous universal-ctags
- Installation: Installing ctags is optional. See the ctags discussion at the end of the
- Installation: * Install development mode with
- Installation: export PATH=/tmp/cbmc-viewer/bin:$PATH

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/model-checking/cbmc-viewer/blob/master/README.md
- README SHA: 4071f9ebfec4a9c9fb542de9c2ce67308e7e2a2e
- Manifests: Makefile, pyproject.toml, docs/Makefile, summary/Makefile, tests/bin/Makefile, tests/coreHTTP/Makefile
- Sampled source files: src/cbmc_viewer/cbmc_viewer.py, src/cbmc_viewer/configt.py, src/cbmc_viewer/coveraget.py
- Git tree state: captured
- Evidence fingerprint: bffe90d8ac959e6ad4a22cee83cf2117d57d46c7e481bc2058a971122c4dbd9d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
