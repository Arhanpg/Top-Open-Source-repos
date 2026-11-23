# aws-amplify/amplify-ci-support

- Company: Amazon
- GitHub account: [https://github.com/aws-amplify](https://github.com/aws-amplify)
- Mapping status: official-directory-listed
- Repository: [aws-amplify/amplify-ci-support](https://github.com/aws-amplify/amplify-ci-support)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-amplify/amplify-ci-support/blob/main/README.md)
- README blob SHA: ea783955f7230627af1bea4026f9b68c05a707ac
- Repository ID: 257432907
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Scripts and tools for managing Amplify projects in continuous integration environments, and for local developer setup of integration test environments.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:58+00:00

### Short excerpt (up to 100 words)

> This package provides scripts and tools for managing Amplify projects in continuous integration environments, and for local developer setup of integration test environments. To deploy resources necessary to run the Android SDK's integration tests, see here. To build a configuration file that can be referenced from an iOS/Android device, see here.

### README headings

- Amplify CI Support

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 266,271 |
| Ruby | 51,763 |
| TypeScript | 45,971 |
| Shell | 8,955 |
| JavaScript | 4,074 |
| Batchfile | 2,176 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: aws_cdk.aws_apigateway, aws_cdk.aws_cloudfront, aws_cdk.aws_cloudfront_origins, aws_cdk.aws_cloudtrail, aws_cdk.aws_cloudwatch, aws_cdk.aws_codebuild, aws_cdk.aws_codepipeline, aws_cdk.aws_codepipeline_actions, aws_cdk.aws_cognito, aws_cdk.aws_iam, aws_cdk.aws_iot, aws_cdk.aws_kinesis, aws_cdk.aws_kinesisfirehose, aws_cdk.aws_kms, aws_cdk.aws_lambda_python, aws_cdk.aws_location, aws_cdk.aws_logs, aws_cdk.aws_pinpoint, aws_cdk.aws_s3, aws_cdk.aws_ssm
- src/build_infrastructure/android/setup.py (capture: captured)
- src/credentials_rotators/npm-token-rotation/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-cloudwatch-actions, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-lambda-nodejs, @aws-cdk/aws-secretsmanager, @aws-cdk/aws-sns, @aws-cdk/aws-sns-subscriptions, @aws-cdk/aws-stepfunctions, @aws-cdk/aws-stepfunctions-tasks, @aws-cdk/core, @types/jest, @types/node, @types/totp-generator, ajv, aws-cdk, axios, esbuild, jest, source-map-support
- src/credentials_rotators/npm/requirements.txt (capture: captured) — dependency clues: aws-cdk.core, aws_cdk.aws_cloudwatch_actions, aws_cdk.aws_iam, aws_cdk.aws_lambda, aws_cdk.aws_secretsmanager, aws_cdk.aws_sns, aws_cdk.aws_sns_subscriptions, boto3
- src/credentials_rotators/npm/setup.py (capture: captured)
- src/fastlane/release_actions/Gemfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 17
- Last updated: 2026-09-25T22:06:13Z
- Last pushed: 2026-10-23T16:24:03Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-amplify/amplify-ci-support)
- [README](https://github.com/aws-amplify/amplify-ci-support/blob/main/README.md)
- [Issues](https://github.com/aws-amplify/amplify-ci-support/issues)
- [Releases](https://github.com/aws-amplify/amplify-ci-support/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
