# aws-solutions/automations-for-aws-firewall-manager

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/automations-for-aws-firewall-manager](https://github.com/aws-solutions/automations-for-aws-firewall-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/automations-for-aws-firewall-manager/blob/main/README.md)
- README blob SHA: c82b9bd5d96dd52132251ad8ff40e4cd2bc4831c
- Repository ID: 298359533
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Automations For AWS Firewall Manager solution is intended for customers looking to easily manage consistent security posture across their entire AWS Organization. The solution uses AWS Firewall Manager Service.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:03:45+00:00

### Short excerpt (up to 100 words)

> ⚠️🚨⚠️ The Automations for AWS Firewall Manager solution has been deprecated and will not be receiving any additional features or updates. We encourage customers to explore using the latest deployment, multi-account management, and compliance features in AWS Firewall Manager for management and enforcement of firewall rules. ⚠️🚨⚠️ **🚀Solution Landing Page** | **🚧Feature request** | **🐛Bug Report** | **📜Documentation Improvement** _Note:_ For any relevant information outside the scope of this readme, please refer to the solution landing page and implementation guide. - Solution Overview - Architecture - Installation - Parameters - Custom Policy - Customization - Setup - Changes - Unit

### README headings

- Automations for AWS Firewall Manager
- Table of contents
- Solution Overview
- Architecture
- Architecture with Automations for AWS Shield Advanced (Optional)
- Installing pre-packaged solution templates
- Parameters for Primary (aws-fms-automations) template
- *[Optional]* Parameters for Prerequisite (aws-fms-prereq) template
- *[Optional]* Parameters for Shield Automations (aws-fms-shield-automations) template
- *[Optional]* Parameters for Proactive Event Response (aws-fms-proactive-event-response) template
- Custom Policy Stack
- Customization
- Setup
- Changes
- Unit Test
- Build
- Deploy
- Build the solution
- Run Unit Tests
- Upload to your buckets
- Deploy
- Sample Scenario
- File structure
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 548,525 |
| JavaScript | 16,333 |
| Shell | 14,526 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-s3, @types/uuid, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, eslint, eslint-config-prettier, eslint-plugin-prettier, jest, prettier, typedoc, typedoc-plugin-no-inherit, typescript
- deployment/cdk-solution-helper/package.json (capture: captured) — dependency clues: @types/jest, @types/node, jest, ts-jest, typescript
- source/resources/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-eventbridge-lambda, @types/jest, @types/node, aws-cdk, aws-cdk-lib, constructs, jest, jest-sonar-reporter, ts-jest, ts-node, typescript
- source/services/complianceGenerator/package.json (capture: captured) — dependency clues: @aws-lambda-powertools/logger, @aws-lambda-powertools/tracer, @aws-sdk/client-ec2, @aws-sdk/client-fms, @aws-sdk/client-s3, @aws-sdk/client-sns, @aws-sdk/client-sqs, @types/aws-lambda, @types/jest, @types/node, aws-sdk-client-mock, csv-writer, got, jest, jest-sonar-reporter, ts-jest, ts-node, typescript
- source/services/helper/package.json (capture: captured) — dependency clues: @aws-lambda-powertools/commons, @aws-lambda-powertools/logger, @aws-lambda-powertools/tracer, @aws-sdk/client-fms, @aws-sdk/client-organizations, @aws-sdk/client-s3, @aws-sdk/client-shield, @aws-sdk/client-support, @aws-sdk/types, @types/aws-lambda, @types/jest, @types/node, @types/uuid, aws-sdk-client-mock, got, jest, jest-sonar-reporter, ts-jest, typescript, uuid
- source/services/policyManager/package.json (capture: captured) — dependency clues: @aws-lambda-powertools/logger, @aws-lambda-powertools/parameters, @aws-lambda-powertools/tracer, @aws-sdk/client-dynamodb, @aws-sdk/client-ec2, @aws-sdk/client-fms, @aws-sdk/client-ram, @aws-sdk/client-route53resolver, @aws-sdk/client-s3, @aws-sdk/client-sns, @aws-sdk/client-sqs, @aws-sdk/client-ssm, @aws-sdk/types, @types/aws-lambda, @types/jest, @types/node, aws-sdk-client-mock, aws-sdk-client-mock-jest, jest, jest-sonar-reporter

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 33
- Forks at capture: 23
- Last updated: 2026-11-19T13:41:38Z
- Last pushed: 2025-11-10T20:26:06Z
- Topics: aws, aws-firewall-manager, aws-security, firewall

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/automations-for-aws-firewall-manager)
- [README](https://github.com/aws-solutions/automations-for-aws-firewall-manager/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/automations-for-aws-firewall-manager/issues)
- [Releases](https://github.com/aws-solutions/automations-for-aws-firewall-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
