# GoogleCloudPlatform/BQ-OTEL-Exporter

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/BQ-OTEL-Exporter](https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter/blob/main/README.md)
- README blob SHA: 78a3f09344d2cc22b6597e9b26c4b8f823320e3b
- README bytes captured: 106819
- README truncated at capture limit: False
- Repository ID: 1438789232
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

High-throughput OpenTelemetry Collector exporter for Google Cloud BigQuery. Stream OTLP traces, logs, and metrics at scale via the Storage Write API.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:19:42+00:00

### Short excerpt (up to 300 words)

> The published BigQuery schema This exporter registers no Non-goals by design: **Exactly-once.**

### README headings

- BigQuery Exporter
- Configuration
- Structural limits
- Redaction
- Examples
- Minimal configuration
- Common Google Cloud setups
- Transports
- Startup errors
- Schema overview
- Operating v1.0.0 tables
- Delivery semantics
- Three-tier read stance for high-volume logs
- Timeout and concurrency envelope
- IAM
- Known limitations and misuse
- Feature gates
- Internal telemetry
- Stream recovery
- Contributing
- Fuzzing and benchmarks
- Community, support, and governance

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Schema overview

> The published BigQuery schema

### Features and capabilities: Feature gates

> This exporter registers no

### Limitations and security: Known limitations and misuse

> Non-goals by design: **Exactly-once.**

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 8,486,749 |
| HCL | 209,561 |
| Shell | 132,164 |
| Python | 14,917 |
| Makefile | 8,162 |
| Dockerfile | 1,884 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/bigquery, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, github.com/apache/arrow/go/v15, github.com/beorn7/perks, github.com/cenkalti/backoff/v5, github.com/cenkalti/backoff/v7, github.com/cespare/xxhash/v2, github.com/dlclark/regexp2, github.com/ebitengine/purego, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-ole/go-ole, github.com/go-viper/mapstructure/v2, github.com/gobwas/glob, github.com/goccy/go-json
- Makefile (capture: captured)
- example/Dockerfile (capture: captured)
- deploy/helm/bigquery-otel-collector/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 3
- Last updated: 2026-11-21T08:42:21Z
- Last pushed: 2026-11-23T19:49:10Z
- Topics: bigquery, genai, golang, google-cloud, logs, mcp, metrics, observability, opentelemetry, opentelemetry-collector, otlp, traces

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter)
- [README](https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter/issues)
- [Releases](https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
