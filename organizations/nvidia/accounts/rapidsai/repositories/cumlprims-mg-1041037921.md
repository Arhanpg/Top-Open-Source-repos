# rapidsai/cumlprims_mg

- Company: NVIDIA
- GitHub account: [https://github.com/rapidsai](https://github.com/rapidsai)
- Mapping status: official-project-linked
- Repository: [rapidsai/cumlprims_mg](https://github.com/rapidsai/cumlprims_mg)
- Default branch: main
- README: [Open upstream README](https://github.com/rapidsai/cumlprims_mg/blob/main/README.md)
- README blob SHA: 4cb69e8dc080944dc7cae0ac10fe6c0ec0a3ba41
- Repository ID: 1041037921
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Multi-node, multi-GPU (MNMG) ML mathematical primitives and some algorithms used by cuML

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:46:19+00:00

### Short excerpt (up to 100 words)

> This repository contains C++ and CUDA code of multi-node multi-GPU (MNMG) ML mathematical primitives and some algorithms, that are used by the main cuML project. The build system uses CMake for build configuration, and an out-of-source build is recommended. The MNMG code included in cuMLPrims follows the model one-process-per-GPU (OPG), where the code uses a communication library (based on cuML's comms) and each process has one GPU assigned to it. This is in contrast to single-process-multi-GPU (SPMG) approaches, which are no longer part of the code base. The folder structure mirrors closely the structure of GitHub cuML. The folders are:

### README headings

- cuMLPrims
- Folder Structure
- Building cuMLPrims:
- Requirements
- Using build.sh script
- General Build Procedure:
- Code Style
- Custom Build Options

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Cuda | 116,427 |
| C++ | 46,833 |
| CMake | 18,514 |
| Shell | 13,779 |
| Dockerfile | 1,368 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- .devcontainer/Dockerfile (capture: captured)
- cpp/CMakeLists.txt (capture: captured)
- cpp/test/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 12
- Last updated: 2026-01-05T15:40:32Z
- Last pushed: 2026-01-02T19:06:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/rapidsai/cumlprims_mg)
- [README](https://github.com/rapidsai/cumlprims_mg/blob/main/README.md)
- [Issues](https://github.com/rapidsai/cumlprims_mg/issues)
- [Releases](https://github.com/rapidsai/cumlprims_mg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
