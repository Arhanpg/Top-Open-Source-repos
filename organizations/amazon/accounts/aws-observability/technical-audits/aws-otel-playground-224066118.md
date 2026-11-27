# aws-observability/aws-otel-playground

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-playground
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:19:40+00:00

## Project purpose

This repository contains a toy application which exhibits a simple yet somewhat representative trace, including AWS SDK calls, a frontend and backend, and HTTP and gRPC.

## Why this project is used

Sample Application for the AWS X-Ray SDK with support for OpenTelemetry

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, HCL, Kotlin
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle Kotlin build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lambda-api/src/main/java/io/awsobservability/opentelemetry/playground/lambdaapi/HelloLambdaHandler.java

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-playground/blob/main/README.md
- README SHA: 6ec2b430b15d7d3b70ef1b7dafab204b57e6e20a
- Manifests: build.gradle.kts, api/build.gradle.kts, appdb/build.gradle.kts, backend-webflux/build.gradle.kts, backend/build.gradle.kts, dependencyManagement/build.gradle.kts
- Sampled source files: lambda-api/src/main/java/io/awsobservability/opentelemetry/playground/lambdaapi/HelloLambdaHandler.java
- Git tree state: captured
- Evidence fingerprint: 0cd5f33757cc4946b1f508713e1519ffe1ddb8c978e61355eb7a3ae8b994be29

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
