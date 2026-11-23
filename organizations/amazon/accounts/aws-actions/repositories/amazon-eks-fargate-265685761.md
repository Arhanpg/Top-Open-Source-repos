# aws-actions/amazon-eks-fargate

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/amazon-eks-fargate](https://github.com/aws-actions/amazon-eks-fargate)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-actions/amazon-eks-fargate/blob/master/README.md)
- README blob SHA: 20e2d4438616a5de0cfefc51505392c1e8604eab
- Repository ID: 265685761
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Creates an EKS on Fargate cluster

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:33:21+00:00

### Short excerpt (up to 100 words)

> This action allows to manage the lifecycle of an Amazon EKS cluster running on AWS Fargate. NOTE: this is work in progress, not yet usable. In a GH Action file, for example, `.github/workflows/main.yaml`: on: [push] jobs: create_cluster: runs-on: ubuntu-latest name: Create an EKS on Fargate cluster steps: - name: Configure AWS credentials uses: aws-actions/configure-aws-credentials@v1 with: aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }} aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }} aws-region: eu-west-1 - name: Provision cluster uses: aws-actions/amazon-eks-fargate@v0.1 Once completed (after ca. 15min) connect to the EKS cluster by updating your `kubeconfig`. This project is licensed under the Apache-2.0 License. If you would like to report a

### README headings

- WIP: Amazon EKS on AWS Fargate GitHub Actions
- Usage
- License
- Security Disclosures

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 1,645 |
| Dockerfile | 1,072 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 58
- Forks at capture: 12
- Last updated: 2026-05-12T17:12:32Z
- Last pushed: 2021-10-13T14:44:30Z
- Topics: amazon-eks, aws-fargate

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/amazon-eks-fargate)
- [README](https://github.com/aws-actions/amazon-eks-fargate/blob/master/README.md)
- [Issues](https://github.com/aws-actions/amazon-eks-fargate/issues)
- [Releases](https://github.com/aws-actions/amazon-eks-fargate/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
