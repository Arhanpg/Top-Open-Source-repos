# aws-observability/amp-cardinality-insights

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/amp-cardinality-insights
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:54:44+00:00

## Project purpose

This project helps you have visibility into high cardinality metrics from an Amazon Managed Service for Prometheus workspace.

## Why this project is used

This project helps you have visibility into high cardinality metrics from an Amazon Managed Service for Prometheus workspace.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Python, Shell, Smarty, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/google/uuid, github.com/jmespath/go-jmespath, github.com/pmezard/go-difflib, github.com/stretchr/testify, go.uber.org/multierr, go.uber.org/zap, gopkg.in/yaml.v3
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lambda/aggregate-counts/main.go, lambda/count-metrics/main.go, lambda/metric-names/main.go, .github/workflows/get-dirs.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-observability/amp-cardinality-insights/blob/main/README.md
- README SHA: f898cfc314f3e2a5ab4d6af43a1bc60b6da08749
- Manifests: lambda/Makefile, lambda/aggregate-counts/go.mod, lambda/aggregate-counts/Makefile, lambda/count-metrics/go.mod, lambda/count-metrics/Makefile, lambda/metric-names/go.mod
- Sampled source files: lambda/aggregate-counts/main.go, lambda/count-metrics/main.go, lambda/metric-names/main.go, .github/workflows/get-dirs.py
- Git tree state: captured
- Evidence fingerprint: 9a7b08c405ae08ecc62a99b0c84622d99ca9d4383ca4722a322473355ed90d89

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
