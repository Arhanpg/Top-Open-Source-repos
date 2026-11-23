# aws-solutions/amazon-marketing-cloud-insights-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/amazon-marketing-cloud-insights-on-aws](https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws/blob/main/README.md)
- README blob SHA: 7d75ac910be2d549bb459ac29b422bb9171567a4
- Repository ID: 620029842
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon Marketing Cloud Insights on AWS helps advertisers and agencies running campaigns on Amazon Ads to easily deploy AWS services to store, query, analyze, and visualize reporting from the AMC API

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:32:47+00:00

### Short excerpt (up to 100 words)

> The following images show the architecture of the solution and its components *Overview* *Workflow Manager* *Amazon Ads Reporting* *Selling Partner Reporting* *Data Lake* **Note**: From v2.0.0, AWS CloudFormation template resources are created by the AWS CDK and AWS Solutions Constructs. well-architected applications. All AWS Solutions Constructs are reviewed by AWS and use best practices established by the AWS Well-Architected Framework. * Amazon Sagemaker Notebook Instance * AWS Key Management Service (KMS) * Amazon S3 * Amazon CloudWatch * AWS Lambda * Amazon DynamoDB * AWS Identity and Access Management (IAM) * AWS Step Functions * Amazon Simple Queue Service (SQS)

### README headings

- **IMPORTANT: Amazon Marketing Cloud Insights on AWS has been deprecated. Customers assume responsibility for maintenance and API-related updates. You can find other AWS Solutions in the [AWS Solutions Library](https://aws.amazon.com/solutions/).**
- Amazon Marketing Cloud Insights on AWS
- Architecture
- AWS CDK Constructs
- AWS Service Requirements
- IAM Roles for Installation and Admin Operation
- Deployment
- Creating a custom build
- Prerequisites
- 1. Download or clone this repo
- 2. Create a Python virtual environment for development
- 3. After introducing changes, run the unit tests to make sure the customizations don't break existing functionality
- 4. Build the solution for deployment
- Using AWS CDK
- bootstrap CDK (required once - deploys a CDK bootstrap CloudFormation stack for assets)
- build the solution
- build and deploy the solution (replacing the indicated variable)
- Using the solution build tools
- Additional Resources
- Collection of operational metrics
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,324,727 |
| Jupyter Notebook | 59,766 |
| Shell | 53,368 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, aws-lambda-powertools, boto3, cdk-nag, crhelper, docker, moto, openapi-spec-validator, pandas, pyparsing, pyspark, pytest, pytest-cov, pytest-env, pytest-mock
- source/infrastructure/setup.py (capture: captured)
- source/tests/setup.py (capture: captured)
- source/cdk_solution_helper_py/helpers_cdk/setup.py (capture: captured)
- source/cdk_solution_helper_py/helpers_common/setup.py (capture: captured)
- source/infrastructure/scripts/requirements.txt (capture: captured) — dependency clues: boto3, crhelper

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 16
- Forks at capture: 12
- Last updated: 2026-01-07T00:43:45Z
- Last pushed: 2025-11-03T22:19:30Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws)
- [README](https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws/issues)
- [Releases](https://github.com/aws-solutions/amazon-marketing-cloud-insights-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
