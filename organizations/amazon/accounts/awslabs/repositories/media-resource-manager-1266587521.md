# awslabs/media-resource-manager

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/media-resource-manager](https://github.com/awslabs/media-resource-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/media-resource-manager/blob/main/README.md)
- README blob SHA: d32e08d7f6d5e7a3a4e0e3bba51a8cc0f6226fa0
- README bytes captured: 59182
- README truncated at capture limit: False
- Repository ID: 1266587521
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A comprehensive AWS-native workstation management solution that enables Media & Entertainment customers to easily deploy, manage, and access secure EC2-based creative workstations for content production, post-production, and live cloud production workflows through a self-service web console with integrated DCV remote access.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:34:55+00:00

### Short excerpt (up to 300 words)

> AWS Media Resource Manager **📚 See the User **Recommended**: Deploy using the The application uses a Before deploying, check for **VPC Isolation**: Private subnets

### README headings

- AWS Media Resource Manager
- Table of Contents
- Overview
- Cost
- Quick Start
- Prerequisites
- One-Click Deployment (CloudFormation + CodeBuild)
- Local Deployment (for developers)
- Clone the repository
- Create configuration files from examples
- Post-Deployment Access
- Deployment Options
- Local Deployment
- CloudShell Deployment
- CodeBuild Deployment
- Then trigger a rebuild
- For ProductName="Media Resource Manager", the SSM path is:
- Edit the file
- Upload and re-deploy
- Trigger rebuild (get project name from stack outputs)
- CodeCommit Repository Setup (Optional)
- For existing CodeCommit repo - creates IAM policies only
- For new repo - creates repo + IAM policies
- Get policy ARN from stack outputs
- Attach to role
- Configuration
- 1. Product Name Configuration (`cdk.json`)
- Lambda log retention (`lambdaLogRetentionDays`)
- 2. Infrastructure Parameters (`parameters.json`)
- Using an existing VPC

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> AWS Media Resource Manager

### Features and capabilities: Features

> **📚 See the User

### Getting started and usage: Quick Start

> **Recommended**: Deploy using the

### Architecture and design: Architecture Overview

> The application uses a

### Technology and requirements: Prerequisites

> Before deploying, check for

### Limitations and security: Security

> **VPC Isolation**: Private subnets

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 3,159,076 |
| JavaScript | 1,436,398 |
| Python | 378,612 |
| Shell | 237,834 |
| PowerShell | 99,346 |
| CSS | 2,269 |
| HTML | 802 |
| Dockerfile | 498 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-directory-service-data, @aws-sdk/client-dynamodb, @aws-sdk/client-imagebuilder, @aws-sdk/client-s3, @aws-sdk/client-ssm, @aws-sdk/client-sts, @aws-sdk/lib-dynamodb, @aws-sdk/lib-storage, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, ts-jest, ts-node, typescript
- frontend/package.json (capture: captured) — dependency clues: @ant-design/icons, @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-ssm, @aws-sdk/credential-providers, @aws-sdk/lib-storage, @aws-sdk/s3-request-presigner, @babel/runtime, @cloudscape-design/chat-components, @cloudscape-design/code-view, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @playwright/test, @types/react, @types/react-dom, @vitejs/plugin-react, @vitest/coverage-v8, antd, jsdom, prop-types
- agents/install-script-agent-python/Dockerfile (capture: captured)
- agents/install-script-agent-python/requirements.txt (capture: captured) — dependency clues: bedrock-agentcore, boto3, strands-agents, strands-agents-tools
- lambda/ad-user-manager/requirements.txt (capture: captured) — dependency clues: boto3, urllib3
- lambda/configure-ontap-cifs/package.json (capture: captured) — dependency clues: ssh2

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 3
- Last updated: 2026-11-22T05:07:47Z
- Last pushed: 2026-11-23T19:30:04Z
- Topics: amazon-dcv, aws, aws-cdk, fsx-ontap, fsx-windows, media-and-entertainment, post-production, remote-editing, typescript, vfx, virtual-workstations

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/media-resource-manager)
- [README](https://github.com/awslabs/media-resource-manager/blob/main/README.md)
- [Issues](https://github.com/awslabs/media-resource-manager/issues)
- [Releases](https://github.com/awslabs/media-resource-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
