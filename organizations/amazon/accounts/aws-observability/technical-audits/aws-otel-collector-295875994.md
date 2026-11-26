# aws-observability/aws-otel-collector

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-collector
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T06:57:17+00:00

## Project purpose

AWS Distro for OpenTelemetry Collector (ADOT Collector) is an AWS supported version of the upstream OpenTelemetry Collector and is distributed by Amazon. It supports the selected components from the OpenTelemetry community. It is fully compatible with AWS computing platforms including EC2, ECS, and EKS. It enables users to send telemetry data to AWS CloudWatch Metrics, Traces, and Logs backends as well as the other supported backends.

## Why this project is used

AWS Distro for OpenTelemetry Collector (see ADOT Roadmap at https://github.com/orgs/aws-observability/projects/4)

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Shell, Python, Makefile, PowerShell, Dockerfile, Go Template
- Frameworks/libraries: Unknown / not established
- Dependency names: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute, cloud.google.com/go/compute/metadata, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4, github.com/Azure/go-ansiterm, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/Code-Hex/go-generics-cache, github.com/DataDog/agent-payload/v5, github.com/DataDog/datadog-agent/comp/api/api/def, github.com/DataDog/datadog-agent/comp/core/config, github.com/DataDog/datadog-agent/comp/core/delegatedauth, github.com/DataDog/datadog-agent/comp/core/flare/builder, github.com/DataDog/datadog-agent/comp/core/flare/types, github.com/DataDog/datadog-agent/comp/core/hostname/hostnameinterface, github.com/DataDog/datadog-agent/comp/core/log/def, github.com/DataDog/datadog-agent/comp/core/secrets/def, github.com/DataDog/datadog-agent/comp/core/secrets/noop-impl, github.com/DataDog/datadog-agent/comp/core/status, github.com/DataDog/datadog-agent/comp/core/tagger/def, github.com/DataDog/datadog-agent/comp/core/tagger/origindetection, github.com/DataDog/datadog-agent/comp/core/tagger/types, github.com/DataDog/datadog-agent/comp/core/tagger/utils, github.com/DataDog/datadog-agent/comp/core/telemetry, github.com/DataDog/datadog-agent/comp/def, github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder, github.com/DataDog/datadog-agent/comp/forwarder/orchestrator/orchestratorinterface, github.com/DataDog/datadog-agent/comp/logs-library, github.com/DataDog/datadog-agent/comp/logs/agent/config, github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline, github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/logsagentpipelineimpl, github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/logsagentexporter, github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/serializerexporter, github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/metricsclient, github.com/DataDog/datadog-agent/comp/serializer/logscompression, github.com/DataDog/datadog-agent/comp/serializer/metricscompression, github.com/DataDog/datadog-agent/comp/trace/compression/def, github.com/DataDog/datadog-agent/comp/trace/compression/impl-gzip, github.com/DataDog/datadog-agent/pkg/aggregator/ckey, github.com/DataDog/datadog-agent/pkg/api, github.com/DataDog/datadog-agent/pkg/collector/check/defaults, github.com/DataDog/datadog-agent/pkg/config/basic, github.com/DataDog/datadog-agent/pkg/config/buildschema, github.com/DataDog/datadog-agent/pkg/config/create, github.com/DataDog/datadog-agent/pkg/config/env, github.com/DataDog/datadog-agent/pkg/config/helper, github.com/DataDog/datadog-agent/pkg/config/mock, github.com/DataDog/datadog-agent/pkg/config/model, github.com/DataDog/datadog-agent/pkg/config/nodetreemodel, github.com/DataDog/datadog-agent/pkg/config/setup, github.com/DataDog/datadog-agent/pkg/config/structure, github.com/DataDog/datadog-agent/pkg/config/utils, github.com/DataDog/datadog-agent/pkg/fips, github.com/DataDog/datadog-agent/pkg/logs/client, github.com/DataDog/datadog-agent/pkg/logs/diagnostic, github.com/DataDog/datadog-agent/pkg/logs/message, github.com/DataDog/datadog-agent/pkg/logs/sources, github.com/DataDog/datadog-agent/pkg/logs/status/statusinterface, github.com/DataDog/datadog-agent/pkg/logs/status/utils, github.com/DataDog/datadog-agent/pkg/logs/types, github.com/DataDog/datadog-agent/pkg/metrics, github.com/DataDog/datadog-agent/pkg/obfuscate, github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata, github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes, github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/logs, github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics, github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/rum, github.com/DataDog/datadog-agent/pkg/orchestrator/model, github.com/DataDog/datadog-agent/pkg/orchestrator/util, github.com/DataDog/datadog-agent/pkg/process/util/api, github.com/DataDog/datadog-agent/pkg/proto, github.com/DataDog/datadog-agent/pkg/remoteconfig/state, github.com/DataDog/datadog-agent/pkg/serializer, github.com/DataDog/datadog-agent/pkg/status/health, github.com/DataDog/datadog-agent/pkg/tagger/types, github.com/DataDog/datadog-agent/pkg/tagset, github.com/DataDog/datadog-agent/pkg/template, github.com/DataDog/datadog-agent/pkg/trace, github.com/DataDog/datadog-agent/pkg/trace/log, github.com/DataDog/datadog-agent/pkg/trace/stats, github.com/DataDog/datadog-agent/pkg/trace/traceutil, github.com/DataDog/datadog-agent/pkg/util/backoff, github.com/DataDog/datadog-agent/pkg/util/buf, github.com/DataDog/datadog-agent/pkg/util/cgroups, github.com/DataDog/datadog-agent/pkg/util/compression, github.com/DataDog/datadog-agent/pkg/util/defaultpaths, github.com/DataDog/datadog-agent/pkg/util/executable, github.com/DataDog/datadog-agent/pkg/util/filesystem, github.com/DataDog/datadog-agent/pkg/util/fxutil, github.com/DataDog/datadog-agent/pkg/util/hostname/validate, github.com/DataDog/datadog-agent/pkg/util/hostport, github.com/DataDog/datadog-agent/pkg/util/http, github.com/DataDog/datadog-agent/pkg/util/json, github.com/DataDog/datadog-agent/pkg/util/log, github.com/DataDog/datadog-agent/pkg/util/option, github.com/DataDog/datadog-agent/pkg/util/otel, github.com/DataDog/datadog-agent/pkg/util/pointer, github.com/Microsoft/go-winio, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ecrpublic, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/cenkalti/backoff, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/awscollector/main.go, cmd/healthcheck/main.go, tools/release/image-mirror/main.go, tools/workflow/cleaner/main.go

## Setup and usage

No setup information established.

## Limitations and caveats

- Security issue notifications: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public github issue.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-collector/blob/main/README.md
- README SHA: 69bd44ce18c851c28e7a0bfed5b161af35dc36c4
- Manifests: go.mod, Makefile, testbed/go.mod, testbed/Makefile, cmd/awscollector/Dockerfile, tools/release/image-mirror/go.mod
- Sampled source files: cmd/awscollector/main.go, cmd/healthcheck/main.go, tools/release/image-mirror/main.go, tools/workflow/cleaner/main.go
- Git tree state: captured
- Evidence fingerprint: b6f00c541571df7e9c7427f465de5610279f44cb522477827846f512c8773dd4

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
