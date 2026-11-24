# Tencent/BlockFusion

- Company: Tencent
- GitHub account: [https://github.com/Tencent](https://github.com/Tencent)
- Mapping status: verified
- Repository: [Tencent/BlockFusion](https://github.com/Tencent/BlockFusion)
- Default branch: main
- README: [Open upstream README](https://github.com/Tencent/BlockFusion/blob/main/README.md)
- README blob SHA: 485a74d33ac36e3ddf88e5f25a57d44a248a9bf9
- Repository ID: 813473905
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:19+00:00

### Short excerpt (up to 100 words)

> This repo contains the official implementation for the paper "BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation". We modified diffusers to adapt triplane structure. Users should build based on the ```./src``` python setup.py install Pretrained weights of MLP, VAE, and Diffuser(Condition/Unconditioned). [Download the model here [10GB]](https://drive.google.com/file/d/19cuQihXzxq9fcM_drMWMhmwHBdT3B8fA/view?usp=sharing) and extract to ```./checkpoints```. To do uncondtional inference, run python unconditioned_prediction.py --batch 4 --save output/uncond To do single block conditional inference, run python conditioned_prediction.py --layout samplelayouts/exp1_32-56-24/0_0.npy --save output/cond We provide some sample layouts for demo. If you would like to draw your own layout maps, you can use ```drawtkinter.py``` to create your own

### README headings

- BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation
- ACM Transactions on Graphics (SIGGRAPH'24)
- [Project page](https://yang-l1.github.io/blockfusion/) | [Paper](https://arxiv.org/abs/2401.17053) | [Video](https://www.youtube.com/watch?v=PxIBtd6G0mA)
- Installation
- clone this repo
- Pretrained model
- Inference
- Citation

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 12,790,297 |
| Jupyter Notebook | 16,371 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 143
- Forks at capture: 11
- Last updated: 2026-11-05T08:18:51Z
- Last pushed: 2024-06-18T06:51:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Tencent/BlockFusion)
- [README](https://github.com/Tencent/BlockFusion/blob/main/README.md)
- [Issues](https://github.com/Tencent/BlockFusion/issues)
- [Releases](https://github.com/Tencent/BlockFusion/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
