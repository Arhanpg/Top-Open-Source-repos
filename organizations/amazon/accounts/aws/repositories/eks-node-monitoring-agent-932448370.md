# aws/eks-node-monitoring-agent

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/eks-node-monitoring-agent](https://github.com/aws/eks-node-monitoring-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/eks-node-monitoring-agent/blob/main/README.md)
- README blob SHA: ebc463182ca12660644b7e25fe1dee8d7c2910d2
- README bytes captured: 7252
- README truncated at capture limit: False
- Repository ID: 932448370
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Agent that detects health issues on Amazon EKS worker nodes

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:53:23+00:00

### Short excerpt (up to 300 words)

> The agent runs as It is recommended to If you discover a

### README headings

- EKS Node Monitoring Agent
- Overview
- Project Layout
- Installation
- Configuring Monitors
- Helm Values
- Config File Format
- Building
- Build the binary
- Run tests
- Build container image
- Running checks on a non-Linux host
- Uses Docker by default; set CONTAINER_TOOL to use finch, podman, etc.
- Contributing
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> The agent runs as

### Getting started and usage: Installation

> It is recommended to

### Limitations and security: Security

> If you discover a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,292,037 |
| Shell | 21,647 |
| Makefile | 16,844 |
| Dockerfile | 6,720 |
| Mustache | 3,778 |
| Python | 3,637 |
| Go Template | 2,480 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/BurntSushi/toml, github.com/Microsoft/go-winio, github.com/NVIDIA/go-dcgm, github.com/NVIDIA/go-nvml, github.com/aws/amazon-vpc-cni-k8s, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/cloudwatch, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/eks, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared
- Makefile (capture: captured)
- charts/eks-node-monitoring-agent/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 99
- Forks at capture: 58
- Last updated: 2026-11-17T21:30:35Z
- Last pushed: 2026-11-23T14:41:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/eks-node-monitoring-agent)
- [README](https://github.com/aws/eks-node-monitoring-agent/blob/main/README.md)
- [Issues](https://github.com/aws/eks-node-monitoring-agent/issues)
- [Releases](https://github.com/aws/eks-node-monitoring-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
