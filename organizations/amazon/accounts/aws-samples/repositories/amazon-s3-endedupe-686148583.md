# aws-samples/amazon-s3-endedupe

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-s3-endedupe](https://github.com/aws-samples/amazon-s3-endedupe)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-s3-endedupe/blob/main/README.md)
- README blob SHA: 96b0d357f2db1e15dbdc2eea0c70256835105855
- README bytes captured: 13611
- README truncated at capture limit: False
- Repository ID: 686148583
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T22:14:07+00:00

### Short excerpt (up to 300 words)

> This package provides an example, and some re-usable code, showing how to prevent out-of-order (for a single key) or duplicate processing of S3 event notifications

### README headings

- Example of handling duplicate/unordered/concurrent EventBridge S3 events
- Sample code notes
- What's in the package
- The SAM application
- Integration tests
- The sample client
- Deploying and exercising the example
- Deploying the example
- Running the integration tests
- Using the sample client
- How does it work?
- Example execution timelines
- Tradeoffs and alternatives
- Timing out the lock
- Delay queue
- Versioning
- Cleanup of the locking table

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Example of handling duplicate/unordered/concurrent EventBridge S3 events

> This package provides an example, and some re-usable code, showing how to prevent out-of-order (for a single key) or duplicate processing of S3 event notifications

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 33,698 |
| Shell | 3,273 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- endedupe/requirements.txt (capture: captured) — dependency clues: Pillow, boto3, pytest
- endedupe_integ_test/requirements.txt (capture: captured) — dependency clues: Pillow, attrs, boto3, botocore, coverage, exceptiongroup, iniconfig, jmespath, packaging, pluggy, pytest, python-dateutil, s3transfer, six, tomli, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 8
- Forks at capture: 1
- Last updated: 2026-11-03T13:35:28Z
- Last pushed: 2024-09-27T14:46:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-s3-endedupe)
- [README](https://github.com/aws-samples/amazon-s3-endedupe/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-s3-endedupe/issues)
- [Releases](https://github.com/aws-samples/amazon-s3-endedupe/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
