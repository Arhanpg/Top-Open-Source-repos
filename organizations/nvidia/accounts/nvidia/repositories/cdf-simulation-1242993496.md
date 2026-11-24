# NVIDIA/cdf-simulation

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/cdf-simulation](https://github.com/NVIDIA/cdf-simulation)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/cdf-simulation/blob/main/README.md)
- README blob SHA: d66ab405ca6131b1fdb55c48972ffa959812398e
- README bytes captured: 13785
- README truncated at capture limit: False
- Repository ID: 1242993496
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Synthetic data generation engine using NVIDIA Isaac Sim and Omniverse Replicator to render photorealistic, fully labeled PCB inspection imagery, including golden and defect boards

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T04:23:52+00:00

### Short excerpt (up to 300 words)

> Loads local, S3, or A job is one The Dockerfile is based

### README headings

- Cosmos Data Factory — Simulation
- What it does
- Entry points
- Documentation
- Requirements and access
- Get the repository
- Get the container image
- Developer setup: simulated solder solver (optional)
- expect 'surface_evolver' in the tuple
- Container networking
- Quick start: render a prepared board
- The image runs as isaac-sim (UID/GID 1234:1234).
- Other ways to run
- Compile YAML without starting Isaac Sim
- YAML with a local Isaac Sim
- Python
- Your own board
- Agent skills
- Project structure
- Troubleshooting
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: What it does

> Loads local, S3, or

### Getting started and usage: Quick start: render a prepared board

> A job is one

### Technology and requirements: Requirements and access

> The Dockerfile is based

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 4,430,177 |
| Dockerfile | 11,325 |
| Standard ML | 10,382 |
| Kit | 2,987 |
| Shell | 2,400 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: PyYAML, pydantic
- requirements.txt (capture: captured) — dependency clues: Pillow, PyYAML, boto3, coacd, manifold3d, numpy, pydantic, scikit-image, scipy, trimesh, usd-core, warp-lang
- docs/tutorials/sim2real-qwen-image-edit/requirements.txt (capture: captured) — dependency clues: accelerate, diffusers, huggingface-hub, ipykernel, jupyterlab, numpy, peft, pillow, safetensors, sentencepiece, torch, torchvision, transformers
- pcb_aoi/solder_evolver/third_party/evolver/upstream/src/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 5
- Last updated: 2026-11-09T01:29:12Z
- Last pushed: 2026-10-27T03:44:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/cdf-simulation)
- [README](https://github.com/NVIDIA/cdf-simulation/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/cdf-simulation/issues)
- [Releases](https://github.com/NVIDIA/cdf-simulation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
