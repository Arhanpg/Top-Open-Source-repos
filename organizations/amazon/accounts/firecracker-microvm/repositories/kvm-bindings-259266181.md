# firecracker-microvm/kvm-bindings

- Company: Amazon
- GitHub account: [https://github.com/firecracker-microvm](https://github.com/firecracker-microvm)
- Mapping status: official-directory-listed
- Repository: [firecracker-microvm/kvm-bindings](https://github.com/firecracker-microvm/kvm-bindings)
- Default branch: master
- README: [Open upstream README](https://github.com/firecracker-microvm/kvm-bindings/blob/master/README.md)
- README blob SHA: 43a607bcfe845dd479c1e4c4f4cad863aef2a760
- Repository ID: 259266181
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:25+00:00

### Short excerpt (up to 100 words)

> Rust FFI bindings to KVM, generated using following target architectures: - x86 - x86_64 - arm - arm64 The bindings exported by this crate are statically generated using header files associated with a specific kernel version, and are not automatically synced with the kernel version running on a particular host. The user must ensure that specific structures, members, or constants are supported and valid for the kernel version they are using. For example, the `immediate_exit` field from the `kvm_run` structure is only meaningful if the `KVM_CAP_IMMEDIATE_EXIT` capability is available. Using invalid fields or features may lead to undefined behaviour. First,

### README headings

- This fork is archived. The serialization functionality has been merged [upstream](https://github.com/rust-vmm/kvm-bindings) since 2024/04/16
- kvm-bindings
- Usage
- Dependencies

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 688,575 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: versionize, versionize_derive, vmm-sys-util

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: True
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 19
- Last updated: 2024-05-08T09:45:55Z
- Last pushed: 2024-05-08T09:45:23Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/firecracker-microvm/kvm-bindings)
- [README](https://github.com/firecracker-microvm/kvm-bindings/blob/master/README.md)
- [Issues](https://github.com/firecracker-microvm/kvm-bindings/issues)
- [Releases](https://github.com/firecracker-microvm/kvm-bindings/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
