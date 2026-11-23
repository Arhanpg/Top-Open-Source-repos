# aws-actions/amazon-ecs-deploy-task-definition

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/amazon-ecs-deploy-task-definition](https://github.com/aws-actions/amazon-ecs-deploy-task-definition)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-actions/amazon-ecs-deploy-task-definition/blob/master/README.md)
- README blob SHA: 5b45ca995f891b03bd72944ff4d607e13d9247a5
- Repository ID: 220386210
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Registers an Amazon ECS task definition and deploys it to an ECS service.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:33:18+00:00

### Short excerpt (up to 100 words)

> Registers an Amazon ECS task definition and deploys it to an ECS service. **Table of Contents** - Usage + Task definition file + Task definition container image values - Credentials and Region - Permissions - AWS CodeDeploy Support - Polling Configuration - Troubleshooting - License Summary - Security Disclosures - name: Deploy to Amazon ECS uses: aws-actions/amazon-ecs-deploy-task-definition@v2 with: task-definition: task-definition.json service: my-service cluster: my-cluster wait-for-service-stability: true See action.yml for the full documentation for this action's inputs and outputs. In most cases when running a one-off task, subnet ID's, subnet groups, and assign public IP will be required. Assign public IP

### README headings

- Amazon ECS "Deploy Task Definition" Action for GitHub Actions
- Usage
- Task definition file
- Task definition container image values
- Tags
- EBS Volume Configuration
- Credentials and Region
- Permissions
- AWS CodeDeploy Support
- Running Tasks
- Tags
- Preserving Empty Values with keep-null-value-keys
- Polling Configuration
- Retries
- Troubleshooting
- License Summary
- Security Disclosures

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 121,081 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @aws-sdk/client-codedeploy, @aws-sdk/client-ecs, @eslint/js, @vercel/ncc, eslint, globals, jest, yaml

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 766
- Forks at capture: 271
- Last updated: 2026-11-10T23:13:33Z
- Last pushed: 2026-10-31T23:55:36Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/amazon-ecs-deploy-task-definition)
- [README](https://github.com/aws-actions/amazon-ecs-deploy-task-definition/blob/master/README.md)
- [Issues](https://github.com/aws-actions/amazon-ecs-deploy-task-definition/issues)
- [Releases](https://github.com/aws-actions/amazon-ecs-deploy-task-definition/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
