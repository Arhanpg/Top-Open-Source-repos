# aws-samples/ai-powered-text-insights

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/ai-powered-text-insights](https://github.com/aws-samples/ai-powered-text-insights)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/ai-powered-text-insights/blob/main/README.md)
- README blob SHA: 4de5ed6a78f5663879b6c9164fb4e135b539dccd
- README bytes captured: 18483
- README truncated at capture limit: False
- Repository ID: 536871613
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T04:45:07+00:00

### Short excerpt (up to 300 words)

> This package includes the Twitter provides endpoints that Deploying the sample application AWS CLI. Refer to

### README headings

- AI Powered Text Insights
- Table of Content
- Overview
- Architecture
- Deployment
- Prerequisites
- Backend resources
- 1. Data format
- 2. Activate the Lookout for Metrics detector
- (Optional) Test the application by streaming sample X.com posts
- (Optional) Stream real X.com posts to the application
- 1. Create application
- 2. Create environment
- 3. Deploy the environment
- 4. Create service
- 5. Create secret to store the Twitter Bearer token
- 6. Edit service manifest
- 7. Add permission to write to the queue
- 8. Deploy service
- 9. Rules examples for filtered stream
- Cost
- Optional costs
- Visualize your insights with Amazon QuickSight
- Clean up
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> This package includes the

### Getting started and usage: 9. Rules examples for filtered stream

> Twitter provides endpoints that

### Architecture and design: Architecture

> Deploying the sample application

### Technology and requirements: Prerequisites

> AWS CLI. Refer to

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 42,267 |
| Dockerfile | 261 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- stream-getter/Dockerfile (capture: captured)
- stream-getter/requirements.txt (capture: captured) — dependency clues: backoff, boto3, botocore, requests
- backend/lambdas/process_post/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, boto3, demoji, langchain, langchain-core, langchain_aws
- backend/lambdas/save_post/requirements.txt (capture: captured) — dependency clues: jsonlines
- backend/lambdas/workflow_from_sqs/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools
- backend/lambdas/custom_resources/lookout4metrics/requirements.txt (capture: captured) — dependency clues: boto3, botocore, cfnresponse, crhelper

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 10
- Forks at capture: 3
- Last updated: 2026-02-04T21:43:05Z
- Last pushed: 2024-08-02T16:54:35Z
- Topics: athena, comprehend, ecr, fargate, kms, lambda, location-service, lookout-for-metrics, quicksight, s3, sagemaker, sns, sqs, step-functions

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/ai-powered-text-insights)
- [README](https://github.com/aws-samples/ai-powered-text-insights/blob/main/README.md)
- [Issues](https://github.com/aws-samples/ai-powered-text-insights/issues)
- [Releases](https://github.com/aws-samples/ai-powered-text-insights/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
