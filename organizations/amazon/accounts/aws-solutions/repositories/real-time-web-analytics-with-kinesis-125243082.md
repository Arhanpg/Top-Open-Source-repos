# aws-solutions/real-time-web-analytics-with-kinesis

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/real-time-web-analytics-with-kinesis](https://github.com/aws-solutions/real-time-web-analytics-with-kinesis)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/real-time-web-analytics-with-kinesis/blob/main/README.md)
- README blob SHA: 4e056b40cd7f1bacc3261933eb58ba25240b3545
- Repository ID: 125243082
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Solution with a CloudFormation template used to deploy an Kinesis Analytics application, optional web server for generating web usage data, and Cognito authenticated dashboard for viewing web analytics in real-time.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:50+00:00

### Short excerpt (up to 100 words)

> This AWS Solution has been archived and is no longer maintained by AWS. To discover other solutions, please visit the AWS Solutions Library. AWS Solution for analyzing web traffic in real-time using Kinesis Data Analytics, an S3 website, and Amazon Cognito. sudo apt-get update sudo apt-get install install zip wget gawk sed -y deployment/build-s3-dist.sh source-bucket-base-name source-bucket-base-name should be the base name for the S3 bucket location where the template will source the Lambda code from. The template will append '-[region_name]' to this value. For example: deployment/build-s3-dist.sh solutions The template will then expect the source code to be located in the

### README headings

- Deprecation Notice
- Real-Time Web Analytics with Kinesis Data Analytics
- OS/Python Environment Setup
- Building Lambda Package
- CF template and Lambda function
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 202,544 |
| CSS | 91,171 |
| HTML | 19,645 |
| Python | 6,480 |
| Shell | 4,779 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/custom-resource/package.json (capture: captured) — dependency clues: amazon-cognito-identity-js, async, aws-sdk, aws-sdk-mock, chai, mocha, moment, node-uuid, npm-run-all, password-generator, sinon, sinon-chai, underscore
- source/wasa/package.json (capture: captured) — dependency clues: aws-sdk, chai, mocha, moment, npm-run-all, sinon, sinon-chai

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 69
- Forks at capture: 19
- Last updated: 2026-01-05T20:44:03Z
- Last pushed: 2023-07-26T16:57:35Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/real-time-web-analytics-with-kinesis)
- [README](https://github.com/aws-solutions/real-time-web-analytics-with-kinesis/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/real-time-web-analytics-with-kinesis/issues)
- [Releases](https://github.com/aws-solutions/real-time-web-analytics-with-kinesis/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
