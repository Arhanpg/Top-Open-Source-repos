# aws-observability/aws-otel-js-instrumentation

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-js-instrumentation](https://github.com/aws-observability/aws-otel-js-instrumentation)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-js-instrumentation/blob/main/README.md)
- README blob SHA: 2123a43b5ffd6210652273b66e8e1cf9d3e9845f
- Repository ID: 824711236
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:07:43+00:00

### Short excerpt (up to 100 words)

> This project is a redistribution of the OpenTelemetry Auto-Instrumentation for NodeJS, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest. The exception to this is support for Application Signals. We provided a NodeJS agent that can be attached to any application using a supported NodeJS version and dynamically injects bytecode to capture telemetry from a number of popular libraries and frameworks. The telemetry

### README headings

- AWS Distro for OpenTelemetry - Instrumentation for JavaScript
- Introduction
- Getting Started
- Supported NodeJS libraries and frameworks
- Generative AI
- Configuration
- Dynamic Instrumentation
- Support
- Security issue notifications
- License
- Notices
- NodeJS Version Support
- Note on Amazon CloudWatch Application Signals
- Checksum Verification

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 2,753,607 |
| Python | 241,689 |
| JavaScript | 115,445 |
| Rust | 14,031 |
| Shell | 13,104 |
| HCL | 8,850 |
| Dockerfile | 7,495 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- package.json (capture: captured) — dependency clues: @types/mocha, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-config-airbnb-base, eslint-config-prettier, eslint-plugin-header, eslint-plugin-import, eslint-plugin-node, eslint-plugin-prettier, glob, lerna, lerna-changelog, markdownlint-cli2, minimatch, prettier, process, semver, util
- aws-distro-opentelemetry-node-autoinstrumentation/package.json (capture: captured) — dependency clues: @ai-sdk/amazon-bedrock, @ai-sdk/anthropic, @ai-sdk/azure, @ai-sdk/cohere, @ai-sdk/google, @ai-sdk/groq, @ai-sdk/mistral, @ai-sdk/openai, @ai-sdk/xai, @aws-sdk/client-bedrock, @aws-sdk/client-bedrock-agent, @aws-sdk/client-bedrock-agent-runtime, @aws-sdk/client-bedrock-agentcore, @aws-sdk/client-bedrock-runtime, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-kinesis, @aws-sdk/client-lambda, @aws-sdk/client-s3, @aws-sdk/client-secrets-manager, @aws-sdk/client-sfn
- cloudwatch-plugin-otel/package.json (capture: captured) — dependency clues: @grpc/grpc-js, @grpc/proto-loader, @opentelemetry/api, @opentelemetry/auto-instrumentations-node, @opentelemetry/resources, @opentelemetry/sdk-metrics, @opentelemetry/sdk-node, @opentelemetry/sdk-trace-base, @opentelemetry/sdk-trace-node, @testcontainers/kafka, @types/express, @types/mocha, @types/node, @types/sinon, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-config-prettier, eslint-plugin-header, eslint-plugin-node
- docker-utils/package.json (capture: captured) — dependency clues: @types/mocha, @types/node, copyfiles, rimraf, typescript
- lambda-layer/package.json (capture: captured) — dependency clues: bestzip, copyfiles

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 14
- Forks at capture: 28
- Last updated: 2026-11-05T23:43:15Z
- Last pushed: 2026-11-21T20:03:10Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-js-instrumentation)
- [README](https://github.com/aws-observability/aws-otel-js-instrumentation/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-js-instrumentation/issues)
- [Releases](https://github.com/aws-observability/aws-otel-js-instrumentation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
