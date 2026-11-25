# GoogleCloudPlatform/BQ-OTEL-Exporter

- Company: Alphabet (Google)
- Account: GoogleCloudPlatform
- Repository: https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:52:59+00:00

## Project purpose

[development]: https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/component-stability.md#development

## Why this project is used

High-throughput OpenTelemetry Collector exporter for Google Cloud BigQuery. Stream OTLP traces, logs, and metrics at scale via the Storage Write API.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/bigquery, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, github.com/apache/arrow/go/v15, github.com/beorn7/perks, github.com/cenkalti/backoff/v5, github.com/cenkalti/backoff/v7, github.com/cespare/xxhash/v2, github.com/dlclark/regexp2, github.com/ebitengine/purego, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-ole/go-ole, github.com/go-viper/mapstructure/v2, github.com/gobwas/glob, github.com/goccy/go-json, github.com/google/flatbuffers, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, github.com/grpc-ecosystem/grpc-gateway/v2, github.com/hashicorp/go-version, github.com/hashicorp/golang-lru/v2, github.com/json-iterator/go, github.com/klauspost/compress, github.com/klauspost/cpuid/v2, github.com/knadh/koanf/maps, github.com/knadh/koanf/providers/confmap, github.com/knadh/koanf/v2, github.com/lufia/plan9stats, github.com/mitchellh/copystructure, github.com/mitchellh/reflectwalk, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/pierrec/lz4/v4, github.com/power-devops/perfstat, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/otlptranslator, github.com/prometheus/procfs, github.com/santhosh-tekuri/jsonschema/v6, github.com/shirou/gopsutil/v4, github.com/stretchr/testify, github.com/tklauser/go-sysconf, github.com/tklauser/numcpus, github.com/yusufpapurcu/wmi, github.com/zeebo/xxh3, go.opencensus.io, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/collector/client, go.opentelemetry.io/collector/component, go.opentelemetry.io/collector/component/componentstatus, go.opentelemetry.io/collector/component/componenttest, go.opentelemetry.io/collector/config/configopaque, go.opentelemetry.io/collector/config/configoptional, go.opentelemetry.io/collector/config/configretry, go.opentelemetry.io/collector/config/configtelemetry, go.opentelemetry.io/collector/confmap, go.opentelemetry.io/collector/connector, go.opentelemetry.io/collector/connector/connectortest, go.opentelemetry.io/collector/connector/xconnector, go.opentelemetry.io/collector/consumer, go.opentelemetry.io/collector/consumer/consumererror, go.opentelemetry.io/collector/consumer/consumertest, go.opentelemetry.io/collector/consumer/xconsumer, go.opentelemetry.io/collector/exporter, go.opentelemetry.io/collector/exporter/exporterhelper, go.opentelemetry.io/collector/exporter/exportertest, go.opentelemetry.io/collector/exporter/xexporter, go.opentelemetry.io/collector/extension, go.opentelemetry.io/collector/extension/extensioncapabilities, go.opentelemetry.io/collector/extension/extensiontest, go.opentelemetry.io/collector/extension/xextension, go.opentelemetry.io/collector/featuregate, go.opentelemetry.io/collector/internal/componentalias, go.opentelemetry.io/collector/internal/fanoutconsumer, go.opentelemetry.io/collector/internal/telemetry, go.opentelemetry.io/collector/pdata, go.opentelemetry.io/collector/pdata/pprofile, go.opentelemetry.io/collector/pdata/testdata, go.opentelemetry.io/collector/pdata/xpdata, go.opentelemetry.io/collector/pipeline, go.opentelemetry.io/collector/pipeline/xpipeline, go.opentelemetry.io/collector/processor, go.opentelemetry.io/collector/processor/processortest, go.opentelemetry.io/collector/processor/xprocessor, go.opentelemetry.io/collector/receiver, go.opentelemetry.io/collector/receiver/receivertest, go.opentelemetry.io/collector/receiver/xreceiver, go.opentelemetry.io/collector/service, go.opentelemetry.io/collector/service/hostcapabilities, go.opentelemetry.io/collector/service/telemetry/telemetrytest, go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/bq-otel-backfill/main.go, cmd/bq-otel-testbench/main.go, cmd/bq-otel-validate/main.go, cmd/bq-quarantine-replay/main.go

## Setup and usage

No setup information established.

## Limitations and caveats

- Known limitations and misuse: - **Exactly-once.** See delivery semantics above.
- Known limitations and misuse: - **In-exporter aggregation or sampling.** Use the Collector's processors for pre-export aggregation or sampling; the companion rollup views (v_gen_ai_model_costs, v_gen_ai_sessions, v_gen_ai_tool_usage) are SQL views in BigQuery.
- Known limitations and misuse: - **GCS batch LOAD inside bigqueryexporter.** Storage Write API is the single export path (one schema, one exporter); stock OTel googlecloudstorageexporter + cron bq load cannot satisfy the flattened row, insert_id, intra-batch ordinal, or object_refs contracts, and shared-pool LOAD has no SLA under BigQuery's 1,500 jobs/table/day limit (including 
- Known limitations and misuse: Operational limits and common misuse:
- Known limitations and misuse: - **At-least-once delivery and _dedup views.** Appends go through Storage Write API default streams (AppendRows), so transient retries or uncertain acknowledgements can leave duplicate rows in otel_spans, otel_logs, or otel_metrics. Read the companion _dedup views (otel_spans_dedup, otel_logs_dedup, otel_metrics_dedup) whenever query correctness re
- Known limitations and misuse: - **Persistent-queue crash replays.** When sending_queue.storage is enabled, unacknowledged batches replayed from disk after a Collector crash or unclean shutdown can produce duplicates outside the in-process uncertain-ack duplicate bound because batches already committed on the server may be re-read before the queue cursor advances.
- Known limitations and misuse: - **Structural rejections drop rows unless quarantine is enabled.** Records rejected by limits.* bounds (limits.max_attribute_count, limits.max_event_count, limits.max_link_count, limits.max_nesting_depth, limits.max_collection_size, limits.max_attribute_key_bytes, limits.max_value_bytes), serialized row-size bounds (write.max_row_bytes), or server
- Known limitations and misuse: - **Storage Write API quotas, write.stream_pool_size, and BACKGROUND slots.** write.stream_pool_size (1..16, default 1, experimental) opens N default-stream writers per destination signal table (otel_spans, otel_logs, otel_metrics), and quarantine.enabled: true opens a separate client and stream for quarantine.table. Increasing write.stream_pool_si

## Evidence and provenance

- README: https://github.com/GoogleCloudPlatform/BQ-OTEL-Exporter/blob/main/README.md
- README SHA: 78a3f09344d2cc22b6597e9b26c4b8f823320e3b
- Manifests: go.mod, Makefile, example/Dockerfile
- Sampled source files: cmd/bq-otel-backfill/main.go, cmd/bq-otel-testbench/main.go, cmd/bq-otel-validate/main.go, cmd/bq-quarantine-replay/main.go
- Git tree state: captured
- Evidence fingerprint: e3780cd8e2d3f4e903a4bef187ae917bd01a693f182f74e74c6e446bb3794300

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
