# aws-solutions/automated-security-response-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/automated-security-response-on-aws](https://github.com/aws-solutions/automated-security-response-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/automated-security-response-on-aws/blob/main/README.md)
- README blob SHA: 4c4884477234db9caf7d26a990a4ffa17b3d37c7
- Repository ID: 285372365
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Automated Security Response on AWS is an add-on solution that works with AWS Security Hub to provide a ready-to-deploy architecture and a library of automated playbooks. The solution makes it easier for AWS Security Hub customers to resolve common security findings and to improve their security posture in AWS.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:33:09+00:00

### Short excerpt (up to 100 words)

> Feature request](https://github.com/aws-solutions/automated-security-response-on-aws/issues/new?assignees=&labels=feature-request%2C+enhancement&template=feature_request.md&title=) \| [🐛 Bug Report](https://github.com/aws-solutions/automated-security-response-on-aws/issues/new?assignees=&labels=bug%2C+triage&template=bug_report.md&title=) Automated Security Response (ASR) on AWS is a solution that enables AWS Security Hub customers to remediate findings with a single click using sets of predefined response and remediation actions called Playbooks. The remediations are implemented as AWS Systems Manager automation documents. The solution includes remediations for issues such as unused access keys, open security groups, weak account password policies, VPC flow logging configurations, and public S3 buckets. Remediations can also be configured to trigger automatically when findings appear in AWS Security Hub. The solution includes the playbook remediations for some of the security

### README headings

- Automated Security Response on AWS
- Architecture Diagram
- Customizing the Solution
- Prerequisites for Customization
- Obtaining Source Code
- Custom Remediations in Existing Playbooks
- Step 1: Create the Remediation Runbook
- Step 2: Create the Control Runbooks.
- Step 3: Integrate Each Control Runbook with a Playbook
- Integrate with /_<playbook_name>_/control_runbooks-construct.ts
- Add to _<playbook_name>_\_remediations.ts
- Step 4: Create the Markdown File
- Step 5: Create the Remediation IAM Role & Integrate Remediation Runbook
- Step 6: Build and update Unit Tests
- Deprecated Controls
- Custom Playbooks
- Configure the Playbook
- Add your playbook as a new nested stack in the solution template
- Create the Remediations
- Connect an AI client to the ASR MCP server
- Claude Code
- Kiro
- Kiro CLI sign-in steps
- OpenAI Codex CLI
- Notes and troubleshooting
- Authoring remediations with an AI coding agent
- Build and Deploy
- Build the solution
- Configuring API rate limits
- Unit Tests

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 7,235,215 |
| Python | 3,111,624 |
| Shell | 88,265 |
| JavaScript | 49,783 |
| CSS | 1,397 |
| HTML | 592 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- deployment/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, aws_lambda_context, black, boto3, boto3-stubs-lite, click, cryptography, filelock, flake8, graphql-core, isort, jinja2, joserfc, moto, mypy, openapi_spec_validator, pytest, pytest-cov, pytest-env, pytest-mock
- source/package.json (capture: captured) — dependency clues: @asr/data-models, @aws-cdk/aws-bedrock-agentcore-alpha, @aws-lambda-powertools/batch, @aws-lambda-powertools/commons, @aws-lambda-powertools/logger, @aws-lambda-powertools/tracer, @aws-sdk/client-dynamodb, @aws-sdk/client-organizations, @aws-sdk/client-s3, @aws-sdk/client-sfn, @aws-sdk/client-ssm, @aws-sdk/lib-dynamodb, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-eventbridge-sqs, @cdklabs/cdk-ssm-documents, @eslint/js, @types/aws-lambda, @types/jest, @types/js-yaml, @types/node
- deployment/manifest-generator/package.json (capture: captured) — dependency clues: minimist
- deployment/utils/package.json (capture: captured) — dependency clues: fast-check, jest
- source/blueprints/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 489
- Forks at capture: 137
- Last updated: 2026-11-19T21:56:07Z
- Last pushed: 2026-11-18T15:54:57Z
- Topics: aws, aws-security-automation, aws-security-hub

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/automated-security-response-on-aws)
- [README](https://github.com/aws-solutions/automated-security-response-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/automated-security-response-on-aws/issues)
- [Releases](https://github.com/aws-solutions/automated-security-response-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
