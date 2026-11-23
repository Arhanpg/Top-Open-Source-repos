# aws/amazon-ecs-cni-plugins

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ecs-cni-plugins](https://github.com/aws/amazon-ecs-cni-plugins)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-ecs-cni-plugins/blob/master/README.md)
- README blob SHA: 0b954440746a1621840e9824e0f4b60cb077c2f0
- Repository ID: 82356037
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Networking Plugins repository for ECS Task Networking

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:30+00:00

### Short excerpt (up to 100 words)

> Amazon ECS CNI Plugins is a collection of Container Network Interface(CNI) Plugins used by the Amazon ECS Agent to configure network namespace of containers with Elastic Network Interfaces (ENIs) For more information about Amazon ECS, see the Amazon ECS Developer Guide. For more information about Plugins in this project, see the individual READMEs. * ECS ENI Plugin: configures the network namespace of the container with an ENI device * ECS Bridge Plugin: configures the network namespace of the container to be able to communicate with the credentials endpoint of the ECS Agent * ECS IPAM Plugin: allocates an IP address

### README headings

- Amazon ECS CNI Plugins
- Description
- Plugins
- Security disclosures

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 579,107 |
| Makefile | 3,430 |
| Shell | 2,318 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/cihub/seelog, github.com/containernetworking/cni, github.com/coreos/go-iptables, github.com/davecgh/go-spew, github.com/docker/libkv, github.com/golang/mock
- Makefile (capture: captured)
- vendor/go.etcd.io/bbolt/Makefile (capture: captured)
- vendor/github.com/aws/smithy-go/Makefile (capture: captured)
- vendor/github.com/pkg/errors/Makefile (capture: captured)
- vendor/github.com/vishvananda/netlink/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 101
- Forks at capture: 29
- Last updated: 2026-08-27T16:27:37Z
- Last pushed: 2026-05-22T21:57:13Z
- Topics: cni-plugin

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ecs-cni-plugins)
- [README](https://github.com/aws/amazon-ecs-cni-plugins/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-ecs-cni-plugins/issues)
- [Releases](https://github.com/aws/amazon-ecs-cni-plugins/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
