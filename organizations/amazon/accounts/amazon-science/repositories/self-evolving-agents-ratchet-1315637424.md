# amazon-science/Self-Evolving-Agents-Ratchet

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/Self-Evolving-Agents-Ratchet](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet/blob/main/README.md)
- README blob SHA: bf708370feaf93052f45c30a4fdab05d9abc8b1c
- README bytes captured: 25609
- README truncated at capture limit: False
- Repository ID: 1315637424
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Reference implementation of Ratchet: a minimal hygiene recipe for self-evolving LLM agents (arXiv:2605.22148)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:03:10+00:00

### Short excerpt (up to 300 words)

> git clone https://github.com/amazon-science/Self-Evolving-Agents-Ratchet cd ┌──────────────────── per task ────────────────────┐ Python 3.10+ An AWS See CONTRIBUTING for more

### README headings

- Ratchet
- Papers
- Quickstart
- Prerequisites
- 1. Install
- add ',swebench' if you plan to use the SWE-Bench Verified suite
- 2. Set credentials
- Optional but recommended (avoids HuggingFace rate limits):
- Optional model overrides:
- export SKILLEVO_BEDROCK_MODEL_ID=global.anthropic.claude-opus-4-7
- export SKILLEVO_BEDROCK_FALLBACK_MODEL_ID=global.anthropic.claude-sonnet-4-6
- export SKILLEVO_BEDROCK_EMBED_MODEL_ID=global.cohere.embed-v4:0
- 3. Verify the environment
- 4. Real run on the hard subset
- MBPP+ hard-100 (60 train / 40 eval)
- SWE-Bench Verified hard-150 (90 train / 60 eval) — same pattern
- 5. Inspect
- Bringing your own skill bank
- Bringing your own task
- Architecture at a glance
- Key artifacts
- Skill
- MetaSkill
- Per-task flow (`Engine.run(task)`)
- Per-round flow (what `run_skill_loop.py` does each round)
- LLM calls, summarised
- Install — extras
- Run
- Direct-LLM baselines + hard-subset selection (one-shot)
- Training loops

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: 1. Install

> git clone https://github.com/amazon-science/Self-Evolving-Agents-Ratchet cd

### Architecture and design: Architecture at a glance

> ┌──────────────────── per task ────────────────────┐

### Technology and requirements: Prerequisites

> Python 3.10+ An AWS

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 788,080 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: boto3, datasets, matplotlib, numpy, pydantic, pytest, pyyaml, swebench

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 0
- Last updated: 2026-10-18T03:42:31Z
- Last pushed: 2026-07-29T05:20:27Z
- Topics: agentic-ai, amazon-bedrock, llm, llm-agents, mbpp, self-evolving-agents, skill-library, swe-bench

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet)
- [README](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet/blob/main/README.md)
- [Issues](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet/issues)
- [Releases](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
