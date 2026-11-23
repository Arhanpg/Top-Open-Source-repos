# aws/amazon-eks-connector

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-eks-connector](https://github.com/aws/amazon-eks-connector)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-eks-connector/blob/main/README.md)
- README blob SHA: 78a5aa16a025a2cc69496354e26f551e4f36c0d6
- Repository ID: 424747406
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:40+00:00

### Short excerpt (up to 100 words)

> EKS Connector is a client-side agent that connects any Kubernetes cluster to AWS. EKS Connector runs in Kubernetes as a Pod that consists of below containers: The init container is responsible for initiating the state of EKS Connector. The proxy container is responsible for proxying Kubernetes API Server traffic and applying appropriate user-impersonation flow. The agent container runs the AWS System Manager Agent. It maintains a persistent, secure connection between the Kubernetes cluster and AWS. AWS SSM agent is published at ECR Public Run the following command against the cluster after retrieving your activation code and id. See the guide

### README headings

- EKS Connector
- How it works
- init container
- proxy container
- agent container
- Development
- Install from repo
- Updating dependencies
- Release
- Test
- Fill in the activation ID and activation code.
- Replace with your custom built images if needed
- Apply the manifest
- After a few seconds the connector pod should be healthy in kubernetes.
- Now get the managed instance at SSM.
- If you are lucky you should see exactly one managed instance.
- Alternatively, grep the logs at init container, which should print out the instance id.
- Now execute non interactive command
- NOTE: fill in TARGET with your own managed instance id like `mi-069f7e4b6ce64c0ce`
- Cleanup
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 80,367 |
| Makefile | 2,101 |
| Dockerfile | 569 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/evanphx/json-patch, github.com/fsnotify/fsnotify, github.com/go-logr/logr, github.com/gogo/protobuf, github.com/golang/protobuf, github.com/google/go-cmp, github.com/google/gofuzz, github.com/google/uuid, github.com/googleapis/gnostic, github.com/hashicorp/hcl, github.com/inconshreveable/mousetrap, github.com/jmespath/go-jmespath, github.com/json-iterator/go, github.com/magiconair/properties, github.com/mitchellh/mapstructure, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/pelletier/go-toml
- Makefile (capture: captured)
- configuration/Dockerfile (capture: captured)
- charts/eks-connector/Chart.yaml (capture: captured)
- vendor/gopkg.in/ini.v1/Makefile (capture: captured)
- vendor/github.com/hashicorp/hcl/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 62
- Forks at capture: 13
- Last updated: 2026-09-14T11:38:01Z
- Last pushed: 2024-07-15T17:31:57Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-eks-connector)
- [README](https://github.com/aws/amazon-eks-connector/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-eks-connector/issues)
- [Releases](https://github.com/aws/amazon-eks-connector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
