# aws/aws-node-termination-handler

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-node-termination-handler](https://github.com/aws/aws-node-termination-handler)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-node-termination-handler/blob/main/README.md)
- README blob SHA: 2cd76b649513e376c58fd351c41e75eea12da15e
- README bytes captured: 43591
- README truncated at capture limit: False
- Repository ID: 216631734
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Gracefully handle EC2 instance shutdown within Kubernetes

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:42:43+00:00

### Short excerpt (up to 300 words)

> This project ensures that Both modes (IMDS and The aws-node-termination-handler can operate When NTH receives an A ✅ indicates that

### README headings

- Project Summary
- Major Features
- Instance Metadata Service (IMDS) Processor
- IMDS Processor with ASG Target Lifecycle State change
- Queue Processor
- Queue Processor with ASG Lifecycle Hooks
- Queue Processor with Instance State Change Events
- Issuing Lifecycle Heartbeats
- How it works
- How to use
- Configurations
- `Heartbeat Interval` (Required)
- `Heartbeat Until` (Optional)
- Example Case
- Example Helm Command
- Important Notes
- Which one should I use?
- Kubernetes Compatibility
- Installation and Configuration
- Installation and Configuration
- Pod Security Admission
- Kubectl Apply
- Helm
- Infrastructure Setup
- 1. Create an SQS Queue:
- Queue Policy
- make sure the queue policy is valid JSON
- Save queue attributes to a temp file
- 2. Create an ASG Termination Lifecycle Hook:
- 3. Tag the Instances:

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Project Summary

> This project ensures that

### Features and capabilities: Major Features

> Both modes (IMDS and

### Getting started and usage: Installation and Configuration

> The aws-node-termination-handler can operate

### Architecture and design: How it works

> When NTH receives an

### Limitations and security: Kubernetes Compatibility

> A ✅ indicates that

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 414,928 |
| Shell | 262,213 |
| Mustache | 9,224 |
| Makefile | 7,654 |
| PowerShell | 4,239 |
| Dockerfile | 1,643 |
| Go Template | 118 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Azure/go-ansiterm, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/aws/aws-sdk-go, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/chai2010/gettext-go, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/exponent-io/jsonpath, github.com/go-errors/errors, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-logr/zerologr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag
- Makefile (capture: captured)
- test/webhook-test-proxy/Dockerfile (capture: captured)
- config/helm/aws-node-termination-handler/Chart.yaml (capture: captured)
- config/helm/localstack/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1764
- Forks at capture: 290
- Last updated: 2026-11-21T11:27:55Z
- Last pushed: 2026-11-12T21:10:33Z
- Topics: aws-ec2, eks, golang, kubernetes, maintenance-events, spot-instances

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-node-termination-handler)
- [README](https://github.com/aws/aws-node-termination-handler/blob/main/README.md)
- [Issues](https://github.com/aws/aws-node-termination-handler/issues)
- [Releases](https://github.com/aws/aws-node-termination-handler/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
