# SAP-cloud-infrastructure/opensearch-query-exporter

- Company: SAP
- Account: SAP-cloud-infrastructure
- Repository: https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:36:37+00:00

## Project purpose

A Prometheus exporter that runs custom OpenSearch queries on a schedule and exposes results as metrics. Designed for Kubernetes deployments where teams define their own queries via ConfigMaps.

## Why this project is used

A Prometheus exporter for OpenSearch queries

## Core features

- **Query-focused**: Only exposes metrics you define, no noise from cluster internals: **Query-focused**: Only exposes metrics you define, no noise from cluster internals
  - Evidence: README.md#Features
- **Secure**: TLS-only with credential failover support: **Secure**: TLS-only with credential failover support
  - Evidence: README.md#Features
- **Efficient**: Concurrent background query execution, minimal footprint: **Efficient**: Concurrent background query execution, minimal footprint
  - Evidence: README.md#Features
- **Resilient**: Configurable error handling (preserve/drop/zero) per query: **Resilient**: Configurable error handling (preserve/drop/zero) per query
  - Evidence: README.md#Features
- **Safe**: max_query_range rejects queries that would hit warm/cold storage: **Safe**: max_query_range rejects queries that would hit warm/cold storage
  - Evidence: README.md#Features
- **Kubernetes-native**: Health probes, env var expansion in config, ConfigMap-friendly: **Kubernetes-native**: Health probes, env var expansion in config, ConfigMap-friendly
  - Evidence: README.md#Features

## Technology stack

- Languages: Go, Dockerfile, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/kr/text, github.com/munnerz/goautoneg, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, golang.org/x/sys, google.golang.org/protobuf, gopkg.in/yaml.v3
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/exporter/main.go, cmd/exporter/main_test.go, pkg/config/config.go, pkg/config/config_test.go

## Setup and usage

No setup information established.

## Limitations and caveats

- Security / Disclosure: If you find any bug that may be a security problem, please follow our instructions in the security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/SAP-cloud-infrastructure/opensearch-query-exporter/blob/main/README.md
- README SHA: a496ca4991172ebd5356f8e5eb0e4da6ded3ee88
- Manifests: Dockerfile, go.mod, Makefile
- Sampled source files: cmd/exporter/main.go, cmd/exporter/main_test.go, pkg/config/config.go, pkg/config/config_test.go
- Git tree state: captured
- Evidence fingerprint: 60ae672baabf255e402d74ddc946142fa6e988dba62b643f6a20f9339aa17ce4

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
