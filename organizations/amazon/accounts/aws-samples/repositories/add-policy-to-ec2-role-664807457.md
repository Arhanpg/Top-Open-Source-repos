# aws-samples/add-policy-to-ec2-role

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/add-policy-to-ec2-role](https://github.com/aws-samples/add-policy-to-ec2-role)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/add-policy-to-ec2-role/blob/main/README.md)
- README blob SHA: f97b14ba1ea7e23ddc2fffa6380d0e5d5d71a6e8
- Repository ID: 664807457
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This project creates Lambda function that automatically add required AWS Identity and Access Management (IAM) policies to current Amazon Elastic Compute Cloud (Amazon EC2) instance profiles or associate a profile to EC2 instances without a profile associated.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:42:44+00:00

### Short excerpt (up to 100 words)

> This project creates Lambda function that automatically add required AWS Identity and Access Management (IAM) policies to current Amazon Elastic Compute Cloud (Amazon EC2) instance profiles or associate a profile to EC2 instances without a profile associated. You can use it as a Lambda function scheduled at a recurrent time using EventBridge Rule or manually running the python code when required. It is a best practice to manage your EC2 instances using AWS Systems Manager Session Manager and get EC2 instance's memory usage metric via CloudWatch Agent. In order to allow SSM Agent and CloudWatch Agent to communicate with their

### README headings

- Automatically update IAM roles with defined policies
- Overview
- Lambda configuration
- Setup
- Setup using CloudFormation
- 1. Validate CloudFormation template
- 2. Create CloudFormation stack
- 3. Create the packaged code
- 4. Update lambda package code
- Setup using Terraform
- 1. Initialize Terraform state
- 2. Validate Terraform template
- 3. Apply Terraform template
- After setup
- 1a. Trigger a test Lambda invocation with the AWS CLI
- 1b. Trigger a test Lambda invocation with the AWS Console
- 2. Clean-up
- Lambda function customization
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 10,165 |
| HCL | 6,233 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 5
- Forks at capture: 1
- Last updated: 2026-02-04T21:42:57Z
- Last pushed: 2023-10-17T12:41:37Z
- Topics: cloudwatch-agent, ec2-instance, iam-policy, iam-role, instance-profile, session-manager, ssm-agent, systems-manager

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/add-policy-to-ec2-role)
- [README](https://github.com/aws-samples/add-policy-to-ec2-role/blob/main/README.md)
- [Issues](https://github.com/aws-samples/add-policy-to-ec2-role/issues)
- [Releases](https://github.com/aws-samples/add-policy-to-ec2-role/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
