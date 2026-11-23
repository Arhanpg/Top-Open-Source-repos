# ai-dynamo/aiconfigurator

- Company: NVIDIA
- GitHub account: [https://github.com/ai-dynamo](https://github.com/ai-dynamo)
- Mapping status: official-project-linked
- Repository: [ai-dynamo/aiconfigurator](https://github.com/ai-dynamo/aiconfigurator)
- Default branch: main
- README: [Open upstream README](https://github.com/ai-dynamo/aiconfigurator/blob/main/README.md)
- README blob SHA: 77e625823b2524b7767298db438fee1d712c4ae9
- Repository ID: 1024020175
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Offline optimization of your disaggregated Dynamo graph

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:16:44+00:00

### Short excerpt (up to 100 words)

> SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved. SPDX-License-Identifier: Apache-2.0 --> Explore the AIC Developer Universe, an interactive map of AIConfigurator and its Dynamo integration. In disaggregated serving, configuring an effective deployment is challenging: you need to decide how many prefill and decode workers to run, and the parallelism for each worker. Combined with SLA targets for TTFT (Time to First Token) and TPOT (Time per Output Token), optimizing throughput at a given latency becomes even more complex. `aiconfigurator` helps you find a strong starting configuration for disaggregated serving. Given your model, GPU count, and GPU type,

### README headings

- aiconfigurator
- Build and Install
- Compatibility install from PyPI
- Upgrading an existing AIC environment from 0.9
- Build and Install from Source
- 1. Clone the repo
- 2. Create and activate a virtual environment
- 3. Install the standalone core, then the upper package
- Build with Docker
- This creates disjoint upper AIC and standalone core wheels
- Run
- CLI
- Python API
- 1. Run default agg vs disagg comparison
- 2. Run experiments from a YAML file or a dictionary config
- Or use a dictionary config directly
- 3. Find minimum GPUs for a performance target (procurement sizing)
- 4. Generate a naive configuration
- 5. Check support for a model/system combination
- Customized Configuration for aiconfigurator
- Deploying to llm-d Platform
- vLLM on llm-d
- SGLang on llm-d
- Generate Configurations for Dynamo and Reproduce the results
- Tuning with Advanced Features
- How It Works
- Modeling and Mechanism
- Supported Features
- Data Collection
- System Data Support Matrix

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 10,390,175 |
| Rust | 2,588,572 |
| Shell | 242,481 |
| Jinja | 133,943 |
| Jupyter Notebook | 60,102 |
| HTML | 24,500 |
| Dockerfile | 8,120 |
| JavaScript | 924 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: aiconfigurator-core, bokeh, fastapi, import-ipynb, jinja2, jsonschema, matplotlib, munch, numpy, nvidia-ml-py, orjson, packaging, pandas, plotext, plotly, pre-commit, prettytable, prometheus-api-client, pyarrow, pydantic
- aic-core/pyproject.toml (capture: captured) — dependency clues: numpy, packaging, pandas, pyarrow, pyyaml, scipy
- docker/Dockerfile (capture: captured)
- aic-core/rust/aiconfigurator-core/Cargo.toml (capture: captured) — dependency clues: bincode, log, parquet, pep440_rs, pyo3, quick_cache, serde, serde_json, serde_yaml, sha2, tempfile, thiserror
- aic-core/rust/tests/public-api/Cargo.toml (capture: captured) — dependency clues: aiconfigurator-core

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 470
- Forks at capture: 175
- Last updated: 2026-11-23T09:23:36Z
- Last pushed: 2026-10-29T04:17:46Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ai-dynamo/aiconfigurator)
- [README](https://github.com/ai-dynamo/aiconfigurator/blob/main/README.md)
- [Issues](https://github.com/ai-dynamo/aiconfigurator/issues)
- [Releases](https://github.com/ai-dynamo/aiconfigurator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
