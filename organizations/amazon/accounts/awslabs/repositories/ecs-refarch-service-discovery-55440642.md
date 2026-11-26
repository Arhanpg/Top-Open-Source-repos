# awslabs/ecs-refarch-service-discovery

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/ecs-refarch-service-discovery](https://github.com/awslabs/ecs-refarch-service-discovery)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/ecs-refarch-service-discovery/blob/master/README.md)
- README blob SHA: 1228b92d2b65729e5b1e724ff54af2f0e67e58d4
- README bytes captured: 15400
- README truncated at capture limit: False
- Repository ID: 55440642
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An EC2 Container Service Reference Architecture for providing Service Discovery to containers using CloudWatch Events, Lambda and Route 53 private hosted zones. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T20:11:27+00:00

### Short excerpt (up to 300 words)

> Service discovery is a 1. [AWS CloudTrail][16] must

### README headings

- Amazon EC2 Container Service - Reference Architecture: Service Discovery
- Background
- Solution
- Deploying the architecture
- Prerequisites
- Build the microservices app and push the images to [ECR][18a]
- Launch the AWS CloudFormation template
- Create your [Lambda][4] function
- Create and configure the CloudWatch event that triggers your Lambda function
- Create your three services
- Test your setup
- Conclusion
- Cleanup
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Amazon EC2 Container Service - Reference Architecture: Service Discovery

> Service discovery is a

### Technology and requirements: Prerequisites

> 1. [AWS CloudTrail][16] must

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 16,470 |
| HTML | 7,516 |
| Python | 2,228 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- microservices/goodreads/Dockerfile (capture: captured)
- microservices/portal/Dockerfile (capture: captured)
- microservices/twitch/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 440
- Forks at capture: 80
- Last updated: 2026-09-08T06:38:03Z
- Last pushed: 2019-02-20T21:31:23Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/ecs-refarch-service-discovery)
- [README](https://github.com/awslabs/ecs-refarch-service-discovery/blob/master/README.md)
- [Issues](https://github.com/awslabs/ecs-refarch-service-discovery/issues)
- [Releases](https://github.com/awslabs/ecs-refarch-service-discovery/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
