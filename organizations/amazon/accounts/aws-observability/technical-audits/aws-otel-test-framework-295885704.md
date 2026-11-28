# aws-observability/aws-otel-test-framework

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-test-framework
- Default branch: terraform
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:50:33+00:00

## Project purpose

Before adding a new component into ADOT Collector, we require contributors to add related end-to-end test cases, this project is a testing framework which helps contributors to easily add testing into AWS Otel Collector.

## Why this project is used

AWS Distro for OpenTelemetry Test Framework

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, HCL, Smarty, Go, Mustache, TypeScript, Shell, Dockerfile, Makefile, Python, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-cdk/aws-ec2, @aws-cdk/aws-eks, @aws-cdk/aws-iam, @aws-cdk/core, @aws-cdk/lambda-layer-kubectl, @aws-cdk/lambda-layer-kubectl-v29, @aws-cdk/lambda-layer-kubectl-v30, @aws-cdk/lambda-layer-kubectl-v31, @aws-cdk/lambda-layer-kubectl-v32, @aws-cdk/lambda-layer-kubectl-v33, @aws-cdk/lambda-layer-kubectl-v34, @types/jest, @types/js-yaml, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, ajv, ajv-errors, aws-cdk, aws-cdk-lib, constructs, eslint, jest, js-yaml, prettier, source-map-support, ts-jest, ts-node, typescript, yaml-schema-validator
- Build/package tools: Gradle build file, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cdk_infra/lib/app.ts, cmd/aotutil/main.go, mocked_servers/grpc_metrics/main.go, mocked_servers/grpc_trace/main.go

## Setup and usage

No setup information established.

## Limitations and caveats

- 1.2.2 platforms: platforms are the platforms the test case will be running on. We require all the platforms to be listed unless you have a special reason to skip some of the platforms. An example for otlp_http_exporter_trace_mock Below are the platforms:
- 1.2.2 platforms: * LOCAL, which will run the test in the pr workflow, the test will be directly running on the github workflow vm.
- 1.2.2 platforms: * EC2, which will run the test in the main branch workflow under an ec2 instance.
- 1.2.2 platforms: * ECS, which will run the test in the main branch workflow under an ecs cluster.
- 1.2.2 platforms: * EKS, which will run the test in the main branch workflow under an eks/k8s cluster.
- 1.2.2 platforms: * SOAKING, which will run every night, and perform high throughput to your test case and monitor the resource usages.
- 1.2.2 platforms: * NEG_SOAKING, which will run every night, and perform high throughput to your test case with false endpoint and monitor the resource usages.
- 1.2.2 platforms: * CANARY, which will run hourly, and test against the latest released version of aoc.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-test-framework/blob/terraform/README.md
- README SHA: 49bbe8d0c98119f449485615bebab09709e31970
- Manifests: build.gradle, Makefile, cdk_infra/Makefile, cdk_infra/package.json, load-generator/build.gradle, terraform/Makefile
- Sampled source files: cdk_infra/lib/app.ts, cmd/aotutil/main.go, mocked_servers/grpc_metrics/main.go, mocked_servers/grpc_trace/main.go
- Git tree state: captured
- Evidence fingerprint: 8f66cb275c703c9c42da23762c38908a2a9ded993100d118eb492477b611f9a9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
