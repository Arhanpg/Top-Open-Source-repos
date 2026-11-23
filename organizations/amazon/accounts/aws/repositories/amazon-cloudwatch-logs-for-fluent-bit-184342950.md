# aws/amazon-cloudwatch-logs-for-fluent-bit

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-cloudwatch-logs-for-fluent-bit](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit)
- Default branch: mainline
- README: [Open upstream README](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit/blob/mainline/README.md)
- README blob SHA: d0ce29e454fd13eb7bba6d0453bfa3e2a2e84693
- Repository ID: 184342950
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Fluent Bit output plugin for CloudWatch Logs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:02:06+00:00

### Short excerpt (up to 100 words)

> **NOTE: A new higher performance Fluent Bit CloudWatch Logs Plugin has been released.** Check out our official guidance. A Fluent Bit output plugin for CloudWatch Logs If you think you’ve found a potential security issue, please do not post it in the Issues. Instead, please follow the instructions here or email AWS security directly at aws-security@amazon.com. Run `make` to build `./bin/cloudwatch.so`. Then use with Fluent Bit: ./fluent-bit -e ./cloudwatch.so -i cpu \ -o cloudwatch \ -p "region=us-west-2" \ -p "log_group_name=fluent-bit-cloudwatch" \ -p "log_stream_name=testing" \ -p "auto_create_group=true" For building Windows binaries, we need to install `mingw-w64` for cross-compilation. The same can

### README headings

- Fluent Bit Plugin for CloudWatch Logs
- Security disclosures
- Usage
- Plugin Options
- Permissions
- Credentials
- Environment Variables
- Retries and Buffering
- Templating Log Group and Stream Names
- Templating Log Group and Stream Names based on Kubernetes metadata
- New Higher Performance Core Fluent Bit Plugin
- Do you plan to deprecate this older plugin?
- Which plugin should I use?
- How can I migrate to the higher performance plugin?
- Do you accept contributions to both plugins?
- Fluent Bit Versions
- Example Fluent Bit Config File
- AWS for Fluent Bit
- GitHub
- Amazon ECR Public Gallery
- Docker Hub
- Amazon ECR
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 95,774 |
| Makefile | 1,660 |
| Shell | 1,513 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/amazon-kinesis-firehose-for-fluent-bit, github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/fluent/fluent-bit-go, github.com/golang/mock, github.com/jmespath/go-jmespath, github.com/json-iterator/go, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/pmezard/go-difflib, github.com/segmentio/ksuid, github.com/sirupsen/logrus, github.com/stretchr/testify, github.com/ugorji/go/codec, github.com/valyala/bytebufferpool, github.com/valyala/fasttemplate, golang.org/x/sys, gopkg.in/yaml.v3
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 189
- Forks at capture: 52
- Last updated: 2026-05-07T13:10:50Z
- Last pushed: 2026-04-24T19:36:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit)
- [README](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit/blob/mainline/README.md)
- [Issues](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit/issues)
- [Releases](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
