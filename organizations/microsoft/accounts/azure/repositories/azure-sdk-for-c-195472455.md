# Azure/azure-sdk-for-c

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-sdk-for-c](https://github.com/Azure/azure-sdk-for-c)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/azure-sdk-for-c/blob/main/README.md)
- README blob SHA: 962c328e80e4ddd2b2ca5dd392ccb49a91456d72
- README bytes captured: 29068
- README truncated at capture limit: False
- Repository ID: 195472455
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository is for active development of the Azure SDK for Embedded C. For consumers of the SDK we recommend visiting our versioned developer docs at https://azure.github.io/azure-sdk-for-c. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:34:19+00:00

### Short excerpt (up to 300 words)

> The SDK can be At the heart of Azure SDK uses Vcpkg This repository is now

### README headings

- ⚠️ Deprecation Notice
- Azure SDK for Embedded C
- Table of Contents
- Documentation
- The GitHub Repository
- Services
- Structure
- Main Branch
- Release Branches and Release Tagging
- Getting Started Using the SDK
- CMake
- CMake Options
- Consume SDK for C as Dependency with CMake
- Visual Studio Code
- Source Files (IDE, command line, etc)
- Running Samples
- Storage Sample
- On linux, set env var like this. For Windows, do it from advanced settings/ env variables
- Libcurl Global Init and Global Clean Up
- IoT samples
- Development Environment
- Third Party Dependencies
- Customize the Vcpkg dependency integration
- Build
- cd to project folder
- create a new folder to generate cmake files for building (i.e. build)
- generate files
- cmake will automatically detect what C compiler is used by system by default and will generate files for it
- compile files. Cmake would call compiler and linker to generate libs
- Visual Studio 2019

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Getting Started Using the SDK

> The SDK can be

### Architecture and design: SDK Architecture

> At the heart of

### Technology and requirements: Third Party Dependencies

> Azure SDK uses Vcpkg

### Limitations and security: ⚠️ Deprecation Notice

> This repository is now

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 1,659,214 |
| PowerShell | 830,752 |
| TypeScript | 74,607 |
| CMake | 57,969 |
| CSS | 37,618 |
| C++ | 36,741 |
| HTML | 12,589 |
| JavaScript | 8,127 |
| Shell | 7,224 |
| Python | 2,009 |
| Batchfile | 1,224 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- eng/common/spelling/package.json (capture: captured) — dependency clues: cspell
- eng/common/tsp-client/package.json (capture: captured) — dependency clues: @azure-tools/typespec-client-generator-cli
- eng/vcpkg-overlay-ports/libuuid/CMakeLists.txt (capture: captured)
- sdk/samples/iot/CMakeLists.txt (capture: captured)
- sdk/tests/core/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 242
- Forks at capture: 135
- Last updated: 2026-11-16T04:24:07Z
- Last pushed: 2026-07-15T18:38:48Z
- Topics: azure, azure-sdk, azure-services, embedded, hacktoberfest, iot

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-sdk-for-c)
- [README](https://github.com/Azure/azure-sdk-for-c/blob/main/README.md)
- [Issues](https://github.com/Azure/azure-sdk-for-c/issues)
- [Releases](https://github.com/Azure/azure-sdk-for-c/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
