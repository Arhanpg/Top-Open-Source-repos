# awslabs/disaster-recovery-for-aws-iot

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/disaster-recovery-for-aws-iot](https://github.com/awslabs/disaster-recovery-for-aws-iot)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/disaster-recovery-for-aws-iot/blob/main/README.md)
- README blob SHA: 14c9b99c6c090755b5f10da263e567c9c6a99694
- README bytes captured: 11665
- README truncated at capture limit: False
- Repository ID: 353833067
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This solution provides a failover strategy for your IoT devices. Customers with critical AWS IoT Core workloads can use this solution to store and process their data in a second AWS Region if the primary Region is not available.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:17:03+00:00

### Short excerpt (up to 300 words)

> Use a quickstart link To create device certificates This AWS Solution has

### README headings

- Deprecation Notice
- Disaster Recovery for AWS IoT
- Architecture
- Launch the solution
- Prepare AWS CloudShell
- Configure
- Create S3 buckets
- Clone the repository
- Prepare artifacts
- Make the build script executable
- Build
- Copy artifacts to S3
- TEMPLATES
- PRIMARY_REGION
- SECONDARY_REGION
- Registry events and fleet indexing
- Registry events
- Fleet indexing
- Quickstart link
- Testing
- All at once

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quickstart link

> Use a quickstart link

### Architecture and design: Architecture

> To create device certificates

### Limitations and security: Deprecation Notice

> This AWS Solution has

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 176,804 |
| Shell | 47,456 |
| Jupyter Notebook | 44,702 |
| Dockerfile | 311 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/tools/requirements.txt (capture: captured) — dependency clues: awsiotsdk, dnspython
- source/lambda/iot-dr-layer/requirements.txt (capture: captured) — dependency clues: dynamodb-json
- source/lambda/iot-dr-r53-health-check/requirements.txt (capture: captured) — dependency clues: awsiotsdk
- source/lambda/iot-dr-region-syncer/Dockerfile (capture: captured)
- source/lambda/iot-dr-region-syncer/requirements.txt (capture: captured) — dependency clues: boto3, dynamodb-json

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 19
- Forks at capture: 6
- Last updated: 2026-04-13T23:03:38Z
- Last pushed: 2023-07-28T15:35:50Z
- Topics: amazon-route53, aws-cloud, aws-iot-core, disaster-recovery, iot

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/disaster-recovery-for-aws-iot)
- [README](https://github.com/awslabs/disaster-recovery-for-aws-iot/blob/main/README.md)
- [Issues](https://github.com/awslabs/disaster-recovery-for-aws-iot/issues)
- [Releases](https://github.com/awslabs/disaster-recovery-for-aws-iot/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
