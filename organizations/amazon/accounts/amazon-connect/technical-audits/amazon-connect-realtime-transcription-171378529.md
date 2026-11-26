# amazon-connect/amazon-connect-realtime-transcription

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/amazon-connect-realtime-transcription
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:52:21+00:00

## Project purpose

Making it easy to get started with Amazon Connect live audio streaming and real-time transcription using Amazon Transcribe.

## Why this project is used

Transcribe Live Customer Audio for Amazon Connect using Amazon Kinesis Video Streams and Amazon Transcribe

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, JavaScript, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/java/com/amazonaws/kvstranscribestreaming/AudioUtils.java, src/main/java/com/amazonaws/kvstranscribestreaming/KVSContactTagProcessor.java, src/main/java/com/amazonaws/kvstranscribestreaming/KVSStreamTrackObject.java, src/main/java/com/amazonaws/kvstranscribestreaming/KVSTranscribeStreamingLambda.java

## Setup and usage

- Getting Started: Getting started with this project is easy. The most basic use case of capturing audio in the Amazon Connect IVR can be accomplished by downloading the pre-packaged Lambda Functions, deploying the CloudFormation template in your account, and importing the Contact Flows into your Amazon Connect Instance.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-connect/amazon-connect-realtime-transcription/blob/master/README.md
- README SHA: f1ad52ddd9214059d78defdf81aeabca6669916a
- Manifests: build.gradle
- Sampled source files: src/main/java/com/amazonaws/kvstranscribestreaming/AudioUtils.java, src/main/java/com/amazonaws/kvstranscribestreaming/KVSContactTagProcessor.java, src/main/java/com/amazonaws/kvstranscribestreaming/KVSStreamTrackObject.java, src/main/java/com/amazonaws/kvstranscribestreaming/KVSTranscribeStreamingLambda.java
- Git tree state: captured
- Evidence fingerprint: 2acd58f4d99993bfe78b7207b4212b33ad7e86f77c012753060305f3660a6af6

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
