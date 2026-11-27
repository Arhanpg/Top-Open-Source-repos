# awslabs/lambda-chef-node-cleanup

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/lambda-chef-node-cleanup](https://github.com/awslabs/lambda-chef-node-cleanup)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/lambda-chef-node-cleanup/blob/master/README.md)
- README blob SHA: 676f28a788ed4cc14f98d13a39833bd1503a3d6d
- README bytes captured: 11409
- README truncated at capture limit: False
- Repository ID: 53090840
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Automatically Delete Terminated Instances in Chef Server with AWS Lambda 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:47:18+00:00

### Short excerpt (up to 300 words)

> Using CloudWatch Events, when an instance is terminated a Lambda function is triggered that will remove the node from Chef server for you. For this

### README headings

- Automatically Delete Terminated Instances in Chef Server with AWS Lambda
- Details
- Prerequisites
- Terraform
- Deploying the Lambda Function
- KMS
- Lambda Function
- Chef Server Permissions
- Chef Nodes
- Some Alternatives to the ec2_instance_id Attribute
- Naming Nodes with the Instance ID
- AWS Config
- Using This Example
- If you don't want to use Terraform
- I Just Want The Lambda Function!
- Destroying
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Automatically Delete Terminated Instances in Chef Server with AWS Lambda

> Using CloudWatch Events, when an instance is terminated a Lambda function is triggered that will remove the node from Chef server for you. For this

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,357,797 |
| HCL | 3,595 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: aws_lambda_sample_events, boto3, botocore, mock, pychef, pytest, pytest-cov

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 69
- Forks at capture: 38
- Last updated: 2026-08-01T11:57:23Z
- Last pushed: 2018-02-19T15:23:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/lambda-chef-node-cleanup)
- [README](https://github.com/awslabs/lambda-chef-node-cleanup/blob/master/README.md)
- [Issues](https://github.com/awslabs/lambda-chef-node-cleanup/issues)
- [Releases](https://github.com/awslabs/lambda-chef-node-cleanup/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
