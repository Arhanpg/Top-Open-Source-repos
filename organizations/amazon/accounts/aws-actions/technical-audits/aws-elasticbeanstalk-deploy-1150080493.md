# aws-actions/aws-elasticbeanstalk-deploy

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/aws-elasticbeanstalk-deploy
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:12:21+00:00

## Project purpose

A GitHub Action for deploying applications to AWS Elastic Beanstalk with automatic version management, environment creation, health monitoring, and intelligent retry logic. It supports both Beanstalk Standard (EC2-backed) environments and Beanstalk Cluster (EKS-backed) container environments.

## Why this project is used

GitHub Action for deploying applications to AWS Elastic Beanstalk

## Core features

- **Automatic Environment Creation**: Creates Elastic Beanstalk applications and environments if they don't exist: **Automatic Environment Creation**: Creates Elastic Beanstalk applications and environments if they don't exist
  - Evidence: README.md#Features
- **Two Deployment Modes**: Deploys to Beanstalk Standard (EC2-backed) environments or to Beanstalk Cluster (EKS-backed) container environments: **Two Deployment Modes**: Deploys to Beanstalk Standard (EC2-backed) environments or to Beanstalk Cluster (EKS-backed) container environments
  - Evidence: README.md#Features
- **Flexible Container Sourcing**: For Beanstalk Cluster environments, deploy a pre-built image or let Elastic Beanstalk build one from your source: **Flexible Container Sourcing**: For Beanstalk Cluster environments, deploy a pre-built image or let Elastic Beanstalk build one from your source
  - Evidence: README.md#Features
- **Deployment Package Management**: Auto-creates deployment packages from your repository or uses pre-built packages: **Deployment Package Management**: Auto-creates deployment packages from your repository or uses pre-built packages
  - Evidence: README.md#Features
- **S3 Upload**: Uploads deployment artifacts to S3 for version management: **S3 Upload**: Uploads deployment artifacts to S3 for version management
  - Evidence: README.md#Features
- **Health Monitoring**: Waits for deployment completion and environment health recovery: **Health Monitoring**: Waits for deployment completion and environment health recovery
  - Evidence: README.md#Features
- **Event Streaming**: Displays real-time deployment events in GitHub Actions logs: **Event Streaming**: Displays real-time deployment events in GitHub Actions logs
  - Evidence: README.md#Features
- **Intelligent Retries**: Exponential backoff for transient API failures: **Intelligent Retries**: Exponential backoff for transient API failures
  - Evidence: README.md#Features
- **Version Reuse**: Optionally deploy an application version that already exists under the label, to promote one version across environments: **Version Reuse**: Optionally deploy an application version that already exists under the label, to promote one version across environments
  - Evidence: README.md#Features

## Technology stack

- Languages: TypeScript, JavaScript, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @actions/exec, @aws-sdk/client-elastic-beanstalk, @aws-sdk/client-s3, @aws-sdk/client-sts, @types/archiver, @types/jest, @types/node, @vercel/ncc, archiver, ignore, jest, ts-jest, typescript
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/__tests__/conflict_detection.test.ts, src/__tests__/option_settings_validation.test.ts, src/__tests__/s3_operations.test.ts, src/__tests__/setup.ts

## Setup and usage

- Quick Start: Create a workflow file in your repository at .github/workflows/deploy-to-elastic-beanstalk.yml (or any name you prefer under .github/workflows/). The core deploy step looks like this:
- Quick Start: - name: Deploy to Elastic Beanstalk
- Quick Start: uses: aws-actions/aws-elasticbeanstalk-deploy@v1
- Quick Start: aws-region: ${{ env.AWS_REGION }}
- Quick Start: application-name: ${{ env.APPLICATION_NAME }}
- Quick Start: environment-name: ${{ env.ENVIRONMENT_NAME }}
- Quick Start: solution-stack-name: '64bit Amazon Linux 2023 v4.3.0 running Python 3.11'
- Quick Start: "Namespace": "aws:autoscaling:launchconfiguration",

## Limitations and caveats

- Platform Configuration: When **creating a new Beanstalk Standard environment**, you must provide **exactly one** of the following:
- Platform Configuration: | Input | Description |
- Platform Configuration: |-------|-------------|
- Platform Configuration: | solution-stack-name | Solution stack name (e.g., 64bit Amazon Linux 2023 v4.9.2 running Python 3.14) |
- Platform Configuration: | platform-arn | Platform ARN (e.g., arn:aws:elasticbeanstalk:us-east-1::platform/Python 3.14 running on 64bit Amazon Linux 2023/4.9.2) |
- Platform Configuration: You can find the list of supported platforms and example values in the AWS Elastic Beanstalk documentation for supported platforms.
- Platform Configuration: When **deploying to an existing environment**, these inputs are **optional**. The existing environment's platform configuration will be used if neither is provided.
- Platform Configuration: > When you specify solution-stack-name or platform-arn, each deployment updates your environment to that platform version if it differs from the current one. To deploy without changing the platform version, omit both options.

## Evidence and provenance

- README: https://github.com/aws-actions/aws-elasticbeanstalk-deploy/blob/main/README.md
- README SHA: 1082da52a7190e0ca306442c293065f09723422a
- Manifests: package.json
- Sampled source files: src/__tests__/conflict_detection.test.ts, src/__tests__/option_settings_validation.test.ts, src/__tests__/s3_operations.test.ts, src/__tests__/setup.ts
- Git tree state: captured
- Evidence fingerprint: 2dece6b0c3de12d19c7a29d85d20e38497ec3ab114543ad12dee489d7c4ad543

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
