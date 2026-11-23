# aws-observability/aws-otel-helm-charts

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-helm-charts](https://github.com/aws-observability/aws-otel-helm-charts)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-helm-charts/blob/main/README.md)
- README blob SHA: 2451bfc6e855360963de87ea532df91b078f7039
- Repository ID: 295886366
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Distro for OpenTelemetry (ADOT) Helm Charts

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:07:35+00:00

### Short excerpt (up to 100 words)

> This AWS Distro for OpenTelemetry (ADOT) Helm Charts repository contains Helm charts to provide easy mechanisms to setup the ADOT Collector and other collection agents to collect telemetry data such as metrics, logs and traces to send to AWS monitoring services. This repository contains a Helm chart to provide easy to operate, end-to-end AWS Elastic Kubernetes Service (EKS) on AWS Elastic Compute Cloud (EC2) monitoring with AWS Distro for OpenTelemetry(ADOT) Collector for metrics. This Helm chart is useful for customers who use EKS on EC2 and want to collect metrics to send to Amazon CloudWatch Container Insights and Amazon Managed

### README headings

- AWS Distro for OpenTelemetry Helm Charts
- :warning: Warning: ADOT Helm Charts is deprecated and the recommended way for users who use EKS on EC2 and want to ingest metrics is using the [ADOT EKS add-on](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on), a wrapper around the OpenTelemetry Operator. By using the respective custom resource configuration you can run it, for example, as a `Deployment` or a `Daemonset`. For details, see this [example of how to use the add-on to ingest metrics into Amazon Managed Service for Prometheus](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on/config-amp).
- Introduction
- Getting Started
- :warning: Warning: Fluent Bit and Fargate logging templates are deprecated and were removed from the Helm chart on December 30th, 2022 (>= 0.11.0)
- Contributing
- License
- ADOT Roadmap
- Support
- Security issue notifications
- Maintainers

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Mustache | 3,109 |
| Shell | 2,417 |
| Makefile | 555 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- charts/adot-exporter-for-eks-on-ec2/Chart.yaml (capture: captured)
- charts/adot-exporter-for-eks-on-ec2/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 48
- Forks at capture: 40
- Last updated: 2026-08-05T00:00:22Z
- Last pushed: 2024-10-30T19:21:20Z
- Topics: adot, aws, helm, helm-charts

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-helm-charts)
- [README](https://github.com/aws-observability/aws-otel-helm-charts/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-helm-charts/issues)
- [Releases](https://github.com/aws-observability/aws-otel-helm-charts/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
