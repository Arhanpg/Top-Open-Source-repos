# amazon-science/SenTSR-Bench

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/SenTSR-Bench](https://github.com/amazon-science/SenTSR-Bench)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/SenTSR-Bench/blob/main/README.md)
- README blob SHA: 472a569f222f659e71c9fa1e5972ffd67dca113e
- README bytes captured: 11152
- README truncated at capture limit: False
- Repository ID: 1271929479
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:21:10+00:00

### Short excerpt (up to 300 words)

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Official implementation of git clone https://github.com/amazon-science/SenTSR-Bench.git cd Python 3.10+ Conda for

### README headings

- Overview
- Key Contributions
- Main Results
- Table of Contents
- Setup
- Prerequisites
- Installation
- (For Claude experiments) Configure AWS credentials
- Benchmark
- SenTSR-Bench Evaluation Benchmark
- Install huggingface_hub if needed
- Download dataset to ./dataset/
- Public Benchmark Data Curation
- Synthetic Data Generation Pipeline
- Method: Knowledge Injection
- Closed-Source: Claude (GRLM) + ChatTS (TSLM)
- 1. Start the ChatTS server
- 2. Run standalone baselines
- 3. Run knowledge injection (generates observations + injects into Claude)
- 4. Stop the server
- Open-Source: Qwen3 (GRLM) + Qwen-VL (TSLM)
- 1. Start both servers
- 2. Run standalone baseline
- 3. Run knowledge injection
- 4. Stop servers
- Open-Source: DeepSeek-R1 (GRLM) + Qwen-VL (TSLM)
- 1. Start servers
- 2. Run knowledge injection
- 3. Stop servers
- TSLM Training

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Official implementation of

### Getting started and usage: Installation

> git clone https://github.com/amazon-science/SenTSR-Bench.git cd

### Technology and requirements: Prerequisites

> Python 3.10+ Conda for

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 296,345 |
| Shell | 100,227 |
| Jinja | 1,418 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: boto3, jinja2, jsonlines, matplotlib, numpy, pandas, requests, scipy, seaborn, tenacity, tqdm
- evaluation/my_ragas/requirements.txt (capture: captured) — dependency clues: langchain, langchain-chroma, langchain-community, langchain-core, langchain-experimental, langchain-openai, langchain-text-splitters, langchainhub, ragas

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 2
- Last updated: 2026-11-11T17:50:58Z
- Last pushed: 2026-07-27T20:02:29Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/SenTSR-Bench)
- [README](https://github.com/amazon-science/SenTSR-Bench/blob/main/README.md)
- [Issues](https://github.com/amazon-science/SenTSR-Bench/issues)
- [Releases](https://github.com/amazon-science/SenTSR-Bench/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
