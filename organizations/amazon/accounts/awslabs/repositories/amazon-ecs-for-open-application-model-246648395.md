# awslabs/amazon-ecs-for-open-application-model

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-ecs-for-open-application-model](https://github.com/awslabs/amazon-ecs-for-open-application-model)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-ecs-for-open-application-model/blob/master/README.md)
- README blob SHA: f08877bda3e2dfb7f7652e98ec4cd0d257eb4c00
- Repository ID: 246648395
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CLI that deploys OAM workloads to Amazon ECS on AWS Fargate

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:43:13+00:00

### Short excerpt (up to 100 words)

> The oam-ecs CLI is a proof-of-concept that partially implements the Open Application Model (OAM) specification, version v1alpha1. The oam-ecs CLI provisions two of the core OAM workload types as Amazon ECS services running on AWS Fargate using AWS CloudFormation. A workload of type `core.oam.dev/v1alpha1.Worker` will deploy a CloudFormation stack containing an ECS service running in private VPC subnets with no accessible endpoint. A workload of type `core.oam.dev/v1alpha1.Server` will deploy a CloudFormation stack containing an ECS service running in private VPC subnets, behind a publicly-accessible network load balancer. For a full comparison with the OAM specification, see the Compatibility page. See

### README headings

- Amazon ECS for Open Application Model
- Build & test
- Deploy an oam-ecs environment
- Deploy OAM workloads with oam-ecs
- Upgrade and scale OAM workloads with oam-ecs
- Tear down
- Credentials and Region
- Security Disclosures
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 115,937 |
| Shell | 3,034 |
| Makefile | 2,022 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/AlecAivazis/survey/v2, github.com/Masterminds/goutils, github.com/Masterminds/semver, github.com/Masterminds/sprig, github.com/aws/aws-sdk-go, github.com/briandowns/spinner, github.com/fatih/color, github.com/fsnotify/fsnotify, github.com/gobuffalo/packd, github.com/gobuffalo/packr/v2, github.com/golang/mock, github.com/google/go-cmp, github.com/google/gofuzz, github.com/google/uuid, github.com/huandu/xstrings, github.com/iancoleman/strcase, github.com/imdario/mergo, github.com/mattn/go-colorable, github.com/mgutz/ansi, github.com/mitchellh/copystructure
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 59
- Forks at capture: 7
- Last updated: 2023-08-02T05:26:08Z
- Last pushed: 2022-07-19T21:39:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-ecs-for-open-application-model)
- [README](https://github.com/awslabs/amazon-ecs-for-open-application-model/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-ecs-for-open-application-model/issues)
- [Releases](https://github.com/awslabs/amazon-ecs-for-open-application-model/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
