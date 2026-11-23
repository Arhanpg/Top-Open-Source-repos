# awslabs/amazon-aurora-postgres-monitoring

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-aurora-postgres-monitoring](https://github.com/awslabs/amazon-aurora-postgres-monitoring)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-aurora-postgres-monitoring/blob/master/README.md)
- README blob SHA: 88bcf916a6adfb2872cfd94c1a068b6fb80a335a
- Repository ID: 279997231
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An advanced monitoring system for Amazon Aurora PostgreSQL that is completely serverless, based on AWS Lambda and Amazon CloudWatch

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:27:13+00:00

### Short excerpt (up to 100 words)

> Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. This GitHub project provides an advanced monitoring system for Amazon Aurora Postgres that is completely serverless, based on AWS Lambda and Amazon CloudWatch. A serverless Lambda function runs on a schedule, connects to the configured Aurora Postgres cluster, and generates CloudWatch custom metrics that are visualized on a custom dashboard. You can create alarms based on these metrics to gain additional visibility and improve incident response capabilities for

### README headings

- Amazon Aurora Postgres Advanced Monitoring
- Overview
- <a name="PreReqs"></a>Pre-Requisites
- Installation
- Configuration
- <a name="EventJson"></a>Option 1: Using Event Parameters (Preferred)
- Option 2: Using Environment Variables
- Manual Deployment Instructions
- Confirming Successful Execution
- <a name="MetricDefinitions"></a>Metric Definitions
- Extensions

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 139,975 |
| Shell | 2,660 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: pg8000, pgpasslib

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 39
- Forks at capture: 7
- Last updated: 2026-07-22T19:33:17Z
- Last pushed: 2025-10-28T02:57:20Z
- Topics: aurora, cloudwatch, lambda, monitoring, monitoring-tool, postgres, postgresql, postgresql-database, serverless

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-aurora-postgres-monitoring)
- [README](https://github.com/awslabs/amazon-aurora-postgres-monitoring/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-aurora-postgres-monitoring/issues)
- [Releases](https://github.com/awslabs/amazon-aurora-postgres-monitoring/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
