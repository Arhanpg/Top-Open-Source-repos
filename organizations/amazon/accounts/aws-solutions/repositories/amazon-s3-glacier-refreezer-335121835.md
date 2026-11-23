# aws-solutions/amazon-s3-glacier-refreezer

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/amazon-s3-glacier-refreezer](https://github.com/aws-solutions/amazon-s3-glacier-refreezer)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/amazon-s3-glacier-refreezer/blob/main/README.md)
- README blob SHA: 7eb615f8e15ed1a9535217badd37ec863d196248
- Repository ID: 335121835
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Amazon S3 Glacier Re:Freezer is a serverless solution that automatically copies entire Amazon S3 Glacier vault archives to a defined destination Amazon Simple Storage Service (Amazon S3 bucket) and S3 storage class.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:32:53+00:00

### Short excerpt (up to 100 words)

> The Amazon S3 Glacier Re:Freezer is a serverless solution that automatically copies entire Amazon S3 Glacier vault archives to a defined destination Amazon Simple Storage Service (Amazon S3 bucket) and S3 storage class. The solution automates the optimized restore, copy, and transfer process and provides a prebuilt Amazon CloudWatch dashboard to visualize the copy operation progress. Deploying this solution allows you to seamlessly copy your S3 Glacier vault archives to more cost effective storage locations such as the Amazon S3 Glacier Deep Archive storage class. Copying your Amazon S3 Glacier vault contents to the S3 Glacier Deep Archive storage class

### README headings

- Amazon S3 Glacier Re:Freezer
- Table of contents
- Architecture
- Stage One: Get Inventory
- Stage Two: Request Archives
- Stage Three: Archive Copy
- Stage Four: Archive Integrity Check
- State management and progress tracking
- Anonymous metric collection
- Deployment
- Custom Build
- Deployment Configuration
- Progress Tracking
- Project structure
- Creating a custom build
- Prerequisites
- 1. Download or clone this repo
- 2. Download NPM packages required for Lambda functions
- 3. After introducing changes, run the unit tests to make sure the customizations don't break existing functionality
- 4. Deploy the solution using CDK
- 5. Prepare Cloudformation Template
- 6. Upload deployment assets to your Amazon S3 buckets
- 7. Launch the CloudFormation template
- Additional Resources
- Services

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 161,473 |
| TypeScript | 94,764 |
| Shell | 13,011 |
| Python | 3,213 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/package.json (capture: captured) — dependency clues: @aws-cdk/aws-glue-alpha, @types/jest, @types/node, @types/prettier, aws-cdk, aws-cdk-lib, constructs, jest, prettier, source-map-support, ts-jest, ts-node, typescript
- deployment/cdk-solution-helper/package.json (capture: captured) — dependency clues: fs
- source/lambda/calculateMetrics/package.json (capture: captured) — dependency clues: aws-sdk, chai, chai-as-promised, glob-parent, mocha, proxyquire, sinon
- source/lambda/calculateTreehash/package.json (capture: captured) — dependency clues: aws-sdk, chai, chai-as-promised, crypto-js, mocha, moment, proxyquire, sinon
- source/lambda/copyChunk/package.json (capture: captured) — dependency clues: aws-sdk, chai, chai-as-promised, mocha, moment, proxyquire, sinon
- source/lambda/copyToDestinationBucket/package.json (capture: captured) — dependency clues: aws-sdk, chai, chai-as-promised, mocha, moment, proxyquire, sinon

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 13
- Last updated: 2026-02-20T13:54:55Z
- Last pushed: 2024-01-29T16:43:32Z
- Topics: amazon-glacier, amazon-s3, aws-cloud, serverless

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/amazon-s3-glacier-refreezer)
- [README](https://github.com/aws-solutions/amazon-s3-glacier-refreezer/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/amazon-s3-glacier-refreezer/issues)
- [Releases](https://github.com/aws-solutions/amazon-s3-glacier-refreezer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
