# aws-observability/cloudwatch-plugin-otel-go

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/cloudwatch-plugin-otel-go
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:14:59+00:00

## Project purpose

A plugin for the OpenTelemetry Go SDK that generates request ("RED") metrics from spans **in-process, from 100% of spans, before trace sampling is applied**.

## Why this project is used

A plugin for the OpenTelemetry Go SDK that generates request ("RED") metrics from spans **in-process, from 100% of spans, before trace sampling is applied**.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/uuid, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp, go.opentelemetry.io/otel, go.opentelemetry.io/otel/metric, go.opentelemetry.io/otel/sdk, go.opentelemetry.io/otel/sdk/metric, go.opentelemetry.io/otel/trace, golang.org/x/sys
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: contract-tests/doc.go, contract-tests/family_test.go, contract-tests/harness_test.go, contract-tests/mode_test.go

## Setup and usage

- Usage: Register the record-forcing sampler and the span-metrics processor on your TracerProvider,
- Usage: and give the processor the MeterProvider the metrics should be recorded into (normally the
- Usage: same one your application already uses for its other metrics):
- Usage: "go.opentelemetry.io/otel"
- Usage: sdkmetric "go.opentelemetry.io/otel/sdk/metric"
- Usage: sdktrace "go.opentelemetry.io/otel/sdk/trace"
- Usage: "github.com/aws-observability/cloudwatch-plugin-otel-go/spanmetrics"
- Usage: // The MeterProvider the span metrics record into. Its resource (service.name, etc.) becomes

## Limitations and caveats

- Security: See CONTRIBUTING for information on reporting a
- Security: potential security issue. Please do not create a public GitHub issue for security reports.

## Evidence and provenance

- README: https://github.com/aws-observability/cloudwatch-plugin-otel-go/blob/main/README.md
- README SHA: 3dbcd7cdeb0f7f2079b8f0f86faebd9511e275a2
- Manifests: go.mod
- Sampled source files: contract-tests/doc.go, contract-tests/family_test.go, contract-tests/harness_test.go, contract-tests/mode_test.go
- Git tree state: captured
- Evidence fingerprint: c76de6ea3a9774a39124f6e78ad218047725189550ab108e26f65bcdbb0d2147

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
