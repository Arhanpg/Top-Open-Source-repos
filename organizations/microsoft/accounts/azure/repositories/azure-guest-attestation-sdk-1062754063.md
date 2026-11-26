# Azure/azure-guest-attestation-sdk

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-guest-attestation-sdk](https://github.com/Azure/azure-guest-attestation-sdk)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/azure-guest-attestation-sdk/blob/main/README.md)
- README blob SHA: 8c57c3028d58933dc7d297be117a127083f1b698
- README bytes captured: 21582
- README truncated at capture limit: False
- Repository ID: 1062754063
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure Guest Attestation SDK

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T21:15:39+00:00

### Short excerpt (up to 300 words)

> cargo run -p azure-guest-attest cargo run -p azure-guest-attest cargo install --locked --force Rust toolchain (install via

### README headings

- Azure Guest Attestation SDK
- Documentation
- Repository Structure
- Quick Start
- Prerequisites
- Setup
- Windows
- Linux/macOS
- Build All
- From repository root
- Build Individual Crates
- Library only
- Attestation CLI tool
- TPM CLI tool
- Testing
- Recommended: cargo-nextest (parallel, process-per-test)
- Install or upgrade
- Run all SDK tests (uses workspace alias)
- Or explicitly
- Fallback: cargo test
- Using workspace alias
- Or explicitly
- Other Test Commands
- Check formatting
- Run clippy lints (all targets including tests)
- Unit tests only (no vTPM, no hardware TPM needed)
- vTPM Test Requirements
- Crates
- [azure-tpm](crates/azure-tpm/)
- [azure-guest-attestation-sdk](crates/azure-guest-attestation-sdk/)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: With summary (enable feature)

> cargo run -p azure-guest-attest

### Features and capabilities: With summary (enable feature)

> cargo run -p azure-guest-attest

### Getting started and usage: Install or upgrade

> cargo install --locked --force

### Technology and requirements: Prerequisites

> Rust toolchain (install via

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 1,101,749 |
| HTML | 54,091 |
| Shell | 45,200 |
| PowerShell | 44,076 |
| JavaScript | 22,728 |
| CSS | 9,452 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- crates/azure-guest-attestation-sdk/Cargo.toml (capture: captured) — dependency clues: aes-gcm, azure-tpm, base64, bitfield-struct, der, hex, injectorpp, num-bigint, rand, rcgen, reqwest, rustls, rustls-symcrypt, serde, serde_json, sha2, symcrypt, tracing, tracing-subscriber, webpki
- crates/azure-tpm-testkit/Cargo.toml (capture: captured) — dependency clues: azure-tpm, getrandom, ms-tpm-20-ref
- crates/azure-tpm/Cargo.toml (capture: captured) — dependency clues: bitfield-struct, hex, rand, serde, serde_json, sha1, sha2, symcrypt, tracing
- tools/azure-guest-attest-web/Cargo.toml (capture: captured) — dependency clues: axum, azure-guest-attestation-sdk, base64, clap, hex, hyper, hyper-util, rcgen, rustls, rustls-symcrypt, serde, serde_json, symcrypt, tokio, tokio-rustls, tower, tracing, yasna
- tools/azure-guest-attest/Cargo.toml (capture: captured) — dependency clues: anyhow, azure-guest-attestation-sdk, base64, clap, hex, jwt, serde, serde_json, x509-parser

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 3
- Forks at capture: 8
- Last updated: 2026-11-02T23:22:39Z
- Last pushed: 2026-11-20T07:15:23Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-guest-attestation-sdk)
- [README](https://github.com/Azure/azure-guest-attestation-sdk/blob/main/README.md)
- [Issues](https://github.com/Azure/azure-guest-attestation-sdk/issues)
- [Releases](https://github.com/Azure/azure-guest-attestation-sdk/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
