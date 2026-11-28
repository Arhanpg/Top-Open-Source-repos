# aws-samples/amazon-s3-object-lambda-decompression

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-s3-object-lambda-decompression](https://github.com/aws-samples/amazon-s3-object-lambda-decompression)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-s3-object-lambda-decompression/blob/main/README.md)
- README blob SHA: 48055d9a5b8fc9c6c3d7ef4877915c2fb6f04180
- README bytes captured: 1374
- README truncated at capture limit: False
- Repository ID: 349173738
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Lambda function S3ObjectLambdaDecompression, is equipped to decompress objects stored in S3 in one of six compressed file formats including bzip2, gzip, snappy, zlib, zstandard and ZIP.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T02:55:42+00:00

### Short excerpt (up to 300 words)

> lambda-code : contains the source code for the six lambda functions, with each sub-directory containing the function itself, a unit-test file, a Makefile containing build

### README headings

- A quick tour of this repository
- How to use this repository

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: A quick tour of this repository

> lambda-code : contains the source code for the six lambda functions, with each sub-directory containing the function itself, a unit-test file, a Makefile containing build

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 27,868 |
| Python | 13,985 |
| Makefile | 746 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- lambda-code/decompress_bz2/requirements.txt (capture: captured)
- lambda-code/decompress_gz/requirements.txt (capture: captured)
- lambda-code/decompress_snappy/Makefile (capture: captured)
- lambda-code/decompress_snappy/requirements.txt (capture: captured) — dependency clues: python-snappy
- lambda-code/decompress_zip/pom.xml (capture: captured) — dependency clues: aws-java-sdk-bom, aws-java-sdk-lambda, aws-java-sdk-s3, aws-lambda-java-core, aws-lambda-java-events, commons-io, commons-lang3, maven-compiler-plugin, maven-failsafe-plugin, maven-practice, maven-shade-plugin, maven-surefire-plugin, powermock-api-mockito2, powermock-module-junit4, spring-web
- lambda-code/decompress_zlib/requirements.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 20
- Forks at capture: 5
- Last updated: 2025-03-11T20:43:02Z
- Last pushed: 2024-06-07T10:20:29Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-s3-object-lambda-decompression)
- [README](https://github.com/aws-samples/amazon-s3-object-lambda-decompression/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-s3-object-lambda-decompression/issues)
- [Releases](https://github.com/aws-samples/amazon-s3-object-lambda-decompression/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
