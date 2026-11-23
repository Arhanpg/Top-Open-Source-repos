# aws-solutions/aws-waf-security-automations

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/aws-waf-security-automations](https://github.com/aws-solutions/aws-waf-security-automations)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/aws-waf-security-automations/blob/main/README.md)
- README blob SHA: 13db3167ac7980f189b702e8cc59bb5542d01f7c
- Repository ID: 68951589
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This solution automatically deploys a single web access control list (web ACL) with a set of AWS WAF rules designed to filter common web-based attacks.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:03+00:00

### Short excerpt (up to 100 words)

> **Important: Security Automations for AWS WAF will retire in December 2026. Deployments (via CloudFormation or GitHub) will remain operational, but customers will assume responsibility for maintenance and API-related updates post-retirement. Customers can explore using native AWS WAF capabilities including AWS Managed Rules, native rate-based rules, and the AWS WAF Console for intuitive configuration and management. These native capabilities provide superior functionality, better performance, real-time updates, and enhanced security features compared to the solution.** **Customers running solution versions prior to v3.0.0 (which deployed AWS WAF Classic) should first migrate to AWS WAF v2 using the AWS WAF migration documentation. Customers on

### README headings

- Table of contents
- Solution overview
- Architecture diagram
- Customizing the solution
- Prerequisites for customization
- Build
- 1. Clone the repository
- 2. Unit test
- 3. Create S3 buckets for storing deployment assets
- 4. Declare enviroment variables
- 5. Build the solution
- Upload deployment assets
- Deploy
- 1. Option to deploy the template in the S3 bucket
- 2. Option to deploy using the ```cdk deploy``` command.
- File structure
- Data Collection
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 410,653 |
| TypeScript | 401,576 |
| Shell | 16,607 |
| JavaScript | 583 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/custom_resource/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, aws-xray-sdk, backoff, boto3, cryptography, jinja2, moto, pytest, pytest-cov, pytest-env, pytest-mock, urllib3
- source/helper/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, aws-xray-sdk, backoff, boto3, cryptography, jinja2, moto, pytest, pytest-cov, pytest-env, pytest-mock, urllib3
- source/infrastructure/package.json (capture: captured) — dependency clues: @eslint/js, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, constructs, eslint, globals, jest, jest-sonar-reporter, prettier, ts-jest, ts-node, typescript
- source/ip_retention_handler/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, aws-xray-sdk, backoff, boto3, cryptography, jinja2, moto, pytest, pytest-cov, pytest-env, pytest-mock, urllib3
- source/log_parser/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, aws-xray-sdk, backoff, boto3, cryptography, freezegun, jinja2, moto, pyparsing, pytest, pytest-cov, pytest-env, pytest-mock, urllib3
- source/metrics/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, aws-xray-sdk, boto3, cryptography, moto, pytest, pytest-cov, pytest-env, pytest-mock, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 928
- Forks at capture: 376
- Last updated: 2026-11-19T20:09:21Z
- Last pushed: 2026-10-28T15:24:19Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/aws-waf-security-automations)
- [README](https://github.com/aws-solutions/aws-waf-security-automations/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/aws-waf-security-automations/issues)
- [Releases](https://github.com/aws-solutions/aws-waf-security-automations/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
