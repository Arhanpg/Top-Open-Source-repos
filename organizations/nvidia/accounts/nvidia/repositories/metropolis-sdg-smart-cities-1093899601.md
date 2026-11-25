# NVIDIA/metropolis-sdg-smart-cities

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/metropolis-sdg-smart-cities](https://github.com/NVIDIA/metropolis-sdg-smart-cities)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/metropolis-sdg-smart-cities/blob/main/README.md)
- README blob SHA: 914851093b5ce17d3c301200ebd3a8ae48f3b104
- README bytes captured: 24395
- README truncated at capture limit: False
- Repository ID: 1093899601
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Metropolis Smart-City Synthetic Data Generation Recipe allows you to generate synthetic data and then augment them. The generated data then can be used to fine-tune VLM models such as Cosmos Reason (CR). 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:09:23+00:00

### Short excerpt (up to 300 words)

> This workflow provides a 1) Clone the repository **Workbench**: Jupyter Lab environment Linux with NVIDIA GPU Never commit secrets. Use

### README headings

- Synthetic Data Generation for Smart City Applications
- Contents
- Overview
- Architecture
- Prerequisites
- Obtain API keys
- Workflow Inputs
- Maps
- Scenario Logs
- Recorder Config
- System Requirements
- Quickstart (Docker Compose)
- Edit values for NGC_API_KEY, HF_TOKEN, GPU IDs, ports, etc.
- On the target machine
- This spins up the Cosmos-Reason1, Nemotron NIMs, Cosmos-Transfer2.5 Gradio Server, CARLA Server, and the Jupyter notebook, which users can follow to generate photo-realistic synthetic data for VLMs.
- By default these are the ports where all of the services get deployed to.
- Workbench → http://<host>:8888
- NIMs: VLM http://<host>:8001, LLM http://<host>:8002, Cosmos-Transfer http://<host>:8080
- Note the printed NIM_HOST and use it on the workbench node.
- On the second machine, ensure steps 1-3 are complete to have the repository and configuration ready before this step.
- The deployment script sources `deploy/compose/env`, where `NIM_HOST` defaults to `localhost`. This will override any previously exported `NIM_HOST`. Before running `./deploy.sh workbench`, edit `deploy/compose/env` and set `NIM_HOST=<ip_of_nim_node>`. The script will prompt you to confirm the detected value.
- If using heterogeneous deployment, set NIM_HOST to the NIM node IP first:
- export NIM_HOST=<ip_of_nim_node>
- Advanced Configuration
- Workflow Usage (Stage-by-Stage)
- Troubleshooting / FAQ
- Setup related issues
- Notebook issues
- Should have the following line
- ...

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> This workflow provides a

### Getting started and usage: Quickstart (Docker Compose)

> 1) Clone the repository

### Architecture and design: Architecture

> **Workbench**: Jupyter Lab environment

### Technology and requirements: System Requirements

> Linux with NVIDIA GPU

### Limitations and security: Security and Compliance

> Never commit secrets. Use

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 254,664 |
| PowerShell | 44,608 |
| Shell | 26,909 |
| Jupyter Notebook | 24,519 |
| Batchfile | 12,476 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: aiohttp, colorama, gradio-client, jupyterlab, matplotlib, notebook, numpy, openai, opencv-python, pyyaml, requests, toml
- modules/pyproject.toml (capture: captured) — dependency clues: aiohttp, colorama, gradio-client, openai, opencv-python, pyyaml, requests, toml
- modules/augmentation/pyproject.toml (capture: captured) — dependency clues: aiohttp, colorama, gradio-client, openai, pyyaml, requests, toml
- modules/carla-ground-truth-generation/pyproject.toml (capture: captured) — dependency clues: carla, matplotlib, numpy, opencv-python, pyyaml
- modules/carla-ground-truth-generation/requirements.txt (capture: captured) — dependency clues: carla, matplotlib, numpy, opencv-python, pyyaml

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 17
- Forks at capture: 6
- Last updated: 2026-10-09T09:45:36Z
- Last pushed: 2025-12-01T20:15:24Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/metropolis-sdg-smart-cities)
- [README](https://github.com/NVIDIA/metropolis-sdg-smart-cities/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/metropolis-sdg-smart-cities/issues)
- [Releases](https://github.com/NVIDIA/metropolis-sdg-smart-cities/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
