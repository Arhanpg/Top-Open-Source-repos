# awslabs/amazon-ec2-instance-qualifier

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-ec2-instance-qualifier](https://github.com/awslabs/amazon-ec2-instance-qualifier)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-ec2-instance-qualifier/blob/main/README.md)
- README blob SHA: 4c776547d1388172105eefbeabebec2ac8577a83
- Repository ID: 281738336
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CLI tool that automates benchmarking on a range of EC2 instance types.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:43:06+00:00

### Short excerpt (up to 100 words)

> How do users know which EC2 instance types are compatible with their application? Currently, there exists no tooling or baselining of any kind provided by AWS. If a user wants to see which of the 250+ different instance types are acceptable, then the user must spin up each instance type individually and test their application’s performance. Spot users often find themselves asking this question when they are told to utilize as many different instance types as possible in order to reduce the chance of spot interruptions. Still, most users will only ever choose a small subset of what could be

### README headings

- Summary
- Major Features
- Impact to AWS Account
- Configuration
- Examples
- Interpreting Results
- Table Headers
- Building
- Communication
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 193,543 |
| Shell | 29,472 |
| Makefile | 3,837 |
| Dockerfile | 614 |
| HCL | 151 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/mitchellh/go-homedir, github.com/olekukonko/tablewriter, github.com/smartystreets/goconvey, gopkg.in/ini.v1
- Makefile (capture: captured)
- test/app-for-e2e/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/google/uuid
- test/go-report-card-test/Dockerfile (capture: captured)
- test/license-test/Dockerfile (capture: captured)
- test/readme-test/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 6
- Last updated: 2026-05-18T20:29:04Z
- Last pushed: 2021-09-16T21:21:59Z
- Topics: aws, aws-ec2, ec2, ec2-instance, ec2-spot

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-ec2-instance-qualifier)
- [README](https://github.com/awslabs/amazon-ec2-instance-qualifier/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-ec2-instance-qualifier/issues)
- [Releases](https://github.com/awslabs/amazon-ec2-instance-qualifier/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
