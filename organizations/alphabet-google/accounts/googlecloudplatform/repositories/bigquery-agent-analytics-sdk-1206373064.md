# GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK/blob/main/README.md)
- README blob SHA: c1924357352047fa6df9e49d54a0fccdabfcccb7
- README bytes captured: 17071
- README truncated at capture limit: False
- Repository ID: 1206373064
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An open-source Python SDK for analyzing, evaluating, and curating agent traces stored in BigQuery. Built on top of the BigQuery Agent Analytics, it provides a consumption-layer toolkit for agent observability, analysis, evaluation, and advanced capabilities like context graph at scale.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T01:59:30+00:00

### Short excerpt (up to 300 words)

> The BigQuery Agent Analytics **Observability** Trace reconstruction and pip install bigquery-agent-analytics With src/bigquery_agent_analytics/ │ ├── Core Python 3.10+ A Google

### README headings

- BigQuery Agent Analytics SDK
- Overview
- Key Features
- How this fits together
- Prerequisites
- Installation
- Quick Start
- Export traces to LangSmith
- Try it: extract decision traces (Agent Context Graph, ~10 minutes)
- 1. Deploy the context graph (one-time DDL: tables, then the property graph).
- 2. Seed five sample agent sessions into agent_events.
- 3. Extract decision traces from the deployed graph
- (read back via INFORMATION_SCHEMA.PROPERTY_GRAPHS — no SQL file passed).
- 4. Query a decision trace: what did the agent weigh, and how did it resolve?
- Documentation
- Architecture
- Related Projects
- Development
- Install with dev dependencies
- Run tests
- Format code
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> The BigQuery Agent Analytics

### Features and capabilities: Key Features

> **Observability** Trace reconstruction and

### Getting started and usage: Installation

> pip install bigquery-agent-analytics With

### Architecture and design: Architecture

> src/bigquery_agent_analytics/ │ ├── Core

### Technology and requirements: Prerequisites

> Python 3.10+ A Google

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 10,530,657 |
| JavaScript | 126,517 |
| Shell | 115,588 |
| TypeScript | 104,104 |
| HTML | 48,392 |
| Go Template | 21,243 |
| CSS | 18,765 |
| Jupyter Notebook | 4,083 |
| Dockerfile | 4,009 |
| Standard ML | 322 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: bigframes, bigquery-agent-analytics, db-dtypes, google-adk, google-cloud-aiplatform, google-cloud-bigquery, google-genai, isort, jsonschema, langsmith, pandas, plotly, pydantic, pyink, pytest, pytest-asyncio, python-dotenv, pyyaml, rdflib, streamlit
- producers/pyproject.toml (capture: captured) — dependency clues: claude-agent-sdk, google-cloud-bigquery, google-cloud-bigquery-storage, google-cloud-pubsub, gunicorn, isort, openai-agents, opentelemetry-proto, pyarrow, pyink, pytest, pytest-asyncio, tomli
- dashboards/legacy_demo/requirements.txt (capture: captured) — dependency clues: db-dtypes, google-cloud-bigquery, pandas, plotly, streamlit
- dashboards/web/package.json (capture: captured) — dependency clues: @google-cloud/bigquery, @tailwindcss/vite, @tanstack/react-query, @types/node, @vitejs/plugin-react, @xyflow/react, autoprefixer, clsx, date-fns, lucide-react, motion, react, react-dom, react-router, recharts, tailwind-merge, tailwindcss, tsx, typescript, vite
- deploy/otlp_receiver/Dockerfile (capture: captured)
- deploy/skill_evolution_job/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 64
- Forks at capture: 32
- Last updated: 2026-11-16T15:44:34Z
- Last pushed: 2026-11-23T18:46:34Z
- Topics: adk-python, agent, context-graph, evaluation, observability

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK)
- [README](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK/issues)
- [Releases](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
