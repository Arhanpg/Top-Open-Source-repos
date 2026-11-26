# aws-samples/amazon-eks-using-cdk-typescript

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-using-cdk-typescript](https://github.com/aws-samples/amazon-eks-using-cdk-typescript)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-using-cdk-typescript/blob/main/README.md)
- README blob SHA: 1cfa6e8f1e7ac412f58d792a57461572093e6916
- README bytes captured: 22954
- README truncated at capture limit: False
- Repository ID: 397331243
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A sample project that deploys an EKS Cluster following a set of best practices with options to install additional addons.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T19:10:26+00:00

### Short excerpt (up to 300 words)

> git clone https://github.com/aws-samples/amazon-eks-using-cdk-typescript.git cdk -c cluster_name=myfirstcluster deploy

### README headings

- Amazon EKS using AWS CDK with Typescript !
- Pre-requisites
- Usage
- Quick Start
- install dependant packages
- If you have not used cdk before, you may be advised to create cdk resources
- check the diff before deployment to understand any changes, on first run all resources will created
- Deploy the stack, you will be prompted for confirmation for creation of IAM and Security Group resources
- Logging into Bastion Host
- Advanced Deployment
- Default Deploy
- Deploy EKS Cluster Only
- Default Deploy with custom prefix for Cloudformation Stack
- Existing VPC
- Custom Deployment
- Configuration
- Available Parameters
- Available Context
- Best Practices
- Advanced Configurations
- Cluster Autoscaler - [Scalability](https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/)
- ALB Ingress Controller - [Scalability](https://aws.github.io/aws-eks-best-practices/security/docs/network/#ingress-controllers-and-load-balancers)
- EBS CSI Driver - [Persistent Data](https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/#ebs-volumes)
- EFS CSI Driver - [Persistent Data](https://aws.github.io/aws-eks-best-practices/security/docs/data/#use-efs-access-points-to-simplify-access-to-shared-datasets)
- Secrets CSI Driver - [Security](https://aws.github.io/aws-eks-best-practices/security/docs/data/#secrets-management)
- Network Policy Engine - [Security](https://aws.github.io/aws-eks-best-practices/security/docs/network/#network-policy)
- Container Insights - [Observability](https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#observability)
- FluentBit - [Observability](https://aws.github.io/aws-eks-best-practices/reliability/docs/application/#use-centralized-logging-tools-to-collect-and-persist-logs)
- Service Account IAM Policy
- application-log.conf

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quick Start

> git clone https://github.com/aws-samples/amazon-eks-using-cdk-typescript.git

### Limitations and security: Deploy the stack, you will be prompted for confirmation for creation of IAM and Security Group resources

> cdk -c cluster_name=myfirstcluster deploy

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 60,863 |
| Shell | 28,713 |
| Python | 4,919 |
| JavaScript | 3,054 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @types/js-yaml, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, constructs, eslint, eslint-config-standard, eslint-plugin-import, eslint-plugin-node, eslint-plugin-prettier, eslint-plugin-promise, js-yaml, prettier, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 62
- Forks at capture: 16
- Last updated: 2026-01-29T21:41:46Z
- Last pushed: 2024-06-17T18:48:55Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-using-cdk-typescript)
- [README](https://github.com/aws-samples/amazon-eks-using-cdk-typescript/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-using-cdk-typescript/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-using-cdk-typescript/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
