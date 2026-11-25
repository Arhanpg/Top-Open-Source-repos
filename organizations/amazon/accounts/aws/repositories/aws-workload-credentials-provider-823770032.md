# aws/aws-workload-credentials-provider

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-workload-credentials-provider](https://github.com/aws/aws-workload-credentials-provider)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-workload-credentials-provider/blob/main/README.md)
- README blob SHA: a6c02476ccd569ac8944387d3a40d282e7a64ee8
- README bytes captured: 88282
- README truncated at capture limit: False
- Repository ID: 823770032
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The AWS Workload Credentials Provider (formerly the AWS Secrets Manager Agent) is a client-side solution that helps you standardize how you consume credentials from AWS services across your compute environments.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T18:55:21+00:00

### Short excerpt (up to 300 words)

> The Workload Credentials Provider The bootstrap installers download RUN apt-get update && The session token gate

### README headings

- AWS Workload Credentials Provider
- Secrets Manager capability
- Certificate Management capability
- Quick install<a name="workload-credentials-provider-quick-install"></a>
- [ Linux quick install ]
- [ Windows quick install ]
- Step 1: Build the Workload Credentials Provider binary<a name="workload-credentials-provider-build"></a>
- [ RPM\-based systems ]
- [ Debian\-based systems ]
- [ Windows ]
- [ Cross\-compile natively ]
- Install clang
- Install cargo-xwin
- Install the Rust build target
- Cross compile for Windows
- Step 2: Install the Workload Credentials Provider<a name="workload-credentials-provider-install"></a>
- [ Amazon EC2 (Linux) ]
- [ Windows EC2 ]
- [ Running as a Secrets Manager Sidecar ]
- [ Running as a Certificate Manager Sidecar ]
- escape=`
- nginx only — for another TLS server, copy its config instead
- Required, no default — must match the certificate's watcher_id in config.toml
- [ AWS Lambda ]
- Step 3: Retrieve secrets with the Workload Credentials Provider<a name="workload-credentials-provider-call"></a>
- [ curl ]
- [ Python ]
- Function that fetches the secret from Workload Credentials Provider for the provided secret id.
- `refreshNow` parameter behavior
- Using the refreshNow parameter

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Secrets Manager capability

> The Workload Credentials Provider

### Getting started and usage: Quick install<a name="workload-credentials-provider-quick-install"></a>

> The bootstrap installers download

### Technology and requirements: Install any necessary dependencies

> RUN apt-get update &&

### Limitations and security: Security

> The session token gate

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 1,429,238 |
| PowerShell | 70,614 |
| Shell | 23,326 |
| Dockerfile | 391 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Dockerfile (capture: captured)
- aws_certificatemanager_provider/Cargo.toml (capture: captured) — dependency clues: aws-config, aws-credential-types, aws-lc-rs, aws-sdk-acm, aws-smithy-mocks, aws-smithy-runtime, aws-smithy-runtime-api, aws-smithy-types, aws_workload_credentials_provider_common, base64ct, http, log, pkcs5, pkcs8, rand_core, serde_json, tempfile, thiserror, tokio, tokio-util
- aws_secretsmanager_caching/Cargo.toml (capture: captured) — dependency clues: aws-config, aws-sdk-secretsmanager, aws-smithy-mocks, aws-smithy-runtime, aws-smithy-runtime-api, aws-smithy-types, criterion, http, linked-hash-map, log, rand, rustls, serde, serde_json, serde_with, thiserror, tokio, tokio-test
- aws_secretsmanager_provider/Cargo.toml (capture: captured) — dependency clues: arc-swap, aws-config, aws-credential-types, aws-runtime, aws-sdk-secretsmanager, aws-sdk-sts, aws-smithy-runtime, aws-smithy-runtime-api, aws-smithy-types, aws_secretsmanager_caching, aws_workload_credentials_provider_common, bytes, http, http-body-util, hyper, hyper-util, log, log4rs, rand, regex
- aws_workload_credentials_provider/Cargo.toml (capture: captured) — dependency clues: aws_certificatemanager_provider, aws_secretsmanager_provider, aws_workload_credentials_provider_common, clap, log, log4rs, tokio-util

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 709
- Forks at capture: 46
- Last updated: 2026-11-19T23:18:24Z
- Last pushed: 2026-11-18T04:51:47Z
- Topics: acm, agent, aws, aws-certificate-manager, aws-secrets-manager, caching, certificates, rust, secretsmanager

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-workload-credentials-provider)
- [README](https://github.com/aws/aws-workload-credentials-provider/blob/main/README.md)
- [Issues](https://github.com/aws/aws-workload-credentials-provider/issues)
- [Releases](https://github.com/aws/aws-workload-credentials-provider/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
