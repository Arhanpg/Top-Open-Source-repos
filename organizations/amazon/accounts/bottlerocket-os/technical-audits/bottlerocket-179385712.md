# bottlerocket-os/bottlerocket

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:47:08+00:00

## Project purpose

Welcome to Bottlerocket!

## Why this project is used

An operating system designed for hosting containers

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust, Shell, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: envy, generate-readme, log, semver, serde, snafu
- Build/package tools: Cargo manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: sources/api/datastore/src/deserialization/mod.rs, sources/api/datastore/src/lib.rs, sources/api/datastore/src/serialization/mod.rs, sources/api/migration/migration-helpers/src/lib.rs

## Setup and usage

No setup information established.

## Limitations and caveats

- Platform-specific settings: Platform-specific settings are automatically set at boot time by early-boot-config based on metadata available on the running platform.
- Platform-specific settings: They can be overridden for testing purposes in the same way as other settings.
- Security: To learn more about security features in Bottlerocket, please see SECURITY FEATURES.
- Security: It describes how we use features like dm-verity and SELinux to protect the system from security threats.
- Security: To learn more about security recommendations for Bottlerocket, please see SECURITY GUIDANCE.
- Security: It documents additional steps you can take to secure the OS, and includes resources such as a Pod Security Policy for your reference.
- Security: In addition, almost all first-party components are written in Rust.
- Security: Rust eliminates some classes of memory safety issues, and encourages design patterns that help security.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md
- README SHA: de13b0d2effa4ae09693d9872bea2339916f62f3
- Manifests: Cargo.toml, sources/Cargo.toml, packages/settings-defaults/Cargo.toml, packages/settings-migrations/Cargo.toml, packages/settings-plugins/Cargo.toml, sources/bottlerocket-release/Cargo.toml
- Sampled source files: sources/api/datastore/src/deserialization/mod.rs, sources/api/datastore/src/lib.rs, sources/api/datastore/src/serialization/mod.rs, sources/api/migration/migration-helpers/src/lib.rs
- Git tree state: captured
- Evidence fingerprint: 18aee65bfd79f6bee1cfe0f84a9584bf22580da2ebe79083f2e83a31a44f2b43

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
