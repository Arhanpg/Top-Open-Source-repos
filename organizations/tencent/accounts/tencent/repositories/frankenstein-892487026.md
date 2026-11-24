# Tencent/Frankenstein

- Company: Tencent
- GitHub account: [https://github.com/Tencent](https://github.com/Tencent)
- Mapping status: verified
- Repository: [Tencent/Frankenstein](https://github.com/Tencent/Frankenstein)
- Default branch: main
- README: [Open upstream README](https://github.com/Tencent/Frankenstein/blob/main/README.md)
- README blob SHA: e3e13627d9cdda61bbff5c48482fc0c3cf28cdd2
- README bytes captured: 4252
- README truncated at capture limit: False
- Repository ID: 892487026
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

[SIGGRAPH ASIA 2024] Frankenstein: Generating Semantic-Compositional 3D Scenes in One Tri-Plane

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:40:27+00:00

### Short excerpt (up to 300 words)

> conda create -n frankenstein

### README headings

- Frankenstein: Generating Semantic-Compositional 3D Scenes in One Tri-Plane
- SIGGRAPH Asia 2024 (Conference Track)
- [Project page](https://wolfball.github.io/frankenstein/) | [arXiv](https://arxiv.org/abs/2403.16210) | [Video](https://youtu.be/lRn-HqyCrLI)
- News
- Installation
- Pretrained Model
- Inference
- generate layout
- move 1-th (-o 1) cabinet (-i 2) along z-axis (-d 2)
- generate latent tri-plane conditioned by layout
- decode to 3D mesh
- generate layout
- move 0-th (-o 0) cabinet (-i 1) along x-axis (-d 0)
- generate latent tri-plane conditioned by layout
- decode to 3D mesh ('-w' activate the wall remeshing algorithm)
- generate latent tri-plane from random noise (unconditional)
- decode to 3D mesh
- Citation
- Acknowledgments

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> conda create -n frankenstein

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 912,937 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: accelerate, einops, huggingface_hub, matplotlib, numpy, omegaconf, open3d, pytorch_lightning, rdp, safetensors, scikit-image, tqdm, transformers, triangulator, xformers

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 20
- Forks at capture: 4
- Last updated: 2026-10-02T07:04:55Z
- Last pushed: 2024-11-25T03:55:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Tencent/Frankenstein)
- [README](https://github.com/Tencent/Frankenstein/blob/main/README.md)
- [Issues](https://github.com/Tencent/Frankenstein/issues)
- [Releases](https://github.com/Tencent/Frankenstein/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
