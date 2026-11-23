# aws-observability/cloudwatch-plugin-otel-go

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/cloudwatch-plugin-otel-go](https://github.com/aws-observability/cloudwatch-plugin-otel-go)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/cloudwatch-plugin-otel-go/blob/main/README.md)
- README blob SHA: 3dbcd7cdeb0f7f2079b8f0f86faebd9511e275a2
- Repository ID: 1388159018
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:30:26+00:00

### Short excerpt (up to 100 words)

> A plugin for the OpenTelemetry Go SDK that generates request ("RED") metrics from spans **in-process, from 100% of spans, before trace sampling is applied**. Span metrics are normally generated downstream (e.g. by the OpenTelemetry Collector's `spanmetrics` connector) from whatever spans arrive there — which is only the *sampled* subset. At low sampling rates that undercounts. This plugin records the metrics inside the SDK, alongside a record-forcing sampler, so the metrics reflect every span while trace **export** still honors the configured sampling rate. Span metrics are the first feature of this plugin. Two metrics, matching the OpenTelemetry SpanMetrics naming: Each datapoint

### README headings

- CloudWatch Plugin for OpenTelemetry (Go)
- What it produces
- Supported instrumentation modes
- Install
- Usage
- Configuration
- Notes
- Security
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 74,128 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/uuid, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp, go.opentelemetry.io/otel, go.opentelemetry.io/otel/metric, go.opentelemetry.io/otel/sdk, go.opentelemetry.io/otel/sdk/metric, go.opentelemetry.io/otel/trace, golang.org/x/sys

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-10-12T21:54:27Z
- Last pushed: 2026-11-14T04:38:44Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/cloudwatch-plugin-otel-go)
- [README](https://github.com/aws-observability/cloudwatch-plugin-otel-go/blob/main/README.md)
- [Issues](https://github.com/aws-observability/cloudwatch-plugin-otel-go/issues)
- [Releases](https://github.com/aws-observability/cloudwatch-plugin-otel-go/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
