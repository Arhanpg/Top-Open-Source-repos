# bottlerocket-os/bottlerocket-ecs-updater

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-ecs-updater](https://github.com/bottlerocket-os/bottlerocket-ecs-updater)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-ecs-updater/blob/develop/README.md)
- README blob SHA: 47de441c115b84dac8543c3292cea6674132a1bc
- Repository ID: 322691393
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A service to automatically manage Bottlerocket updates in an Amazon ECS cluster.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:02+00:00

### Short excerpt (up to 100 words)

> The Bottlerocket ECS Updater is a service you can install into your ECS cluster that helps you keep your Bottlerocket container instances up to date. When installed, the Bottlerocket ECS Updater will periodically query each Bottlerocket container instance to find whether an update is available and drain tasks while an update is in progress. Updates to Bottlerocket are rolled out in waves to reduce the impact of issues; the container instances in your cluster may not all see updates at the same time. You can install the Bottlerocket ECS Updater into your cluster with the provided CloudFormation template. The following

### README headings

- Bottlerocket ECS Updater
- Installation
- Getting Started
- Subnet info
- Log Group
- Install
- How it works
- Troubleshooting
- Why do only some of my Bottlerocket instances have an update available?
- My Bottlerocket instance has an update available.  Why didn't the Bottlerocket ECS Updater update it?
- Why do new container instances launch with older Bottlerocket versions?
- Developer guide
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 87,791 |
| Shell | 13,364 |
| Makefile | 2,679 |
| Dockerfile | 1,599 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Makefile (capture: captured)
- updater/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/jmespath/go-jmespath, github.com/pmezard/go-difflib, github.com/stretchr/testify, gopkg.in/yaml.v3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 50
- Forks at capture: 9
- Last updated: 2026-10-22T00:05:53Z
- Last pushed: 2026-01-26T09:20:56Z
- Topics: aws, bottlerocket, containers, ecs, linux

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-ecs-updater)
- [README](https://github.com/bottlerocket-os/bottlerocket-ecs-updater/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-ecs-updater/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-ecs-updater/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
