# aws-solutions/cost-optimizer-for-amazon-workspaces

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:51:04+00:00

## Project purpose

*🚀 Solution Landing Page** | **🚧 Feature request** | **🐛 Bug Report**

## Why this project is used

This solution analyzes all of your Amazon WorkSpaces usage data and automatically converts the WorkSpace to the most cost-effective billing option (hourly or monthly), depending on your individual usage. Use this with a single account, or with AWS Organizations across multiple accounts, to help you monitor your WorkSpace usage and optimize costs.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, TypeScript, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-cdk/assert, @eslint/js, @types/jest, @types/node, @types/sinon, aws-cdk, aws-cdk-lib, aws-lambda-powertools, boto3, botocore, cdk-nag, certifi, charset-normalizer, constructs, eslint, eslint-config-prettier, eslint-plugin-headers, eslint-plugin-prettier, globals, idna, jest, jmespath, prettier, python-dateutil, requests, s3transfer, sinon, six, ts-jest, ts-node, typescript, typescript-eslint, urllib3
- Build/package tools: Docker build configuration, npm-compatible manifest, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/workspaces_app/main.py, source/lib/cdk-helper/add-cfn-nag-suppression.ts, source/lib/cdk-helper/condition-aspect.ts, source/lib/cdk-helper/override-logical-id.ts

## Setup and usage

- Getting Started: For deployment flexability and backwards compatability, there are two ways of deploying this solution: via Cloudformation and via CDK. The simplest way to get started is via AWS Cloudformation's WebUI. The programatic way via CDK allows customization of input parameters. Feel free to choose either ways of deployment to fit your needs.
- Getting Started: Deploy via the CloudFormation Template for WorkSpaces Cost Optimizer
- Getting Started: Deploy via CDKv2 with npm:
- Getting Started: Preconfigure aws profile
- Getting Started: git clone git@github.com:aws-solutions/cost-optimizer-for-amazon-workspaces.git

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces/blob/main/README.md
- README SHA: 2026688cb369939bf1f237484668824fbb640bac
- Manifests: source/Dockerfile, source/package.json, source/pyproject.toml
- Sampled source files: source/workspaces_app/main.py, source/lib/cdk-helper/add-cfn-nag-suppression.ts, source/lib/cdk-helper/condition-aspect.ts, source/lib/cdk-helper/override-logical-id.ts
- Git tree state: captured
- Evidence fingerprint: 36b15c2e3d2352ff05ab6c20a47d10d19c262ffdc27b70548f0c7816a9116363

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
