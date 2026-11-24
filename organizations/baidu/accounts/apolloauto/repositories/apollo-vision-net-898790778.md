# ApolloAuto/Apollo-Vision-Net

- Company: Baidu
- GitHub account: [https://github.com/ApolloAuto](https://github.com/ApolloAuto)
- Mapping status: official-project-linked
- Repository: [ApolloAuto/Apollo-Vision-Net](https://github.com/ApolloAuto/Apollo-Vision-Net)
- Default branch: main
- README: [Open upstream README](https://github.com/ApolloAuto/Apollo-Vision-Net/blob/main/README.md)
- README blob SHA: 8617913b7f168856ed347609fffcf0a9d54d1f83
- Repository ID: 898790778
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Apollo BEV+OCC network training

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:45+00:00

### Short excerpt (up to 100 words)

> This repository introduces the Apollo Vision Network, a new 3D detection and occupancy prediction network for autonomous driving. - We feed multi-camera images to the backbone network, and obtain the features of diffetrent camera views. - Use Transformer encoder to generate the bev features. - The encoder layer contains grid-shaped BEV queries, temporal self-attention, and spatial cross-attention. - In spatial cross- attention, each BEV query only interacts with image features in the regions of interest. - In temporal self-attention, each BEV query interacts with two features: the BEV queries at the current timestamp and the BEV features at the previous

### README headings

- Apollo Vision Net
- Overview
- Highlights
- Getting Started
- Results and Pre-trained Models
- Related resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,415,006 |
| Cuda | 57,993 |
| C++ | 8,224 |
| Shell | 1,466 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 28
- Forks at capture: 13
- Last updated: 2026-11-23T03:51:43Z
- Last pushed: 2024-12-05T04:56:51Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ApolloAuto/Apollo-Vision-Net)
- [README](https://github.com/ApolloAuto/Apollo-Vision-Net/blob/main/README.md)
- [Issues](https://github.com/ApolloAuto/Apollo-Vision-Net/issues)
- [Releases](https://github.com/ApolloAuto/Apollo-Vision-Net/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
