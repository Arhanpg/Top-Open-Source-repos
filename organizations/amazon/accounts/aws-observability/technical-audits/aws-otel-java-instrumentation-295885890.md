# aws-observability/aws-otel-java-instrumentation

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-java-instrumentation
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:46:37+00:00

## Project purpose

This project is a redistribution of the OpenTelemetry Agent for Java, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest.

## Why this project is used

AWS Distro for OpenTelemetry Java Instrumentation Library

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Rust, Python, Shell, HCL, Dockerfile, Kotlin
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle Kotlin build file, Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: appsignals-tests/images/grpc/grpc-client/src/main/java/software/amazon/opentelemetry/Main.java, appsignals-tests/images/http-clients/spring-mvc-client/src/main/java/com/amazon/sampleapp/Application.java, appsignals-tests/images/jdbc/src/main/java/software/amazon/opentelemetry/Application.java, cloudwatch-plugin-otel/contract-tests/mock-collector/src/main/java/software/amazon/opentelemetry/cloudwatch/spanmetrics/e2e/mockcollector/Main.java

## Setup and usage

- Getting Started: Check out the getting started documentation.

## Limitations and caveats

- Security issue notifications: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public github issue.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-java-instrumentation/blob/main/README.md
- README SHA: 78178a5ff9c30c68cfda62fa0cdc7e20fceec545
- Manifests: build.gradle.kts, Dockerfile, awsagentprovider/build.gradle.kts, awspropagator/build.gradle.kts, buildSrc/build.gradle.kts, cloudwatch-plugin-otel/build.gradle.kts
- Sampled source files: appsignals-tests/images/grpc/grpc-client/src/main/java/software/amazon/opentelemetry/Main.java, appsignals-tests/images/http-clients/spring-mvc-client/src/main/java/com/amazon/sampleapp/Application.java, appsignals-tests/images/jdbc/src/main/java/software/amazon/opentelemetry/Application.java, cloudwatch-plugin-otel/contract-tests/mock-collector/src/main/java/software/amazon/opentelemetry/cloudwatch/spanmetrics/e2e/mockcollector/Main.java
- Git tree state: captured
- Evidence fingerprint: bc728e147cc5a22260d56c71355e32b55e525ba5c7e43483f846234bcd92a566

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
