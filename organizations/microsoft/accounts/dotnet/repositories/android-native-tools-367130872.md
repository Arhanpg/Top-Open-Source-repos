# dotnet/android-native-tools

- Company: Microsoft
- GitHub account: [https://github.com/dotnet](https://github.com/dotnet)
- Mapping status: official-project-linked
- Repository: [dotnet/android-native-tools](https://github.com/dotnet/android-native-tools)
- Default branch: main
- README: [Open upstream README](https://github.com/dotnet/android-native-tools/blob/main/README.md)
- README blob SHA: 1b4442c2bb84746612174758fd506ec2876f0e76
- Repository ID: 367130872
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

LLVM toolchain for .NET for Android

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:22:16+00:00

### Short excerpt (up to 100 words)

> This repository hosts builds of select Xamarin.Android uses a handful of utilities from LLVM (`llvm-mc` assembler, `llvm-strip/objcopy` and the `lld` linker), a custom wrapper for `llvm-mc` which implements the GNU AS interface required by Mono AOT and Xamarin.Android alike. These utilities are used in Xamarin.Android application build process, parts of which entail generation of native assembly for `ARM`, `ARM64`, `x86` and `x86_64` devices. They are also required when using the AOT and Profiled AOT capabilities of Mono and dotnet runtimes. The build requires sources from various locations and at different versions. This section explains how to update and where to

### README headings

- Binary utilities for Xamarin.Android
- Component versions
- LLVM
- Xamarin.Android Utilities
- How to build and publish new version of utilities

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 50,002 |
| Shell | 15,098 |
| CMake | 6,090 |
| Batchfile | 4,999 |
| C | 3,195 |
| PowerShell | 327 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/CMakeLists.txt (capture: captured)
- src/gas/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 12
- Forks at capture: 11
- Last updated: 2026-10-12T17:27:07Z
- Last pushed: 2026-07-03T13:44:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/dotnet/android-native-tools)
- [README](https://github.com/dotnet/android-native-tools/blob/main/README.md)
- [Issues](https://github.com/dotnet/android-native-tools/issues)
- [Releases](https://github.com/dotnet/android-native-tools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
