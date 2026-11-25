# model-checking/kani-github-action

- Company: Amazon
- Account: model-checking
- Repository: https://github.com/model-checking/kani-github-action
- Default branch: v1
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:46:32+00:00

## Project purpose

This repository provides a GitHub Action for running the Kani Rust Verifier in CI.

## Why this project is used

This repository provides a GitHub Action for running the Kani Rust Verifier in CI.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Shell, Rust
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Cargo manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/install-kani.sh, scripts/copyright_check.py, scripts/run-autopep8.sh, scripts/run-clang-format.sh

## Setup and usage

- Example usage in a workflow YAML file:: Here are a few examples of workflow YAML files for the Kani Github Action:

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/model-checking/kani-github-action/blob/v1/README.md
- README SHA: 9971d6ab4afacdea7ab9391fb8a5e65a64cd5a64
- Manifests: tests/cargo-kani/simple-lib/Cargo.toml
- Sampled source files: src/install-kani.sh, scripts/copyright_check.py, scripts/run-autopep8.sh, scripts/run-clang-format.sh
- Git tree state: captured
- Evidence fingerprint: 3b3e0f0b25a16a52062cc801f7662b58e09f857c2d2518314e5af2a210fbe54c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
