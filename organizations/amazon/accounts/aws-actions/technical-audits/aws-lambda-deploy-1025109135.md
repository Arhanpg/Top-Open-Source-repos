# aws-actions/aws-lambda-deploy

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/aws-lambda-deploy
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:19:58+00:00

## Project purpose

Updates the code and configuration of AWS Lambda functions as part of GitHub Actions workflow steps. Supports both .zip file archives and container images stored in Amazon ECR.

## Why this project is used

Deploys a Lambda function.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @actions/github, @aws-sdk/client-lambda, @aws-sdk/client-s3, @aws-sdk/client-sts, @aws-sdk/util-retry, @smithy/node-http-handler, @vercel/ncc, adm-zip, eslint, eslint-plugin-jest, glob, jest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: index.js, .eslintrc.js, __tests__/code_artifacts.test.js, __tests__/container_image_support.test.js

## Setup and usage

- Usage: name: Deploy to AWS Lambda
- Usage: id-token: write # This is required for OIDC authentication
- Usage: contents: read # This is required to checkout the repository
- Usage: runs-on: ubuntu-latest
- Usage: environment: production
- Usage: uses: actions/checkout@v5
- Usage: - name: Configure AWS credentials
- Usage: uses: aws-actions/configure-aws-credentials@v4

## Limitations and caveats

- Security Disclosures: If you would like to report a potential security issue in this project, please
- Security Disclosures: do not create a GitHub issue. Instead, please follow the instructions
- Security Disclosures: security directly](mailto:aws-security@amazon.com).

## Evidence and provenance

- README: https://github.com/aws-actions/aws-lambda-deploy/blob/main/README.md
- README SHA: 6ee0ff0f14faea33bd856aa32faca18c7c5976ab
- Manifests: package.json
- Sampled source files: index.js, .eslintrc.js, __tests__/code_artifacts.test.js, __tests__/container_image_support.test.js
- Git tree state: captured
- Evidence fingerprint: 3b177ae9dadd2e1a5683ab65acb0d88fb43ef95db9caadb62b28a9a664f05e1f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
