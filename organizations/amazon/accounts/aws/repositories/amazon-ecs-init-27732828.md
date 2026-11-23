# aws/amazon-ecs-init

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ecs-init](https://github.com/aws/amazon-ecs-init)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-ecs-init/blob/master/README.md)
- README blob SHA: 3b1845ffe55d1dc4474786977936282ff2d806ff
- Repository ID: 27732828
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ecs-init is now part of the amazon-ecs-agent repo https://github.com/aws/amazon-ecs-agent/tree/master/ecs-init

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:32+00:00

### Short excerpt (up to 100 words)

> The Amazon Elastic Container Service RPM is software developed to support the [Amazon ECS Container Agent](http://github.com/aws/amazon-ecs-agent). The Amazon ECS RPM is packaged for RPM-based systems that utilize The upstart script installed by the Amazon ECS RPM runs at the completion of runlevel 3, 4, or 5 as the system starts. The script will clean up any previous copies of the Amazon ECS Container Agent, and then start a new copy. Logs from the RPM are available at `/var/log/ecs/ecs-init.log`, while logs from the Amazon ECS Container Agent are available at `/var/log/ecs/ecs-agent.log`. The Amazon ECS RPM makes the Amazon ECS Container Agent

### README headings

- Amazon Elastic Container Service RPM
- Behavior
- Usage
- Updates
- Security disclosures
- Development
- Building the RPM for test
- send rpm either through s3 or scp
- Dev dependencies
- Generating mocks
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 245,749 |
| Shell | 32,374 |
| Makefile | 7,038 |
| Roff | 3,196 |
| Python | 1,442 |
| Dockerfile | 1,387 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- ecs-init/vendor/github.com/fsouza/go-dockerclient/Makefile (capture: captured)
- ecs-init/vendor/github.com/jmespath/go-jmespath/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 197
- Forks at capture: 109
- Last updated: 2026-09-08T05:18:37Z
- Last pushed: 2023-08-31T17:19:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ecs-init)
- [README](https://github.com/aws/amazon-ecs-init/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-ecs-init/issues)
- [Releases](https://github.com/aws/amazon-ecs-init/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
