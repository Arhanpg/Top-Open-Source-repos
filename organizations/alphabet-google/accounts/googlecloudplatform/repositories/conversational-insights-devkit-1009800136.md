# GoogleCloudPlatform/conversational-insights-devkit

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/conversational-insights-devkit](https://github.com/GoogleCloudPlatform/conversational-insights-devkit)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/conversational-insights-devkit/blob/main/README.md)
- README blob SHA: 57382f1b2834dda80a1cea767856d4789136cbf7
- README bytes captured: 7999
- README truncated at capture limit: False
- Repository ID: 1009800136
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A high level scripting API for Conversational Insights

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:11:36+00:00

### Short excerpt (up to 300 words)

> **Read & Analytics APIs**: Requires **Python 3.11+**. python3 Requires **Python 3.11+**. python3

### README headings

- Conversational Insights DevKit (`cxidk` 2.0)
- Key Features
- When to Use `cxidk` vs. `google-cloud-contact-center-insights`
- Requirements & Installation
- Core SDK
- With MCP server + Google ADK + Speech + DLP extras
- Local editable install for contributors
- Quickstart 1: Python SDK (`CxContext` & Read APIs)
- Quickstart 2: Gemini CLI Extension & Local MCP Server (`stdio`)
- Quickstart 3: Google ADK Agents
- Read-only analyst agent with redacted transcript defaults
- Guarded release agent (requires plan_token + ADK ToolConfirmation on writes)
- Quickstart 4: Vendor Transcript Conversion & Ingestion
- Convert an AWS Transcribe JSON payload locally
- Upload to GCS and ingest into CCAI Insights
- Cloud Run & Terraform Deployment
- Documentation for AI Systems
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Key Features

> **Read & Analytics APIs**:

### Getting started and usage: Requirements & Installation

> Requires **Python 3.11+**. python3

### Technology and requirements: Requirements & Installation

> Requires **Python 3.11+**. python3

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,344,584 |
| JavaScript | 47,393 |
| HTML | 29,754 |
| CSS | 23,876 |
| Shell | 11,577 |
| Dockerfile | 9,144 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: Flask, Flask-Cors, Werkzeug, audioop-lts, build, cloudevents, coverage, functions-framework, google-adk, google-api-core, google-auth, google-cloud-bigquery, google-cloud-contact-center-insights, google-cloud-dialogflow, google-cloud-dialogflow-cx, google-cloud-dlp, google-cloud-iam, google-cloud-logging, google-cloud-resource-manager, google-cloud-speech
- requirements.txt (capture: captured)
- deploy/mcp-cloud-run/Dockerfile (capture: captured)
- examples/terraform/cloud_run_function_ingest/function/requirements.txt (capture: captured) — dependency clues: cloudevents, cxidk, functions-framework
- src/cxidk/workflow/demo_artifacts/ui/Dockerfile (capture: captured)
- src/cxidk/workflow/demo_artifacts/ui/requirements.txt (capture: captured) — dependency clues: Flask, Flask-Cors, Werkzeug, google-api-core, google-auth, google-cloud-contact-center-insights, google-cloud-storage, gunicorn, python-dotenv

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 9
- Last updated: 2026-11-18T14:25:40Z
- Last pushed: 2026-11-18T14:14:01Z
- Topics: agent-skills, ai-agents, analytics, applied-ai, ccai-insights, contact-center, contact-center-ai, conversational, conversational-insights, gemini, gemini-cli-extension, google, google-adk, google-cloud, insights, llms-txt, mcp, mcp-server, python, vertex-ai

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/conversational-insights-devkit)
- [README](https://github.com/GoogleCloudPlatform/conversational-insights-devkit/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/conversational-insights-devkit/issues)
- [Releases](https://github.com/GoogleCloudPlatform/conversational-insights-devkit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
