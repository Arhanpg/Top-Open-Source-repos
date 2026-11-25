# aws/aws-network-policy-agent

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-network-policy-agent](https://github.com/aws/aws-network-policy-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-network-policy-agent/blob/main/README.md)
- README blob SHA: feb5ac9509c50d939abde6874ff6b33fed5b6433
- README bytes captured: 14015
- README truncated at capture limit: False
- Repository ID: 642985312
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Network Policy Agent is a daemonset that is responsible for enforcing configured network policies on the cluster.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:06:42+00:00

### Short excerpt (up to 300 words)

> You’ll need a Kubernetes This project aims to You need to install If you think you’ve

### README headings

- aws-network-policy-agent
- Getting Started
- Prerequisites
- Setup
- Network Policy Agent Configuration flags
- `enable-network-policy`
- `enable-policy-event-logs`
- `policy-event-logs-scope`
- `enable-cloudwatch-logs`
- `enable-ipv6`
- `log-level`
- `conntrack-cache-cleanup-period` (from v1.0.7+)
- `conntrack-cache-table-size` (from v1.1.3+)
- `enable-tcp-reset-on-deny`
- Network Policy Agent CLI
- Metrics
- Available Metrics
- `network_policy_drop_count_total`
- `network_policy_drop_bytes_total`
- Accessing Metrics
- HELP network_policy_drop_bytes_total Total number of bytes dropped by network policy agent
- TYPE network_policy_drop_bytes_total counter
- HELP network_policy_drop_count_total Total number of packets dropped by network policy agent
- TYPE network_policy_drop_count_total counter
- Contributing
- How it works
- Modifying the API definitions
- License
- Security Disclosures

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Getting Started

> You’ll need a Kubernetes

### Architecture and design: How it works

> This project aims to

### Technology and requirements: Prerequisites

> You need to install

### Limitations and security: Security Disclosures

> If you think you’ve

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,596,654 |
| C | 97,863 |
| Shell | 53,728 |
| Python | 32,142 |
| Makefile | 18,917 |
| Dockerfile | 2,531 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver/v3, github.com/aws/amazon-network-policy-controller-k8s, github.com/aws/amazon-vpc-cni-k8s, github.com/aws/aws-ebpf-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts
- Makefile (capture: captured)
- test/agent/Dockerfile (capture: captured)
- test/agent/go.mod (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 81
- Forks at capture: 79
- Last updated: 2026-11-12T06:20:16Z
- Last pushed: 2026-11-23T18:26:12Z
- Topics: network-policy

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-network-policy-agent)
- [README](https://github.com/aws/aws-network-policy-agent/blob/main/README.md)
- [Issues](https://github.com/aws/aws-network-policy-agent/issues)
- [Releases](https://github.com/aws/aws-network-policy-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
