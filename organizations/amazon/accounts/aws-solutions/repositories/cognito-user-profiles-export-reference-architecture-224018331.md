# aws-solutions/cognito-user-profiles-export-reference-architecture

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/cognito-user-profiles-export-reference-architecture](https://github.com/aws-solutions/cognito-user-profiles-export-reference-architecture)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/cognito-user-profiles-export-reference-architecture/blob/main/README.md)
- README blob SHA: d319c548bc28c0944af2ca8d945fa757f4d2c571
- Repository ID: 224018331
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This solution has been replaced by Guidance for User Profiles Export with Amazon Cognito

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:31+00:00

### Short excerpt (up to 100 words)

> ⚠️🚨⚠️ This solution has been replaced by Guidance for User Profiles Export with Amazon Cognito ⚠️🚨⚠️ This solution uses an AWS Step Functions workflow (`ExportWorkflow`) to periodically export user profiles, groups, and group membership details from your user pool to an Amazon DynamoDB global table with automatic, asynchronous replication to a backup Region for added resiliency. This solution is designed to provide a framework for exporting user profile and group information from your user pool, allowing you to focus on extending the solution’s functionality rather than managing the underlying infrastructure operation. This solution’s `ImportWorkflow` Step Functions workflow can be used

### README headings

- Cognito User Profiles Export Reference Architecture
- On This Page
- Architecture Overview
- Getting Started
- 1. Prerequsites
- 2. Clone the Cognito User Profiles Export Reference Architecture repository
- 3. Run unit tests
- 4. Declare environment variables
- 5. Create an Amazon S3 bucket
- 6. Build the Cognito User Profiles Export Reference Architecture for deployment
- 7. Upload deployment assets to your Amazon S3 bucket
- 8. Launch the Cognito User Profiles Export Reference Architecture
- File Structure
- Collection of operational metrics
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 245,306 |
| Shell | 5,969 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/custom-resources/package.json (capture: captured) — dependency clues: @aws-sdk/client-cloudformation, @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-dynamodb, @aws-sdk/client-sfn, @aws-sdk/client-ssm, aws-sdk-client-mock, axios, axios-mock-adapter, jest, uuid
- source/utils/package.json (capture: captured) — dependency clues: axios, axios-mock-adapter, jest, moment
- source/workflow-common/package.json (capture: captured) — dependency clues: @aws-sdk/client-dynamodb, @aws-sdk/client-sfn, @aws-sdk/client-sns, @aws-sdk/client-sqs, @aws-sdk/lib-dynamodb, aws-sdk-client-mock, jest
- source/workflow-export/package.json (capture: captured) — dependency clues: @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-dynamodb, @aws-sdk/client-sqs, @aws-sdk/lib-dynamodb, aws-sdk-client-mock, jest, uuid
- source/workflow-import/package.json (capture: captured) — dependency clues: @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-dynamodb, @aws-sdk/client-s3, @aws-sdk/client-sqs, @aws-sdk/lib-dynamodb, @aws-sdk/node-http-handler, aws-sdk-client-mock, axios, axios-mock-adapter, jest, uuid

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 55
- Forks at capture: 19
- Last updated: 2025-06-26T19:38:30Z
- Last pushed: 2025-06-26T19:35:33Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/cognito-user-profiles-export-reference-architecture)
- [README](https://github.com/aws-solutions/cognito-user-profiles-export-reference-architecture/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/cognito-user-profiles-export-reference-architecture/issues)
- [Releases](https://github.com/aws-solutions/cognito-user-profiles-export-reference-architecture/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
