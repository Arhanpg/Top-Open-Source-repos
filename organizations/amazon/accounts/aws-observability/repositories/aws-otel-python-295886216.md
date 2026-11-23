# aws-observability/aws-otel-python

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-python](https://github.com/aws-observability/aws-otel-python)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-python/blob/main/README.md)
- README blob SHA: e77e6c335120120398ea9acd98f9c221a0e32075
- Repository ID: 295886216
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Distro for OpenTelemetry Python

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:14:17+00:00

### Short excerpt (up to 100 words)

> This repo hosts documentation and sample apps for the ADOT Python library which provides the AWS service integrations for traces and metrics for the OpenTelemetry Python library. The library can be configured to support trace applications with the AWS X-Ray service. This enables all the features of the OpenTelemetry project and configures its components to create traces that can be viewed in the AWS X-Ray console and allow propagation of those contexts across multiple downstream AWS services. OpenTelemetry is a project maintained by the Cloud Native Computing Foundation which provides open source APIs, libraries, and agents to collect distributed traces

### README headings

- AWS Distro for OpenTelemetry Python Language
- How it works
- Getting Started
- Applications for integration testing - Auto-instrumentation (DEPRECATED)
- Applications for integration testing - Manual instrumentation (DEPRECATED)
- Requirements
- Useful Links
- Security issue notifications
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 14,658 |
| Shell | 4,305 |
| Dockerfile | 716 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- .github/docker-performance-tests/alarms-poller/Dockerfile (capture: captured)
- .github/docker-performance-tests/load-generator/Dockerfile (capture: captured)
- integration-test-apps/auto-instrumentation/flask/Dockerfile (capture: captured)
- integration-test-apps/auto-instrumentation/flask/requirements.txt (capture: captured) — dependency clues: boto3, flask, opentelemetry-distro, opentelemetry-propagator-aws-xray, opentelemetry-sdk-extension-aws, requests
- integration-test-apps/manual-instrumentation/flask/Dockerfile (capture: captured)
- integration-test-apps/manual-instrumentation/flask/requirements.txt (capture: captured) — dependency clues: boto3, flask, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 28
- Forks at capture: 20
- Last updated: 2026-11-03T04:19:02Z
- Last pushed: 2026-03-18T21:19:33Z
- Topics: observability, opensource, opentelemetry, opentelemetry-api

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-python)
- [README](https://github.com/aws-observability/aws-otel-python/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-python/issues)
- [Releases](https://github.com/aws-observability/aws-otel-python/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
