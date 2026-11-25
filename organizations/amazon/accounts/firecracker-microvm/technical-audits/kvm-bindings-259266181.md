# firecracker-microvm/kvm-bindings

- Company: Amazon
- Account: firecracker-microvm
- Repository: https://github.com/firecracker-microvm/kvm-bindings
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:54:25+00:00

## Project purpose

Rust FFI bindings to KVM, generated using bindgen. It currently has support for the following target architectures:

## Why this project is used

Rust FFI bindings to KVM, generated using bindgen. It currently has support for the following target architectures:

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust
- Frameworks/libraries: Unknown / not established
- Dependency names: versionize, versionize_derive, vmm-sys-util
- Build/package tools: Cargo manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/arm64/mod.rs, src/lib.rs, src/x86/mod.rs, src/arm64/fam_wrappers.rs

## Setup and usage

- Usage: First, add the following to your Cargo.toml:
- Usage: Next, add this to your crate root:
- Usage: extern crate kvm_bindings;
- Usage: This crate also offers safe wrappers over FAM structs - FFI structs that have
- Usage: a Flexible Array Member in their definition.
- Usage: These safe wrappers can be used if the fam-wrappers feature is enabled for
- Usage: kvm-bindings = { version = "0.4", features = ["fam-wrappers"]}

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/firecracker-microvm/kvm-bindings/blob/master/README.md
- README SHA: 43a607bcfe845dd479c1e4c4f4cad863aef2a760
- Manifests: Cargo.toml
- Sampled source files: src/arm64/mod.rs, src/lib.rs, src/x86/mod.rs, src/arm64/fam_wrappers.rs
- Git tree state: captured
- Evidence fingerprint: 4b1dfa92db055ce9683e9c35632f0f0cd9deb1b14f8caf467a434448cf1877d5

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
