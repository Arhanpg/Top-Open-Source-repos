# awslabs/node-latency-for-k8s

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/node-latency-for-k8s](https://github.com/awslabs/node-latency-for-k8s)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/node-latency-for-k8s/blob/main/README.md)
- README blob SHA: 3f250d6157d069d68f942c5119306ade0266d5c2
- README bytes captured: 12933
- README truncated at capture limit: False
- Repository ID: 579133904
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The node-latency-for-k8s tool provides process-level telemetry via prometheus metrics, cloudwatch metrics, and markdown timing charts to optimized K8s node launch times.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:26:43+00:00

### Short excerpt (up to 300 words)

> Usage for node-latency-for-k8s: Flags: NLK currently only supports See CONTRIBUTING for more

### README headings

- Node-Latency-for-K8s (NLK)
- Usage:
- Installation
- Prerequisites
- K8s DaemonSet (Helm)
- RPM / Deb / Binary
- Examples:
- Example 1 - Chart
- i-0681ec41ddb32ba4e (192.168.23.248) | c6a.large | x86_64 | us-east-2b | ami-0bf8f0f9cd3cce116
- Example 2 - Prometheus Metrics
- i-0f5a78a8cb71c9ef9 (192.168.147.219) | c6a.large | x86_64 | us-east-2c | ami-0bf8f0f9cd3cce116
- HELP aws_node_start
- TYPE aws_node_start gauge
- HELP cloudinit_config_start
- TYPE cloudinit_config_start gauge
- HELP cloudinit_final_finish
- TYPE cloudinit_final_finish gauge
- HELP cloudinit_final_start
- TYPE cloudinit_final_start gauge
- HELP cloudinit_initial_start
- TYPE cloudinit_initial_start gauge
- HELP conatinerd_initialized
- TYPE conatinerd_initialized gauge
- HELP conatinerd_start
- TYPE conatinerd_start gauge
- HELP instance_pending
- TYPE instance_pending gauge
- HELP instance_requested
- TYPE instance_requested gauge
- HELP kube_proxy_start

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage:

> Usage for node-latency-for-k8s: Flags:

### Technology and requirements: Prerequisites

> NLK currently only supports

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 56,248 |
| Makefile | 4,513 |
| Smarty | 1,912 |
| Shell | 1,538 |
| Dockerfile | 317 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/cloudwatch, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/fxamacker/cbor/v2
- Makefile (capture: captured)
- test/Dockerfile (capture: captured)
- charts/node-latency-for-k8s-chart/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 99
- Forks at capture: 10
- Last updated: 2026-07-10T17:07:42Z
- Last pushed: 2025-10-27T20:12:33Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/node-latency-for-k8s)
- [README](https://github.com/awslabs/node-latency-for-k8s/blob/main/README.md)
- [Issues](https://github.com/awslabs/node-latency-for-k8s/issues)
- [Releases](https://github.com/awslabs/node-latency-for-k8s/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
