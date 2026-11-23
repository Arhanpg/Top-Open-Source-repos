# aws/amazon-ecs-ami

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ecs-ami](https://github.com/aws/amazon-ecs-ami)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-ecs-ami/blob/main/README.md)
- README blob SHA: dda3a8406a1af59e2c585085bbaecea30124b711
- Repository ID: 416118048
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Packer recipes for building the official ECS-optimized Amazon Linux AMIs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:20+00:00

### Short excerpt (up to 100 words)

> This is a packer recipe for creating an ECS-optimized AMI. It will create a private AMI in whatever account you are running it in. 1. Setup AWS cli credentials. 2. Make the recipe that you want, REGION must be specified. Options are: al2, al2arm, al2gpu, al2keplergpu, al2inf, al2kernel5dot10, al2kernel5dot10arm, al2kernel5dot10gpu, al2kernel5dot10inf, al2023, al2023arm, al2023neu, al2023gpu. REGION=us-west-2 make al2023 **NOTE**: `al2keplergpu` is a build recipe that this package supports to build ECS-Optimized GPU AMIs for instances with GPUs with Kepler architecture (such as P2 type instances). ECS-Optimized GPU AMIs for this target are not officially built and published. This recipe allows

### README headings

- ECS-optimized AMI Build Recipes
- Instructions
- Configuration
- Overrides
- Additional Packages
- ECS Logs Collector
- Installation Details
- Cleanup
- IAM Permissions
- Version-locked packages in AL2023 ECS GPU AMIs
- unlock a single package
- unlock all packages
- Memory Overcommit Fix for g6f.large instance type
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 142,691 |
| HCL | 41,923 |
| Makefile | 4,053 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 240
- Forks at capture: 67
- Last updated: 2026-11-19T23:55:53Z
- Last pushed: 2026-11-23T18:16:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ecs-ami)
- [README](https://github.com/aws/amazon-ecs-ami/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-ecs-ami/issues)
- [Releases](https://github.com/aws/amazon-ecs-ami/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
