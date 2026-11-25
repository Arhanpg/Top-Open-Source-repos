# NVIDIA/kubevirt-gpu-device-plugin

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/kubevirt-gpu-device-plugin](https://github.com/NVIDIA/kubevirt-gpu-device-plugin)
- Default branch: master
- README: [Open upstream README](https://github.com/NVIDIA/kubevirt-gpu-device-plugin/blob/master/README.md)
- README blob SHA: 68c68d58e86aa0626592757ae7ee78654598ae95
- README bytes captured: 8278
- README truncated at capture limit: False
- Repository ID: 202012660
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA k8s device plugin for Kubevirt

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:34:57+00:00

### Short excerpt (up to 300 words)

> This is a kubernetes Discovers Nvidia GPUs which Before starting the device Need to have Nvidia

### README headings

- NVIDIA K8s Device Plugin to assign GPUs and vGPUs to KubeVirt VMs
- Table of Contents
- About
- Features
- Prerequisites
- Quick Start
- Whitelist GPU and vGPU in KubeVirt CR
- Preparing a GPU to be used in pass through mode
- 1. Enable IOMMU and blacklist nouveau driver on KVM Host
- line 6: add (if AMD CPU, add [amd_iommu=on])
- Legacy Mode (BIOS)
- UEFI Mode
- 2. Enable vfio-pci kernel module
- Preparing a GPU to be used in vGPU mode
- 1. Change to the mdev_supported_types directory for the physical GPU.
- 2. Find out which subdirectory of mdev_supported_types contains registration information for the vGPU type that you want to create.
- 3. Confirm that you can create an instance of the vGPU type on the physical GPU.
- 4. Generate a correctly formatted universally unique identifier (UUID) for the vGPU.
- 5. Write the UUID that you obtained in the previous step to create the file in the registration information directory for the vGPU type that you want to create.
- 6. Confirm that the vGPU was created.
- Docs
- Deployment
- Build
- To Do

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
| Go | 95,979 |
| Shell | 33,752 |
| Makefile | 8,394 |
| Go Template | 1,108 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver/v3, github.com/NVIDIA/gpu-monitoring-tools, github.com/fsnotify/fsnotify, github.com/go-logr/logr, github.com/go-task/slim-sprig/v3, github.com/google/go-cmp, github.com/google/pprof, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/rogpeppe/go-internal, go.yaml.in/yaml/v3, golang.org/x/mod, golang.org/x/net, golang.org/x/sync, golang.org/x/sys, golang.org/x/text, golang.org/x/tools, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf
- Makefile (capture: captured)
- tools/go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/go-logr/logr, github.com/golang/groupcache, github.com/google/go-licenses/v2, github.com/google/licenseclassifier/v2, github.com/inconshreveable/mousetrap, github.com/otiai10/copy, github.com/sergi/go-diff, github.com/spf13/cobra, github.com/spf13/pflag, go.opencensus.io, golang.org/x/mod, golang.org/x/net, golang.org/x/sync, golang.org/x/sys, golang.org/x/text, golang.org/x/tools, k8s.io/klog/v2
- deployments/container/Makefile (capture: captured)
- vendor/google.golang.org/grpc/Makefile (capture: captured)
- vendor/github.com/Masterminds/semver/v3/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 296
- Forks at capture: 94
- Last updated: 2026-11-12T08:41:39Z
- Last pushed: 2026-11-20T12:43:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/kubevirt-gpu-device-plugin)
- [README](https://github.com/NVIDIA/kubevirt-gpu-device-plugin/blob/master/README.md)
- [Issues](https://github.com/NVIDIA/kubevirt-gpu-device-plugin/issues)
- [Releases](https://github.com/NVIDIA/kubevirt-gpu-device-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
