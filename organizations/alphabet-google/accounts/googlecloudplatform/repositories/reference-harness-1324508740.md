# GoogleCloudPlatform/reference-harness

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/reference-harness](https://github.com/GoogleCloudPlatform/reference-harness)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/reference-harness/blob/master/README.md)
- README blob SHA: 50f6171efc17352c4cb310dc8c42d0d50fe224eb
- README bytes captured: 52433
- README truncated at capture limit: False
- Repository ID: 1324508740
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:52:30+00:00

### Short excerpt (up to 300 words)

> The security scan identified gcloud auth login gcloud graph TD subgraph Ingestion This command creates .venv/ **Location:** /tmp/demo-target/app.py:8 **Evidence:** The

### README headings

- Reference Harness
- How it works
- Deployment & Integration Architecture
- Distribution and Deployment Options
- Option A: Centralized Service API (Cloud Run)
- Option B: Local Developer CLI (Artifact Registry)
- IAM & Authentication Policy
- Storage & Telemetry Configurations
- Setup
- 1. Choose Authentication Method
- Option A: Google Cloud Vertex AI (Enterprise Mode)
- Auth via gcloud SDK (Install: https://cloud.google.com/sdk/docs/install)
- Option B: Google AI Studio (Developer Key Mode - Recommended)
- 2. Install uv + CLI tools
- Install uv + CLI tools
- 📦 Recommended: Isolated Virtual-Environment Installation (Zero-Sudo)
- Install Semgrep SAST package
- Install Gitleaks binary (macOS Apple Silicon arm64 example)
- 🌐 System-Wide Installation (Optional)
- On macOS:
- On Linux / Manual Installers:
- Install Trivy (vulnerable-dependency / secrets / IaC scanner)
- Install Bandit (Python SAST scanner)
- Optional: Install ripgrep (speeds up Gemini discovery grep_code tool)
- (apt: `apt install ripgrep`, brew: `brew install ripgrep`)
- Optional: Install Tree-sitter AST structural querying engine
- Private Registry / 401 Unauthorized Workaround
- Standard Scans
- Evaluation Runs
- 3. Clone the project

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Executive summary

> The security scan identified

### Getting started and usage: Auth via gcloud SDK (Install: https://cloud.google.com/sdk/docs/install)

> gcloud auth login gcloud

### Architecture and design: How it works

> graph TD subgraph Ingestion

### Technology and requirements: 4. Install project dependencies

> This command creates .venv/

### Limitations and security: python.flask.security.injection.user-eval.eval-injection

> **Location:** /tmp/demo-target/app.py:8 **Evidence:** The

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 316,224 |
| JavaScript | 19,891 |
| Jsonnet | 11,130 |
| Shell | 7,962 |
| HCL | 4,707 |
| Dockerfile | 2,712 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: codespell, gcsfs, google-adk, google-agents-cli, google-cloud-logging, google-cloud-storage, opentelemetry-instrumentation-google-genai, rich, ruff, tree-sitter, tree-sitter-c, tree-sitter-c-sharp, tree-sitter-cpp, tree-sitter-css, tree-sitter-go, tree-sitter-html, tree-sitter-java, tree-sitter-javascript, tree-sitter-json, tree-sitter-php
- api/package.json (capture: captured) — dependency clues: @c6fc/spellcraft, @c6fc/spellcraft-gcp-auth, @c6fc/spellcraft-gcp-terraform
- api/cloud_run_functions/api/package.json (capture: captured) — dependency clues: @google-cloud/logging, @google-cloud/run, express, uuid

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 3
- Last updated: 2026-10-21T00:17:19Z
- Last pushed: 2026-11-16T20:23:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/reference-harness)
- [README](https://github.com/GoogleCloudPlatform/reference-harness/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/reference-harness/issues)
- [Releases](https://github.com/GoogleCloudPlatform/reference-harness/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
