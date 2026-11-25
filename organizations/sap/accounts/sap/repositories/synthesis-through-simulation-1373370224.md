# SAP/synthesis-through-simulation

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/synthesis-through-simulation](https://github.com/SAP/synthesis-through-simulation)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/synthesis-through-simulation/blob/main/README.md)
- README blob SHA: 6c4452e3fccf6301ba2a75ea7d05d4994d90402a
- README bytes captured: 13087
- README truncated at capture limit: False
- Repository ID: 1373370224
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

[NeurIPS 2026] Generating Coherent Enterprise Data via Scalable Agent-System Interaction

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T06:00:28+00:00

### Short excerpt (up to 300 words)

> Most synthetic-data generators learn Requires **Python 3.13** and The agent interacts with If you find any

### README headings

- Synthesis Through Simulation
- About this project
- Why it's different
- How it works
- Environments
- Installation
- Install everything, including the Generalist Populator (deepagents / LangChain)
- Configure the LLM
- Quickstart
- 1. Build a clean environment database from schema + reference data
- 2. Run the Generalist Populator (10 trajectories, K=3 exploration cycles)
- 3. Confirm every business rule still holds
- 4. Score the run's fidelity
- Useful flags
- Benchmarking
- Full metric suite over a finished run directory
- Or just fidelity, straight from the CLI helper
- Onboarding a new environment
- Reproducing the paper
- All GP experiments (sections selectable via SECTION=...)
- Tabular baselines (CTGAN / TVAE) — needs: uv pip install sdv scipy
- EnvScaler blind-agent baseline
- Repository structure
- Citation
- Authors
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About this project

> Most synthetic-data generators learn

### Getting started and usage: Installation

> Requires **Python 3.13** and

### Architecture and design: How it works

> The agent interacts with

### Limitations and security: Security / Disclosure

> If you find any

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,572,864 |
| Shell | 5,413 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: deepagents, faker, langchain-anthropic, langchain-openai, langfuse, openai, pydantic, pytest, python-dotenv, ruff, sqlite-vec
- src/synthesize/environments/airline/setup.py (capture: captured)
- src/synthesize/environments/banking/setup.py (capture: captured)
- src/synthesize/environments/cloud/setup.py (capture: captured)
- src/synthesize/environments/ecommerce/setup.py (capture: captured)
- src/synthesize/environments/forum/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 0
- Last updated: 2026-11-10T23:05:43Z
- Last pushed: 2026-10-16T17:29:50Z
- Topics: agent-evaluation, agents, ai-agents, benchmark, data-generation, data-synthesis, enterprise-data, generative-ai, langchain, llm, llm-agents, machine-learning, mock-apis, neurips, python, simulation, synthetic-data, synthetic-data-generation, tabular-data

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/synthesis-through-simulation)
- [README](https://github.com/SAP/synthesis-through-simulation/blob/main/README.md)
- [Issues](https://github.com/SAP/synthesis-through-simulation/issues)
- [Releases](https://github.com/SAP/synthesis-through-simulation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
