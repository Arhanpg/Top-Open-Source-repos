# awslabs/amazon-eks-serverless-drainer

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-eks-serverless-drainer](https://github.com/awslabs/amazon-eks-serverless-drainer)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-eks-serverless-drainer/blob/master/README.md)
- README blob SHA: d344c33a788ec61d7f98e12e1cafcc4486b4e737
- Repository ID: 198470006
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon EKS node drainer with AWS Lambda.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:46+00:00

### Short excerpt (up to 100 words)

> Amazon EKS node drainer with AWS Lambda. **amazon-eks-serverless-drainer** is an Amazon EKS node drainer with AWS Lambda. If you provision spot instances or spotfleet in your Amazon EKS nodegroup, you can listen to the spot termination signal from **CloudWatch Events** 120 seconds in prior to the final termination process. By configuring this Lambda function as the CloudWatch Event target, **amazon-eks-serverless-drainer** will drain the terminating node and all the pods without relative toleration will be evicted and rescheduled to another node - your workload will get very minimal impact on the spot instance termination. Previously this project has a native `golang`

### README headings

- Amazon EKS Serverless Drainer
- Implementations
- Option 1: Deployt from SAR(Serverless App Repository)
- Option 2: Building from scratch
- Prepare your Layer
- Edit the sam.yaml
- update Makefile
- package and deploy with `SAM`
- print the cloudformation stack outputs
- Add Lambda Role into ConfigMap
- Validation
- In Actions
- kubectl drain or kubectl taint
- cluster name auto discovery
- clean up
- License Summary

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 3,424 |
| Makefile | 2,971 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 61
- Forks at capture: 15
- Last updated: 2026-11-13T18:38:13Z
- Last pushed: 2019-07-24T14:17:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-eks-serverless-drainer)
- [README](https://github.com/awslabs/amazon-eks-serverless-drainer/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-eks-serverless-drainer/issues)
- [Releases](https://github.com/awslabs/amazon-eks-serverless-drainer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
