# aws-samples/amazon-eks-observability-demo

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-observability-demo](https://github.com/aws-samples/amazon-eks-observability-demo)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-observability-demo/blob/main/README.md)
- README blob SHA: 412e730a82dcbe23676cee1c58f525d93c84a041
- README bytes captured: 7198
- README truncated at capture limit: False
- Repository ID: 360066696
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:43:00+00:00

### Short excerpt (up to 300 words)

> cd utils/ Running this project require See CONTRIBUTING for more

### README headings

- Amazon EKS Observability DEMO
- Prerequisites
- Steps
- Set up some environment variables
- The name of EKS cluster to be created
- Region unique export names
- Install Prerequisites for Utility Code
- install prequisites for utility classes
- Create a cluster for this demo
- Create a cluster
- Set up AWS Loadbalancer Controller
- Set up kubeconfig
- Deploy sample applications
- Make sure that the ingress URL can be accessed.
- Set up Amazon CloudWatch Container Insights
- Create a cluster
- Make sure the namespace have been created
- Deploy a cloudwatch-agent in the cluster
- Make sure the cloudwatch-agent have been deployed
- Set up cluster logging using CloudWatch Logs
- Deploy a cloudwatch-agent in the cluster
- Make sure the fluent-bit have been deployed
- Access to the sample app for generating logs
- Set up application tracing using AWS X-Ray
- Deploy a X-Ray agent in the cluster
- Make sure the agent have been deployed
- Restart sample apps for a new DNS info of X-Ray Daemon
- Access to the sample app for generating logs
- Set up CloudWatch agent for Prometheus metrics
- Deploy a cwagent-prometheus in the cluster

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install Prerequisites for Utility Code

> cd utils/

### Technology and requirements: Prerequisites

> Running this project require

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 14,727 |
| Go | 5,130 |
| Dockerfile | 1,741 |
| JavaScript | 1,570 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- base/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-ec2, @aws-cdk/aws-eks, @aws-cdk/aws-iam, @aws-cdk/core, @types/jest, @types/js-yaml, @types/node, aws-cdk, eks-cdk-utils, jest, js-yaml, source-map-support, ts-jest, ts-node, typescript
- observability/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-ec2, @aws-cdk/aws-eks, @aws-cdk/aws-iam, @aws-cdk/core, @types/jest, @types/node, aws-cdk, eks-cdk-utils, jest, js-yaml, source-map-support, ts-jest, ts-node, typescript
- utils/package.json (capture: captured) — dependency clues: @aws-cdk/aws-eks, @aws-cdk/core, @types/axios, @types/js-yaml, @types/node, js-yaml, source-map-support, ts-node, typescript
- apps/simple-backend/Dockerfile (capture: captured)
- apps/simple-backend/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/aws/aws-xray-sdk-go, github.com/cihub/seelog, github.com/jmespath/go-jmespath, github.com/pkg/errors
- apps/simple-frontend-otel/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 10
- Forks at capture: 4
- Last updated: 2025-05-11T09:33:49Z
- Last pushed: 2023-10-11T21:11:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-observability-demo)
- [README](https://github.com/aws-samples/amazon-eks-observability-demo/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-observability-demo/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-observability-demo/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
