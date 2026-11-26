# rapidsai/clang-recipe

- Company: NVIDIA
- Account: rapidsai
- Repository: https://github.com/rapidsai/clang-recipe
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:16:47+00:00

## Project purpose

This repo contains recipe for building clang library, clang-format, clang-tidy and also the python wrapper for clang library.

## Why this project is used

Clang build recipe for anaconda

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Dockerfile, Shell, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/build.sh, py/build.sh, py/setup.py

## Setup and usage

- Usage: git clone https://github.com/teju85/clang-recipe
- Usage: docker build -t conda:dev .
- Usage: docker run --rm -it conda:dev /bin/bash
- Usage: inside-container# anaconda login
- Usage: inside-container# conda build lib
- Usage: inside-container# anaconda upload /path/to/libclang/package.tar.gz
- Usage: inside-container# conda build py
- Usage: inside-container# anaconda upload /path/to/clang/package.tar.gz

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/rapidsai/clang-recipe/blob/master/README.md
- README SHA: 961a20096e9ca2b732f112c2b3cbb484855c2ed6
- Manifests: Dockerfile, py/setup.py
- Sampled source files: lib/build.sh, py/build.sh, py/setup.py
- Git tree state: captured
- Evidence fingerprint: d9c415bb66688fb0ab10d6a11adbfaa3f5365659b1ba95b693f77e9592ea809f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
