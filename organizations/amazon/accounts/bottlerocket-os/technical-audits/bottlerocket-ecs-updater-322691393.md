# bottlerocket-os/bottlerocket-ecs-updater

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-ecs-updater
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:45:52+00:00

## Project purpose

The Bottlerocket ECS Updater is a service you can install into your ECS cluster that helps you keep your Bottlerocket container instances up to date. When installed, the Bottlerocket ECS Updater will periodically query each Bottlerocket container instance to find whether an update is available and drain tasks while an update is in progress. Updates to Bottlerocket are rolled out in waves to reduce the impact of issues; the container instances in your cluster may not all see updates at the same time.

## Why this project is used

A service to automatically manage Bottlerocket updates in an Amazon ECS cluster.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Shell, Makefile, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/jmespath/go-jmespath, github.com/pmezard/go-difflib, github.com/stretchr/testify, gopkg.in/yaml.v3
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: updater/main.go, integ/cleanup.sh, integ/common.sh, integ/run-updater.sh

## Setup and usage

- Installation: You can install the Bottlerocket ECS Updater into your cluster with the provided CloudFormation template.
- Installation: The following information is required when creating the CloudFormation stack:
- Installation: * The name of the ECS cluster where you are running Bottlerocket container instances
- Installation: * The name of the CloudWatch Logs log group where the Bottlerocket ECS Updater will send its logs
- Installation: * At least one subnet ID that has Internet access (which does not need to be shared with the rest of your cluster)
- Installation: When installed, the CloudFormation template will create the following resources in your account:
- Installation: * A task definition for the Bottlerocket ECS Updater
- Installation: * A CloudWatch Events scheduled rule to execute the Bottlerocket ECS Updater

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-ecs-updater/blob/develop/README.md
- README SHA: 47de441c115b84dac8543c3292cea6674132a1bc
- Manifests: Dockerfile, Makefile, updater/go.mod
- Sampled source files: updater/main.go, integ/cleanup.sh, integ/common.sh, integ/run-updater.sh
- Git tree state: captured
- Evidence fingerprint: 65adce0b0ab0a8aface99fcd5ca5d9ba541213308be4565c6b03ea381e71b152

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
