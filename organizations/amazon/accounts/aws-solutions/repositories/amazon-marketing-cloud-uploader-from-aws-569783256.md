# aws-solutions/amazon-marketing-cloud-uploader-from-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/amazon-marketing-cloud-uploader-from-aws](https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws/blob/main/README.md)
- README blob SHA: b2be86a832269dd319b98bcb510c255a332ac728
- Repository ID: 569783256
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Easily upload first-party signals into Amazon Marketing Cloud (AMC) for evaluating and planning advertising campaigns

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:32:50+00:00

### Short excerpt (up to 100 words)

> This solution enables users to upload first party datasets from Amazon S3 into the Amazon Marketing Cloud (AMC). It includes a web application in which users are guided through the process of defining datasets and their PII attributes. Once this information is submitted, the solution initiates an ETL workflow that performs data normalization, hashing of plain-text PII, time-series partitioning, and upload to AMC. The architecture diagram for this solution is shown above. The process flow is described below: 1. User uploads first party data to designated Amazon S3 Bucket or exports data from AWS Clean Rooms to Amazon S3 Bucket

### README headings

- **IMPORTANT: This AWS Solution has been retired. Customers assume responsibility for maintenance and API-related updates. The functionality provided by this solution has been superseded by functionality in [Amazon Ads Data Manager Console and APIs](https://advertising.amazon.com/API/docs/en-us/adm/1_ads-data-manager-console-overview). We encourage you to explore this solution for uploading data to Amazon Ads and Amazon Marketing Cloud.**
- Amazon Marketing Cloud (AMC) Uploader from AWS
- Architecture
- User Interface:
- INSTALLATION
- INPUT
- Advanced Installation Options
- Building the solution from source code
- Deploy
- Post-Deployment
- User Authentication
- User account management
- Unit Tests
- Pre-Commit
- Collection of operational metrics
- Advanced Usage
- Integration with solution for file upload automation
- Inputs
- Outputs
- Using Postman
- Troubleshooting
- Why did so few identities resolve for my dataset?
- Uninstall
- Option 1: Uninstall using the AWS Management Console
- Option 2: Uninstall using AWS Command Line Interface
- Known Issues
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 258,930 |
| Vue | 209,957 |
| Shell | 56,546 |
| JavaScript | 9,869 |
| CSS | 4,398 |
| HTML | 519 |
| Dockerfile | 489 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/lambda_layer_factory/Dockerfile (capture: captured)
- deployment/lambda_layer_factory/requirements.txt (capture: captured) — dependency clues: aws-xray-sdk
- source/amc_uploader/requirements.txt (capture: captured) — dependency clues: chalice, requests
- source/amc_uploader/setup.py (capture: captured)
- source/anonymous_data_logger/requirements.txt (capture: captured) — dependency clues: requests, urllib3
- source/api/requirements.txt (capture: content_not_returned)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 21
- Forks at capture: 6
- Last updated: 2026-10-26T21:51:20Z
- Last pushed: 2025-10-02T21:51:36Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws)
- [README](https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws/issues)
- [Releases](https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
