# model-checking/verify-rust-std

- Company: Amazon
- GitHub account: [https://github.com/model-checking](https://github.com/model-checking)
- Mapping status: official-directory-listed
- Repository: [model-checking/verify-rust-std](https://github.com/model-checking/verify-rust-std)
- Default branch: main
- README: [Open upstream README](https://github.com/model-checking/verify-rust-std/blob/main/README.md)
- README blob SHA: 3987760dee80b04d068a29729974622fd402eaae
- Repository ID: 805582040
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Verifying the Rust standard library

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:07:04+00:00

### Short excerpt (up to 100 words)

> This repository is a fork of the official Rust programming language repository, created solely to verify the Rust standard library. It should not be used as an alternative to the official Rust releases. The repository is tool agnostic and welcomes the addition of new tools. The currently accepted tools are Flux, ESBMC, Kani, KMIR, and VeriFast. The goal is to have a verified Rust standard library and prove that it is safe. 1. Contributing to the core mechanism of verifying the rust standard library 2. Creating new techniques to perform scalable verification 3. Apply techniques to verify previously unverified parts

### README headings

- Rust standard library verification
- Citing this project
- Contact
- Security
- License
- Kani
- ESBMC
- Flux
- VeriFast
- KMIR
- Rust
- Introducing a New Tool

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 44,100,189 |
| C | 1,157,335 |
| Python | 230,360 |
| Shell | 74,970 |
| Assembly | 69,549 |
| Dockerfile | 24,104 |
| Julia | 4,196 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- library/Cargo.toml (capture: captured)
- testable-simd-models/Cargo.toml (capture: captured) — dependency clues: pastey, rand
- doc/mdbook-metrics/Cargo.toml (capture: captured) — dependency clues: mdbook, mdbook-linkcheck, serde_json
- library/alloc/Cargo.toml (capture: captured) — dependency clues: compiler_builtins, core, safety
- library/alloctests/Cargo.toml (capture: captured) — dependency clues: rand, rand_xorshift
- library/compiler-builtins/Cargo.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 374
- Forks at capture: 96
- Last updated: 2026-11-23T12:22:56Z
- Last pushed: 2026-11-22T18:20:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/model-checking/verify-rust-std)
- [README](https://github.com/model-checking/verify-rust-std/blob/main/README.md)
- [Issues](https://github.com/model-checking/verify-rust-std/issues)
- [Releases](https://github.com/model-checking/verify-rust-std/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
