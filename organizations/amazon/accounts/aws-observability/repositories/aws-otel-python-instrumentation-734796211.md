# aws-observability/aws-otel-python-instrumentation

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-python-instrumentation](https://github.com/aws-observability/aws-otel-python-instrumentation)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-python-instrumentation/blob/main/README.md)
- README blob SHA: 1ca9642c193a973d69505b1c4a3caad12b9c3c20
- Repository ID: 734796211
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:14:19+00:00

### Short excerpt (up to 100 words)

> This project is a redistribution of the OpenTelemetry Distro for Python, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest. The exception to this is support for Application Signals. We provided a Python agent that can be attached to any application using a supported Python version and dynamically injects bytecode to capture telemetry from a number of popular libraries and frameworks. The telemetry

### README headings

- AWS Distro for OpenTelemetry - Instrumentation for Python
- Introduction
- Getting Started
- Supported Python libraries and frameworks
- Generative AI
- Configuration
- Support
- Security issue notifications
- License
- Notices
- Python Version Support
- Note on Amazon CloudWatch Application Signals
- Checksum Verification

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 4,458,318 |
| Java | 70,810 |
| Dockerfile | 17,970 |
| Shell | 14,219 |
| Rust | 14,031 |
| HCL | 5,979 |
| JavaScript | 3,001 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured)
- aws-opentelemetry-distro/pyproject.toml (capture: captured) — dependency clues: botocore, bytecode, cachetools, certifi, opentelemetry-api, opentelemetry-distro, opentelemetry-exporter-otlp-proto-common, opentelemetry-exporter-otlp-proto-grpc, opentelemetry-exporter-otlp-proto-http, opentelemetry-instrumentation, opentelemetry-instrumentation-aio-pika, opentelemetry-instrumentation-aiohttp-client, opentelemetry-instrumentation-aiokafka, opentelemetry-instrumentation-aiopg, opentelemetry-instrumentation-asgi, opentelemetry-instrumentation-asyncpg, opentelemetry-instrumentation-aws-lambda, opentelemetry-instrumentation-boto3sqs, opentelemetry-instrumentation-botocore, opentelemetry-instrumentation-cassandra
- cloudwatch-plugin-otel/pyproject.toml (capture: captured) — dependency clues: opentelemetry-api, opentelemetry-instrumentation, opentelemetry-sdk, opentelemetry-semantic-conventions, typing-extensions
- performance-tests/build.gradle.kts (capture: captured)
- contract-tests/tests/pyproject.toml (capture: captured) — dependency clues: docker, grpcio, jsonschema, opentelemetry-proto, opentelemetry-sdk, requests, testcontainers

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 42
- Last updated: 2026-11-12T01:30:40Z
- Last pushed: 2026-11-23T18:41:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-python-instrumentation)
- [README](https://github.com/aws-observability/aws-otel-python-instrumentation/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-python-instrumentation/issues)
- [Releases](https://github.com/aws-observability/aws-otel-python-instrumentation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
