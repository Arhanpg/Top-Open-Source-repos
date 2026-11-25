# NVIDIA/k8s-device-plugin

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/k8s-device-plugin/blob/main/README.md)
- README blob SHA: 2d1fb216f25aef76287430111ed01fa301152cc9
- README bytes captured: 46513
- README truncated at capture limit: False
- Repository ID: 106473613
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA device plugin for Kubernetes

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T18:56:33+00:00

### Short excerpt (up to 300 words)

> The NVIDIA device plugin As of v0.12.0, the For instructions on installing The list of prerequisites

### README headings

- NVIDIA device plugin for Kubernetes
- Table of Contents
- About
- Prerequisites
- Quick Start
- Preparing your GPU Nodes
- Example for debian-based systems with `docker` and `containerd`
- Install the NVIDIA Container Toolkit
- Notes on `CRI-O` configuration
- Enabling GPU Support in Kubernetes
- Running GPU Jobs
- Configuring the NVIDIA device plugin binary
- As command line flags or envvars
- As a configuration file
- Configuration Option Details
- Shared Access to GPUs
- With CUDA Time-Slicing
- With CUDA MPS
- IMEX Support
- Catalog of Labels
- Deployment via `helm`
- Configuring the device plugin's `helm` chart
- Passing configuration to the plugin via a `ConfigMap`
- Single Config File Example
- Multiple Config File Example
- Updating Per-Node Configuration With a Node Label
- Setting other helm chart values
- Deploying with gpu-feature-discovery for automatic node labels
- Deploying gpu-feature-discovery in standalone mode
- Deploying via `helm install` with a direct URL to the `helm` package

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About

> The NVIDIA device plugin

### Features and capabilities: Deploying with gpu-feature-discovery for automatic node labels

> As of v0.12.0, the

### Getting started and usage: Install the NVIDIA Container Toolkit

> For instructions on installing

### Technology and requirements: Prerequisites

> The list of prerequisites

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 602,604 |
| Shell | 32,085 |
| Makefile | 16,180 |
| Mustache | 9,004 |
| Dockerfile | 3,868 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cyphar.com/go-pathrs, github.com/Masterminds/semver/v3, github.com/NVIDIA/go-gpuallocator, github.com/NVIDIA/go-nvlib, github.com/NVIDIA/go-nvml, github.com/NVIDIA/nvidia-container-toolkit, github.com/cpuguy83/go-md2man/v2, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/google/gnostic-models, github.com/google/renameio, github.com/google/uuid, github.com/josharian/intern
- Makefile (capture: captured)
- tests/go.mod (capture: captured) — dependency clues: dario.cat/mergo, filippo.io/edwards25519, github.com/Azure/go-ansiterm, github.com/BurntSushi/toml, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/ProtonMail/go-crypto, github.com/asaskevich/govalidator, github.com/aws/aws-sdk-go, github.com/blang/semver/v4, github.com/boombuler/barcode, github.com/chai2010/gettext-go, github.com/cloudflare/circl, github.com/cpuguy83/go-md2man/v2, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/dylibso/observe-sdk/go
- deployments/container/Dockerfile (capture: captured)
- deployments/container/Makefile (capture: captured)
- deployments/devel/go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/fatih/structs, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-viper/mapstructure/v2, github.com/golang/groupcache, github.com/google/go-licenses/v2, github.com/google/licenseclassifier/v2, github.com/inconshreveable/mousetrap, github.com/knadh/koanf/maps, github.com/knadh/koanf/providers/file, github.com/knadh/koanf/providers/posflag, github.com/knadh/koanf/providers/structs, github.com/knadh/koanf/v2, github.com/losisin/helm-values-schema-json/v2, github.com/matryer/moq, github.com/mitchellh/copystructure, github.com/mitchellh/reflectwalk, github.com/otiai10/copy

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3928
- Forks at capture: 890
- Last updated: 2026-11-22T11:37:29Z
- Last pushed: 2026-11-23T07:44:42Z
- Topics: kubernetes

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/k8s-device-plugin)
- [README](https://github.com/NVIDIA/k8s-device-plugin/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/k8s-device-plugin/issues)
- [Releases](https://github.com/NVIDIA/k8s-device-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
