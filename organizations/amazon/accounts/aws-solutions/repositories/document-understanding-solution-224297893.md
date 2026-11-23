# aws-solutions/document-understanding-solution

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/document-understanding-solution](https://github.com/aws-solutions/document-understanding-solution)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/document-understanding-solution/blob/main/README.md)
- README blob SHA: 6161b1c737e9c0b7d8970d25bcd9ead21da3dbfa
- Repository ID: 224297893
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Example of integrating & using Amazon Textract, Amazon Comprehend, Amazon Comprehend Medical, Amazon Kendra to automate the processing of documents for use cases such as enterprise search and discovery, control and compliance, and general business process workflow.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:28:28+00:00

### Short excerpt (up to 100 words)

> As of 09/14/2023, Document Understanding Solution has been deprecated and will not be receiving any additional features or updates. We encourage customers to explore the new solution: https://aws.amazon.com/solutions/implementations/enhanced-document-understanding-on-aws/. DUS leverages the power of Amazon Textract, Amazon Comprehend , Amazon Comprehend Medical Amazon OpenSearch Service and Amazon Kendra to provide digitization , domain-specific data discovery, redaction controls , structural component extraction and other document processing & understanding capabilities. Current document formats supported : **PDF,JPG,PNG** Current maximum document file size supported : **150MB** Current concurrent document uploads (via UI ) supported : **100** - aws cli `sudo yum -y install aws-cli` -

### README headings

- Deprecation Notice
- Document Understanding Solution
- Architecture Diagram
- Note
- 1. CICD Deploy
- Requirements
- Getting Started with CICD Deploy
- Notes
- Development Deploy
- Requirements
- Development Deploy Commands
- Development Deploy Workflow and stack naming
- Developing Locally
- Start Dev Server
- Generate Production Build
- Code Quality Tools
- Generating License Report
- DUS Modes:
- Classic Mode
- Kendra-Enabled Mode
- Read-Only Mode
- Notes
- Document Bulk Processing
- Other
- Cost
- Delete demo application
- License
- Additional Notes

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 369,599 |
| Python | 161,263 |
| TypeScript | 73,529 |
| SCSS | 70,164 |
| Shell | 13,670 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/package.json (capture: captured) — dependency clues: @aws-cdk/aws-apigateway, @aws-cdk/aws-cloudformation, @aws-cdk/aws-cognito, @aws-cdk/aws-dynamodb, @aws-cdk/aws-ec2, @aws-cdk/aws-elasticsearch, @aws-cdk/aws-events, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-lambda-event-sources, @aws-cdk/aws-logs, @aws-cdk/aws-s3, @aws-cdk/aws-s3-deployment, @aws-cdk/aws-s3-notifications, @aws-cdk/aws-sns, @aws-cdk/aws-sqs, @aws-cdk/core, @babel/helper-validator-identifier, @types/node, autoprefixer
- deployment/document-understanding-cicd/package.json (capture: captured) — dependency clues: adm-zip, aws-sdk, logger
- deployment/logger/package.json (capture: captured) — dependency clues: aws-sdk-mock, chai, mocha, npm-run-all, proxyquire, sinon, sinon-chai
- source/lambda/boto3/requirements.txt (capture: captured) — dependency clues: boto3, botocore, docutils, filetype, jmespath, python_dateutil, s3transfer, six, urllib3
- source/lambda/elasticsearch/requirements.txt (capture: captured) — dependency clues: certifi, chardet, elasticsearch, idna, requests, requests-aws4auth, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 229
- Forks at capture: 89
- Last updated: 2026-10-06T08:52:53Z
- Last pushed: 2023-10-25T22:30:27Z
- Topics: amazon-comprehend, amazon-elasticsearch, amazon-kendra, amazon-textract, aws, aws-cdk, aws-machine-learning, cdk, machine-learning

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/document-understanding-solution)
- [README](https://github.com/aws-solutions/document-understanding-solution/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/document-understanding-solution/issues)
- [Releases](https://github.com/aws-solutions/document-understanding-solution/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
