# aws/amazon-kinesis-video-streams-parser-library

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-kinesis-video-streams-parser-library](https://github.com/aws/amazon-kinesis-video-streams-parser-library)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-kinesis-video-streams-parser-library/blob/master/README.md)
- README blob SHA: 93357e170bbac5f7c9488a879a3030b4557d1c64
- Repository ID: 111009803
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon Kinesis Video Streams parser library is for developers to include in their applications that makes it easy to work with the output of video streams such as retrieving frame-level objects, metadata for fragments, and more.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:54+00:00

### Short excerpt (up to 100 words)

> This library is licensed under the Apache 2.0 License. The Amazon Kinesis Video Streams Parser Library for Java enables Java developers to parse the streams returned by `GetMedia` calls to Amazon Kinesis Video. It contains: * A streaming Mkv Parser called `StreamingMkvReader` that provides an iterative interface to read the `MkvElement`s in a stream. * Applications such as `OutputSegmentMerger` and `FragmentMetadataVisitor` built using the `StreamingMkvReader` . * A callback based parser called `EBMLParser` that minimizes data buffering and copying. `StreamingMkvReader` is built on top of `EBMLParser` * Unit tests for the applications and parsers that demonstrate how the applications work.

### README headings

- Amazon Kinesis Video Streams Parser Library
- License
- Introduction
- Building from Source
- Details
- StreamingMkvReader
- MkvElement
- MkvElementVisitor
- Visitors
- ResponseStreamConsumers
- MergedOutputPiper
- Example
- KinesisVideoExample
- KinesisVideoRendererExample
- KinesisVideoGStreamerPiperExample
- KinesisVideo - Rekognition Examples
- KinesisVideoRekognitionIntegrationExample
- KinesisVideoRekognitionLambdaExample
- Release Notes
- Release 1.2.4 (Mar 2022)
- Release 1.2.3 (Feb 2022)
- Release 1.2.2 (Jan 2022)
- Release 1.2.1 (Jan 2022)
- Release 1.2.0 (Jan 2022)
- Release 1.1.0 (Dec 2021)
- Release 1.0.15 (Aug 2020)
- Release 1.0.14 (Aug 2019)
- Release 1.0.13 (Apr 2019)
- Release 1.0.12 (Mar 2019)
- Release 1.0.11 (Mar 2019)

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 611,868 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-kinesis-client, amazon-kinesis-video-streams-parser-library, amazon-kinesis-video-streams-producer-sdk-java, aws-java-sdk-bom, aws-java-sdk-dynamodb, aws-java-sdk-kinesis, aws-java-sdk-kinesisvideo, aws-java-sdk-rekognition, aws-lambda-java-core, aws-lambda-java-events, aws-lambda-java-log4j2, commons-lang3, jackson-databind, jackson-dataformat-cbor, jcodec, jcodec-javase, junit, log4j-slf4j-impl, lombok, lombok-maven-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 110
- Forks at capture: 58
- Last updated: 2026-08-16T07:02:01Z
- Last pushed: 2026-06-30T04:43:33Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-kinesis-video-streams-parser-library)
- [README](https://github.com/aws/amazon-kinesis-video-streams-parser-library/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-kinesis-video-streams-parser-library/issues)
- [Releases](https://github.com/aws/amazon-kinesis-video-streams-parser-library/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
