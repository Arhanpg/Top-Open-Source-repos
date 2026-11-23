# firecracker-microvm/versionize_derive

- Company: Amazon
- GitHub account: [https://github.com/firecracker-microvm](https://github.com/firecracker-microvm)
- Mapping status: official-directory-listed
- Repository: [firecracker-microvm/versionize_derive](https://github.com/firecracker-microvm/versionize_derive)
- Default branch: main
- README: [Open upstream README](https://github.com/firecracker-microvm/versionize_derive/blob/main/README.md)
- README blob SHA: b0b5a224b4db4024a672b4fc5e3994e201527bc5
- Repository ID: 259238816
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Exports the Versionize derive proc macro that generates the Versionize implementation for structs, enums and unions by using structure annotations.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:06:27+00:00

### Short excerpt (up to 100 words)

> **Versionize is a framework for version tolerant serializion/deserialization of Rust data structures, designed for usecases that need fast deserialization times and minimal size overhead. It does not aim to be a generic serialization framework and only the bincode backend is supported.** - Versionize documentation - Releases This crate is currently used for cross-version serialization with the other use cases. It should be considered **experimental software** outside the Firecracker context. It’s likely that this crate will see both interface and implementation changes in the future. extern crate versionize; extern crate versionize_derive; use versionize::{VersionMap, Versionize, VersionizeResult}; use versionize_derive::Versionize; // The test structure

### README headings

- You may be looking for:
- Important note
- Versionize in action

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 32,240 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: proc-macro2, quote, syn

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 14
- Forks at capture: 21
- Last updated: 2026-07-23T16:32:48Z
- Last pushed: 2023-08-24T10:40:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/firecracker-microvm/versionize_derive)
- [README](https://github.com/firecracker-microvm/versionize_derive/blob/main/README.md)
- [Issues](https://github.com/firecracker-microvm/versionize_derive/issues)
- [Releases](https://github.com/firecracker-microvm/versionize_derive/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
