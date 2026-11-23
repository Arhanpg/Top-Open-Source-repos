# SAP/agent-quality-inspect

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/agent-quality-inspect](https://github.com/SAP/agent-quality-inspect)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/agent-quality-inspect/blob/main/README.md)
- README blob SHA: 4578879a77eef73898ef763c15ebca5038e07ec0
- Repository ID: 1147797107
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Evaluation package that allows benchmarking of agentic AIs from various sources and frameworks by producing statistical results which can be compared across different use cases and datasets.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:41:53+00:00

### Short excerpt (up to 100 words)

> Paper Link: https://openreview.net/pdf?id=fHsVNklKOc Documentation Link: https://sap.github.io/agent-quality-inspect/ - Talk, Evaluate, Diagnose: User-aware Agent Evaluation with Automated Error Analysis - Table of Contents - Overview - Features - Installation - Prerequisites - Setup - Quick Start - Option 1. Using it as a Metrics Package - Option 2. Using it via the provided runners - Viewing Results - Agents Leaderboard UI - Bring Your Own Agent - Creating your own evaluation dataset - Known Issues - How to obtain support - Contributing - Citation - License that similar low-level errors are clustered into the same high-level category.](error_analysis_framework.png) This repository contains the implementation

### README headings

- Agent Quality Inspect
- Talk, Evaluate, Diagnose: User-aware Agent Evaluation with Automated Error Analysis (ICLR 2026)
- Table of Contents
- Overview
- Features
- Installation
- Prerequisites
- Setup
- Quick Start
- Option 1. Using it as a Metrics Package
- Create LLM client (requires env vars: AZURE_API_VERSION, AZURE_API_BASE, AZURE_API_KEY)
- Build a minimal agent trace with a single turn
- 2. Define the evaluation data sample and subgoals
- Step 1: Calculate progress rates using the evaluation sample and agent trace
- Step 2: Calculate AUC from progress scores
- Step 3: Run error analysis
- Extract validation results from the final turn
- Prepare data for error analysis
- Run error analysis
- Display results
- Option 2. Using it via the provided runners
- Viewing Results
- Agents Leaderboard
- Example
- Download and View Pre-computed Results from HuggingFace
- Bring Your Own Agent
- Creating your own evaluation dataset
- Known Issues
- How to obtain support
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,489,936 |
| Shell | 2,648 |
| Makefile | 839 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: backoff, numpy, openai
- docs/Makefile (capture: captured)
- agent_runners/tau2-bench/Makefile (capture: captured)
- agent_runners/tau2-bench/pyproject.toml (capture: captured) — dependency clues: PyYAML, addict, deepdiff, docstring-parser, fastapi, fs, langfuse, litellm, loguru, matplotlib, pandas, plotly, psutil, pydantic-argparse, pytest, redis, rich, ruff, scikit-learn, seaborn
- agent_runners/tau2-bench/requirements.txt (capture: captured) — dependency clues: addict, aiohappyeyeballs, aiohttp, aiosignal, annotated-types, anyio, appdirs, attrs, backoff, certifi, charset-normalizer, click, colorama, contourpy, cycler, deepdiff, distro, docstring-parser, fastapi, filelock

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 79
- Forks at capture: 1
- Last updated: 2026-11-19T18:25:00Z
- Last pushed: 2026-06-26T05:40:53Z
- Topics: agentic-ai, error-analysis, evaluation, llm, llm-as-a-judge, metrics, user-proxy

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/agent-quality-inspect)
- [README](https://github.com/SAP/agent-quality-inspect/blob/main/README.md)
- [Issues](https://github.com/SAP/agent-quality-inspect/issues)
- [Releases](https://github.com/SAP/agent-quality-inspect/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
