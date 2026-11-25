# Azure/AKSInvestigator

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/AKSInvestigator](https://github.com/Azure/AKSInvestigator)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/AKSInvestigator/blob/main/README.md)
- README blob SHA: bf56e7946dbeb5818f57e2c78b8a6d8215ce4125
- README bytes captured: 18516
- README truncated at capture limit: False
- Repository ID: 1322338696
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T23:56:29+00:00

### Short excerpt (up to 300 words)

> For Azure Local disconnected

### README headings

- AKSInvestigator
- What's added vs upstream
- Layout
- Sync from upstream
- Install
- CPU (default) — installs anywhere with AVX-512 (Standard_D*s_v5)
- GPU — requires an NVIDIA-equipped node pool
- Bring your own model only (disable Saturn explicitly)
- Model source options
- Optional: download the ModelPack OCI artifact with ORAS
- Optional: use the model image directly from a private source ACR
- Install the kubectl plugin
- Per-release plugin publication
- Saturn model configuration
- Use Saturn and Azure OpenAI together
- Model delivery
- Publish the Saturn model

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install

> For Azure Local disconnected

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 63,700 |
| Go Template | 51,641 |
| Go | 18,375 |
| Shell | 5,251 |
| Dockerfile | 767 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- helm/Chart.yaml (capture: captured)
- kubectl-plugin/go.mod (capture: captured) — dependency clues: golang.org/x/sys, golang.org/x/term
- docker/saturn-model/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-12T00:44:44Z
- Last pushed: 2026-11-11T23:44:41Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/AKSInvestigator)
- [README](https://github.com/Azure/AKSInvestigator/blob/main/README.md)
- [Issues](https://github.com/Azure/AKSInvestigator/issues)
- [Releases](https://github.com/Azure/AKSInvestigator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
