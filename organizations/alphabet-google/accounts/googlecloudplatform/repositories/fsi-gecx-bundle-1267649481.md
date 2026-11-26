# GoogleCloudPlatform/fsi-gecx-bundle

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/fsi-gecx-bundle](https://github.com/GoogleCloudPlatform/fsi-gecx-bundle)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/fsi-gecx-bundle/blob/main/README.md)
- README blob SHA: b880ddb781ef2af5ba56bb1cc80878e2963df831
- README bytes captured: 15894
- README truncated at capture limit: False
- Repository ID: 1267649481
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This digital banking demo showcases a flexible, secure, and AI-driven platform designed to modernize the banking experience.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T22:12:39+00:00

### Short excerpt (up to 300 words)

> Use the Makefile bootstrapper A Google Cloud Project:

### README headings

- FSI GECX Bundle
- Solution Diagram
- Prerequisites
- Available Terraform Variables
- GCP Secrets
- Deployment
- Authenticate to Google Cloud
- Log in with Application Default Credentials (ADC)
- Set the specified project as the active project in your configuration
- Check the configuration to ensure the project and account are correct
- Create Terraform state bucket
- Create tfbackend file
- Create TF vars file from template
- Return to the root of the repository
- Enable required APIs
- Enable OAuth Consent Screen Branding
- Create OAuth client
- Create Secrets
- Generate GitHub Token Secret
- Infrastructure Deployment
- From the root of the repository
- If you need to reconfigure use `make tf-init ARGS="--reconfigure"`
- Make note of the load_balancer_ip output for use later in the [Create DNS A entry](#create-dns-a-entry)
- CX Agent Studio Deployment
- Trigger site crawl to populate Agent Search datastore
- Create DNS A entry:
- Local Development Setup
- 1. Install All Dependencies
- 2. Configure Local Frontend Credentials
- 3. Run Services Locally

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: 1. Install All Dependencies

> Use the Makefile bootstrapper

### Technology and requirements: Prerequisites

> A Google Cloud Project:

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,761,604 |
| JavaScript | 1,410,796 |
| HCL | 287,113 |
| Shell | 100,975 |
| Makefile | 32,479 |
| Java | 29,086 |
| HTML | 13,852 |
| Dockerfile | 7,940 |
| CSS | 4,796 |
| Mako | 1,280 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- banking-service/Dockerfile (capture: captured)
- banking-service/pyproject.toml (capture: captured) — dependency clues: alembic, cachetools, cryptography, fastapi, fastmcp, firebase-admin, google-adk, google-cloud-bigquery, google-cloud-dataplex, google-cloud-discoveryengine, google-cloud-documentai, google-cloud-kms, google-cloud-monitoring, google-cloud-pubsub, google-cloud-secret-manager, google-cloud-storage, greenlet, httpx, jeepney, joserfc
- banking-ui/Dockerfile (capture: captured)
- banking-ui/package.json (capture: captured) — dependency clues: @eslint/js, @microsoft/fetch-event-source, @tailwindcss/vite, @types/react, @types/react-dom, @vitejs/plugin-react, axios, eslint, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals, js-yaml, livekit-client, lucide-react, react, react-dom, react-joyride, react-markdown, react-router-dom, tailwindcss
- blocking-function/package.json (capture: captured) — dependency clues: @eslint/js, eslint, gcip-cloud-functions, globals

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 2
- Last updated: 2026-11-10T01:22:11Z
- Last pushed: 2026-11-14T06:33:54Z
- Topics: agent-search, banking, bigquery, cx-agent-studio, document-ai, gcp, gecx, gemini-enterprise, vertex-ai-search

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/fsi-gecx-bundle)
- [README](https://github.com/GoogleCloudPlatform/fsi-gecx-bundle/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/fsi-gecx-bundle/issues)
- [Releases](https://github.com/GoogleCloudPlatform/fsi-gecx-bundle/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
