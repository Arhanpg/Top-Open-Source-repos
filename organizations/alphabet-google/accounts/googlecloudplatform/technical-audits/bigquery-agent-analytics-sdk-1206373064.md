# GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK

- Company: Alphabet (Google)
- Account: GoogleCloudPlatform
- Repository: https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:11:26+00:00

## Project purpose

An open-source Python SDK for analyzing, evaluating, and curating agent traces stored in BigQuery. Built on top of the BigQuery Agent Analytics, it provides a consumption-layer toolkit for agent observability, analysis, evaluation, and advanced capabilities like the Agent Context Graph — extracting decision traces from your agent's context graph — at scale.

## Why this project is used

An open-source Python SDK for analyzing, evaluating, and curating agent traces stored in BigQuery. Built on top of the BigQuery Agent Analytics, it provides a consumption-layer toolkit for agent observability, analysis, evaluation, and advanced capabilities like context graph at scale.

## Core features

- Trace reconstruction and DAG visualization: Trace reconstruction and DAG visualization
  - Evidence: README.md#Key Features
- Per-event-type BigQuery views: Per-event-type BigQuery views
  - Evidence: README.md#Key Features
- Observability dashboards (Looker Studio, Streamlit, SQL, and BigFrames), including BQCA Prompt & Response Logging dashboards for Conversational Analytics data a: Observability dashboards (Looker Studio, Streamlit, SQL, and BigFrames), including BQCA Prompt & Response Logging dashboards for Conversational Analytics data agents
  - Evidence: README.md#Key Features
- System metrics (latency, turn count, tool call error rate, token efficiency, time to first token, cost): System metrics (latency, turn count, tool call error rate, token efficiency, time to first token, cost)
  - Evidence: README.md#Key Features
- Performance Metrics (correctness, hallucination, sentiment, efficiency, etc): Performance Metrics (correctness, hallucination, sentiment, efficiency, etc)
  - Evidence: README.md#Key Features
- Multi-trial system and performance metrics: Multi-trial system and performance metrics
  - Evidence: README.md#Key Features
- Grader composition (weighted, binary, majority strategies): Grader composition (weighted, binary, majority strategies)
  - Evidence: README.md#Key Features
- Eval suite lifecycle management with graduation and saturation detection: Eval suite lifecycle management with graduation and saturation detection
  - Evidence: README.md#Key Features
- Static quality validation (ambiguous tasks, class imbalance, suspicious thresholds): Static quality validation (ambiguous tasks, class imbalance, suspicious thresholds)
  - Evidence: README.md#Key Features
- BigQuery AI.GENERATE, AI.EMBED, AI.CLASSIFY: BigQuery AI.GENERATE, AI.EMBED, AI.CLASSIFY
  - Evidence: README.md#Key Features
- Anomaly detection and latency forecasting: Anomaly detection and latency forecasting
  - Evidence: README.md#Key Features
- Categorical (Hatteras-style) evaluation via BigFrames: Categorical (Hatteras-style) evaluation via BigFrames
  - Evidence: README.md#Key Features
- Agent Context Graph — extract decision traces from your agent's context graph: the requests an agent handled, the options it weighed, and the outcomes it commit: Agent Context Graph — extract decision traces from your agent's context graph: the requests an agent handled, the options it weighed, and the outcomes it committed, materialized into a queryable BigQuery property graph (GQL traversal, scheduled refresh via bqaa context-graph)
  - Evidence: README.md#Key Features
- Long-horizon cross-session memory: Long-horizon cross-session memory
  - Evidence: README.md#Key Features
- Multi-stage agent insights pipeline: Multi-stage agent insights pipeline
  - Evidence: README.md#Key Features

## Technology stack

- Languages: Python, JavaScript, Shell, TypeScript, HTML, Go Template, CSS, Jupyter Notebook, Dockerfile, Standard ML
- Frameworks/libraries: Unknown / not established
- Dependency names: @google-cloud/bigquery, @tailwindcss/vite, @tanstack/react-query, @types/node, @vitejs/plugin-react, @xyflow/react, autoprefixer, clsx, date-fns, db-dtypes, google-adk, google-cloud-bigquery, lucide-react, motion, pandas, plotly, pydantic, pyyaml, react, react-dom, react-router, recharts, streamlit, tailwind-merge, tailwindcss, tsx, typer, typescript, vite
- Build/package tools: Docker build configuration, npm-compatible manifest, Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: producers/src/bigquery_agent_analytics_tracing/otlp/app.py, producers/src/bigquery_agent_analytics_tracing/otlp/cli.py, src/bigquery_agent_analytics/export/cli.py, src/bigquery_ontology/cli.py

## Setup and usage

- Installation: pip install bigquery-agent-analytics
- Installation: With optional LLM judge support:
- Installation: pip install bigquery-agent-analytics[llm]
- Installation: With BigFrames support:
- Installation: pip install bigquery-agent-analytics[bigframes]
- Installation: With LangSmith export support:
- Installation: pip install bigquery-agent-analytics[langsmith]
- Quick Start: from bigquery_agent_analytics import Client, TraceFilter

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK/blob/main/README.md
- README SHA: c1924357352047fa6df9e49d54a0fccdabfcccb7
- Manifests: pyproject.toml, producers/pyproject.toml, dashboards/legacy_demo/requirements.txt, dashboards/web/package.json, deploy/otlp_receiver/Dockerfile, deploy/skill_evolution_job/Dockerfile
- Sampled source files: producers/src/bigquery_agent_analytics_tracing/otlp/app.py, producers/src/bigquery_agent_analytics_tracing/otlp/cli.py, src/bigquery_agent_analytics/export/cli.py, src/bigquery_ontology/cli.py
- Git tree state: captured
- Evidence fingerprint: 1560dbe32cb7d05165a54e79e81e1f9b5f0c8c34db1f53ac72be6859d3201b5a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
