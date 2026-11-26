# aws-observability/aws-otel-dotnet

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-dotnet
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:13:09+00:00

## Project purpose

This repo hosts documentation and sample apps for the ADOT .NET library which provides the AWS service integrations for traces and metrics for the OpenTelemetry .NET library. The library can be configured to support trace applications with the AWS X-Ray service. This way, all the features of the OpenTelemetry project are available, but its components are configured to create traces which can be viewed in the AWS X-Ray console and are configured to allow propagation of those contexts across multiple downstream AWS services.

## Why this project is used

AWS Distro for OpenTelemetry .NET

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C#, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: .github/docker-performance-tests/alarms-poller/metric_data_params.py, .github/docker-performance-tests/alarms-poller/poll_during_performance_tests.py, .github/scripts/performance-tests/get-metric-data/metric_data_params.py, .github/scripts/performance-tests/get-metric-data/produce_performance_test_results.py

## Setup and usage

- Getting Started: Check out the getting started documentation

## Limitations and caveats

- Security issue notifications: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public github issue.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-dotnet/blob/main/README.md
- README SHA: 248fb8c21e41238a6651ed56258d1307d982c19a
- Manifests: integration-test-app/Dockerfile, .github/docker-performance-tests/alarms-poller/Dockerfile, .github/docker-performance-tests/load-generator/Dockerfile
- Sampled source files: .github/docker-performance-tests/alarms-poller/metric_data_params.py, .github/docker-performance-tests/alarms-poller/poll_during_performance_tests.py, .github/scripts/performance-tests/get-metric-data/metric_data_params.py, .github/scripts/performance-tests/get-metric-data/produce_performance_test_results.py
- Git tree state: captured
- Evidence fingerprint: b673c9b5749956f9814e59bf28237ca981be105251bcea1291b921379bb1086d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
