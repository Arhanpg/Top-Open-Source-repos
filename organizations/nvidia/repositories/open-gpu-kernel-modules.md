# NVIDIA Linux Open GPU Kernel Modules

- **Company:** NVIDIA
- **GitHub organization:** [NVIDIA](https://github.com/NVIDIA)
- **Repository:** [NVIDIA/open-gpu-kernel-modules](https://github.com/NVIDIA/open-gpu-kernel-modules)
- **Default branch:** main
- **README:** [Open upstream README](https://github.com/NVIDIA/open-gpu-kernel-modules/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `2858956ff00ff43ea8373708ea11b578e516ef1e`
- **Lifecycle:** Check current upstream release and support status before adoption

## Project overview

A source release of NVIDIA's open GPU kernel modules for Linux. The README describes the repository as a published driver source snapshot that must be paired with matching NVIDIA user-space driver components and GSP firmware.

## Features and capabilities

- Builds kernel modules with make modules and installs them with make modules_install.
- Supports x86_64 and aarch64 target CPU architectures, including cross-compilation configuration.
- Documents GCC or Clang toolchain support; the kernel interface layer must use the toolchain used to build the target kernel.
- The README states Linux kernel 4.15 or newer is supported, consistent with the proprietary kernel-module support range stated there.
- Separates OS-agnostic module code from kernel-interface layers and documents directory layout and Nouveau integration.
- Provides contribution, issue-reporting and security-disclosure guidance.

## Technology stack

Linux kernel modules; C/C++-oriented kernel build workflow; Make; GCC or Clang; x86_64/aarch64; target Linux kernel headers/toolchain; paired NVIDIA GSP firmware and corresponding user-space GPU driver release.

## Getting started

The README instructs users to build with make modules and install using make modules_install after uninstalling existing NVIDIA kernel modules. The resulting modules must be paired with GSP firmware and user-space components from the matching driver release.

## Lifecycle, compatibility and operational considerations

The README says this repository is generated from a shared codebase and functions mostly as a snapshot of each driver release. Per-change history may not be available, and contributions require manual merging into the shared codebase, making large refactors difficult to accept.

## Evaluation guidance

Review the exact driver/model/runtime versions, hardware compatibility, licence, security guidance and maintenance state before using this project. Performance or deployment assumptions should be validated on the actual target hardware and software stack. This dossier summarizes the README; it is not a source-code, security or benchmark audit.

## Upstream references

- [Repository](https://github.com/NVIDIA/open-gpu-kernel-modules)
- [README](https://github.com/NVIDIA/open-gpu-kernel-modules/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/open-gpu-kernel-modules/issues)
- [Releases](https://github.com/NVIDIA/open-gpu-kernel-modules/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. The technology and lifecycle claims above are limited to the README evidence; source-level dependency validation is a separate task.*
