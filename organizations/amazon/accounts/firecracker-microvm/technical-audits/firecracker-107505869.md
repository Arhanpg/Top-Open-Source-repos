# firecracker-microvm/firecracker

- Company: Amazon
- Account: firecracker-microvm
- Repository: https://github.com/firecracker-microvm/firecracker
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:47:32+00:00

## Project purpose

Our mission is to enable secure, multi-tenant, minimal-overhead execution of container and function workloads.

## Why this project is used

Secure and fast microVMs for serverless computing.

## Core features

- Configure the microvm by:: Configure the microvm by:
  - Evidence: README.md#Features & Capabilities
- Setting the number of vCPUs (the default is 1).: Setting the number of vCPUs (the default is 1).
  - Evidence: README.md#Features & Capabilities
- Setting the memory size (the default is 128 MiB).: Setting the memory size (the default is 128 MiB).
  - Evidence: README.md#Features & Capabilities
- Configuring a CPU template.: Configuring a CPU template.
  - Evidence: README.md#Features & Capabilities
- Add one or more network interfaces to the microVM.: Add one or more network interfaces to the microVM.
  - Evidence: README.md#Features & Capabilities
- Add one or more read-write or read-only disks to the microVM, each represented: Add one or more read-write or read-only disks to the microVM, each represented
  - Evidence: README.md#Features & Capabilities
- Trigger a block device re-scan while the guest is running. This enables the: Trigger a block device re-scan while the guest is running. This enables the
  - Evidence: README.md#Features & Capabilities
- Change the backing file for a block device, before or after the guest boots.: Change the backing file for a block device, before or after the guest boots.
  - Evidence: README.md#Features & Capabilities
- Configure rate limiters for virtio devices which can limit the bandwidth,: Configure rate limiters for virtio devices which can limit the bandwidth,
  - Evidence: README.md#Features & Capabilities
- Configure the logging and metric system.: Configure the logging and metric system.
  - Evidence: README.md#Features & Capabilities
- [BETA] Configure the data tree of the guest-facing metadata service. The: [BETA] Configure the data tree of the guest-facing metadata service. The
  - Evidence: README.md#Features & Capabilities
- Add a vsock socket to the microVM.: Add a vsock socket to the microVM.
  - Evidence: README.md#Features & Capabilities
- Add a entropy device to the microVM.: Add a entropy device to the microVM.
  - Evidence: README.md#Features & Capabilities
- Add a pmem device to the microVM.: Add a pmem device to the microVM.
  - Evidence: README.md#Features & Capabilities
- Configure and manage memory hotplugging.: Configure and manage memory hotplugging.
  - Evidence: README.md#Features & Capabilities

## Technology stack

- Languages: Rust, Python, Shell, C, Dockerfile, Go
- Frameworks/libraries: Unknown / not established
- Dependency names: cargo_toml, clap, displaydoc, event-manager, itertools, libc, log-instrument, micro_http, proc-macro2, quote, seccompiler, semver, serde, serde_derive, serde_json, syn, thiserror, userfaultfd, utils, uuid, vm-memory, vmm, vmm-sys-util, walkdir, zerocopy
- Build/package tools: Cargo manifest, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/acpi-tables/src/lib.rs, src/clippy-tracing/src/main.rs, src/cpu-template-helper/src/fingerprint/mod.rs, src/cpu-template-helper/src/main.rs

## Setup and usage

- Getting Started: To get started with Firecracker, download the latest
- Getting Started: or build it from source.
- Getting Started: You can build Firecracker on any Unix/Linux system that has Docker running (we
- Getting Started: use a development container) and bash installed, as follows:
- Getting Started: git clone https://github.com/firecracker-microvm/firecracker
- Getting Started: toolchain="$(uname -m)-unknown-linux-musl"
- Getting Started: The Firecracker binary will be placed at
- Getting Started: build/cargo_target/${toolchain}/debug/firecracker. For more information on

## Limitations and caveats

- Tested platforms: We test all combinations of:
- Tested platforms: | Instance | Host OS & Kernel | Guest Rootfs | Guest Kernel |
- Tested platforms: | :------------------------------------------ | :---------------- | :----------- | :----------- |
- Tested platforms: | m5n.metal (Intel Cascade Lake) | al2 linux_5.10 | ubuntu 24.04 | linux_5.10 |
- Tested platforms: | m6i.metal (Intel Ice Lake) | al2023 linux_6.1 | | linux_6.1 |
- Tested platforms: | | al2023 linux_6.18 | | |
- Tested platforms: | m7i.metal-24xl (Intel Sapphire Rapids) | | | |
- Tested platforms: | m7i.metal-48xl (Intel Sapphire Rapids) | | | |

## Evidence and provenance

- README: https://github.com/firecracker-microvm/firecracker/blob/main/README.md
- README SHA: fc4aa8ee2250e9e953b4cff8bf603bc4e5de80c3
- Manifests: Cargo.toml, tests/pyproject.toml, src/acpi-tables/Cargo.toml, src/clippy-tracing/Cargo.toml, src/cpu-template-helper/Cargo.toml, src/firecracker/Cargo.toml
- Sampled source files: src/acpi-tables/src/lib.rs, src/clippy-tracing/src/main.rs, src/cpu-template-helper/src/fingerprint/mod.rs, src/cpu-template-helper/src/main.rs
- Git tree state: captured
- Evidence fingerprint: 7c2cb031ddfe3192abf911039ff336a9f5c0e34c410c0037efa09195a10357f1

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
