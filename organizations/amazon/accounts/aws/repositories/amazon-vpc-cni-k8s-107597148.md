# aws/amazon-vpc-cni-k8s

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-vpc-cni-k8s](https://github.com/aws/amazon-vpc-cni-k8s)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/README.md)
- README blob SHA: 019de09d58b8f0f083776f769273f56389544eb6
- README bytes captured: 50801
- README truncated at capture limit: False
- Repository ID: 107597148
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Networking plugin repository for pod networking in Kubernetes using Elastic Network Interfaces on AWS

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T06:35:27+00:00

### Short excerpt (up to 300 words)

> There are 2 components: Type: String Default: strict

### README headings

- amazon-vpc-cni-k8s
- Setup
- IAM Policy
- Building
- Components
- Help & Feedback
- Recommended Version
- Version Upgrade
- ENI Allocation
- Privileged mode
- Network Policies
- Network Policy Related Components
- ConfigMap
- Helm Charts
- CNI Configuration Variables<a name="cni-env-vars"></a>
- `AWS_MANAGE_ENIS_NON_SCHEDULABLE` (v1.12.6+)
- `AWS_VPC_CNI_NODE_PORT_SUPPORT`
- `AWS_VPC_K8S_CNI_CUSTOM_NETWORK_CFG`
- `ENI_CONFIG_ANNOTATION_DEF`
- `ENI_CONFIG_LABEL_DEF`
- `HOST_CNI_BIN_PATH`
- `HOST_CNI_CONFDIR_PATH`
- `AWS_VPC_ENI_MTU` (v1.6.0+)
- `AWS_VPC_K8S_CNI_EXTERNALSNAT`
- `AWS_VPC_K8S_CNI_RANDOMIZESNAT`
- `AWS_VPC_K8S_CNI_EXCLUDE_SNAT_CIDRS` (v1.6.0+)
- `POD_MTU` (v1.16.4+)
- `WARM_ENI_TARGET`
- `WARM_IP_TARGET`
- `MINIMUM_IP_TARGET` (v1.6.0+)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Components

> There are 2 components:

### Limitations and security: `POD_SECURITY_GROUP_ENFORCING_MODE` (v1.11.0+)

> Type: String Default: strict

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 2,302,230 |
| Shell | 97,834 |
| Makefile | 19,829 |
| Mustache | 5,646 |
| Go Template | 1,882 |
| Dockerfile | 1,298 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: dario.cat/mergo, github.com/Azure/go-ansiterm, github.com/BurntSushi/toml, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/ProtonMail/go-crypto, github.com/apparentlymart/go-cidr, github.com/asaskevich/govalidator, github.com/aws/amazon-vpc-cni-k8s/test/agent, github.com/aws/amazon-vpc-resource-controller-k8s, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a
- Makefile (capture: captured)
- charts/aws-vpc-cni/Chart.yaml (capture: captured)
- charts/cni-metrics-helper/Chart.yaml (capture: captured)
- test/agent/Dockerfile (capture: captured)
- test/agent/go.mod (capture: captured) — dependency clues: github.com/aws/amazon-vpc-cni-k8s, github.com/coreos/go-iptables, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/vishvananda/netlink, github.com/vishvananda/netns, go.uber.org/multierr, go.uber.org/zap, golang.org/x/sys, gopkg.in/natefinch/lumberjack.v2

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2460
- Forks at capture: 852
- Last updated: 2026-11-19T22:07:36Z
- Last pushed: 2026-11-23T18:13:26Z
- Topics: cni-plugin, kubernetes, pod-networking

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-vpc-cni-k8s)
- [README](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-vpc-cni-k8s/issues)
- [Releases](https://github.com/aws/amazon-vpc-cni-k8s/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
