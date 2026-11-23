# awslabs/amazon-accessible-rl-sdk

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-accessible-rl-sdk](https://github.com/awslabs/amazon-accessible-rl-sdk)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-accessible-rl-sdk/blob/main/README.md)
- README blob SHA: 4b860692141d2567a98f7af800703b2f8479105e
- Repository ID: 526043695
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A2RL is a Python library for offline reinforcement learning

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:48+00:00

### Short excerpt (up to 100 words)

> Amazon Accessible RL (A2RL) is an open-source Python package for [sequential decision making problem](https://en.wikipedia.org/wiki/Sequential_decision_making) using offline time-series data. It focuses on offline RL using state-of-the-art generative transformer technology – the same technology behind GATO, [trajectory transformer](https://trajectory-transformer.github.io/) and [decision transformer](https://arxiv.org/abs/2106.01345). A2RL guides you through problem formulation via [data frames API](https://awslabs.github.io/amazon-accessible-rl-sdk/example.html#historical-data), conduct analysis](https://awslabs.github.io/amazon-accessible-rl-sdk/auto-notebooks/data_properties.html) to see if a solution is possible, use the data to train a *digital twin*) based on the data, and providing [recommended actions](https://awslabs.github.io/amazon-accessible-rl-sdk/auto-notebooks/planner_byo_example.html). pip install a2rl You should start by formulating your problem into *states*, *actions*, and *rewards* (see the dataset that reflects the formulation, using A2RL's Pandas-like API.

### README headings

- Amazon Accessible RL SDK <!-- omit from toc -->
- Installation
- Usage
- Load a sample dataset which contains historical states, actions, and rewards.
- Checks and analysis
- Train a simulator
- Get recommended actions given an input context (s,a,r,v,...s).
- Context must end with states, and its members must be tokenized.
- Show recommendations (i.e., trajectory)
- Help and Support

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 303,918 |
| Jupyter Notebook | 140,357 |
| Shell | 885 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- requirements.txt (capture: captured) — dependency clues: PyYaml, cloudpickle, gym, loguru, matplotlib, nptyping, numpy, pandas, pytorch-lightning, scikit-learn, scipy, seaborn, tensorboardX, torch, tqdm, typeguard, typing_extensions
- setup.py (capture: captured)
- docs/Makefile (capture: captured)
- examples/sagemaker-training/dynamic_pricing/requirements.txt (capture: captured) — dependency clues: PyYaml, gym, loguru, matplotlib, nptyping, numpy, pandas, pygame, scikit-learn, scipy, seaborn, stable_baselines3, torch, tqdm, typeguard, typing_extensions

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 36
- Forks at capture: 8
- Last updated: 2024-07-28T12:07:19Z
- Last pushed: 2024-09-03T22:14:49Z
- Topics: exploratory-data-analysis, optimization, reinforcement-learning, simulation, trajectory-transformer

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-accessible-rl-sdk)
- [README](https://github.com/awslabs/amazon-accessible-rl-sdk/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-accessible-rl-sdk/issues)
- [Releases](https://github.com/awslabs/amazon-accessible-rl-sdk/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
