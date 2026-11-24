# aws-solutions/real-time-insights-account-activity

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/real-time-insights-account-activity](https://github.com/aws-solutions/real-time-insights-account-activity)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-solutions/real-time-insights-account-activity/blob/master/README.md)
- README blob SHA: 8a4272e637e11044bb4897022bb1eb85836e7fa7
- Repository ID: 121668873
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An application and real-time dashboard providing insights into AWS account activity.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:47+00:00

### Short excerpt (up to 100 words)

> This AWS Solution leverages AWS CloudTrail, AWS Kinesis Analytics, Amazon DynamoDB, AWS Lambda, Amazon S3, Amazon Cognito, and Chart.js to provide real-time insights into AWS account activity. sudo apt-get update sudo apt-get install zip sed wget -y sudo pip install --upgrade pip sudo pip install --upgrade setuptools sudo pip install --upgrade virtualenv export DIST_OUTPUT_BUCKET=my-bucket-name # bucket where customized code will reside export VERSION=my-version # version number for the customized code cd deployment ./build-s3-dist.sh $DIST_OUTPUT_BUCKET real-time-insights-account-activity $VERSION source-bucket-base-name should be the base name for the S3 bucket location where the template will source the Lambda code from. The template will append

### README headings

- Note: As of 09/08/2022, Real-Time Insights on AWS Account Activity has been deprecated. The code is no longer being maintained.
- AWS Real-Time Insights into AWS Account Activity with Kinesis Analytics
- OS/Python Environment Setup
- Building Lambda Package
- CF template and Lambda function

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| CSS | 84,535 |
| JavaScript | 68,692 |
| HTML | 19,992 |
| Python | 9,429 |
| Shell | 4,252 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/manifest-generator/package.json (capture: captured) — dependency clues: minimist
- source/helper/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, chai, mocha, moment, node-uuid, npm-run-all, password-generator, sinon, sinon-chai, underscore

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 42
- Forks at capture: 16
- Last updated: 2023-01-27T21:28:25Z
- Last pushed: 2022-09-08T18:56:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/real-time-insights-account-activity)
- [README](https://github.com/aws-solutions/real-time-insights-account-activity/blob/master/README.md)
- [Issues](https://github.com/aws-solutions/real-time-insights-account-activity/issues)
- [Releases](https://github.com/aws-solutions/real-time-insights-account-activity/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
