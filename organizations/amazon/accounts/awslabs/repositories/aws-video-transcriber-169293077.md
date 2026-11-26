# awslabs/aws-video-transcriber

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-video-transcriber](https://github.com/awslabs/aws-video-transcriber)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/aws-video-transcriber/blob/master/README.md)
- README blob SHA: d52af9f8170eebd77f998acfe2f50dfa1a676fe2
- README bytes captured: 9899
- README truncated at capture limit: False
- Repository ID: 169293077
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This solution provides a serverless single page web application and set of supporting Amazon API Gateway end points and AWS Lambda functions which allow users to upload videos into S3 and compute and edit closed captions. AWS services used: Amazon S3, Amazon Elastic Transcoder, Amazon Transcribe, Amazon API Gateway, AWS Lambda and Amazon DynamoDB.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:06:24+00:00

### Short excerpt (up to 300 words)

> This solution deploys the

### README headings

- AWS Video Transcriber
- Architecture
- Deploying the Solution
- Solution Pricing
- Example: In US East (N. Virginia) Region (us-east-1), process 1 hour video, edit video captions for 500 times, tranlsate 10000 characters captions
- Access the web interface
- Upload videos and perform operations related to video captions
- Upload video
- Proofread and edit captions
- Translate captions
- Burn captions into the video
- Download captions or video with captions
- Custom code and build locally.
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> This solution deploys the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 172,604 |
| Handlebars | 51,521 |
| Shell | 14,919 |
| HTML | 2,411 |
| CSS | 2,119 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/web/package.json (capture: captured) — dependency clues: axios, bootstrap, datatables.net, datatables.net-bs4, dropzone, file-saver, handlebars, jquery, vanilla-router
- source/lambda/createcaptions/package.json (capture: captured) — dependency clues: srt-parser-2
- source/lambda/customresource/package.json (capture: captured) — dependency clues: @anttiviljami/serverless-stack-output, axios, debug, serverless-parameters, uuid
- source/lambda/extractaudio/package.json (capture: captured) — dependency clues: @anttiviljami/serverless-stack-output, axios, debug, serverless-parameters, uuid
- source/lambda/putlanguage/package.json (capture: captured) — dependency clues: uuid
- source/lambda/reprocessvideo/package.json (capture: captured) — dependency clues: parse-aws-s3-url

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 180
- Forks at capture: 48
- Last updated: 2026-06-29T10:15:53Z
- Last pushed: 2025-09-29T07:14:28Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-video-transcriber)
- [README](https://github.com/awslabs/aws-video-transcriber/blob/master/README.md)
- [Issues](https://github.com/awslabs/aws-video-transcriber/issues)
- [Releases](https://github.com/awslabs/aws-video-transcriber/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
