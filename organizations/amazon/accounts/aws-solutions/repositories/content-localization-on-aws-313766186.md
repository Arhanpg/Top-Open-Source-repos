# aws-solutions/content-localization-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/content-localization-on-aws](https://github.com/aws-solutions/content-localization-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/content-localization-on-aws/blob/main/README.md)
- README blob SHA: db2bd42823297de1ad8267264c314dc981274b7b
- Repository ID: 313766186
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Automatically generate multi-language subtitles using AWS  AI/ML services. Machine generated subtitles can be edited to improve accuracy and downstream tracks will automatically be regenerated based on the edits. Built on Media Insights Engine (https://github.com/awslabs/aws-media-insights-engine)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:36+00:00

### Short excerpt (up to 100 words)

> Welcome to the Content Localization on AWS project! This project will help you extend the reach of your VOD content by quickly and efficiently creating accurate multi-language subtitles using AWS AI Services. You can make manual corrections to the automatically created subtitles and use advanced AWS AI Service customization features to improve the results of the automation for your content domain. Content Localization is built on Media Insights on AWS, a framework that helps accelerate the development of serverless applications that process video, images, audio, and text with artificial intelligence services and multimedia services on AWS. Localization is the process

### README headings

- NOTE: This solution is no longer being supported
- Content Localization on AWS
- Why use customizations and human-in-the-loop?
- Doesn’t content localization involve more than just subtitles?
- Screenshots
- COST
- Subtitle workflow
- Search Capabilities:
- Advanced Installation Options
- Building the solution from source code
- *Option 1:* Install Content Localization on AWS over an existing Media Insights on AWS stack
- *Option 2:* Install Content Localization on AWS with a new Media Insights on AWS stack
- Tests
- Advanced Usage
- Starting workflows from the command line
- Starting workflows from a Python Lambda function
- Starting workflows from an S3 trigger
- Adding new operators and extending data stream consumers:
- Validate metadata in OpenSearch
- User Authentication
- User account management
- Uninstall
- Option 1: Uninstall using the AWS Management Console
- Option 2: Uninstall using AWS Command Line Interface
- Deleting Content Localization S3 buckets
- Collection of operational metrics
- *Option 1:* Deploy Media Insights on AWS separately with metric reporting disabled
- *Option 2:* Modify the source template that is used to deploy Media Insights on AWS as a nested stack
- Help
- Known Issues

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Vue | 372,851 |
| Python | 147,004 |
| Shell | 33,904 |
| JavaScript | 8,850 |
| CSS | 2,653 |
| HTML | 724 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/anonymized-data-logger/requirements.txt (capture: captured) — dependency clues: requests, urllib3
- source/consumer/requirements.txt (capture: captured) — dependency clues: elasticsearch, requests-aws4auth
- source/helper/requirements.txt (capture: content_not_returned)
- source/website/package.json (capture: captured) — dependency clues: @eslint/eslintrc, @vitejs/plugin-vue, @vue/compat, @vue/compiler-sfc, aws-amplify, aws-amplify-vue, axios, bootstrap, bootstrap-vue, chart.js, diff, dropzone, eslint, eslint-plugin-vue, jquery, jwt-decode, latest-version, lodash, number-to-words, unplugin-vue-components
- test/e2e/requirements.txt (capture: captured) — dependency clues: boto3, pytest, requests, requests-aws4auth, selenium, webdriver-manager
- test/unit/requirements.txt (capture: captured) — dependency clues: boto3, botocore, pytest, pytest-cov, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 44
- Forks at capture: 18
- Last updated: 2026-07-10T00:02:42Z
- Last pushed: 2025-08-29T16:24:40Z
- Topics: amazon-comprehend, amazon-polly, amazon-transcribe, amazon-translate, audio, aws-media-insights-engine, captions, content-analysis, localisation, localization, media, mie, nlp, nlp-machine-learning, speech-to-text, subtitles, video, video-on-demand, vod

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/content-localization-on-aws)
- [README](https://github.com/aws-solutions/content-localization-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/content-localization-on-aws/issues)
- [Releases](https://github.com/aws-solutions/content-localization-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
