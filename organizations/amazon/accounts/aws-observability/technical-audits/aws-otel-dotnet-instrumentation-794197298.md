# aws-observability/aws-otel-dotnet-instrumentation

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-dotnet-instrumentation
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:20:47+00:00

## Project purpose

This project is a redistribution of the OpenTelemetry Agent for DotNet, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest.

## Why this project is used

This project is a redistribution of the OpenTelemetry Agent for DotNet, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C#, JavaScript, Python, Shell, Rust, Dockerfile, PowerShell, HCL, HTML, Batchfile, CSS, ASP.NET
- Frameworks/libraries: Unknown / not established
- Dependency names: docker, grpcio, mock-collector, opentelemetry-proto, opentelemetry-sdk, requests, tempfile, testcontainers, uuid
- Build/package tools: Cargo manifest, Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: tools/cp-utility/src/main.rs, sample-applications/lambda-test-apps/SimpleLambdaFunction/src/SimpleLambdaFunction/Function.cs, src/AWS.Distro.OpenTelemetry.AutoInstrumentation/AdaptiveSampler.cs, src/AWS.Distro.OpenTelemetry.AutoInstrumentation/AdaptiveSamplingConfig.cs

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-dotnet-instrumentation/blob/main/README.md
- README SHA: 0f04e5dc962b8ac74fb5a162f1d9c4dd4a139530
- Manifests: sample-applications/integration-test-app/Dockerfile, sample-applications/udp-exporter-test-app/Dockerfile, tools/cp-utility/Cargo.toml, test/contract-tests/tests/pyproject.toml, test/images/MockCollector/Dockerfile, test/contract-tests/images/mock-collector/Dockerfile
- Sampled source files: tools/cp-utility/src/main.rs, sample-applications/lambda-test-apps/SimpleLambdaFunction/src/SimpleLambdaFunction/Function.cs, src/AWS.Distro.OpenTelemetry.AutoInstrumentation/AdaptiveSampler.cs, src/AWS.Distro.OpenTelemetry.AutoInstrumentation/AdaptiveSamplingConfig.cs
- Git tree state: captured
- Evidence fingerprint: 7e3ef70adafe03e6d40b527111deefa3e3956220e8cf475af78d0709623d143d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
