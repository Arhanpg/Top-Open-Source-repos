# aws/aws-lambda-rust-runtime

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-lambda-rust-runtime](https://github.com/aws/aws-lambda-rust-runtime)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-lambda-rust-runtime/blob/main/README.md)
- README blob SHA: 7b0cc9438bc4190ce6a13b416f0fdab6c9eeb219
- README bytes captured: 24796
- README truncated at capture limit: False
- Repository ID: 156752158
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Rust runtime for AWS Lambda

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T02:50:34+00:00

### Short excerpt (up to 300 words)

> The easiest way to See CONTRIBUTING for more

### README headings

- Rust Runtime for AWS Lambda
- Getting started
- Your first function
- Example function
- Understanding Lambda errors
- Implement your own Diagnostic
- Anyhow, Eyre, and Miette
- Graceful shutdown
- Building and deploying your Lambda functions
- CPU jitter entropy and cold starts
- 1. Cross-compiling your Lambda functions
- 1.1. Build your Lambda functions
- 2. Deploying the binary to AWS Lambda
- 2.1. Deploying with Cargo Lambda
- 2.2. Deploying with the AWS CLI
- 2.3. AWS Serverless Application Model (SAM)
- Local development and testing
- Testing your code with unit and integration tests
- Local dev server with Cargo Lambda
- Local testing with Runtime Interface Emulator (RIE)
- Dockerized test harness
- Lambda Debug Proxy
- Tracing and Logging
- AWS event objects
- Builder pattern for event responses
- Custom event objects
- Supported Rust Versions (MSRV)
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Getting started

> The easiest way to

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 1,128,668 |
| Makefile | 10,685 |
| Shell | 4,012 |
| Python | 2,914 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Makefile (capture: captured)
- lambda-events/Cargo.toml (capture: captured) — dependency clues: base64, bon, bytes, chrono, flate2, http, http-body, http-serde, lambda_runtime, query_map, serde, serde_dynamo, serde_json, serde_with
- lambda-extension/Cargo.toml (capture: captured) — dependency clues: async-stream, chrono, http, http-body-util, hyper, hyper-util, lambda_runtime_api_client, serde, serde_json, tokio, tokio-stream, tower, tracing
- lambda-http/Cargo.toml (capture: captured) — dependency clues: aws_lambda_events, axum-core, axum-extra, bytes, encoding_rs, futures-util, http, http-body, http-body-util, hyper, lambda_runtime, lambda_runtime_api_client, log, maplit, mime, percent-encoding, pin-project-lite, serde, serde_json, serde_urlencoded
- lambda-integration-tests/Cargo.toml (capture: captured) — dependency clues: aws_lambda_events, lambda_runtime, reqwest, serde, serde_json, tokio, tracing

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3622
- Forks at capture: 403
- Last updated: 2026-11-19T21:09:53Z
- Last pushed: 2026-10-26T08:35:12Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-lambda-rust-runtime)
- [README](https://github.com/aws/aws-lambda-rust-runtime/blob/main/README.md)
- [Issues](https://github.com/aws/aws-lambda-rust-runtime/issues)
- [Releases](https://github.com/aws/aws-lambda-rust-runtime/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
