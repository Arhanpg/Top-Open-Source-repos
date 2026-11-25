# GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai](https://github.com/GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai/blob/main/README.md)
- README blob SHA: b6c235219285ee9300c342ff5a590b8a1335db1a
- README bytes captured: 1233
- README truncated at capture limit: False
- Repository ID: 748828291
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A jump start solution using GKE or Cloud Run with Cloud SQL and VertexAI

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:46:59+00:00

### Short excerpt (up to 300 words)

> This app can be

### README headings

- Deploy a production ready GenAI app in less than 30 minutes
- Choose your Architecture
- Cloud Run ([README](run/README.md))
- GKE ([README](gke/README.md))

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Choose your Architecture

> This app can be

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 42,588 |
| Python | 32,965 |
| Dockerfile | 4,890 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- gke/chatbot-api/Dockerfile (capture: captured)
- gke/chatbot-api/requirements.txt (capture: captured) — dependency clues: aiohttp, asyncpg, fastapi, google-auth, google-cloud-aiplatform, langchain, langchain-core, langchain-google-vertexai, langchain-text-splitters, numpy, pandas, pgvector, uvicorn
- gke/init-db/Dockerfile (capture: captured)
- gke/init-db/requirements.txt (capture: captured) — dependency clues: async-timeout, asyncpg
- gke/load-embeddings/Dockerfile (capture: captured)
- gke/load-embeddings/requirements.txt (capture: captured) — dependency clues: aiohttp, asyncpg, google-auth, google-cloud-aiplatform, langchain, langchain-google-vertexai, langchain-text-splitters, numpy, pandas, pgvector

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 64
- Forks at capture: 36
- Last updated: 2026-10-20T22:52:40Z
- Last pushed: 2026-06-20T02:04:59Z
- Topics: cloud-run, gke, google-cloud

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai)
- [README](https://github.com/GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloudsql-jump-start-solution-for-genai/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
