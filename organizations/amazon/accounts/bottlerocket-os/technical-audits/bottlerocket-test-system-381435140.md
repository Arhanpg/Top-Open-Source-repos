# bottlerocket-os/bottlerocket-test-system

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-test-system
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:14:14+00:00

## Project purpose

A system for testing Bottlerocket. To learn more about how it works, see the design document.

## Why this project is used

A system for testing Bottlerocket

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust, Dockerfile, Makefile, Shell, Go
- Frameworks/libraries: Unknown / not established
- Dependency names: anyhow, assert_cmd, aws-config, aws-lc-rs, aws-sdk-cloudwatchlogs, aws-types, clap, env_logger, futures, http, k8s-openapi, kube, kube-runtime, lazy_static, log, selftest, serde_json, snafu, terminal_size, testsys-model, tokio
- Build/package tools: Cargo manifest, Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: agent/agent-common/src/lib.rs, agent/builder-derive/src/lib.rs, agent/configuration-derive/src/lib.rs, agent/resource-agent/src/clients/mod.rs

## Setup and usage

- Quickstart: See our QUICKSTART for a walk through of compiling, deploying, and running a quick test.
- Quickstart: More detailed quickstart guides can be found in the main Bottlerocket repo.
- Quickstart: See the QUICKSTART-*.md files for information on the various deployment targets.

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-test-system/blob/develop/README.md
- README SHA: 37983de30f6e4b50d3ad7ec5b61c997b7476be86
- Manifests: Cargo.toml, Dockerfile, Makefile, cli/Cargo.toml, controller/Cargo.toml, controller/Dockerfile
- Sampled source files: agent/agent-common/src/lib.rs, agent/builder-derive/src/lib.rs, agent/configuration-derive/src/lib.rs, agent/resource-agent/src/clients/mod.rs
- Git tree state: captured
- Evidence fingerprint: d0b74f98af6a4e47327820fd871ce64dab43dd085cf7ff96afae8737800db4e5

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
