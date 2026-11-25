# aws/credentials-fetcher

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/credentials-fetcher](https://github.com/aws/credentials-fetcher)
- Default branch: mainline
- README: [Open upstream README](https://github.com/aws/credentials-fetcher/blob/mainline/README.md)
- README blob SHA: 1d0da21a77ad04d5d0c53bcb4813e28c0a4821b0
- README bytes captured: 9431
- README truncated at capture limit: False
- Repository ID: 530317838
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Credentials-fetcher is a Linux daemon that retrieves gMSA credentials from Active Directory over LDAP. It creates and refreshes kerberos tickets from gMSA credentials. Kerberos tickets can be used by containers to run apps/services that authenticate using Active Directory.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:37:22+00:00

### Short excerpt (up to 300 words)

> sudo dnf install -y **Supported Platforms:** Amazon Linux

### README headings

- Credentials Fetcher
- Table of Contents
- Prerequisites
- Install Go
- Install golangci-lint (Optional)
- Install gosec (Optional)
- Add to PATH
- Building from Source
- Quick Build
- Build Options
- Build Flags
- Manual Installation
- Installation
- Installing the latest version of credentials-fetcher
- Verify Installation
- Configuration
- Configuration Options
- Default Configuration (ECS/Fargate/Standalone)
- /etc/credentials-fetcher.conf
- Standalone Non-Domain-Joined with Auto-Renewal
- /etc/credentials-fetcher.conf
- Setting up testing environment
- Setting up gMSA accounts
- Setting up domain credentials to retrieve gMSA password
- Testing
- Quick Test Setup
- Running Tests
- Replace {CREDSPEC_PLACEHOLDER} with your credspec JSON
- Delete lease (replace {LEASE_ID_PLACEHOLDER} with returned lease_id)
- Replace {CREDSPEC_PLACEHOLDER} and {PASSWORD_PLACEHOLDER} with actual values

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install Go

> sudo dnf install -y

### Technology and requirements: Prerequisites

> **Supported Platforms:** Amazon Linux

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 562,388 |
| Shell | 17,648 |
| Python | 4,714 |
| Makefile | 3,740 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/secretsmanager, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/coreos/go-systemd/v22
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 133
- Forks at capture: 36
- Last updated: 2026-11-14T21:07:53Z
- Last pushed: 2026-06-12T17:24:51Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/credentials-fetcher)
- [README](https://github.com/aws/credentials-fetcher/blob/mainline/README.md)
- [Issues](https://github.com/aws/credentials-fetcher/issues)
- [Releases](https://github.com/aws/credentials-fetcher/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
