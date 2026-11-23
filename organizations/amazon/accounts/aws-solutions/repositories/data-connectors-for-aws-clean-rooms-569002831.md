# aws-solutions/data-connectors-for-aws-clean-rooms

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/data-connectors-for-aws-clean-rooms](https://github.com/aws-solutions/data-connectors-for-aws-clean-rooms)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/data-connectors-for-aws-clean-rooms/blob/main/README.md)
- README blob SHA: 088dc5ac0290c6a2e62d0bed69cd2fcf79901acd
- Repository ID: 569002831
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Simplify the process of selecting application sources and preparing data for collaborating in AWS Clean Rooms

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:39+00:00

### Short excerpt (up to 100 words)

> The following image shows the architecture of the solution for pulling data from a provider using Amazon AppFlow. The following image shows the architecture of the solution for pushing S3 data from a provider into an S3 bucket. **Note**: From v1.0.0, AWS CloudFormation template resources are created by the AWS CDK and AWS Solutions Constructs. well-architected applications. All AWS Solutions Constructs are reviewed by AWS and use best practices established by the AWS Well-Architected Framework. You can launch this solution with one click from the AWS Solutions landing page. To customize the solution, or to contribute to the solution, see

### README headings

- Data Connectors for AWS Clean Rooms
- Table of Contents
- Architecture
- AWS CDK Constructs
- Deployment
- Configuration
- Creating a custom build
- Prerequisites
- 1. Download or clone this repo
- 2. Create a Python virtual environment for development
- 2. After introducing changes, run the unit tests to make sure the customizations don't break existing functionality
- 3. Build the solution for deployment
- Using AWS CDK (recommended)
- set environment variables required by the solution
- bootstrap CDK (required once - deploys a CDK bootstrap CloudFormation stack for assets)
- build the solution
- build and deploy the solution
- Using the solution build tools
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 454,418 |
| Shell | 3,604 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/aws_lambda/setup.py (capture: captured)
- source/infrastructure/setup.py (capture: captured)
- source/cdk_solution_helper_py/helpers_cdk/setup.py (capture: captured)
- source/cdk_solution_helper_py/helpers_common/setup.py (capture: captured)
- source/aws_lambda/custom_resource/remove_s3_object/requirements.txt (capture: captured) — dependency clues: crhelper
- source/aws_lambda/custom_resource/salesforce/requirements.txt (capture: captured) — dependency clues: boto3, crhelper, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 5
- Last updated: 2024-08-13T19:10:38Z
- Last pushed: 2024-01-22T22:19:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/data-connectors-for-aws-clean-rooms)
- [README](https://github.com/aws-solutions/data-connectors-for-aws-clean-rooms/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/data-connectors-for-aws-clean-rooms/issues)
- [Releases](https://github.com/aws-solutions/data-connectors-for-aws-clean-rooms/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
