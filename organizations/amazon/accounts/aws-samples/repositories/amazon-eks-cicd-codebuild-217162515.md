# aws-samples/amazon-eks-cicd-codebuild

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-cicd-codebuild](https://github.com/aws-samples/amazon-eks-cicd-codebuild)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-cicd-codebuild/blob/main/README.md)
- README blob SHA: 6e8abf818aaff5d4461fe0046483be22bc236d6d
- README bytes captured: 6980
- README truncated at capture limit: False
- Repository ID: 217162515
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon EKS CI/CD with CodeBuild in AWS CDK

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:58:00+00:00

### Short excerpt (up to 300 words)

> Just deploy the stack

### README headings

- Amazon EKS CI/CD with AWS CodeBuild
- Resource List
- Pre-requisities
- Usage
- install required packages
- if you have not used cdk in this account previously you may be advised to create the necessary resources in the account
- check the diff before deployment
- deploy the complete stack
- when finished with the demo delete the created resources
- note that the flask resources were created independently of the cdk and must be deleted first
- Walkthrough
- copy the 'aws eks update-kubeconfig' command string and run it in the terminal to generate/update the kubeconfig
- list the nodes with kubectl
- deploy the initial flask sample service
- list the service and deployment
- copy the ELB dns name from the EXTERNAL-IP column and open it in browser.
- You will see the Flask-demo homepage
- set codecommit as another upstream
- push all current repo to codecommit. This will trigger CodeBuild for CI/CD.
- FAQ
- deploy to the default VPC
- Or to deploy to VPC ID vpc-xxxxxx
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage

> Just deploy the stack

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 4,183 |
| Shell | 1,578 |
| JavaScript | 1,480 |
| Dockerfile | 1,431 |
| HTML | 1,028 |
| Python | 920 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, constructs, esbuild, eslint, eslint-import-resolver-node, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, json-schema, npm-check-updates, projen, ts-jest, ts-node, typescript
- dockerAssets.d/Dockerfile (capture: captured)
- flask-docker-app/Dockerfile (capture: captured)
- flask-docker-app/requirements.txt (capture: captured) — dependency clues: Flask

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 195
- Forks at capture: 84
- Last updated: 2026-11-03T22:28:02Z
- Last pushed: 2022-10-05T19:30:47Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-cicd-codebuild)
- [README](https://github.com/aws-samples/amazon-eks-cicd-codebuild/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-cicd-codebuild/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-cicd-codebuild/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
