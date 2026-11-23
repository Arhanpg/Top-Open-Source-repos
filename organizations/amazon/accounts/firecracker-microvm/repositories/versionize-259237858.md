# firecracker-microvm/versionize

- Company: Amazon
- GitHub account: [https://github.com/firecracker-microvm](https://github.com/firecracker-microvm)
- Mapping status: official-directory-listed
- Repository: [firecracker-microvm/versionize](https://github.com/firecracker-microvm/versionize)
- Default branch: main
- README: [Open upstream README](https://github.com/firecracker-microvm/versionize/blob/main/README.md)
- README blob SHA: 31425a1586614bd49a458d1d7a4362d6ff00dc84
- Repository ID: 259237858
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Versionize is a framework for version tolerant serializion/deserialization of Rust data structures, designed for usecases that need fast deserialization times and minimal size overhead. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:06:25+00:00

### Short excerpt (up to 100 words)

> **Versionize is a framework for version tolerant serializion/deserialization of Rust data structures, designed for usecases that need fast deserialization times and minimal size overhead. It does not aim to be a generic serialization framework and only the bincode backend is supported.** This crate is currently used for cross-version serialization with the other use cases. It should be considered **experimental software** outside the Firecracker context. It’s likely that this crate will see both interface and implementation changes in the future. extern crate versionize; extern crate versionize_derive; use versionize::{VersionMap, Versionize, VersionizeResult}; use versionize_derive::Versionize; // The test structure is at version 3. pub

### README headings

- Important note
- Versionize in action

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 100,540 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: bincode, crc64, proc-macro2, quote, serde, serde_derive, syn, versionize_derive, vmm-sys-util

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 63
- Forks at capture: 36
- Last updated: 2026-07-23T16:32:47Z
- Last pushed: 2024-01-02T15:14:27Z
- Topics: serialization

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/firecracker-microvm/versionize)
- [README](https://github.com/firecracker-microvm/versionize/blob/main/README.md)
- [Issues](https://github.com/firecracker-microvm/versionize/issues)
- [Releases](https://github.com/firecracker-microvm/versionize/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
