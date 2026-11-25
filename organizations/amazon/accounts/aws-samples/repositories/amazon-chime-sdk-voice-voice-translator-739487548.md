# aws-samples/amazon-chime-sdk-voice-voice-translator

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-chime-sdk-voice-voice-translator](https://github.com/aws-samples/amazon-chime-sdk-voice-voice-translator)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-chime-sdk-voice-voice-translator/blob/main/README.md)
- README blob SHA: ec760d9530cf31fe5dfc112f894460afb3f9f8ee
- README bytes captured: 15827
- README truncated at capture limit: False
- Repository ID: 739487548
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T03:29:22+00:00

### Short excerpt (up to 300 words)

> This project leverages the

### README headings

- Amazon Chime SDK Voice to Voice Translator
- Overview
- How it works
- Meeting Setup
- Call Legs
- Inbound Call from PSTN
- Outbound Call to PBX
- Meeting Audio Processing
- Preventing `Speak` action interruptions
- No existing response being played
- Existing response being played
- Determining if a previous action is being played
- SETTING UP RESOURCES NEEDED TO RUN KVS CONSUMER ON ECS
- KVS Consumer breakdown
- Conversion of Audio Format using ffmpeg
- MEDIA STREAM PIPELINE
- Testing It Out
- Deploy
- Create Service Linked Role
- CDK Deployment
- Cleanup

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> This project leverages the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 110,403 |
| JavaScript | 19,628 |
| Shell | 1,648 |
| Python | 865 |
| HTML | 533 |
| CSS | 372 |
| Dockerfile | 226 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-bedrock-runtime, @aws-sdk/client-chime-sdk-media-pipelines, @aws-sdk/client-chime-sdk-meetings, @aws-sdk/client-chime-sdk-voice, @aws-sdk/client-cloudwatch, @aws-sdk/client-dynamodb, @aws-sdk/client-ecs, @aws-sdk/client-kinesis-video, @aws-sdk/client-kinesis-video-media, @aws-sdk/client-lambda, @aws-sdk/client-transcribe-streaming, @aws-sdk/client-translate, @types/aws-lambda, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, aws-lambda, axios
- utils/pyproject.toml (capture: captured) — dependency clues: boto3
- src/resources/kvsConsumer/Dockerfile (capture: captured)
- src/resources/kvsConsumer/src/package.json (capture: captured) — dependency clues: @aws-sdk/client-chime-sdk-voice, @aws-sdk/client-dynamodb, @aws-sdk/client-kinesis-video, @aws-sdk/client-kinesis-video-media, @aws-sdk/client-transcribe-streaming, @aws-sdk/client-translate, @types/aws-lambda, @types/fluent-ffmpeg, @types/node, fastify, fluent-ffmpeg, typescript
- src/resources/server/assets/site/package.json (capture: captured) — dependency clues: @aws-amplify/ui-react, @babel/core, @babel/preset-env, @babel/preset-react, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @types/react, @types/react-dom, aws-amplify, babel-loader, css-loader, dotenv-webpack, html-webpack-plugin, react, react-dom, react-phone-number-input, sip.js, style-loader, ts-loader

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 12
- Forks at capture: 4
- Last updated: 2025-03-28T17:44:33Z
- Last pushed: 2024-12-14T09:48:42Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-chime-sdk-voice-voice-translator)
- [README](https://github.com/aws-samples/amazon-chime-sdk-voice-voice-translator/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-chime-sdk-voice-voice-translator/issues)
- [Releases](https://github.com/aws-samples/amazon-chime-sdk-voice-voice-translator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
