# XNU — Darwin kernel

- **Company:** Apple
- **GitHub organization:** [apple](https://github.com/apple)
- **Repository:** [apple/darwin-xnu](https://github.com/apple/darwin-xnu)
- **Default branch:** main
- **README:** [Open upstream README](https://github.com/apple/darwin-xnu/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `da6bb7bc15a8eec1644a6223709f21f3be93dbae`

## Project overview

XNU is the kernel used as part of the Darwin operating system for macOS and iOS. The README describes it as a hybrid kernel combining Mach components from Carnegie Mellon University with FreeBSD components and the C++ IOKit driver API.

## Features and capabilities

- Contains Mach kernel subsystems, BSD subsystems, platform-specific code, security policy interfaces and driver-related IOKit components.
- The source tree separates exported API configuration, kernel bootstrapping, system-call interfaces, kernel subsystems, platform expert code and development tools.
- Supports configurable kernel builds such as DEVELOPMENT, DEBUG, RELEASE and PROFILE variants.
- The build system accepts architecture and kernel-configuration selections and can create bootable kernel images and symbol-bearing binaries.
- Documents kernelcache construction, debug-symbol formats, build logging, parallel jobs and remote-build options.

## Technology stack

Kernel-level C/C++ codebase with a Make-based build system, Clang/GCC toolchain references, macOS SDK usage and architecture-specific configuration. The README describes C++ IOKit and Mach/BSD components.

## Getting started

The README shows builds using make with SDKROOT, ARCH_CONFIGS and KERNEL_CONFIGS. A development-kernel build requires the appropriate macOS SDK and platform configuration. The repository also documents kernelcache creation and installation targets.

## Platform, lifecycle and operational considerations

Kernel development is highly platform- and SDK-sensitive. The README includes architecture-specific examples; verify current hardware and platform support from the source and Apple platform documentation before attempting a live kernel build.

## Evaluation guidance

Check release-specific documentation, manifests, supported hardware/OS versions, licence and security guidance before adopting the project. This dossier summarizes the upstream README and is not a full source-code, security or performance audit.

## Upstream references

- [Repository](https://github.com/apple/darwin-xnu)
- [README](https://github.com/apple/darwin-xnu/blob/main/README.md)
- [Issues](https://github.com/apple/darwin-xnu/issues)
- [Releases](https://github.com/apple/darwin-xnu/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology claims are limited to the README; additional manifest and source-level verification remains a separate step.*
