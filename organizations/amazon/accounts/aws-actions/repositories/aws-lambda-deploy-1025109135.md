# aws-actions/aws-lambda-deploy

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/aws-lambda-deploy](https://github.com/aws-actions/aws-lambda-deploy)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-actions/aws-lambda-deploy/blob/main/README.md)
- README blob SHA: 6ee0ff0f14faea33bd856aa32faca18c7c5976ab
- Repository ID: 1025109135
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Deploys a Lambda function.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:14+00:00

### Short excerpt (up to 100 words)

> Updates the code and configuration of AWS Lambda functions as part of GitHub Actions workflow steps. Supports both .zip file archives and container images stored in Amazon ECR. **Table of Contents** - Usage * Update Function Configuration * Using S3 Deployment Method * Dry Run Mode * Container Image Deployment - Build from Source - Inputs - Outputs - Credentials and Region - Permissions - License Summary - Security Disclosures name: Deploy to AWS Lambda on: push: branches: [ "main" ] permissions: id-token: write # This is required for OIDC authentication contents: read # This is required to checkout the

### README headings

- AWS Lambda Deploy GitHub Action
- Usage
- Update Function Configuration
- Using S3 Deployment Method
- Dry Run Mode
- Container Image Deployment
- Build from Source
- Node.js
- Python
- Inputs
- Outputs
- Credentials and Region
- OpenID Connect (OIDC)
- Permissions
- License Summary
- Security Disclosures

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 259,941 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @actions/github, @aws-sdk/client-lambda, @aws-sdk/client-s3, @aws-sdk/client-sts, @aws-sdk/util-retry, @smithy/node-http-handler, @vercel/ncc, adm-zip, eslint, eslint-plugin-jest, glob, jest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 271
- Forks at capture: 21
- Last updated: 2026-11-19T00:01:53Z
- Last pushed: 2026-05-13T20:56:55Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/aws-lambda-deploy)
- [README](https://github.com/aws-actions/aws-lambda-deploy/blob/main/README.md)
- [Issues](https://github.com/aws-actions/aws-lambda-deploy/issues)
- [Releases](https://github.com/aws-actions/aws-lambda-deploy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
