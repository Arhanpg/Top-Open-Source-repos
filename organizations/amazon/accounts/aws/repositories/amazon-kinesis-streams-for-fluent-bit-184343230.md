# aws/amazon-kinesis-streams-for-fluent-bit

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-kinesis-streams-for-fluent-bit](https://github.com/aws/amazon-kinesis-streams-for-fluent-bit)
- Default branch: mainline
- README: [Open upstream README](https://github.com/aws/amazon-kinesis-streams-for-fluent-bit/blob/mainline/README.md)
- README blob SHA: 85129121f2f17b042302103d02000e165a261138
- Repository ID: 184343230
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Fluent Bit output plugin for Kinesis Streams

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:53+00:00

### Short excerpt (up to 100 words)

> **NOTE: A new higher performance Fluent Bit Kinesis Plugin has been released.** Check out our official guidance. A Fluent Bit output plugin for Amazon Kinesis Data Streams. If you think you’ve found a potential security issue, please do not post it in the Issues. Instead, please follow the instructions here or email AWS security directly at aws-security@amazon.com. Run `make` to build `./bin/kinesis.so`. Then use with Fluent Bit: ./fluent-bit -e ./kinesis.so -i cpu \ -o kinesis \ -p "region=us-west-2" \ -p "stream=test-stream" For building Windows binaries, we need to install `mingw-64w` for cross-compilation. The same can be done using- sudo apt-get

### README headings

- Fluent Bit Plugin for Amazon Kinesis Data Streams
- Security disclosures
- Usage
- Plugin Options
- Permissions
- Credentials
- Environment Variables
- Fluent Bit Versions
- Example Fluent Bit Config File
- AWS for Fluent Bit
- GitHub
- Amazon ECR Public Gallery
- Docker Hub
- Amazon ECR
- KPL aggregation
- Tuning for aggregation
- Example Fluent Bit Aggregation Config File
- ZLIB Compression
- New Higher Performance Core Fluent Bit Plugin
- Do you plan to deprecate this older plugin?
- Which plugin should I use?
- How can I migrate to the higher performance plugin?
- Do you accept contributions to both plugins?

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 59,434 |
| Makefile | 1,495 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/amazon-kinesis-firehose-for-fluent-bit, github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/fluent/fluent-bit-go, github.com/golang/mock, github.com/golang/protobuf, github.com/jmespath/go-jmespath, github.com/json-iterator/go, github.com/lestrrat-go/strftime, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/pmezard/go-difflib, github.com/sirupsen/logrus, github.com/stretchr/testify, github.com/ugorji/go/codec, golang.org/x/sys, google.golang.org/protobuf, gopkg.in/yaml.v3
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 67
- Forks at capture: 43
- Last updated: 2026-07-07T05:43:19Z
- Last pushed: 2026-08-24T07:33:27Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-kinesis-streams-for-fluent-bit)
- [README](https://github.com/aws/amazon-kinesis-streams-for-fluent-bit/blob/mainline/README.md)
- [Issues](https://github.com/aws/amazon-kinesis-streams-for-fluent-bit/issues)
- [Releases](https://github.com/aws/amazon-kinesis-streams-for-fluent-bit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
