# NVIDIA/apt-packaging-cuda-keyring

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/apt-packaging-cuda-keyring](https://github.com/NVIDIA/apt-packaging-cuda-keyring)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/apt-packaging-cuda-keyring/blob/main/README.md)
- README blob SHA: 6783e4869c0a536db4129baa25554ea420984316
- Repository ID: 509501959
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CUDA keyring packaging for Debian

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:24:57+00:00

### Short excerpt (up to 100 words)

> Packaging for cuda-keyring 1. Install GPG public key in `/usr/share/keyrings/` 2. Set repository priority with apt pinning 3. Enable Nvidia's CUDA repository with `.list` for `apt-get` deb [signed-by=/path/to/keyring] https://$repositoryURL $suite deb [signed-by=/usr/share/keyrings/cuda-archive-keyring.gpg] https://developer.download.nvidia.com/compute/cuda/repos/debian11/x86_64/ / - cuda-keyring The `apt-key` command is deprecated in Debian 12, Ubuntu 21.10 and derivative distros. NVIDIA provides the repo GPG keys in both `*.pub` and encapsulated keyring formats. wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-archive-keyring.gpg **OR** wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/$shortname.pub cat $shortname.pub | gpg --dearmor > cuda-archive.keyring.gpg Repositories maintained by different organizations may contain packages with the same name. To ensure `apt` selects software from one repository over another, priority pinning may be

### README headings

- cuda-keyring
- Overview
- Note on enabling a repository
- Blog post
- Deliverables
- Prerequisites
- Download GPG public key
- Download priority pin
- Install build dependencies
- Usage
- Example
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 886 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 15
- Forks at capture: 5
- Last updated: 2026-11-16T05:23:28Z
- Last pushed: 2023-04-14T20:08:33Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/apt-packaging-cuda-keyring)
- [README](https://github.com/NVIDIA/apt-packaging-cuda-keyring/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/apt-packaging-cuda-keyring/issues)
- [Releases](https://github.com/NVIDIA/apt-packaging-cuda-keyring/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
