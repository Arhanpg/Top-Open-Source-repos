# aws-samples/amazon-connect-cicd-workshop

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-connect-cicd-workshop](https://github.com/aws-samples/amazon-connect-cicd-workshop)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-connect-cicd-workshop/blob/main/README.md)
- README blob SHA: ddc9fcd4ee529d60478f0092fafb993ecaade96f
- README bytes captured: 24878
- README truncated at capture limit: False
- Repository ID: 678121490
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:17:47+00:00

### Short excerpt (up to 300 words)

> The pipelines that deploy Four AWS accounts Tooling 1. If your solution

### README headings

- Amazon Connect Automation using AWS Developer Tools, AWS Cloud Development Kit (CDK), and TypeScript
- Concepts
- CI/CD Pipeline Architecture
- Monorepo Architecture
- Amazon Connect Flows
- Limitations
- Prerequisites
- AWS Cloud9
- AWS and GitHub Configuration Steps
- Develop, Stage, and Production accounts
- CDK Bootstrap
- Create the AWS IAM Roles that will be used by the AWS CodePipelines
- Fork this repository to your GitHub account
- Clone the forked repository in your IDE (e.g., AWS Cloud9)
- Create a GitHub connection in the Tooling account
- Update amzconnect-devops-pipelines/env/accountvars.json
- Update amzconnect-devops-pipelines/env/devops.json
- Push the modified files to your repository's main branch
- Deploy the CodePipelines
- Create a GitHub Webhook
- Add the GitHub Webhook secret to AWS Secrets Manager
- Run the individual pipelines in each environment
- Create a develop branch
- Create an Amazon Connect instance using the amzconnect-instance-develop CodePipeline
- Create all the supporting infrastructure (e.g., Amazon Lex) except for the Lambda functions
- Create the Lambda Functions
- Deploy the Contact Flows
- Additional Details
- How to Deploy Contact Flows
- Test the solution

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: CI/CD Pipeline Architecture

> The pipelines that deploy

### Technology and requirements: Prerequisites

> Four AWS accounts Tooling

### Limitations and security: Limitations

> 1. If your solution

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 122,432 |
| JavaScript | 45,927 |
| Shell | 445 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured)
- amzconnect-contact-flows/package.json (capture: captured) — dependency clues: @aws-sdk/client-codecommit, @aws-sdk/client-connect, @aws-sdk/client-lambda, @aws-sdk/client-lex-models-v2, @aws-sdk/client-s3, @aws-sdk/client-ssm, @aws-sdk/lib-storage, @types/jest, @types/node, @types/node-fetch, @types/prettier, aws-cdk, aws-cdk-lib, aws-xray-sdk-core, constructs, fs-extra, jest, jszip, node-fetch, rmdir-cli
- amzconnect-devops-pipelines/package.json (capture: captured) — dependency clues: @aws-cdk/aws-logs, @aws-lambda-powertools/logger, @aws-lambda-powertools/metrics, @aws-lambda-powertools/tracer, @aws-sdk/client-codecommit, @aws-sdk/client-codepipeline, @aws-sdk/client-connect, @aws-sdk/client-lambda, @aws-sdk/client-lex-models-v2, @aws-sdk/client-s3, @aws-sdk/client-secrets-manager, @aws-sdk/client-ssm, @aws-sdk/lib-storage, @middy/core, @types/aws-lambda, @types/aws-regions, @types/jest, @types/node, @types/node-fetch, @types/prettier
- amzconnect-instance/package.json (capture: captured) — dependency clues: @types/jest, @types/node, @types/node-fetch, @types/prettier, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdk-nag, constructs, eslint, fs-extra, jest, jszip, node-fetch, rmdir-cli, shelljs, source-map-support, ts-jest, ts-node
- amzconnect-lambdas/package.json (capture: captured) — dependency clues: @aws-lambda-powertools/logger, @aws-lambda-powertools/metrics, @aws-lambda-powertools/tracer, @aws-sdk/client-codecommit, @aws-sdk/client-codepipeline, @aws-sdk/client-connect, @aws-sdk/client-lambda, @aws-sdk/client-lex-models-v2, @aws-sdk/client-s3, @aws-sdk/client-ssm, @aws-sdk/lib-storage, @middy/core, @types/aws-lambda, @types/jest, @types/js-beautify, @types/node, @types/node-fetch, @types/prettier, @types/readable-stream, @typescript-eslint/eslint-plugin
- amzconnect-supporting-infra/package.json (capture: captured) — dependency clues: @aws-sdk/client-codecommit, @aws-sdk/client-connect, @aws-sdk/client-lambda, @aws-sdk/client-lex-models-v2, @aws-sdk/client-s3, @aws-sdk/client-ssm, @aws-sdk/lib-storage, @types/jest, @types/node, @types/node-fetch, @types/prettier, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, aws-xray-sdk-core, cdk-nag, constructs, eslint, fs-extra

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 18
- Forks at capture: 61
- Last updated: 2026-11-18T23:38:24Z
- Last pushed: 2024-08-11T14:25:46Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-connect-cicd-workshop)
- [README](https://github.com/aws-samples/amazon-connect-cicd-workshop/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-connect-cicd-workshop/issues)
- [Releases](https://github.com/aws-samples/amazon-connect-cicd-workshop/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
