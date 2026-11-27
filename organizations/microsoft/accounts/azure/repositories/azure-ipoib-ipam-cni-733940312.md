# Azure/azure-ipoib-ipam-cni

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-ipoib-ipam-cni](https://github.com/Azure/azure-ipoib-ipam-cni)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/azure-ipoib-ipam-cni/blob/main/README.md)
- README blob SHA: 7cfe5ac77afa642690a39467cc7dbbe962d0818c
- README bytes captured: 7786
- README truncated at capture limit: False
- Repository ID: 733940312
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

cni ipam plugin for azure vm which supports infiniband/RDMA

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:26:30+00:00

### Short excerpt (up to 300 words)

> azure-ipoib-ipam-cni is intended to helm upgrade -i --wait Install ofed drivers It only works on

### README headings

- azure-ipoib-ipam-cni
- Overview
- Requirements
- Usage
- Apply required manifests
- Install node feature discovery
- Install the network-operator
- Usage with DRANet (Profile Provider webhook)
- Running the webhook
- Enabling the webhook in DRANet

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> azure-ipoib-ipam-cni is intended to

### Features and capabilities: Install node feature discovery

> helm upgrade -i --wait

### Getting started and usage: Usage

> Install ofed drivers

### Technology and requirements: Requirements

> It only works on

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 27,915 |
| Makefile | 3,280 |
| Go Template | 1,342 |
| Dockerfile | 180 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Azure/hyperkv, github.com/containernetworking/cni, github.com/containernetworking/plugins, github.com/vishvananda/netlink, github.com/vishvananda/netns, golang.org/x/sys
- Makefile (capture: captured)
- charts/azure-ipoib-webhook/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 2
- Forks at capture: 11
- Last updated: 2026-10-27T18:05:16Z
- Last pushed: 2026-09-15T02:13:21Z
- Topics: aks, azure, hpc, infiniband, ipoib, rdma

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-ipoib-ipam-cni)
- [README](https://github.com/Azure/azure-ipoib-ipam-cni/blob/main/README.md)
- [Issues](https://github.com/Azure/azure-ipoib-ipam-cni/issues)
- [Releases](https://github.com/Azure/azure-ipoib-ipam-cni/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
