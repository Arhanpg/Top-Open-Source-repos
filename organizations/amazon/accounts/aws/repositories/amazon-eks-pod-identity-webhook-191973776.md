# aws/amazon-eks-pod-identity-webhook

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-eks-pod-identity-webhook](https://github.com/aws/amazon-eks-pod-identity-webhook)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-eks-pod-identity-webhook/blob/master/README.md)
- README blob SHA: bc3306dc2b221e31c8b635f591723f418ab6f560
- Repository ID: 191973776
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon EKS Pod Identity Webhook

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:44+00:00

### Short excerpt (up to 100 words)

> This webhook is for mutating pods that will require AWS IAM access. After version v0.3.0, `--in-cluster=true` no longer works and is deprecated. Please use `--in-cluster=false` and manage the cluster certificate with cert-manager or some other external certificate provisioning system. This is because certificates using the `legacy-unknown` signer are no longer signed when using the v1 certificates API. 1. [Create an OIDC provider][1] in IAM for your cluster. You can find the OIDC discovery endpoint by describing your EKS cluster. aws eks describe-cluster --name $CLUSTER_NAME --query cluster.identity.oidc And enter "sts.amazonaws.com" as the client-id 2. Create an IAM role for your pods

### README headings

- Amazon EKS Pod Identity Webhook
- Note
- EKS Walkthrough
- Usage with Windows container workloads
- Usage with non-root container user
- Usage
- AWS_DEFAULT_REGION Injection
- AWS_STS_REGIONAL_ENDPOINTS Injection
- Container credentials workload identity socket
- pod-identity-webhook ConfigMap
- Container Images
- Installation
- Pre-requisites
- In-cluster
- On API server
- Notes
- Code of Conduct
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 125,647 |
| Makefile | 2,445 |
| Shell | 1,609 |
| Dockerfile | 561 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-jose/go-jose/v4, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/golang/protobuf, github.com/google/gnostic-models, github.com/google/uuid, github.com/josharian/intern, github.com/json-iterator/go, github.com/mailru/easyjson
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 692
- Forks at capture: 206
- Last updated: 2026-11-23T07:28:37Z
- Last pushed: 2026-11-11T05:11:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-eks-pod-identity-webhook)
- [README](https://github.com/aws/amazon-eks-pod-identity-webhook/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-eks-pod-identity-webhook/issues)
- [Releases](https://github.com/aws/amazon-eks-pod-identity-webhook/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
