# aws-observability/aws-otel-js-instrumentation

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-js-instrumentation
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T06:59:21+00:00

## Project purpose

This project is a redistribution of the OpenTelemetry Auto-Instrumentation for NodeJS, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest. The exception to this is support for Application Signals.

## Why this project is used

This project is a redistribution of the OpenTelemetry Auto-Instrumentation for NodeJS, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest. The exception to this is support for Application Signals.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Python, JavaScript, Rust, Shell, HCL, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @ai-sdk/amazon-bedrock, @ai-sdk/anthropic, @ai-sdk/azure, @ai-sdk/cohere, @ai-sdk/google, @ai-sdk/groq, @ai-sdk/mistral, @ai-sdk/openai, @ai-sdk/xai, @aws-sdk/client-bedrock, @aws-sdk/client-bedrock-agent, @aws-sdk/client-bedrock-agent-runtime, @aws-sdk/client-bedrock-agentcore, @aws-sdk/client-bedrock-runtime, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-kinesis, @aws-sdk/client-lambda, @aws-sdk/client-s3, @aws-sdk/client-secrets-manager, @aws-sdk/client-sfn, @aws-sdk/client-sns, @aws-sdk/client-sts, @grpc/grpc-js, @grpc/proto-loader, @jridgewell/trace-mapping, @langchain/anthropic, @langchain/aws, @langchain/cohere, @langchain/core, @langchain/deepseek, @langchain/google-genai, @langchain/groq, @langchain/langgraph, @langchain/mistralai, @langchain/openai, @langchain/xai, @openai/agents, @openai/agents-extensions, @opentelemetry/api, @opentelemetry/api-logs, @opentelemetry/auto-configuration-propagators, @opentelemetry/auto-instrumentations-node, @opentelemetry/baggage-span-processor, @opentelemetry/contrib-test-utils, @opentelemetry/core, @opentelemetry/exporter-logs-otlp-grpc, @opentelemetry/exporter-logs-otlp-http, @opentelemetry/exporter-logs-otlp-proto, @opentelemetry/exporter-metrics-otlp-grpc, @opentelemetry/exporter-metrics-otlp-http, @opentelemetry/exporter-metrics-otlp-proto, @opentelemetry/exporter-prometheus, @opentelemetry/exporter-trace-otlp-proto, @opentelemetry/exporter-zipkin, @opentelemetry/id-generator-aws-xray, @opentelemetry/instrumentation, @opentelemetry/instrumentation-aws-sdk, @opentelemetry/otlp-transformer, @opentelemetry/propagator-aws-xray, @opentelemetry/resource-detector-aws, @opentelemetry/resources, @opentelemetry/sdk-logs, @opentelemetry/sdk-metrics, @opentelemetry/sdk-node, @opentelemetry/sdk-trace-base, @opentelemetry/sdk-trace-node, @opentelemetry/semantic-conventions, @smithy/node-http-handler, @smithy/protocol-http, @smithy/signature-v4, @testcontainers/kafka, @types/express, @types/mocha, @types/node, @types/proxyquire, @types/sinon, @types/uuid, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, acorn, ai, ajv, bestzip, copyfiles, eslint, eslint-config-airbnb-base, eslint-config-prettier, eslint-plugin-header, eslint-plugin-import, eslint-plugin-node, eslint-plugin-prettier, expect, express, glob, kafkajs, lerna, lerna-changelog, markdownlint-cli2, minimatch, mocha, nock, node-fetch, nyc, pg, pirates, prettier, process, proxyquire, rimraf, rotating-file-stream, semver, sinon, test-all-versions, testcontainers, ts-mocha, typescript, util, uuid, zod
- Build/package tools: Docker build configuration, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: aws-distro-opentelemetry-node-autoinstrumentation/src/dynamic-instrumentation/index.ts, aws-distro-opentelemetry-node-autoinstrumentation/src/serviceevents/collectors/index.ts, aws-distro-opentelemetry-node-autoinstrumentation/src/serviceevents/exporter/index.ts, aws-distro-opentelemetry-node-autoinstrumentation/src/serviceevents/index.ts

## Setup and usage

- Getting Started: The official AWS Documentation for getting started with ADOT JS Auto-Instrumentation is under construction.
- Getting Started: Meanwhile, check out the getting started documentation for manual instrumentation.

## Limitations and caveats

- Security issue notifications: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public github issue.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-js-instrumentation/blob/main/README.md
- README SHA: 2123a43b5ffd6210652273b66e8e1cf9d3e9845f
- Manifests: Dockerfile, package.json, aws-distro-opentelemetry-node-autoinstrumentation/package.json, cloudwatch-plugin-otel/package.json, docker-utils/package.json, lambda-layer/package.json
- Sampled source files: aws-distro-opentelemetry-node-autoinstrumentation/src/dynamic-instrumentation/index.ts, aws-distro-opentelemetry-node-autoinstrumentation/src/serviceevents/collectors/index.ts, aws-distro-opentelemetry-node-autoinstrumentation/src/serviceevents/exporter/index.ts, aws-distro-opentelemetry-node-autoinstrumentation/src/serviceevents/index.ts
- Git tree state: captured
- Evidence fingerprint: 8e5cc1aeefd362bfaa0086f8c918d24740c75013a2578634e8f54137506ba201

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
