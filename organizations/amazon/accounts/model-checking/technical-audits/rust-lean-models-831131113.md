# model-checking/rust-lean-models

- Company: Amazon
- Account: model-checking
- Repository: https://github.com/model-checking/rust-lean-models
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T06:58:59+00:00

## Project purpose

-- Copyright Kani Contributors -- SPDX-License-Identifier: Apache-2.0 OR MIT --->

## Why this project is used

Lean models of Rust libraries

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Lean
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: none

## Setup and usage

- Installation: - Add the following lines to your lakefile.lean:
- Installation: require «rust-lean-models» from git "https://github.com/model-checking/rust-lean-models"
- Installation: - Change the lean version in your lean-toolchain to the one in
- Installation: - Run lake update in the terminal.
- Installation: - Import the packages and open the namespaces in your Lean files
- Installation: (see ProofTutorial.lean)
- Installation: import RustLeanModels.Basic
- Installation: import RustLeanModels.RustString

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/model-checking/rust-lean-models/blob/main/README.md
- README SHA: bc8db31c133ad9e7ae47bbcf58c6f2a0134b2af2
- Manifests: none
- Sampled source files: none
- Git tree state: captured
- Evidence fingerprint: d9a2ce9871811491d3549034e3e15a947ab179cfcc52aa189983a09468474065

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
