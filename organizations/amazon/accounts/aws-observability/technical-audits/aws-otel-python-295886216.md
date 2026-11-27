# aws-observability/aws-otel-python

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-python
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:19:12+00:00

## Project purpose

This repo hosts documentation and sample apps for the ADOT Python library which provides the AWS service integrations for traces and metrics for the OpenTelemetry Python library. The library can be configured to support trace applications with the AWS X-Ray service. This enables all the features of the OpenTelemetry project and configures its components to create traces that can be viewed in the AWS X-Ray console and allow propagation of those contexts across multiple downstream AWS services.

## Why this project is used

AWS Distro for OpenTelemetry Python

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: boto3, flask, opentelemetry-distro, opentelemetry-propagator-aws-xray, opentelemetry-sdk-extension-aws, requests
- Build/package tools: Docker build configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: .github/docker-performance-tests/alarms-poller/metric_data_params.py, .github/docker-performance-tests/alarms-poller/poll_during_performance_tests.py, .github/scripts/performance-tests/get-metric-data/metric_data_params.py, .github/scripts/performance-tests/get-metric-data/produce_performance_test_results.py

## Setup and usage

- Getting Started: Check out the links below for information on getting started with ADOT in Python:
- Getting Started: - Tracing with Automatic Instrumentation
- Getting Started: - Tracing with Manual Instrumentation

## Limitations and caveats

- Security issue notifications: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public github issue.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-python/blob/main/README.md
- README SHA: e77e6c335120120398ea9acd98f9c221a0e32075
- Manifests: .github/docker-performance-tests/alarms-poller/Dockerfile, .github/docker-performance-tests/load-generator/Dockerfile, integration-test-apps/auto-instrumentation/flask/Dockerfile, integration-test-apps/auto-instrumentation/flask/requirements.txt, integration-test-apps/manual-instrumentation/flask/Dockerfile, integration-test-apps/manual-instrumentation/flask/requirements.txt
- Sampled source files: .github/docker-performance-tests/alarms-poller/metric_data_params.py, .github/docker-performance-tests/alarms-poller/poll_during_performance_tests.py, .github/scripts/performance-tests/get-metric-data/metric_data_params.py, .github/scripts/performance-tests/get-metric-data/produce_performance_test_results.py
- Git tree state: captured
- Evidence fingerprint: ce2beda0a9c5a592ea52172aad0786d9342d05052fea69a5d016bc0f7453e029

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
