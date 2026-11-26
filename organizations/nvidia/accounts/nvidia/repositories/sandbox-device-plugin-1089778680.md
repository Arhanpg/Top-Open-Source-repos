# NVIDIA/sandbox-device-plugin

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/sandbox-device-plugin](https://github.com/NVIDIA/sandbox-device-plugin)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/sandbox-device-plugin/blob/main/README.md)
- README blob SHA: 366c5f40d0ddfc21c2759003ae89a43525aff4b3
- README bytes captured: 4755
- README truncated at capture limit: False
- Repository ID: 1089778680
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Kubernetes Device Plugin to help cold plug vfio/iommufd GPUs in Kata VMs for Confidential Containers

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T21:30:39+00:00

### Short excerpt (up to 300 words)

> This is a kubernetes Discovers Nvidia GPUs which Before starting the device Need to have Nvidia

### README headings

- NVIDIA K8s Device Plugin to assign Passthrough GPUs to Kata VMs for Confidential Containers
- Table of Contents
- About
- Features
- Prerequisites
- Quick Start
- Preparing a GPU to be used in pass through mode
- 1. Enable IOMMU and blacklist nouveau driver on KVM Host
- line 6: add (if AMD CPU, add [amd_iommu=on])
- Legacy Mode (BIOS)
- UEFI Mode
- 2. Enable vfio-pci kernel module
- Docs
- Deployment
- Build
- To Do
- Contributions

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About

> This is a kubernetes

### Features and capabilities: Features

> Discovers Nvidia GPUs which

### Getting started and usage: Quick Start

> Before starting the device

### Technology and requirements: Prerequisites

> Need to have Nvidia

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 67,328 |
| Shell | 17,371 |
| Makefile | 10,304 |
| Dockerfile | 4,925 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: 4d63.com/gocheckcompilerdirectives, 4d63.com/gochecknoglobals, github.com/4meepo/tagalign, github.com/Abirdcfly/dupword, github.com/Antonboom/errname, github.com/Antonboom/nilnil, github.com/Antonboom/testifylint, github.com/BurntSushi/toml, github.com/Crocmagnon/fatcontext, github.com/Djarvur/go-err113, github.com/GaijinEntertainment/go-exhaustruct/v3, github.com/Masterminds/semver/v3, github.com/NVIDIA/go-nvlib, github.com/OpenPeeDeeP/depguard/v2, github.com/alecthomas/go-check-sumtype, github.com/alexkohler/nakedret/v2, github.com/alexkohler/prealloc, github.com/alingse/asasalint, github.com/alingse/nilnesserr, github.com/ashanbrown/forbidigo
- Makefile (capture: captured)
- hack/Dockerfile (capture: captured)
- deployments/container/Makefile (capture: captured)
- deployments/devel/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 10
- Forks at capture: 27
- Last updated: 2026-11-04T14:50:13Z
- Last pushed: 2026-11-17T04:34:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/sandbox-device-plugin)
- [README](https://github.com/NVIDIA/sandbox-device-plugin/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/sandbox-device-plugin/issues)
- [Releases](https://github.com/NVIDIA/sandbox-device-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
