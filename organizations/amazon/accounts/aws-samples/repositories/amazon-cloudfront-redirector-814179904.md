# aws-samples/amazon-cloudfront-redirector

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-cloudfront-redirector](https://github.com/aws-samples/amazon-cloudfront-redirector)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-cloudfront-redirector/blob/main/README.md)
- README blob SHA: 1852d03b34653e51e1d22ad0b293bd9b1ce6b547
- README bytes captured: 12013
- README truncated at capture limit: False
- Repository ID: 814179904
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T05:25:19+00:00

### Short excerpt (up to 300 words)

> This proposal leverages CDK See CONTRIBUTING for more

### README headings

- Amazon CloudFront Redirector
- Architecture
- Deployment
- Required: set the AWS credentials for the session the terminal
- Optional: set whether you want to debug the request.
- DEBUG_MODE possible values 0,1,2.
- 2 -> print all log lines in CloudWatch and also send debug response headers
- 1 -> sent only debug response headers
- 0 -> turn off debug mode (default, recommended for production)
- Post Instalation
- Populating redirection rules for the first time
- Importing a custom csv input file
- Testing
- Troubleshooting
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> This proposal leverages CDK

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 25,575 |
| Python | 19,404 |
| TypeScript | 9,694 |
| Shell | 682 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/aws-lambda-python-alpha, @aws-sdk/client-cloudfront-keyvaluestore, @types/jest, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, jest, source-map-support, ts-jest, ts-node, typescript
- src/lambda-functions/llm-layer/requirements.txt (capture: captured) — dependency clues: langchain, pandas, urllib3
- src/lambda-functions/redirect-importer/package.json (capture: captured)
- src/lambda-functions/kvs-layer/nodejs/kvs_utils/package.json (capture: captured) — dependency clues: @aws-sdk/client-cloudfront-keyvaluestore, @aws-sdk/signature-v4-crt, @aws-sdk/signature-v4-multi-region
- src/lambda-functions/s3-layer/nodejs/s3_utils/package.json (capture: captured) — dependency clues: papaparse

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 6
- Forks at capture: 0
- Last updated: 2026-07-08T14:14:02Z
- Last pushed: 2026-05-15T15:27:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-cloudfront-redirector)
- [README](https://github.com/aws-samples/amazon-cloudfront-redirector/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-cloudfront-redirector/issues)
- [Releases](https://github.com/aws-samples/amazon-cloudfront-redirector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
