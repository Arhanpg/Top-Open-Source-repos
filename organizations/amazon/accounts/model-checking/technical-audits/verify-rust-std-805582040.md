# model-checking/verify-rust-std

- Company: Amazon
- Account: model-checking
- Repository: https://github.com/model-checking/verify-rust-std
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:07:02+00:00

## Project purpose

This repository is a fork of the official Rust programming language repository, created solely to verify the Rust standard library. It should not be used as an alternative to the official Rust releases. The repository is tool agnostic and welcomes the addition of new tools. The currently accepted tools are Flux, ESBMC, Kani, KMIR, and VeriFast.

## Why this project is used

Verifying the Rust standard library

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust, C, Python, Shell, Assembly, Dockerfile, Julia
- Frameworks/libraries: Unknown / not established
- Dependency names: compiler_builtins, core, mdbook, mdbook-linkcheck, pastey, rand, rand_xorshift, safety, serde_json
- Build/package tools: Cargo manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: doc/mdbook-metrics/src/main.rs, library/alloc/src/collections/binary_heap/mod.rs, library/alloc/src/collections/btree/mod.rs, library/alloc/src/collections/mod.rs

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: See SECURITY for more information.

## Evidence and provenance

- README: https://github.com/model-checking/verify-rust-std/blob/main/README.md
- README SHA: 3987760dee80b04d068a29729974622fd402eaae
- Manifests: library/Cargo.toml, testable-simd-models/Cargo.toml, doc/mdbook-metrics/Cargo.toml, library/alloc/Cargo.toml, library/alloctests/Cargo.toml, library/compiler-builtins/Cargo.toml
- Sampled source files: doc/mdbook-metrics/src/main.rs, library/alloc/src/collections/binary_heap/mod.rs, library/alloc/src/collections/btree/mod.rs, library/alloc/src/collections/mod.rs
- Git tree state: captured
- Evidence fingerprint: 4b5bd11c5bd00e2df6e5fe943004d2d586b1a156c4e73fc5345f2ea4cb05362c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
