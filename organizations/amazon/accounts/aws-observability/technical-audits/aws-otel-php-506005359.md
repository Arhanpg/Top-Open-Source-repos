# aws-observability/aws-otel-php

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-php
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:12:56+00:00

## Project purpose

This repository contains documentation and sample apps for the AWS Distro for OpenTelemetry in PHP. It provides the AWS service integrations for traces for the OpenTelemetry PHP library. The library can be configured to support trace applications with the AWS X-Ray service.

## Why this project is used

AWS Distro for OpenTelemetry PHP

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: PHP, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: aws/aws-sdk-php, aws/aws-sdk-php-symfony, ext-ctype, ext-grpc, ext-iconv, google/protobuf, grpc/grpc, monolog/monolog, open-telemetry/api, open-telemetry/contrib-aws, open-telemetry/exporter-otlp, open-telemetry/sdk, open-telemetry/transport-grpc, php-http/guzzle7-adapter, php-http/message, php-http/message-factory, sensio/framework-extra-bundle, symfony/console, symfony/dotenv, symfony/flex, symfony/framework-bundle, symfony/http-client, symfony/runtime, symfony/yaml
- Build/package tools: Composer manifest, Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: SampleApp/src/Controller/AwsSdkInstrumentationController.php, SampleApp/src/Kernel.php, SampleApp/config/bundles.php, SampleApp/config/preload.php

## Setup and usage

- Getting Started: See the links below for information on getting started with ADOT PHP:
- Getting Started: - ADOT PHP manual instrumentation

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-php/blob/main/README.md
- README SHA: 5a6322cb2791820090fffad0bb560ef6ffbd872e
- Manifests: composer.json, SampleApp/composer.json, SampleApp/Dockerfile
- Sampled source files: SampleApp/src/Controller/AwsSdkInstrumentationController.php, SampleApp/src/Kernel.php, SampleApp/config/bundles.php, SampleApp/config/preload.php
- Git tree state: captured
- Evidence fingerprint: 4742b8cbd8a6104fae9b754dee2b135a00aca917071d072a2e7badb2bff55a94

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
