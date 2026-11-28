# GoogleCloudPlatform/race-condition

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/race-condition](https://github.com/GoogleCloudPlatform/race-condition)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/race-condition/blob/main/README.md)
- README blob SHA: e916002100100859554a549c6c890bf42e185a51
- README bytes captured: 30559
- README truncated at capture limit: False
- Repository ID: 1193970689
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The open source multi-agent simulation from the Developer Keynote at Google Cloud Next '26. A deployable reference architecture for autonomous AI agents using Gemini and ADK.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:36:31+00:00

### Short excerpt (up to 300 words)

> make init graph TD Frontend["Frontend<br/>Angular + Install these before you

### README headings

- Race Condition
- What this repo is good for
- What's different from the keynote build
- How the agents split the work
- Get started with your AI coding assistant
- If you use Claude Code
- If you use Gemini CLI, OpenCode, Cursor, or GitHub Copilot
- Architecture
- Prerequisites
- Cost note
- Quickstart
- 1. Set up your GCP project
- Log in and write Application Default Credentials in one step
- Set your project (replace MY_PROJECT_ID everywhere below)
- Enable required APIs
- Set the quota project so API calls are billed correctly
- 2. Clone and initialize
- Install everything and build (checks prereqs, creates .env, installs deps)
- Set your GCP project in .env (this is what the agents actually read)
- sed -i 's/your-gcp-project-id/MY_PROJECT_ID/g' .env   # Linux
- 3. Start the simulation
- What `make init` does
- What `make start` does
- Using the frontend
- Demos
- Camera
- Sandbox
- Google Maps API key (optional)
- Step 1: Enable the Maps APIs
- Step 2: Create an API key

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install everything and build (checks prereqs, creates .env, installs deps)

> make init

### Architecture and design: Architecture

> graph TD Frontend["Frontend<br/>Angular +

### Technology and requirements: Prerequisites

> Install these before you

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,401,313 |
| TypeScript | 882,329 |
| Go | 498,540 |
| HCL | 168,671 |
| SCSS | 117,544 |
| HTML | 77,934 |
| Shell | 50,009 |
| JavaScript | 23,247 |
| CSS | 14,075 |
| Makefile | 8,924 |
| Gherkin | 6,758 |
| Dockerfile | 5,710 |
| Procfile | 1,274 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/pubsub/v2, github.com/alicebob/miniredis/v2, github.com/bytedance/gopkg, github.com/bytedance/sonic, github.com/bytedance/sonic/loader, github.com/cespare/xxhash/v2, github.com/cloudwego/base64x, github.com/cucumber/gherkin/go/v42, github.com/cucumber/godog, github.com/cucumber/messages/go/v34, github.com/felixge/httpsnoop, github.com/gabriel-vasile/mimetype, github.com/gin-contrib/sse, github.com/gin-gonic/gin, github.com/go-logr/logr, github.com/go-logr/stdr
- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: a2a-sdk, anyio, asyncpg, fastapi, google-adk, google-adk-community, google-cloud-aiplatform, google-cloud-iamconnectorcredentials, google-cloud-pubsub, google-cloud-secret-manager, google-genai, grpcio-tools, httpx, protobuf, pydantic, pypdf, python-dotenv, redis, uvicorn, websockets
- web/admin-dash/package.json (capture: captured) — dependency clues: @vitest/coverage-v8, jsdom, vite, vitest
- web/frontend/package.json (capture: captured) — dependency clues: @angular/animations, @angular/build, @angular/cli, @angular/common, @angular/compiler, @angular/compiler-cli, @angular/core, @angular/forms, @angular/platform-browser, @angular/platform-browser-dynamic, @angular/router, @ngx-env/builder, @types/three, ngx-countup, ngx-markdown, protobufjs, rxjs, socket.io-client, three, tslib

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 244
- Forks at capture: 86
- Last updated: 2026-11-20T06:31:19Z
- Last pushed: 2026-11-23T06:59:05Z
- Topics: agent-development-kit, ai-agents, angular, cloud-run, gemini, golang, google-cloud, multi-agent-systems, python, reference-architecture, threejs

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/race-condition)
- [README](https://github.com/GoogleCloudPlatform/race-condition/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/race-condition/issues)
- [Releases](https://github.com/GoogleCloudPlatform/race-condition/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
