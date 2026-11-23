# aws-observability/aws-sigv4-proxy-admission-controller

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-sigv4-proxy-admission-controller](https://github.com/aws-observability/aws-sigv4-proxy-admission-controller)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-observability/aws-sigv4-proxy-admission-controller/blob/master/README.md)
- README blob SHA: 79ef33012a76add63d8fbc7905a2a0528926ad4e
- Repository ID: 288855626
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This project creates a mutation admission controller that injects AWS SIGv4 proxy as a sidecar.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:14:28+00:00

### Short excerpt (up to 100 words)

> The mutation admission controller will inject the AWS SIGv4 Proxy as a sidecar into a pod if there are annotations specified in a container's deployment.yaml file or specific namespace labels. A helm chart exists to deploy all the resources needed to use the admission controller here: https://github.com/aws/eks-charts/tree/master/stable/aws-sigv4-proxy-admission-controller/. Add the EKS repository to Helm: helm repo add eks https://aws.github.io/eks-charts Install the AWS SIGv4 Admission Controller chart with default configuration: helm install aws-sigv4-proxy-admission-controller eks/aws-sigv4-proxy-admission-controller --namespace <namespace> To uninstall/delete the `aws-sigv4-proxy-admission-controller` release: helm uninstall aws-sigv4-proxy-admission-controller --namespace <namespace> If you wish to build the image on your own, change the variables in Makefile for

### README headings

- AWS SIGv4 Proxy Admission Controller
- Getting Started
- Installing the Controller via Helm Chart
- Uninstalling the Helm Chart
- Doing It Yourself
- Usage
- Configuration
- Example Deployment
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 28,961 |
| Dockerfile | 573 |
| Makefile | 514 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/gogo/protobuf, github.com/golang/protobuf, github.com/google/gnostic-models, github.com/google/gofuzz, github.com/google/uuid, github.com/josharian/intern, github.com/json-iterator/go, github.com/mailru/easyjson, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/pmezard/go-difflib, github.com/stretchr/objx, github.com/stretchr/testify
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 27
- Forks at capture: 12
- Last updated: 2026-10-28T23:19:13Z
- Last pushed: 2026-11-02T23:49:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-sigv4-proxy-admission-controller)
- [README](https://github.com/aws-observability/aws-sigv4-proxy-admission-controller/blob/master/README.md)
- [Issues](https://github.com/aws-observability/aws-sigv4-proxy-admission-controller/issues)
- [Releases](https://github.com/aws-observability/aws-sigv4-proxy-admission-controller/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
