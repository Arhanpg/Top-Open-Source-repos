# aws-samples/amazon-cloudfront-tagbased-invalidations

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-cloudfront-tagbased-invalidations](https://github.com/aws-samples/amazon-cloudfront-tagbased-invalidations)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-cloudfront-tagbased-invalidations/blob/main/README.md)
- README blob SHA: c9a1dc425da03a34c99260b2fea68ad2f1d52415
- README bytes captured: 5694
- README truncated at capture limit: False
- Repository ID: 516052195
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T05:42:15+00:00

### Short excerpt (up to 300 words)

> See CONTRIBUTING for more

### README headings

- Tag based Invalidations in Amazon CloudFront
- Architecture
- Tag Ingest Workflow
- Tag Purge Workflow
- Pre-requisites
- Steps to build
- Required: set the AWS CLI profile name
- Optional: set the SNS topic name
- Required: set the AWS region where the primary deployment of solution resides.
- Required: Specify delimiter when multiple tags are passed, possible values ',' or ' ' (space)
- Required: Specify the response header name where tags are present
- Optional: Specify the response header name where tag Time-to-Live (TTL) in seconds
- will be specified from origin.
- Optional: Specify how to determine the TTL of the Tag reocord in DynamoDB.
- whether to use Cache-Control header max-age or take the TTL specified as part of the tag
- leave it empty if you do not want to set a TTL
- possible values 'Tag' or 'Cache-Control' or ''
- Pricing Calculations
- Assumptions
- AWS Service wise break up of calculations
- Troubleshooting
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 18,110 |
| Python | 17,400 |
| JavaScript | 4,453 |
| Shell | 3,213 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- cdk/package.json (capture: captured) — dependency clues: @types/jest, @types/node, @types/prettier, aws-cdk, aws-cdk-lib, constructs, jest, source-map-support, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 7
- Forks at capture: 0
- Last updated: 2026-04-23T19:01:12Z
- Last pushed: 2023-10-18T14:18:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-cloudfront-tagbased-invalidations)
- [README](https://github.com/aws-samples/amazon-cloudfront-tagbased-invalidations/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-cloudfront-tagbased-invalidations/issues)
- [Releases](https://github.com/aws-samples/amazon-cloudfront-tagbased-invalidations/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
