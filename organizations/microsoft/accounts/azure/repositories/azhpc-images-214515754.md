# Azure/azhpc-images

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azhpc-images](https://github.com/Azure/azhpc-images)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/azhpc-images/blob/master/README.md)
- README blob SHA: 068cd3f83e834eacbe175743f0128c11788c0f1f
- README bytes captured: 12119
- README truncated at capture limit: False
- Repository ID: 214515754
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure HPC/AI VM Images

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:45:58+00:00

### Short excerpt (up to 300 words)

> sudo apt-mark hold linux-azure sed -i "$ s/$/

### README headings

- Azure HPC/AI VM Images
- How to Use
- Sign in Azure CLI
- Initialize Packer with Azure plugin
- Kernel Update/Patching
- Collecting Diagnostics
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Hold the Azure kernel meta-package (adjust the name to your installed kernel, e.g. linux-azure, linux-azure-6.8, linux-azure-lts-22.04, linux-azure-nvidia)

> sudo apt-mark hold linux-azure

### Technology and requirements: Disable dependencies on kernel core

> sed -i "$ s/$/

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 456,940 |
| HCL | 67,989 |
| Python | 43,502 |
| Cuda | 6,709 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- components/torset-tool/requirements.txt (capture: captured) — dependency clues: loguru, parallel-ssh

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 132
- Forks at capture: 114
- Last updated: 2026-11-11T03:28:52Z
- Last pushed: 2026-11-22T01:03:27Z
- Topics: ai-image, alma-hpc, azhpc, centos-hpc, hpc-image, ubuntu-hpc

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azhpc-images)
- [README](https://github.com/Azure/azhpc-images/blob/master/README.md)
- [Issues](https://github.com/Azure/azhpc-images/issues)
- [Releases](https://github.com/Azure/azhpc-images/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
