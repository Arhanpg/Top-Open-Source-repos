# aws/NitroTPM-Tools

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/NitroTPM-Tools
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:12:13+00:00

## Project purpose

A collection of utilities for working with NitroTPM attestation.

## Why this project is used

A collection of utilities for working with NitroTPM attestation.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: anyhow, authenticode, aws-config, aws-lc-rs, aws-nitro-enclaves-nsm-api, aws-sdk-kms, base64ct, ciborium, clap, digest, env_logger, hex, log, object, openssl, semver, serde, serde_json, thiserror, tokio, tss-esapi, tss-esapi-sys, uuid, x509-cert
- Build/package tools: Cargo manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: nitro-tpm-attest/src/lib.rs, nitro-tpm-attest/src/main.rs, nitro-tpm-attest/src/raw/mod.rs, nitro-tpm-attest/src/tss/message_buffer/mod.rs

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws/NitroTPM-Tools/blob/main/README.md
- README SHA: 087b7ab1119290aca58f54b2e26ca793b65b98d3
- Manifests: Cargo.toml, nitro-tpm-attest/Cargo.toml, nitro-tpm-pcr-compute/Cargo.toml
- Sampled source files: nitro-tpm-attest/src/lib.rs, nitro-tpm-attest/src/main.rs, nitro-tpm-attest/src/raw/mod.rs, nitro-tpm-attest/src/tss/message_buffer/mod.rs
- Git tree state: captured
- Evidence fingerprint: 7779f7c962abb55aeae051c1e3fbca7a9ce3b867cf7fc950deb669f55bc0a802

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
