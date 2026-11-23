# aws-observability/aws-otel-collector

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-collector](https://github.com/aws-observability/aws-otel-collector)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-collector/blob/main/README.md)
- README blob SHA: 69bd44ce18c851c28e7a0bfed5b161af35dc36c4
- Repository ID: 295875994
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Distro for OpenTelemetry Collector (see ADOT Roadmap at https://github.com/orgs/aws-observability/projects/4)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:07:20+00:00

### Short excerpt (up to 100 words)

> AWS Distro for OpenTelemetry Collector (ADOT Collector) is an AWS supported version of the upstream OpenTelemetry Collector and is distributed by Amazon. It supports the selected components from the OpenTelemetry community. It is fully compatible with AWS computing platforms including EC2, ECS, and EKS. It enables users to send telemetry data to AWS CloudWatch Metrics, Traces, and Logs backends as well as the other supported backends. See the AWS Distro for OpenTelemetry documentation for more information. Additionally, the ADOT Collector is now generally available for metrics. Use the community resources below for getting help with the ADOT Collector. * Open

### README headings

- Overview
- Getting Help
- Notice: ADOT Collector Planned Breaking Changes
- ADOT Collector Built-in Components
- Getting Started
- Prerequisites
- ADOT Collector Configuration
- Try out the ADOT Collector
- Build Your Own Artifacts
- Development
- Benchmark
- Support
- Supported Versions
- Security issue notifications
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 171,190 |
| Shell | 48,794 |
| Python | 16,297 |
| Makefile | 11,353 |
| PowerShell | 11,222 |
| Dockerfile | 2,698 |
| Go Template | 1,120 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute, cloud.google.com/go/compute/metadata, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/Code-Hex/go-generics-cache, github.com/DataDog/agent-payload/v5, github.com/DataDog/datadog-agent/comp/api/api/def, github.com/DataDog/datadog-agent/comp/core/config, github.com/DataDog/datadog-agent/comp/core/delegatedauth, github.com/DataDog/datadog-agent/comp/core/flare/builder, github.com/DataDog/datadog-agent/comp/core/flare/types, github.com/DataDog/datadog-agent/comp/core/hostname/hostnameinterface, github.com/DataDog/datadog-agent/comp/core/log/def, github.com/DataDog/datadog-agent/comp/core/secrets/def
- Makefile (capture: captured)
- testbed/go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute, cloud.google.com/go/compute/metadata, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5, github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/Code-Hex/go-generics-cache, github.com/DataDog/agent-payload/v5, github.com/DataDog/datadog-agent/comp/api/api/def, github.com/DataDog/datadog-agent/comp/core/config, github.com/DataDog/datadog-agent/comp/core/delegatedauth, github.com/DataDog/datadog-agent/comp/core/flare/builder, github.com/DataDog/datadog-agent/comp/core/flare/types, github.com/DataDog/datadog-agent/comp/core/hostname/hostnameinterface, github.com/DataDog/datadog-agent/comp/core/log/def, github.com/DataDog/datadog-agent/comp/core/secrets/def
- testbed/Makefile (capture: captured)
- cmd/awscollector/Dockerfile (capture: captured)
- tools/release/image-mirror/go.mod (capture: captured) — dependency clues: github.com/Azure/go-ansiterm, github.com/Microsoft/go-winio, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ecrpublic, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/cenkalti/backoff, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 756
- Forks at capture: 275
- Last updated: 2026-11-23T11:38:17Z
- Last pushed: 2026-11-23T18:45:13Z
- Topics: observability, opensource, opentelemetry, opentelemetry-collector

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-collector)
- [README](https://github.com/aws-observability/aws-otel-collector/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-collector/issues)
- [Releases](https://github.com/aws-observability/aws-otel-collector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
