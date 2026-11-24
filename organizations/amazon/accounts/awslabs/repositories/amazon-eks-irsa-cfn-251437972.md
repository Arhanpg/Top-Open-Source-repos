# awslabs/amazon-eks-irsa-cfn

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-eks-irsa-cfn](https://github.com/awslabs/amazon-eks-irsa-cfn)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-eks-irsa-cfn/blob/main/README.md)
- README blob SHA: 19291f7f3dc9e4ec8d18d765595dc0fc2d1b31ee
- Repository ID: 251437972
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS CloudFormation and CDK Construct Library for IAM Roles for EKS Service Accounts 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:44+00:00

### Short excerpt (up to 100 words)

> This repository contains an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) [Custom Resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) that creates an [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that is assumable by a [Kubernetes Service Account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/). This role is known as an IRSA, or [IAM Role for Service Account](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html). This role can be associated with an Amazon EKS Cluster that you're creating in the same CloudFormation stack. Alternatively, the EKS Cluster can be created in a different stack and referenced by name. For ease of implementation, this repository also contains a [CDK Construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) library you can import and use to easily create a Role. This is the quickest and most programmatic way to build

### README headings

- Amazon EKS IAM Role for Service Accounts CDK/CloudFormation Library
- CDK Construct Library usage
- SAM Template and CloudFormation Custom Resources
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 30,065 |
| TypeScript | 18,744 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-cloudformation, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/core, @types/jest, @types/node, aws-cdk, jest, ts-jest, typescript
- lambda-packages/identity_provider_handler/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, eslint, jest, lambda-tester, nock, standard
- lambda-packages/role_handler/package.json (capture: captured) — dependency clues: aws-sdk, aws-sdk-mock, eslint, jest, lambda-tester, nock, standard

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 19
- Forks at capture: 13
- Last updated: 2026-09-29T13:46:24Z
- Last pushed: 2024-05-11T00:46:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-eks-irsa-cfn)
- [README](https://github.com/awslabs/amazon-eks-irsa-cfn/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-eks-irsa-cfn/issues)
- [Releases](https://github.com/awslabs/amazon-eks-irsa-cfn/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
