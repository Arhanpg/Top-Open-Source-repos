# NVIDIA/build-system-archive-import-examples

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/build-system-archive-import-examples](https://github.com/NVIDIA/build-system-archive-import-examples)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/build-system-archive-import-examples/blob/main/README.md)
- README blob SHA: 854ecd66f2174eb506e7f4b185f801d82d1be6e2
- Repository ID: 406451289
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Examples for importing precompiled binary tarball and zip archives into various build and packaging systems

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:49+00:00

### Short excerpt (up to 100 words)

> Examples for importing precompiled binary `tarball` and `zip` archives into various CI/CD build and packaging systems Sample scripts for parsing `redistrib_${label}.json` manifests (JSON schema). - Downloads each archive - Validates SHA256 checksums - Extracts archives - Flattens into a collapsed directory structure usage: parse_redist.py (-u URL | [-l LABEL] [-p PRODUCT] | --channel CHANNEL) [-o OUTPUT] [--list] option filters: [--component COMPONENT] ([--os OS] [--arch ARCH]) option toggles: [--no-download] [--no-checksum] [--no-extract] [--no-flatten] python3 ./parse_redist.py --product cuda --label 11.4.2 or equivalent python3 ./parse_redist.py --url https://developer.download.nvidia.com/compute/cuda/redist/redistrib_11.4.2.json Use `--channel` to resolve a release from the NVIDIA Repo Channels CDN (packages.nvidia.com) instead of `developer.download.nvidia.com`. `--list`

### README headings

- build-system-archive-import-examples
- Overview
- Redistrib JSON
- Python Usage
- Example (python)
- Repo Channels CDN (packages.nvidia.com)
- BASH Usage
- Example (bash)
- CMake
- FindCUDAToolkit
- ExternalProject
- Bazel
- pkg_tar
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 19,772 |
| Shell | 15,888 |
| Makefile | 1,356 |
| Starlark | 964 |
| CMake | 282 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- debian/Makefile (capture: captured)
- rpm/Makefile (capture: captured)
- cmake/1_FindCUDAToolkit/CMakeLists.txt (capture: captured)
- cmake/2_ExternalProject/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 23
- Forks at capture: 11
- Last updated: 2026-07-27T17:30:01Z
- Last pushed: 2026-07-27T17:31:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/build-system-archive-import-examples)
- [README](https://github.com/NVIDIA/build-system-archive-import-examples/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/build-system-archive-import-examples/issues)
- [Releases](https://github.com/NVIDIA/build-system-archive-import-examples/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
