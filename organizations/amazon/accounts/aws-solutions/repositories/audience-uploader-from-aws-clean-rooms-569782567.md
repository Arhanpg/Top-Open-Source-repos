# aws-solutions/audience-uploader-from-aws-clean-rooms

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/audience-uploader-from-aws-clean-rooms](https://github.com/aws-solutions/audience-uploader-from-aws-clean-rooms)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/audience-uploader-from-aws-clean-rooms/blob/main/README.md)
- README blob SHA: 151e762046d7fd75e428eef6107e772980220530
- Repository ID: 569782567
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Audience Uploader from AWS Clean Rooms deploys the resources required to enable users to upload privacy-protected data to 3rd party platform to add users to a specific segment.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:33:04+00:00

### Short excerpt (up to 100 words)

> - Solution Overview - Architecture for Audience Uploader from AWS Clean Rooms - AWS CDK Constructs - Deployment - Creating a custom build - Collection of operational metrics Audience Uploader from AWS Clean Rooms deploys the resources required to enable users to upload privacy-protected data to 3rd party platform (TikTok in the case of this solution) to add users to a specific segment (i.e. audience). This solution can be easily installed in your AWS accounts via launching the provided AWS CloudFormation template. The solution provides a graphical user interface GUI to perform the following actions: - Login using Cognito credentials

### README headings

- Audience Uploader from AWS Clean Rooms
- Table of Contents
- Solution Overview
- Architecture
- AWS CDK Constructs
- Build
- Deployment
- Option 1 - using cdk deploy
- Option 2 - using aws cloudformation create-stack
- Configuration
- Creating a custom build
- Prerequisites
- 1. Download or clone this repo
- 2. Create a Python virtual environment for development
- 2. After introducing changes, run the unit tests to make sure the customizations don't break existing functionality
- TikTok Credentials Setup
- Manual Prerequisites
- Credentials Setup
- TikTok Data File Schema
- Testing
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 310,600 |
| Vue | 68,179 |
| Shell | 22,251 |
| JavaScript | 6,078 |
| HTML | 589 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/api/requirements.txt (capture: captured) — dependency clues: aws-xray-sdk, requests, wrapt
- source/api/setup.py (capture: captured)
- source/aws_lambda/setup.py (capture: captured)
- source/infrastructure/setup.py (capture: captured)
- source/website/package.json (capture: captured) — dependency clues: @vue/cli-plugin-babel, @vue/cli-plugin-eslint, @vue/cli-plugin-pwa, @vue/cli-service, aws-amplify, aws-amplify-vue, axios, babel-eslint, bootstrap, bootstrap-vue, core-js, dropzone, eslint, eslint-plugin-vue, jquery, jwt-decode, lodash, register-service-worker, vue, vue-highlightjs
- source/api/chalicelib/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 0
- Last updated: 2025-04-03T12:08:20Z
- Last pushed: 2024-01-22T22:26:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/audience-uploader-from-aws-clean-rooms)
- [README](https://github.com/aws-solutions/audience-uploader-from-aws-clean-rooms/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/audience-uploader-from-aws-clean-rooms/issues)
- [Releases](https://github.com/aws-solutions/audience-uploader-from-aws-clean-rooms/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
