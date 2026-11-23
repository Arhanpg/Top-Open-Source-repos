# bottlerocket-os/bottlerocket-kernel-kit

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-kernel-kit](https://github.com/bottlerocket-os/bottlerocket-kernel-kit)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-kernel-kit/blob/develop/README.md)
- README blob SHA: 1dd81f483fca49a64e86865df22bf80abd2e7aec
- Repository ID: 884539052
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A kit with kernels, bootloaders, and firmware packaged for Bottlerocket 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:05+00:00

### Short excerpt (up to 100 words)

> This is the kernel kit for Bottlerocket. It includes Linux kernels and dependencies for downstream package and variant builds. The kernel kit includes: * multiple versions of the Linux kernel * bootloaders * firmware The Bottlerocket kernel kit is available through Amazon ECR Public. The kernel kit can be built on either an **x86_64** or an **aarch64** host. To do this you can use the following commands. make OR make ARCH=<aarch64, x86_64> See the BUILDING guide for more details.

### README headings

- Bottlerocket Kernel Kit
- Contents
- Availability
- Development

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 39,336 |
| Rust | 35,864 |
| Makefile | 1,920 |
| JavaScript | 1,895 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Makefile (capture: captured)
- sources/Cargo.toml (capture: captured)
- kits/bottlerocket-kernel-kit/Cargo.toml (capture: captured) — dependency clues: grub, kernel-6_1, kernel-6_12, kernel-6_18, kernel-6_18-microvm, kernel-6_18-shared-configs, kernel-next, kmod-6_1-efa, kmod-6_1-nvidia-r580, kmod-6_1-nvidia-r595, kmod-6_12-efa, kmod-6_12-nvidia-r580, kmod-6_12-nvidia-r595, kmod-6_18-efa, kmod-6_18-nvidia-r580, kmod-6_18-nvidia-r595, kmod-next-efa, kmod-next-nvidia-r620, libkcapi, linux-firmware
- packages/grub/Cargo.toml (capture: captured)
- packages/kernel-6.1/Cargo.toml (capture: captured) — dependency clues: microcode

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 14
- Forks at capture: 43
- Last updated: 2026-11-11T20:21:12Z
- Last pushed: 2026-11-18T23:04:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-kernel-kit)
- [README](https://github.com/bottlerocket-os/bottlerocket-kernel-kit/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-kernel-kit/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-kernel-kit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
