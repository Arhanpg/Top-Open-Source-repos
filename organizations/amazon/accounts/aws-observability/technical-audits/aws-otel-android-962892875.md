# aws-observability/aws-otel-android

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-android
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:08:58+00:00

## Project purpose

This repo contains the AWS Distro for OpenTelemetry (ADOT) on Android. It is a bundle that ships a few things out of the box: 1. OpenTelemetry Java SDK (https://github.com/open-telemetry/opentelemetry-java) 2. OpenTelemetry Android automated instrumentation (https://github.com/open-telemetry/opentelemetry-android) 4. Additional automated instrumentation not currently part of upstream OpenTelemetry Android, like the "Time to first draw" telemetry 5. AWS-specific exporter and auth configuration that works out of the box when exporting telemetry to AWS CloudWatch Real User Monitoring (RUM)

## Why this project is used

This repo contains the AWS Distro for OpenTelemetry (ADOT) on Android. It is a bundle that ships a few things out of the box: 1. OpenTelemetry Java SDK (https://github.com/open-telemetry/opentelemetry-java) 2. OpenTelemetry Android automated instrumentation (https://github.com/open-telemetry/opentelemetry-android) 4. Additional automated instrumentation not currently part of upstream OpenTelemetry Android, like the "Time to first draw" telemetry 5. AWS-specific exporter and auth configuration that works out of the box when exporting telemetry to AWS CloudWatch Real User Monitoring (RUM)

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Kotlin, Shell, JavaScript, Java, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle Kotlin build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: tools/contract-test-endpoint/server.js, agent/src/main/kotlin/software/amazon/opentelemetry/android/agent/AwsConfigReader.kt, agent/src/main/kotlin/software/amazon/opentelemetry/android/agent/RumAgentProvider.kt, aws-runtime/kotlin-sdk-auth/src/main/kotlin/software/amazon/opentelemetry/android/auth/kotlin/AwsRequestSigner.kt

## Setup and usage

No setup information established.

## Limitations and caveats

- Security issue notifications: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public github issue.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-android/blob/main/README.md
- README SHA: 2e503da3bc5b3aa6e120e434d9ad8470495fe39c
- Manifests: build.gradle.kts, agent/build.gradle.kts, buildSrc/build.gradle.kts, common/build.gradle.kts, core/build.gradle.kts, ui-loading/build.gradle.kts
- Sampled source files: tools/contract-test-endpoint/server.js, agent/src/main/kotlin/software/amazon/opentelemetry/android/agent/AwsConfigReader.kt, agent/src/main/kotlin/software/amazon/opentelemetry/android/agent/RumAgentProvider.kt, aws-runtime/kotlin-sdk-auth/src/main/kotlin/software/amazon/opentelemetry/android/auth/kotlin/AwsRequestSigner.kt
- Git tree state: captured
- Evidence fingerprint: 979a78e8c3fdb8ab122b8621add0009ec15cd0b78ca01ca9888c08eb5b1ef345

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
