# firecracker-microvm/firecracker

- Company: Amazon
- GitHub account: [https://github.com/firecracker-microvm](https://github.com/firecracker-microvm)
- Mapping status: official-directory-listed
- Repository: [firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)
- Default branch: main
- README: [Open upstream README](https://github.com/firecracker-microvm/firecracker/blob/main/README.md)
- README blob SHA: fc4aa8ee2250e9e953b4cff8bf603bc4e5de80c3
- Repository ID: 107505869
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Secure and fast microVMs for serverless computing.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:15+00:00

### Short excerpt (up to 100 words)

> Our mission is to enable secure, multi-tenant, minimal-overhead execution of container and function workloads. Read more about the Firecracker Charter here. Firecracker is an open source virtualization technology that is purpose-built for creating and managing secure, multi-tenant container and function-based services that provide serverless operational models. Firecracker runs workloads in lightweight virtual machines, called microVMs, which combine the security and isolation properties provided by hardware virtualization technology with the speed and flexibility of containers. The main component of Firecracker is a virtual machine monitor (VMM) that uses the Linux Kernel Virtual Machine (KVM) to create and run microVMs. Firecracker can

### README headings

- What is Firecracker?
- Overview
- Getting Started
- Contributing
- Releases
- Design
- Features & Capabilities
- Tested platforms
- Known issues and Limitations
- Performance
- Policy for Security Disclosures
- FAQ & Contact

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 5,192,127 |
| Python | 1,292,338 |
| Shell | 107,670 |
| C | 43,039 |
| Dockerfile | 14,678 |
| Go | 3,759 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- tests/pyproject.toml (capture: captured)
- src/acpi-tables/Cargo.toml (capture: captured) — dependency clues: displaydoc, thiserror, vm-memory, zerocopy
- src/clippy-tracing/Cargo.toml (capture: captured) — dependency clues: clap, itertools, proc-macro2, quote, syn, uuid, walkdir
- src/cpu-template-helper/Cargo.toml (capture: captured) — dependency clues: clap, displaydoc, libc, log-instrument, serde, serde_json, thiserror, vmm, vmm-sys-util
- src/firecracker/Cargo.toml (capture: captured) — dependency clues: cargo_toml, displaydoc, event-manager, libc, log-instrument, micro_http, seccompiler, semver, serde, serde_derive, serde_json, thiserror, userfaultfd, utils, vmm, vmm-sys-util

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 38190
- Forks at capture: 2776
- Last updated: 2026-11-23T18:57:02Z
- Last pushed: 2026-11-23T16:57:25Z
- Topics: containers, minimalist, open-source, oversubscription, rust, sandbox, serverless, virtual-machine, virtualization

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/firecracker-microvm/firecracker)
- [README](https://github.com/firecracker-microvm/firecracker/blob/main/README.md)
- [Issues](https://github.com/firecracker-microvm/firecracker/issues)
- [Releases](https://github.com/firecracker-microvm/firecracker/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
