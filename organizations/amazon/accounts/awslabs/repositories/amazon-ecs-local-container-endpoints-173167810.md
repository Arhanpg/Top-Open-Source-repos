# awslabs/amazon-ecs-local-container-endpoints

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-ecs-local-container-endpoints](https://github.com/awslabs/amazon-ecs-local-container-endpoints)
- Default branch: mainline
- README: [Open upstream README](https://github.com/awslabs/amazon-ecs-local-container-endpoints/blob/mainline/README.md)
- README blob SHA: ee29d0483c832442579973c2262f6a7842374931
- Repository ID: 173167810
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A container that provides local versions of the ECS Task Metadata Endpoint and ECS Task IAM Roles Endpoint. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:40+00:00

### Short excerpt (up to 100 words)

> Amazon ECS Local Container Endpoints ==================================== A container that provides local versions of the ECS Task IAM Roles endpoint and the ECS Task Metadata Endpoints. This project will help you test applications locally before you deploy to ECS/Fargate. This repository contains the source code for the project. To use it, pull the amazon/amazon-ecs-local-container-endpoints:latest image from ECR. * Tutorial * Setup Networking * Option 1: Use a User Defined Docker Bridge Network * Option 2: Set up iptables rules * Configuration * Credentials * Custom IAM and STS Endpoints * Docker * Environment Variables * Features * Vend Credentials to Containers

### README headings

- Table of Contents
- Security disclosures
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 157,734 |
| Makefile | 6,712 |
| JavaScript | 4,506 |
| Shell | 2,896 |
| Dockerfile | 1,190 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Microsoft/go-winio, github.com/aws/amazon-ecs-agent/agent, github.com/aws/aws-sdk-go, github.com/awslabs/go-config-generator-for-fluentd-and-fluentbit, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/cihub/seelog, github.com/cilium/ebpf, github.com/containerd/cgroups, github.com/containerd/log, github.com/containernetworking/cni, github.com/containernetworking/plugins, github.com/coreos/go-systemd/v22, github.com/davecgh/go-spew, github.com/distribution/reference, github.com/docker/docker, github.com/docker/go-connections, github.com/docker/go-units, github.com/fatih/structs, github.com/felixge/httpsnoop
- Makefile (capture: captured)
- infra/package.json (capture: captured) — dependency clues: @aws-cdk/aws-codebuild, @aws-cdk/aws-codepipeline, @aws-cdk/aws-codepipeline-actions, @aws-cdk/aws-ec2, @aws-cdk/aws-ecr, @aws-cdk/aws-ecs, @aws-cdk/aws-iam, @aws-cdk/core, @types/node, typescript
- integ/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 517
- Forks at capture: 60
- Last updated: 2026-11-06T00:13:56Z
- Last pushed: 2025-03-31T21:33:12Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-ecs-local-container-endpoints)
- [README](https://github.com/awslabs/amazon-ecs-local-container-endpoints/blob/mainline/README.md)
- [Issues](https://github.com/awslabs/amazon-ecs-local-container-endpoints/issues)
- [Releases](https://github.com/awslabs/amazon-ecs-local-container-endpoints/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
