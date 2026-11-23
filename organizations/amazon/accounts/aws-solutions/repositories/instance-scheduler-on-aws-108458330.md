# aws-solutions/instance-scheduler-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/instance-scheduler-on-aws](https://github.com/aws-solutions/instance-scheduler-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/instance-scheduler-on-aws/blob/main/README.md)
- README blob SHA: 740eaa6271671d8f6906acd487d4d3469b585c2f
- Repository ID: 108458330
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A cross-account and cross-region solution that allows customers to automatically start and stop EC2 and RDS Instances

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:43:57+00:00

### Short excerpt (up to 100 words)

> The Instance Scheduler on AWS solution automates the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances. This solution helps reduce operational costs by stopping resources that are not in use and starting them when they are needed. The cost savings can be significant if you leave all of your instances running at full utilization continuously. To understand how to use Instance Scheduler on AWS, please review the [implementation guide](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html) on the [solution landing page](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/). To deploy the solution, see **Launch in AWS Console** Refer to the deployment instructions in our

### README headings

- Instance Scheduler on AWS
- Getting Started
- Repository Organization
- Deploying the Solution
- One-Click Deploy From Amazon Web Services
- Deploy from source code using CDK
- Prerequisites
- Deploying the hub stack
- Deploying Remote Stacks in Other Accounts
- Deploy from GitHub (AWS Console)
- Overview
- You will need:
- Step 1 - Download from GitHub
- Step 2 - Build the solution
- Step 3 - Upload to your buckets
- Step 4 - Deploy The Solution
- Testing the Solution
- Prerequisites
- Running Tests Locally
- Modifying the Solution
- projen
- Package installation
- For Node.js dependencies
- For Python dependencies
- CDK Documentation
- Collection of Operational Metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,141,422 |
| TypeScript | 244,706 |
| Shell | 3,987 |
| JavaScript | 759 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/aws-lambda-python-alpha, @aws-cdk/aws-neptune-alpha, @types/jest, @types/node, @typescript-eslint/eslint-plugin, aws-cdk, aws-cdk-lib, cdk-nag, constructs, esbuild, eslint, eslint-config-prettier, eslint-plugin-header, eslint-plugin-import, eslint-plugin-prettier, jest, jest-extended, jest-junit, projen, source-map-support
- deployment/cdk-solution-helper/package.json (capture: captured) — dependency clues: @types/adm-zip, @types/jest, @types/node, adm-zip, aws-cdk-lib, jest, ts-jest, ts-node, typescript
- source/app/pyproject.toml (capture: captured) — dependency clues: attrs, aws-lambda-powertools, black, boto3, boto3-stubs-lite, botocore, botocore-stubs, flake8, freezegun, isort, jmespath, moto, mypy, packaging, pydantic, pytest, pytest-cov, pytest-mock, pytest-runner, pytest-xdist
- source/cli/pyproject.toml (capture: captured) — dependency clues: attrs, black, boto3, boto3-stubs-lite, flake8, isort, jmespath, jsonschema, moto, mypy, pytest, pytest-cov, tox, types-PyYAML, types-jmespath, types-requests, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 625
- Forks at capture: 298
- Last updated: 2026-11-17T04:06:41Z
- Last pushed: 2026-11-12T23:14:06Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/instance-scheduler-on-aws)
- [README](https://github.com/aws-solutions/instance-scheduler-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/instance-scheduler-on-aws/issues)
- [Releases](https://github.com/aws-solutions/instance-scheduler-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
