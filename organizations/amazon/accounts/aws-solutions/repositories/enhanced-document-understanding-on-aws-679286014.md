# aws-solutions/enhanced-document-understanding-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/enhanced-document-understanding-on-aws](https://github.com/aws-solutions/enhanced-document-understanding-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/enhanced-document-understanding-on-aws/blob/main/README.md)
- README blob SHA: 004802c804dab81df47502f2e2871d6216819f6d
- Repository ID: 679286014
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Enhanced Document Understanding on AWS delivers an easy-to-use web application that ingests and analyzes documents, extracts content, identifies and redacts sensitive customer information, and creates search indexes from the analyzed data.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:28:38+00:00

### Short excerpt (up to 100 words)

> ⚠️🚨⚠️ __Important: Enhanced Document Understanding on AWS has been deprecated and will not be receiving any additional features or updates. Customers can explore using Bedrock Data Automation, which allows insights and extraction of content from various unstructured files (video, audio, documents etc.), as well as Guidance for Intelligent Document Processing on AWS.__ ⚠️🚨⚠️ Organizations across industries are increasingly required to process large volumes of semi-structured and unstructured documents with greater accuracy and speed. They need a document processing system that ingests and analyzes documents, extracts their content, identifies and redacts sensitive customer information, and creates search indexes from the analyzed

### README headings

- Enhanced Document Understanding on AWS
- On this page
- Architecture Overview
- Deployment
- 1. Using `cdk deploy`
- 2. Using CloudFormation templates
- Source code
- Project directory structure
- Creating a custom build
- 1. Clone the repository
- 2. Build the solution for deployment
- Anonymized data collection

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 1,313,086 |
| TypeScript | 829,928 |
| Java | 214,219 |
| Python | 198,005 |
| Shell | 17,330 |
| CSS | 5,321 |
| Makefile | 1,834 |
| HTML | 612 |
| Dockerfile | 37 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/cdk-solution-helper/package.json (capture: captured)
- source/infrastructure/package.json (capture: captured) — dependency clues: @aws-sdk/client-sfn, @aws-sdk/util-arn-parser, @aws-solutions-constructs/aws-apigateway-lambda, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-eventbridge-lambda, @aws-solutions-constructs/aws-eventbridge-stepfunctions, @aws-solutions-constructs/aws-lambda-dynamodb, @aws-solutions-constructs/aws-lambda-s3, @aws-solutions-constructs/aws-lambda-sns, @aws-solutions-constructs/aws-lambda-stepfunctions, @aws-solutions-constructs/aws-sns-sqs, @aws-solutions-constructs/aws-sqs-lambda, @aws-solutions-constructs/aws-wafwebacl-apigateway, @aws-solutions-constructs/core, @types/dockerode, @types/jest, @types/mock-fs, @types/node, @types/npmlog, @types/uuid
- source/ui/package.json (capture: captured) — dependency clues: @aws-amplify/ui-react, @babel/plugin-proposal-private-property-in-object, @babel/preset-env, @babel/preset-react, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @cloudscape-design/jest-preset, @reduxjs/toolkit, @tanstack/react-table, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/jest, @types/ramda, @types/react-test-renderer, @types/uuid, @types/whatwg-fetch, babel-jest, bootstrap
- source/lambda/create-presigned-url/package.json (capture: captured) — dependency clues: aws-sdk-mock, eslint, jest, prettier
- source/lambda/custom-resource/pyproject.toml (capture: captured) — dependency clues: PyYAML, boto3-layer, custom_boto3_init, freezegun, mock, moto, pytest, pytest-cov, pytest-env, requests, setuptools, urllib3
- source/lambda/entity-detection/package.json (capture: captured) — dependency clues: aws-sdk-mock, eslint, jest, prettier

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 41
- Forks at capture: 18
- Last updated: 2026-01-07T04:19:48Z
- Last pushed: 2025-10-10T16:58:58Z
- Topics: document-analysis, document-processing

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/enhanced-document-understanding-on-aws)
- [README](https://github.com/aws-solutions/enhanced-document-understanding-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/enhanced-document-understanding-on-aws/issues)
- [Releases](https://github.com/aws-solutions/enhanced-document-understanding-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
