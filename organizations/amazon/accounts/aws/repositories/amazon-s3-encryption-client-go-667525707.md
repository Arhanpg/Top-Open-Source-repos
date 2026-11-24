# aws/amazon-s3-encryption-client-go

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-s3-encryption-client-go](https://github.com/aws/amazon-s3-encryption-client-go)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-s3-encryption-client-go/blob/main/README.md)
- README blob SHA: 7297935c7ae49338e38f3940e912e95c55cba5fe
- README bytes captured: 4567
- README truncated at capture limit: False
- Repository ID: 667525707
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Amazon S3 Encryption Client is a client-side encryption library that enables you to encrypt an object locally to ensure its security before passing it to Amazon Simple Storage Service (Amazon S3).

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T04:27:18+00:00

### Short excerpt (up to 300 words)

> To get started working $ go get github.com/aws/amazon-s3-encryption-client-go/v4 The v4 Encryption Client

### README headings

- Amazon S3 Encryption Client for Go V4
- Maintenance and support for SDK major versions
- Go version support policy
- Getting started
- Initialize Project
- Add SDK Dependencies
- Write Code
- Migration
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Getting started

> To get started working

### Technology and requirements: Add SDK Dependencies

> $ go get github.com/aws/amazon-s3-encryption-client-go/v4

### Limitations and security: Go version support policy

> The v4 Encryption Client

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 820,802 |
| TypeScript | 3,760 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- cdk/package.json (capture: captured) — dependency clues: @types/node, aws-cdk, aws-cdk-lib, constructs, source-map-support, ts-node, typescript
- v3/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/kms, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go
- v4/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/kms, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go
- v3/testvectors/go.mod (capture: captured) — dependency clues: github.com/aws/amazon-s3-encryption-client-go/v3, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/kms, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts
- v4/testvectors/go.mod (capture: captured) — dependency clues: github.com/aws/amazon-s3-encryption-client-go/v4, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/kms, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts
- examples/migration/v3-to-v4/go.mod (capture: captured) — dependency clues: github.com/aws/amazon-s3-encryption-client-go/v3, github.com/aws/amazon-s3-encryption-client-go/v4, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/kms, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 22
- Forks at capture: 6
- Last updated: 2026-10-06T17:22:08Z
- Last pushed: 2026-11-16T19:30:56Z
- Topics: amazon-s3, aws, aws-kms, client-side-encryption, encryption, golang

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-s3-encryption-client-go)
- [README](https://github.com/aws/amazon-s3-encryption-client-go/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-s3-encryption-client-go/issues)
- [Releases](https://github.com/aws/amazon-s3-encryption-client-go/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
