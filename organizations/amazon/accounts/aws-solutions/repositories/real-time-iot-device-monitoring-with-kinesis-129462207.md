# aws-solutions/real-time-iot-device-monitoring-with-kinesis

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/real-time-iot-device-monitoring-with-kinesis](https://github.com/aws-solutions/real-time-iot-device-monitoring-with-kinesis)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/real-time-iot-device-monitoring-with-kinesis/blob/main/README.md)
- README blob SHA: cfc8be0d64a16f3cd3201ca44d5f4485de135e61
- Repository ID: 129462207
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Solution with a CloudFormation template for an ingestion mechanism for analytics about device connectivity and activity (i.e. sensor readings), as well as a dashboard for visualizing this data.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:48+00:00

### Short excerpt (up to 100 words)

> This AWS Solution has been archived and is no longer maintained by AWS. To discover other solutions, please visit the AWS Solutions Library. AWS Solution for analyzing IoT Device Connectivity using Kinesis Analytics sudo apt-get update sudo apt-get install install zip wget gawk sed -y cd deployment/ ./build-s3-dist.sh source-bucket-base-name solution-name solution-version source-bucket-base-name should be the base name for the S3 bucket location where the template will source the Lambda code from. The template will append '-[region_name]' to this value. For example: ./build-s3-dist.sh solutions The template will then expect the source code to be located in the solutions-[region_name] bucket The CF

### README headings

- Deprecation Notice
- Real Time IoT Device Monitoring with Kinesis Analytics
- OS/Python Environment Setup
- Building Lambda Package
- CF template and Lambda function
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| CSS | 91,171 |
| JavaScript | 64,023 |
| HTML | 15,501 |
| Python | 8,750 |
| Shell | 6,073 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/manifest-generator/package.json (capture: captured) — dependency clues: minimist
- source/custom-resource/package.json (capture: captured) — dependency clues: amazon-cognito-identity-js, aws-sdk, aws-sdk-mock, chai, mocha, moment, node-uuid, npm-run-all, sinon, sinon-chai, underscore

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 66
- Forks at capture: 42
- Last updated: 2025-09-26T06:07:04Z
- Last pushed: 2023-06-29T14:51:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/real-time-iot-device-monitoring-with-kinesis)
- [README](https://github.com/aws-solutions/real-time-iot-device-monitoring-with-kinesis/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/real-time-iot-device-monitoring-with-kinesis/issues)
- [Releases](https://github.com/aws-solutions/real-time-iot-device-monitoring-with-kinesis/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
