# bottlerocket-os/bottlerocket-kernel-kit

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-kernel-kit
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:54:01+00:00

## Project purpose

This is the kernel kit for Bottlerocket. It includes Linux kernels and dependencies for downstream package and variant builds.

## Why this project is used

A kit with kernels, bootloaders, and firmware packaged for Bottlerocket

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Shell, Rust, Makefile, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: grub, kernel-6_1, kernel-6_12, kernel-6_18, kernel-6_18-microvm, kernel-6_18-shared-configs, kernel-next, kmod-6_1-efa, kmod-6_1-nvidia-r580, kmod-6_1-nvidia-r595, kmod-6_12-efa, kmod-6_12-nvidia-r580, kmod-6_12-nvidia-r595, kmod-6_18-efa, kmod-6_18-nvidia-r580, kmod-6_18-nvidia-r595, kmod-next-efa, kmod-next-nvidia-r620, libkcapi, linux-firmware, microcode, nvidia-migmanager, nvlsm, shim
- Build/package tools: Cargo manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: sources/generate-readme/src/lib.rs, sources/nvidia-migmanager/src/main.rs, sources/nvidia-migmanager/src/mig_profile.rs, kits/build.rs

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-kernel-kit/blob/develop/README.md
- README SHA: 1dd81f483fca49a64e86865df22bf80abd2e7aec
- Manifests: Cargo.toml, Makefile, sources/Cargo.toml, kits/bottlerocket-kernel-kit/Cargo.toml, packages/grub/Cargo.toml, packages/kernel-6.1/Cargo.toml
- Sampled source files: sources/generate-readme/src/lib.rs, sources/nvidia-migmanager/src/main.rs, sources/nvidia-migmanager/src/mig_profile.rs, kits/build.rs
- Git tree state: captured
- Evidence fingerprint: 5832ea9a4ecc1045de73c216823fecd587ff5f4a59f7992b537be849147ff333

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
