# awslabs/config-for-kubernetes

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/config-for-kubernetes](https://github.com/awslabs/config-for-kubernetes)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/config-for-kubernetes/blob/main/README.md)
- README blob SHA: 18486653088b241640f8968666ca3344a773d376
- README bytes captured: 14785
- README truncated at capture limit: False
- Repository ID: 1068702201
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:28:47+00:00

### Short excerpt (up to 300 words)

> AWS Config is a After deploying the solution, AWS CLI installed and The solution only works

### README headings

- Kubernetes Resource Recorder for AWS Config
- Overview
- Deployment Instructions
- Prerequisites
- Deployment Steps
- 1. Deploy the Custom Resource Type
- Navigate to the custom resource package directory
- Validate the schema
- Generate the resource provider package
- Submit the resource type to AWS CloudFormation
- Replace us-east-1 with your AWS region
- 2. Build and Upload Lambda Functions
- Navigate to the project root
- Run the build script
- Replace us-east-1 with your AWS region
- 3. Deploy the CloudFormation Stack
- Replace 123456789012 with your AWS account ID and us-east-1 with your region
- CloudFormation Parameters
- Example Parameter Combinations
- Example 1: Monitor only Deployments and Services in production namespaces
- Replace 123456789012 with your AWS account ID and us-east-1 with your region
- Example 2: Monitor all resources with specific labels
- Replace 123456789012 with your AWS account ID and us-east-1 with your region
- Example 3: Monitor only clusters with specific tags
- Replace 123456789012 with your AWS account ID and us-east-1 with your region
- Testing Functionality After Deployment
- 1. Verify Step Functions Execution
- 2. View Recorded Kubernetes Resources
- 3. Query Resources Using Advanced Query
- Cost

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> AWS Config is a

### Features and capabilities: Testing Functionality After Deployment

> After deploying the solution,

### Technology and requirements: Prerequisites

> AWS CLI installed and

### Limitations and security: Limitations

> The solution only works

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 52,310 |
| Shell | 4,260 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- custom-resource-package/requirements.txt (capture: captured) — dependency clues: cloudformation-cli-python-lib
- source/functions/discover_resources/requirements.txt (capture: captured) — dependency clues: kubernetes

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 0
- Last updated: 2025-11-27T12:02:44Z
- Last pushed: 2026-11-20T21:25:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/config-for-kubernetes)
- [README](https://github.com/awslabs/config-for-kubernetes/blob/main/README.md)
- [Issues](https://github.com/awslabs/config-for-kubernetes/issues)
- [Releases](https://github.com/awslabs/config-for-kubernetes/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
