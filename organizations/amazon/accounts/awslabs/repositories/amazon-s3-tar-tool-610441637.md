# awslabs/amazon-s3-tar-tool

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-s3-tar-tool](https://github.com/awslabs/amazon-s3-tar-tool)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-s3-tar-tool/blob/main/README.md)
- README blob SHA: edae2da515999b6f30383da3299313b9aa2407f7
- README bytes captured: 23720
- README truncated at capture limit: False
- Repository ID: 610441637
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A utility tool to create a tarball of existing objects in Amazon S3

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T10:08:03+00:00

### Short excerpt (up to 300 words)

> The tool follows the This tool still has

### README headings

- Amazon S3 Tar Tool
- Usage
- Storage Class Options
- Examples
- this will create tarballs that are 1GB in size
- outputs:
- s3://bucket/archive.01.tar
- s3://bucket/archive.02.tar
- s3://bucket/archive.03.tar
- Manifest Input
- the manifest file can be a local file or an object in Amazon S3
- The manifest can also contain the etag as a fourth column if its is known
- Large-Objects vs Small-Objects (In Memory)
- TOC & Extract
- or a dir
- Extracting existing uncompressed tarballs
- List
- Generating manifest files
- Column 1 is the bucket
- Column 2 is the key
- Column 6 has the size
- Column 7 has the LastModified timestamp
- Column 8 is the ETag
- Performance
- Installation
- IAM Permissions
- How the tool works
- Testing & Validation
- Pricing
- Traditional Amazon S3 backend operations

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage

> The tool follows the

### Limitations and security: Limitations of the tool

> This tool still has

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 126,853 |
| Makefile | 954 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/cpuguy83/go-md2man/v2, github.com/remeh/sizedwaitgroup
- Makefile (capture: captured)
- cmd/bucket-dist/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/s3/manager, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/jmespath/go-jmespath

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 236
- Forks at capture: 19
- Last updated: 2026-10-29T17:56:02Z
- Last pushed: 2026-04-08T02:24:52Z
- Topics: amazon-s3, archive, aws, aws-s3, tar

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-s3-tar-tool)
- [README](https://github.com/awslabs/amazon-s3-tar-tool/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-s3-tar-tool/issues)
- [Releases](https://github.com/awslabs/amazon-s3-tar-tool/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
