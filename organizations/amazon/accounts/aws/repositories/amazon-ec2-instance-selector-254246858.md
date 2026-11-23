# aws/amazon-ec2-instance-selector

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ec2-instance-selector](https://github.com/aws/amazon-ec2-instance-selector)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-ec2-instance-selector/blob/main/README.md)
- README blob SHA: 442951eb61b22b89b6c9111f263ade8e9e17cf10
- Repository ID: 254246858
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CLI tool and go library which recommends instance types based on resource criteria like vcpus and memory

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:12+00:00

### Short excerpt (up to 100 words)

> There are over 800 different instance types available on EC2 which can make the process of selecting appropriate instance types difficult. Instance Selector helps you select compatible instance types for your application to run on. The command line interface can be passed resource criteria like vcpus, memory, network performance, and much more and then return the available, matching instance types. If you are using spot instances to save on costs, it is a best practice to use multiple instances types within your auto-scaling group (ASG) to ensure your application doesn't experience downtime due to one instance type being interrupted. Instance

### README headings

- Summary
- Major Features
- Installation and Configuration
- Install w/ Homebrew
- Install w/ Curl for Linux/Mac
- Examples
- CLI
- Go Library
- Building
- Communication
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 352,364 |
| Shell | 39,294 |
| Makefile | 4,335 |
| Dockerfile | 1,025 |
| HCL | 407 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: dario.cat/mergo, github.com/atotto/clipboard, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/pricing, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/aymanbagabas/go-osc52/v2, github.com/blang/semver/v4, github.com/charmbracelet/bubbles
- Makefile (capture: captured)
- test/license-test/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 934
- Forks at capture: 109
- Last updated: 2026-11-19T21:46:21Z
- Last pushed: 2025-12-22T15:45:18Z
- Topics: aws, aws-ec2, ec2, ec2-instance, ec2-spot

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ec2-instance-selector)
- [README](https://github.com/aws/amazon-ec2-instance-selector/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-ec2-instance-selector/issues)
- [Releases](https://github.com/aws/amazon-ec2-instance-selector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
