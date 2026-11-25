# bottlerocket-os/bottlerocket-control-container

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-control-container
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:14:13+00:00

## Project purpose

This is the control container for the Bottlerocket operating system. This container runs the AWS SSM Agent that lets you run commands, or start interactive sessions, on Bottlerocket instances in EC2 and hybrid environments.

## Why this project is used

A container for remote control of Bottlerocket

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust, Shell, Dockerfile, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: aws-credential-types, aws-lc-rs, aws-sigv4, aws-smithy-runtime-api, base64, chrono, flate2, hex, log, reqwest, rustls, serde, serde_json, sha2, simplelog, snafu, uuid
- Build/package tools: Cargo manifest, Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: sources/corgid/src/main.rs, sources/corgid/src/error.rs, sources/corgid/src/imds.rs, sources/corgid/src/inspector.rs

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-control-container/blob/develop/README.md
- README SHA: b31c3286332188abeaaeef4229a456180e4a9bdb
- Manifests: Dockerfile, Makefile, sources/Cargo.toml, sources/corgid/Cargo.toml
- Sampled source files: sources/corgid/src/main.rs, sources/corgid/src/error.rs, sources/corgid/src/imds.rs, sources/corgid/src/inspector.rs
- Git tree state: captured
- Evidence fingerprint: 5e5cce2b7d378b8df204a59385b5d72b527a83dd3636b54169f13ab4d1813d2f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
