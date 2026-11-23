# amazon-connect/amazon-connect-audio-utils

- Company: Amazon
- GitHub account: [https://github.com/amazon-connect](https://github.com/amazon-connect)
- Mapping status: official-directory-listed
- Repository: [amazon-connect/amazon-connect-audio-utils](https://github.com/amazon-connect/amazon-connect-audio-utils)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-connect/amazon-connect-audio-utils/blob/master/README.md)
- README blob SHA: 4df2dabf82dad0eb61a3792281b68b7e043ed3cc
- Repository ID: 257719482
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A set of tools for working with audio created from Amazon Connect

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:38:31+00:00

### Short excerpt (up to 100 words)

> This is a set of lambda and ffmpeg powered tools for working with audio from Amazon Connect This layer includes: * statically compiled ffmpeg * boto3 * pydub * requests * ffmpeg-python This function overlays two audio tracks and accepts input in the following form: { "sources": [{ "Bucket": "", "Key": "" }, { "Bucket": "", "Key": "" }], "target": { "Bucket": "", "Key": "" } } This function mutes/removes sections of audio from a track based no timestamps and accepts input in the following form: { "source": { "Bucket": "", "Key": "" }, "target": { "Bucket": "", "Key": ""

### README headings

- Connect Audio Utils
- Tools
- Connect Audio Utils Layer
- Overlay Audio
- Redact Audio
- Build Instructions
- Useful commands
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,645 |
| TypeScript | 1,686 |
| JavaScript | 418 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-lambda, @aws-cdk/core, @types/jest, @types/node, aws-cdk, jest, source-map-support, ts-jest, ts-node, typescript
- resources/connect-audio-utils-layer/requirements.txt (capture: captured) — dependency clues: aws-xray-sdk, boto3, ffmpeg-python, pydub, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 4
- Last updated: 2023-06-01T13:22:26Z
- Last pushed: 2020-04-21T22:30:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-connect/amazon-connect-audio-utils)
- [README](https://github.com/amazon-connect/amazon-connect-audio-utils/blob/master/README.md)
- [Issues](https://github.com/amazon-connect/amazon-connect-audio-utils/issues)
- [Releases](https://github.com/amazon-connect/amazon-connect-audio-utils/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
