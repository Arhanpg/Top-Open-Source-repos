# GoogleCloudPlatform/prometheus-engine

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/prometheus-engine](https://github.com/GoogleCloudPlatform/prometheus-engine)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/README.md)
- README blob SHA: 4010f9408d0ef8113f369c912187ce3c5c9cd88b
- README bytes captured: 14369
- README truncated at capture limit: False
- Repository ID: 381500711
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Google Cloud Managed Service for Prometheus libraries and manifests.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T04:56:32+00:00

### Short excerpt (up to 300 words)

> In order to best

### README headings

- Prometheus Engine
- Binaries
- Docker Images
- Deploying Self-Managed Manifests & Custom Resources
- 1. Create namespaces (gmp-system, gmp-public), CRDs, and cluster RBAC:
- 2. Deploy gmp-operator, admission webhooks, and default OperatorConfig:
- 3. (Optional) Deploy standalone rule-evaluator:
- Custom Resource Definitions (CRDs)
- Development
- Repository Layout & Go Modules
- Dependencies
- Then in separate terminal.
- Presubmit, Code Generation & Linting
- Building
- Testing
- Unit
- Kubernetes End-to-end tests
- Or re-run against already-built images:
- GCM integration
- Debugging
- Benchmarking

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Dependencies

> In order to best

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,390,419 |
| Shell | 55,024 |
| JavaScript | 54,418 |
| Dockerfile | 27,439 |
| Makefile | 11,260 |
| Go Template | 10,231 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/monitoring, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/alecthomas/kingpin/v2, github.com/alecthomas/units, github.com/antlr4-go/antlr/v4, github.com/armon/go-metrics, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a
- Makefile (capture: captured)
- hack/Dockerfile (capture: captured)
- charts/datasource-syncer/Chart.yaml (capture: captured)
- charts/inject-gmp-sidecar/Chart.yaml (capture: captured)
- charts/operator/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: True
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 233
- Forks at capture: 113
- Last updated: 2026-11-18T08:21:04Z
- Last pushed: 2026-11-23T20:23:19Z
- Topics: gcp, golang, kubernetes, prometheus

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/prometheus-engine)
- [README](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/prometheus-engine/issues)
- [Releases](https://github.com/GoogleCloudPlatform/prometheus-engine/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
