# aws-solutions/quota-monitor-for-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/quota-monitor-for-aws](https://github.com/aws-solutions/quota-monitor-for-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/quota-monitor-for-aws/blob/main/README.md)
- README blob SHA: 08f8adeaab60d1f0d3f3b8bd116fdadb3cc81e48
- Repository ID: 58246818
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This solution leverages AWS Trusted Advisor and Service Quotas to monitor AWS resource usage and raise alerts.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:45+00:00

### Short excerpt (up to 100 words)

> **Important: This solution will retire in December 2026. Deployments (via CloudFormation or GitHub) will remain operational, but customers will assume responsibility for maintenance and API-related updates post-retirement.** **Customers can explore using AWS Service Quotas for proactive usage monitoring and automated management of your service quotas. Service Quotas Automatic Management provides a fully AWS-managed alternative that covers the most common quota monitoring and alerting needs without requiring customer-managed infrastructure.** **Planning your migration: When transitioning to Automatic Management, note these key differences to ensure full coverage: it uses standardized AWS-defined thresholds (80% and 95%), focuses on resource quotas (not API rate limits),

### README headings

- Quota Monitor for AWS
- Table of content
- Solution overview
- Architecture
- Deployment scenarios:
- Installing pre-packaged solution template
- Parameters for hub template
- Parameters for spoke templates
- Customization
- Setup
- Running unit tests for customization
- Build
- Deploy
- Independent spoke templates
- SSM Parameter Store based workflow
- File Structure
- License
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 459,547 |
| Shell | 6,507 |
| JavaScript | 2,461 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-service-quotas, @types/jest, @types/node, @types/uuid, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-config-prettier, eslint-plugin-prettier, prettier, typescript
- deployment/cdk-solution-helper/package.json (capture: captured)
- source/resources/package.json (capture: captured) — dependency clues: @aws-cdk/aws-servicecatalogappregistry-alpha, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, ts-jest, ts-node, typescript
- source/lambda/utilsLayer/package.json (capture: captured) — dependency clues: @aws-sdk/client-cloudformation, @aws-sdk/client-cloudwatch, @aws-sdk/client-cloudwatch-events, @aws-sdk/client-dynamodb, @aws-sdk/client-dynamodb-streams, @aws-sdk/client-ec2, @aws-sdk/client-organizations, @aws-sdk/client-service-quotas, @aws-sdk/client-sns, @aws-sdk/client-sqs, @aws-sdk/client-ssm, @aws-sdk/client-support, @aws-sdk/lib-dynamodb, @types/jest, @types/node, aws-sdk-client-mock, aws-sdk-client-mock-jest, jest, ts-jest, ts-node
- source/lambda/services/cwPoller/package.json (capture: captured) — dependency clues: @aws-sdk/client-cloudwatch, @aws-sdk/client-cloudwatch-events, @aws-sdk/client-service-quotas, @types/jest, @types/node, jest, ts-jest, ts-node, typescript
- source/lambda/services/deploymentManager/package.json (capture: captured) — dependency clues: @types/jest, @types/node, jest, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 494
- Forks at capture: 123
- Last updated: 2026-11-15T13:07:35Z
- Last pushed: 2026-10-20T19:28:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/quota-monitor-for-aws)
- [README](https://github.com/aws-solutions/quota-monitor-for-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/quota-monitor-for-aws/issues)
- [Releases](https://github.com/aws-solutions/quota-monitor-for-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
