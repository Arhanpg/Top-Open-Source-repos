# aws-amplify/amplify-ci-support

- Company: Amazon
- Account: aws-amplify
- Repository: https://github.com/aws-amplify/amplify-ci-support
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:20:50+00:00

## Project purpose

This package provides scripts and tools for managing Amplify projects in continuous integration environments, and for local developer setup of integration test environments.

## Why this project is used

Scripts and tools for managing Amplify projects in continuous integration environments, and for local developer setup of integration test environments.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Ruby, TypeScript, Shell, JavaScript, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-cdk/assert, @aws-cdk/aws-cloudwatch-actions, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-lambda-nodejs, @aws-cdk/aws-secretsmanager, @aws-cdk/aws-sns, @aws-cdk/aws-sns-subscriptions, @aws-cdk/aws-stepfunctions, @aws-cdk/aws-stepfunctions-tasks, @aws-cdk/core, @types/jest, @types/node, @types/totp-generator, ajv, aws-cdk, aws-cdk.core, aws_cdk.aws_apigateway, aws_cdk.aws_cloudfront, aws_cdk.aws_cloudfront_origins, aws_cdk.aws_cloudtrail, aws_cdk.aws_cloudwatch, aws_cdk.aws_cloudwatch_actions, aws_cdk.aws_codebuild, aws_cdk.aws_codepipeline, aws_cdk.aws_codepipeline_actions, aws_cdk.aws_cognito, aws_cdk.aws_iam, aws_cdk.aws_iot, aws_cdk.aws_kinesis, aws_cdk.aws_kinesisfirehose, aws_cdk.aws_kms, aws_cdk.aws_lambda, aws_cdk.aws_lambda_python, aws_cdk.aws_location, aws_cdk.aws_logs, aws_cdk.aws_pinpoint, aws_cdk.aws_s3, aws_cdk.aws_secretsmanager, aws_cdk.aws_sns, aws_cdk.aws_sns_subscriptions, aws_cdk.aws_ssm, aws_cdk.core, axios, black, boto3, esbuild, flake8, isort, jest, source-map-support, totp-generator, ts-jest, ts-node, typescript
- Build/package tools: Bundler manifest, npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/build_infrastructure/android/app.py, src/credentials_rotators/npm-token-rotation/src/lambda/create-new-token/index.ts, src/credentials_rotators/npm-token-rotation/src/lambda/step-01-publish-token/index.ts, src/credentials_rotators/npm-token-rotation/src/lambda/step-02-delete-old-token/index.ts

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-amplify/amplify-ci-support/blob/main/README.md
- README SHA: ea783955f7230627af1bea4026f9b68c05a707ac
- Manifests: requirements.txt, src/build_infrastructure/android/setup.py, src/credentials_rotators/npm-token-rotation/package.json, src/credentials_rotators/npm/requirements.txt, src/credentials_rotators/npm/setup.py, src/fastlane/release_actions/Gemfile
- Sampled source files: src/build_infrastructure/android/app.py, src/credentials_rotators/npm-token-rotation/src/lambda/create-new-token/index.ts, src/credentials_rotators/npm-token-rotation/src/lambda/step-01-publish-token/index.ts, src/credentials_rotators/npm-token-rotation/src/lambda/step-02-delete-old-token/index.ts
- Git tree state: captured
- Evidence fingerprint: d2a45547e34dbd8396f19d39bec0e9b96cf024ac337ac83316105c19ab54f322

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
