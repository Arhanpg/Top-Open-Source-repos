# aws/aws-emulator

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-emulator](https://github.com/aws/aws-emulator)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-emulator/blob/main/README.md)
- README blob SHA: 0cc5bbf5c3ddf7d6d00ea865f1058226382d110c
- README bytes captured: 8586
- README truncated at capture limit: False
- Repository ID: 1366593263
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Emulator is a local emulator of the AWS APIs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T23:12:51+00:00

### Short excerpt (up to 300 words)

> A Rust toolchain with To see how closely

### README headings

- AWS Emulator README
- Quick start
- With an AI coding agent
- Local process
- Embedded mode
- Known issues
- Building from source
- Prerequisites
- Build and run
- Embedded mode build
- Repository layout
- Telemetry
- Use a command-line option
- Use an environment variable
- Use a configuration file
- Use the embedded configuration API
- Reporting issues and contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Prerequisites

> A Rust toolchain with

### Limitations and security: Known issues

> To see how closely

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 981,696,536 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- core/embedded/Cargo.toml (capture: captured) — dependency clues: aws-emulator-router, aws-smithy-runtime-api, emulator-server, emulator-telemetry, engine, smithy-server-runtime
- core/router/Cargo.toml (capture: captured) — dependency clues: automod, aws-credential-types, aws-sigv4, aws-smithy-runtime-api, aws-smithy-types, bytes, emulator-core-build-support, emulator-server, emulator-telemetry, engine, hex, http, reqwest, rustls, rustls-webpki, serde_json, service-com-amazonaws-accessanalyzer-accessanalyzer, service-com-amazonaws-account-account, service-com-amazonaws-accountaccess-awsaccountaccess, service-com-amazonaws-accountaccessruntime-awsaccountaccessruntime
- services/common/Cargo.toml (capture: captured) — dependency clues: aws-credential-types, aws-lc-rs, aws-sdk-cloudwatchlogs, aws-sdk-dynamodbstreams, aws-sdk-eventbridge, aws-sdk-firehose, aws-sdk-iam, aws-sdk-kinesis, aws-sdk-kms, aws-sdk-organizations, aws-sdk-s3, aws-sdk-sns, aws-sdk-sqs, aws-sdk-ssm, aws-sdk-xray, aws-sigv4, aws-smithy-runtime-api, aws-smithy-schema, aws-smithy-schema-server, aws-smithy-types
- services/service-com-amazonaws-accessanalyzer-accessanalyzer/Cargo.toml (capture: captured) — dependency clues: aws-sdk-cloudtrail, aws-smithy-runtime-api, aws-smithy-schema, aws-smithy-schema-server, aws-smithy-types, bytes, emulator-core-build-support, emulator-server, emulator-telemetry, engine, hex, http, jsonc-parser, percent-encoding, serde_json, service-com-amazonaws-cloudtrail-cloudtrail-20131101, service-com-amazonaws-iam-awsidentitymanagementv20100508, service-com-amazonaws-s3-amazons3, service-com-amazonaws-sqs-amazonsqs, service-common
- services/service-com-amazonaws-account-account/Cargo.toml (capture: captured) — dependency clues: aws-smithy-runtime-api, aws-smithy-schema, aws-smithy-schema-server, aws-smithy-types, bytes, emulator-core-build-support, emulator-server, emulator-telemetry, engine, hex, http, rust_iso3166, serde_json, service-common, sha2, smithy-macros, smithy-server-runtime, tokio, tracing

- Manifest scan truncated by GitHub: True
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: CC0-1.0
- Stars at capture: 9984
- Forks at capture: 494
- Last updated: 2026-11-23T19:17:45Z
- Last pushed: 2026-11-23T15:40:06Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-emulator)
- [README](https://github.com/aws/aws-emulator/blob/main/README.md)
- [Issues](https://github.com/aws/aws-emulator/issues)
- [Releases](https://github.com/aws/aws-emulator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
