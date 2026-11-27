# awslabs/live-streaming-with-automated-multi-language-subtitling

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/live-streaming-with-automated-multi-language-subtitling](https://github.com/awslabs/live-streaming-with-automated-multi-language-subtitling)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/live-streaming-with-automated-multi-language-subtitling/blob/master/README.md)
- README blob SHA: f702ae44993007dd76dec1e0f53dc63bf5b385c4
- README bytes captured: 14104
- README truncated at capture limit: False
- Repository ID: 157429875
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Live Streaming with Automated Multi-Language Subtitling is a project to automatically generates multi-language subtitles for live streaming web video content. Adding subtitles to your live video content can help improve reach and access, exposing your content to a much larger audience.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:06:54+00:00

### Short excerpt (up to 300 words)

> **We currently have no The included AWS CloudFormation AWS Command Line Interface

### README headings

- Live Streaming with Automated Multi-Language Subtitling
- On this Page
- Architecture Overview
- Launching the stack
- Deployment
- Considerations:
- Profanity is showing up in my stream
- Amazon Transcribe streaming limits
- Why do Subtitiles show up after someone says something?
- Encoding profile
- Amazon VPC limits
- Changing input language
- Changing translated languages
- Regional deployment
- Additional considerations
- Troubleshooting
- Creating a custom build
- Prerequisites:
- 1. Clone the repo
- 2. Go to the deployment directory
- 3. Create an Amazon S3 Bucket
- 4. Create the deployment packages
- 5. Launch the CloudFormation template.
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> **We currently have no

### Architecture and design: Architecture Overview

> The included AWS CloudFormation

### Technology and requirements: Prerequisites:

> AWS Command Line Interface

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 42,952 |
| JavaScript | 7,418 |
| Shell | 6,174 |
| Dockerfile | 1,008 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/transcribedocker/Dockerfile (capture: captured)
- source/transcribedocker/package.json (capture: captured) — dependency clues: @aws-sdk/client-transcribe-streaming, @aws-sdk/eventstream-marshaller, @aws-sdk/util-utf8-node, aws-sdk, aws-signature-v4, query-string, sleep, websocket
- source/customresources/custom-resource-py/requirements.txt (capture: captured) — dependency clues: requests
- source/lambdafunctions/lambdaedge/requirements.txt (capture: captured) — dependency clues: aws_embedded_metrics, boto3, botocore
- source/lambdafunctions/SNSTriggerAWSTranslateLambda/requirements.txt (capture: captured) — dependency clues: boto3, botocore

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 171
- Forks at capture: 91
- Last updated: 2026-04-11T07:43:35Z
- Last pushed: 2021-12-16T19:17:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/live-streaming-with-automated-multi-language-subtitling)
- [README](https://github.com/awslabs/live-streaming-with-automated-multi-language-subtitling/blob/master/README.md)
- [Issues](https://github.com/awslabs/live-streaming-with-automated-multi-language-subtitling/issues)
- [Releases](https://github.com/awslabs/live-streaming-with-automated-multi-language-subtitling/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
