# Azure/azure-functions-golang-worker

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-functions-golang-worker](https://github.com/Azure/azure-functions-golang-worker)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/azure-functions-golang-worker/blob/main/README.md)
- README blob SHA: a67049d9b463a6a3e256bad236c5ca981192dd22
- README bytes captured: 20361
- README truncated at capture limit: False
- Repository ID: 928022361
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Run your Go serverless workloads on Azure Functions with first-class runtime support.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:50:51+00:00

### Short excerpt (up to 300 words)

> **Native Go Feel:** Use npm i -g azure-functions-core-tools@4 Go 1.24+ for the

### README headings

- Azure Functions Go Worker
- Features
- Getting Started
- Prerequisites
- Install Azure Functions Core Tools
- Writing Your First Function
- Examples & Samples
- Trigger Model: Core Triggers vs Extension Triggers
- Core Triggers (`sdk/`)
- Extension Triggers (`triggers/`)
- When is each tier used?
- Generic host triggers
- Option 1 - Direct registration
- Option 2 - Typed helper package
- Goroutine safety & panic recovery
- Propagate panics as errors: `sdk.RecoverTo`
- Best-effort work: `sdk.Recover`
- Telemetry & Observability
- Dependency metadata
- Structured logging
- OpenTelemetry distributed tracing
- Custom Handlers vs First-Class Go Worker
- Contributing
- Trademarks

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> **Native Go Feel:** Use

### Getting started and usage: Install Azure Functions Core Tools

> npm i -g azure-functions-core-tools@4

### Technology and requirements: Prerequisites

> Go 1.24+ for the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,133,971 |
| Python | 28,538 |
| Shell | 1,856 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/spf13/pflag, go.opentelemetry.io/otel, go.opentelemetry.io/otel/sdk/metric, golang.org/x/net, golang.org/x/sys, golang.org/x/text, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf
- otelcollector/go.mod (capture: captured) — dependency clues: github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/azure/azure-functions-golang-worker, github.com/beorn7/perks, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/ebitengine/purego, github.com/felixge/httpsnoop, github.com/foxboron/go-tpm-keyfiles, github.com/fsnotify/fsnotify, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-ole/go-ole, github.com/go-viper/mapstructure/v2, github.com/gobwas/glob, github.com/gogo/protobuf, github.com/golang-jwt/jwt/v5
- middleware/durabletask/go.mod (capture: captured) — dependency clues: github.com/azure/azure-functions-golang-worker, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/uuid, github.com/microsoft/durabletask-go, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/otel, go.opentelemetry.io/otel/metric, go.opentelemetry.io/otel/sdk, go.opentelemetry.io/otel/trace, golang.org/x/net, golang.org/x/sys, golang.org/x/text, google.golang.org/genproto, google.golang.org/grpc, google.golang.org/protobuf
- middleware/otelfunc/go.mod (capture: captured) — dependency clues: github.com/azure/azure-functions-golang-worker, github.com/beorn7/perks, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/uuid, github.com/grpc-ecosystem/grpc-gateway/v2, github.com/munnerz/goautoneg, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/otlptranslator, github.com/prometheus/procfs, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/contrib/bridges/otelslog, go.opentelemetry.io/contrib/bridges/prometheus, go.opentelemetry.io/contrib/exporters/autoexport, go.opentelemetry.io/otel, go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc
- samples/blobTrigger/Dockerfile (capture: captured)
- samples/httpTrigger/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 15
- Forks at capture: 7
- Last updated: 2026-11-17T16:22:54Z
- Last pushed: 2026-11-11T20:58:39Z
- Topics: azure, go, golang, serverless, serverless-functions

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-functions-golang-worker)
- [README](https://github.com/Azure/azure-functions-golang-worker/blob/main/README.md)
- [Issues](https://github.com/Azure/azure-functions-golang-worker/issues)
- [Releases](https://github.com/Azure/azure-functions-golang-worker/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
