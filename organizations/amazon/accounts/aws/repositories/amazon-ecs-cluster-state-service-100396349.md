# aws/amazon-ecs-cluster-state-service

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ecs-cluster-state-service](https://github.com/aws/amazon-ecs-cluster-state-service)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-ecs-cluster-state-service/blob/master/README.md)
- README blob SHA: 9a08c95c4ee60b74065cd15483bf90330c734f33
- Repository ID: 100396349
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Materialized local view of your ECS cluster state built on top of the Amazon ECS event stream.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:27+00:00

### Short excerpt (up to 100 words)

> The amazon-ecs-cluster-state-service consumes events from a stream of all changes to containers and instances across your Amazon ECS clusters, persists the events in a local data store, and provides APIs (e.g., search, filter, list, etc.) that enable you to query the state of your cluster so you can respond to changes in real-time. The amazon-ecs-cluster-state-service utilizes etcd as the data store to track your Amazon ECS cluster state locally, and it also manages any drift in state by periodically reconciling state with Amazon ECS. The amazon-ecs-cluster-state-service API operations: * Lists and describes container instances and tasks * Filters container instances

### README headings

- amazon-ecs-cluster-state-service
- Description
- REST API
- Building amazon-ecs-cluster-state-service
- Find the cluster-state-service binary in 'out' folder
- Usage
- Prerequisites
- Quick Start - Launching the amazon-ecs-cluster-state-service
- API endpoint
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 798,422 |
| Shell | 12,100 |
| Python | 10,420 |
| Gherkin | 7,335 |
| Makefile | 5,395 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- canary/Makefile (capture: captured)
- misc/certs/Dockerfile (capture: captured)
- vendor/google.golang.org/grpc/Makefile (capture: captured)
- vendor/github.com/go-ini/ini/Makefile (capture: captured)
- vendor/github.com/gucumber/gucumber/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 16
- Forks at capture: 8
- Last updated: 2024-05-22T21:55:40Z
- Last pushed: 2023-04-10T09:20:11Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ecs-cluster-state-service)
- [README](https://github.com/aws/amazon-ecs-cluster-state-service/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-ecs-cluster-state-service/issues)
- [Releases](https://github.com/aws/amazon-ecs-cluster-state-service/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
