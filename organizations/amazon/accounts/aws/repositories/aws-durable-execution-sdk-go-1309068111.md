# aws/aws-durable-execution-sdk-go

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-durable-execution-sdk-go](https://github.com/aws/aws-durable-execution-sdk-go)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-durable-execution-sdk-go/blob/main/README.md)
- README blob SHA: 090126186fee6c0b4386182821a8e1b62e25ac90
- README bytes captured: 61104
- README truncated at capture limit: False
- Repository ID: 1309068111
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Durable Execution SDK for Go

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T21:49:02+00:00

### Short excerpt (up to 300 words)

> examples/ holds one deployable See CONTRIBUTING for information

### README headings

- AWS Durable Execution SDK for Go
- Your first durable function
- The handler and the context
- Determinism
- Goroutines
- Errors
- Operations
- Step
- Pausing from a retry decision (experimental)
- Wait
- Invoke
- WaitForCondition
- Callbacks
- Child contexts
- Retry
- Map and Parallel
- ParallelMixed
- Combinators
- Serialization
- Testing a handler locally
- Logging
- Replayed log records
- Records the SDK writes
- Plugin API
- Deliberate differences from the JavaScript SDK
- Examples
- Versioning
- Go versions
- Feedback & Support
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Examples

> examples/ holds one deployable

### Limitations and security: Security

> See CONTRIBUTING for information

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 3,616,916 |
| Shell | 8,549 |
| Makefile | 440 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/lambda, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go
- Makefile (capture: captured)
- analysis/go.mod (capture: captured) — dependency clues: github.com/golangci/plugin-module-register, golang.org/x/mod, golang.org/x/sync, golang.org/x/tools
- conformance-telemetry/go.mod (capture: captured) — dependency clues: github.com/aws/aws-durable-execution-sdk-go, github.com/aws/aws-durable-execution-sdk-go/telemetry, github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/dynamodb, github.com/aws/aws-sdk-go-v2/service/eventbridge, github.com/aws/aws-sdk-go-v2/service/firehose, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/endpoint-discovery, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared
- conformance/go.mod (capture: captured) — dependency clues: github.com/aws/aws-durable-execution-sdk-go, github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/dynamodb, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/endpoint-discovery, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/lambda, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go
- examples/go.mod (capture: captured) — dependency clues: github.com/aws/aws-durable-execution-sdk-go, github.com/aws/aws-durable-execution-sdk-go/telemetry, github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/dynamodb, github.com/aws/aws-sdk-go-v2/service/eventbridge, github.com/aws/aws-sdk-go-v2/service/firehose, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/endpoint-discovery, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 5
- Last updated: 2026-11-10T23:06:25Z
- Last pushed: 2026-11-23T18:56:19Z
- Topics: aws-lambda, durable-execution, durable-functions, durable-workflows, go, golang, lambda-functions

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-durable-execution-sdk-go)
- [README](https://github.com/aws/aws-durable-execution-sdk-go/blob/main/README.md)
- [Issues](https://github.com/aws/aws-durable-execution-sdk-go/issues)
- [Releases](https://github.com/aws/aws-durable-execution-sdk-go/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
