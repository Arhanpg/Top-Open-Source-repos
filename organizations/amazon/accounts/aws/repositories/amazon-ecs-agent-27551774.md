# aws/amazon-ecs-agent

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ecs-agent](https://github.com/aws/amazon-ecs-agent)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-ecs-agent/blob/master/README.md)
- README blob SHA: 3e8cc2084c00762c16a0c6988533210bf43b60e2
- Repository ID: 27551774
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon Elastic Container Service Agent

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:17+00:00

### Short excerpt (up to 100 words)

> The Amazon ECS Container Agent is a component of Amazon Elastic Container Service (Amazon ECS) and is responsible for managing containers on behalf of Amazon ECS. This repository comes with ECS-Init, which is a systemd based service to support the Amazon ECS Container Agent and keep it running. It is used for systems that utilize `systemd` as init systems and is packaged as deb or rpm. The source for ECS-Init is available in this repository at `./ecs-init` while the packaging is available at `./packaging`. The best source of information on running this software is the On the Amazon Linux AMI,

### README headings

- Amazon ECS Container Agent
- Usage
- On the Amazon Linux AMI
- On Other Linux AMIs
- On the ECS Optimized Windows AMI
- Downloading Different Version of ECS Agent
- Build ECS Agent from source
- Build ECS Agent Image (Linux)
- Build and run standalone (Linux)
- Standalone (Windows)
- Scripts (Windows)
- Build ECS-Init Package (Linux)
- Advanced Usage
- Environment Variables
- Persistence
- Flags
- Make Targets (on Linux)
- Contributing
- Security disclosures
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 8,933,807 |
| Shell | 108,345 |
| PowerShell | 33,171 |
| Makefile | 32,678 |
| Dockerfile | 20,777 |
| Roff | 3,197 |
| C | 1,742 |
| Python | 1,466 |
| Go Template | 106 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- agent/go.mod (capture: captured) — dependency clues: github.com/Microsoft/go-winio, github.com/aws/amazon-ecs-agent/ecs-agent, github.com/aws/amazon-ecs-agent/ecs-agent/daemonimages/csidriver, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/s3/manager, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/ecr, github.com/aws/aws-sdk-go-v2/service/ecs, github.com/aws/aws-sdk-go-v2/service/fsx, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum
- aws-sdk-go-v2/Dockerfile (capture: captured)
- ecs-agent/go.mod (capture: captured) — dependency clues: github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/ecs, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/cihub/seelog
- ecs-init/go.mod (capture: captured) — dependency clues: github.com/Azure/go-ansiterm, github.com/Microsoft/go-winio, github.com/NVIDIA/go-nvml, github.com/aws/amazon-ecs-agent/ecs-agent, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/s3/manager, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/signin
- misc/certs/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2183
- Forks at capture: 669
- Last updated: 2026-11-19T19:24:54Z
- Last pushed: 2026-11-23T00:04:32Z
- Topics: amazon-ec2, amazon-ecs-agent, amazon-linux-ami, docker-container, go

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ecs-agent)
- [README](https://github.com/aws/amazon-ecs-agent/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-ecs-agent/issues)
- [Releases](https://github.com/aws/amazon-ecs-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
