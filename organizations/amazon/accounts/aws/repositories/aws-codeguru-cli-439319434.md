# aws/aws-codeguru-cli

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-codeguru-cli](https://github.com/aws/aws-codeguru-cli)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-codeguru-cli/blob/main/README.md)
- README blob SHA: a7a923235bbf58503f0a8c0a97f17eace118b4b4
- README bytes captured: 9851
- README truncated at capture limit: False
- Repository ID: 439319434
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Command line wrapper to interact with CodeGuru Reviewer

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T19:59:40+00:00

### Short excerpt (up to 300 words)

> To run the CLI, See CONTRIBUTING for more

### README headings

- CodeGuru Reviewer CLI Wrapper
- Table of Contents
- Installation
- Prerequisites
- Using the CLI
- Scan an Example
- Using Encryption
- Suppressing Recommendations
- The CodeGuru Reviewer CLI produces a recommendations.json file which contains deterministic IDs for each
- recommendation. This ID can be excluded so that this recommendation will not be reported in future runs of the
- CLI.
- We can tell the CLI to exclude all recommendations below a certain severity. This can be useful in CI/CD integration.
- We can exclude all recommendations that have a certain tag. Available Tags can be found here:
- https://docs.aws.amazon.com/codeguru/detector-library/java/tags/
- https://docs.aws.amazon.com/codeguru/detector-library/python/tags/
- We can also exclude recommendations by Detector ID. Detector IDs can be found here:
- https://docs.aws.amazon.com/codeguru/detector-library
- Ignore all recommendations for a given Detector ID
- Ignore all recommendations for a given Detector ID in a provided set of locations.
- Locations can be written as Unix GLOB expressions using wildcard symbols.
- Excludes all recommendations in the provided files. Files can be provided as Unix GLOB expressions.
- Running from CI/CD
- Build from Source
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Prerequisites

> To run the CLI,

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 152,562 |
| Shell | 63,732 |
| Perl | 13,308 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 23
- Forks at capture: 16
- Last updated: 2025-02-07T01:43:50Z
- Last pushed: 2026-11-13T19:53:18Z
- Topics: aws, static-analysis

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-codeguru-cli)
- [README](https://github.com/aws/aws-codeguru-cli/blob/main/README.md)
- [Issues](https://github.com/aws/aws-codeguru-cli/issues)
- [Releases](https://github.com/aws/aws-codeguru-cli/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
