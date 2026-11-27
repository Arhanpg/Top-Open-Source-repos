# aws-samples/amazon-redshift-data-lifecycle-manager

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-redshift-data-lifecycle-manager](https://github.com/aws-samples/amazon-redshift-data-lifecycle-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-redshift-data-lifecycle-manager/blob/main/README.md)
- README blob SHA: 7c6a09bf36bc69ccf5b7f7b3978c63fe906dc998
- README bytes captured: 19284
- README truncated at capture limit: False
- Repository ID: 311706320
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This code sample focuses on automating movement (unload) and management (delete/vacuum/analyze) of data in Amazon Redshift tables with temporal attributes through a simple configuration while maintaining movement and management choice, priority, logging, auditing and checkpointing.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:54:19+00:00

### Short excerpt (up to 300 words)

> Following building blocks are See CONTRIBUTING for more

### README headings

- Amazon Redshift Data Lifecycle Management
- Table of Contents
- Context
- Components
- Amazon DynamoDB
- Parameters from the utility:
- Parameters from Amazon Redshift Unload command:
- Amazon Redshift stored PL/pgSQL procedure
- AWS Glue
- Python shell job
- Database connection
- AWS Secrets Manager
- Amazon S3
- Amazon CloudWatch
- Architectural Patterns & Best Practices
- Deploying the solution with AWS CloudFormation
- Pre-requisites
- Deployment Steps
- Load Configuration data
- Create Amazon Redshift PL/pgSQL stored procedure
- Add Data Unload IAM Role to Amazon Redshift cluster
- AWS Glue Job
- Clean Up
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Components

> Following building blocks are

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 64,772 |
| PLpgSQL | 7,336 |
| Makefile | 2,362 |
| Shell | 452 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- requirements.txt (capture: captured) — dependency clues: pg8000
- config/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 9
- Forks at capture: 2
- Last updated: 2026-05-13T16:10:45Z
- Last pushed: 2025-10-28T02:59:59Z
- Topics: data, lifecycle-management, redshift

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-redshift-data-lifecycle-manager)
- [README](https://github.com/aws-samples/amazon-redshift-data-lifecycle-manager/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-redshift-data-lifecycle-manager/issues)
- [Releases](https://github.com/aws-samples/amazon-redshift-data-lifecycle-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
