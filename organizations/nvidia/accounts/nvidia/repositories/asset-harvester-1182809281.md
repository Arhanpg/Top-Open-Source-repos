# NVIDIA/asset-harvester

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/asset-harvester](https://github.com/NVIDIA/asset-harvester)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/asset-harvester/blob/main/README.md)
- README blob SHA: 333dc1773cef5df9347652a82daa00ace3192a3d
- Repository ID: 1182809281
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA Asset Harvester is a generative AI model for autonomous vehicle simulation that extracts reusable 3D Gaussian assets directly from captured driving scenes, even from partial or obstructed views.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:07+00:00

### Short excerpt (up to 100 words)

> NVIDIA Asset Harvester is a generative AI model that extracts 3D Gaussian object representations directly from captured driving scenes, even from partial or obstructed views, removing manual asset creation. Each extracted asset feeds into Harmonizer for scene integration, enabling scalable data generation for autonomous vehicle simulation. Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge,

### README headings

- Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation
- Abstract
- Pipeline Overview
- User Guide
- Prerequisites
- Download Model Checkpoints
- Setup
- Usage
- License
- Support
- Citation
- Disclaimer

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 845,577 |
| Shell | 20,878 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: Pillow, PyYAML, accelerate, boto3, click, decord, diffusers, einops, huggingface_hub, imageio, imageio-ffmpeg, kiui, lpips, matplotlib, numpy, nvidia-ncore, omegaconf, open-clip-torch, opencv-python, packaging

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 277
- Forks at capture: 26
- Last updated: 2026-11-22T13:26:34Z
- Last pushed: 2026-11-13T16:37:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/asset-harvester)
- [README](https://github.com/NVIDIA/asset-harvester/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/asset-harvester/issues)
- [Releases](https://github.com/NVIDIA/asset-harvester/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
