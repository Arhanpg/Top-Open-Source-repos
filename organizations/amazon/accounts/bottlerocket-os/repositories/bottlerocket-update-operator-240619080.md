# bottlerocket-os/bottlerocket-update-operator

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-update-operator](https://github.com/bottlerocket-os/bottlerocket-update-operator)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-update-operator/blob/develop/README.md)
- README blob SHA: 42bb367d2e83cd5e15d85f2e5a86e11a0a60923f
- Repository ID: 240619080
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Kubernetes operator for automated updates to Bottlerocket

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:06:12+00:00

### Short excerpt (up to 100 words)

> The Bottlerocket update operator (or, for short, Brupop) is a Kubernetes operator that coordinates Bottlerocket updates on hosts in a cluster. When installed, the Bottlerocket update operator starts a controller deployment on one node, an agent daemon set on every Bottlerocket node, and an Update Operator API Server deployment. The controller orchestrates updates across your cluster, while the agent is responsible for periodically querying for Bottlerocket updates, draining the node, and performing the update when asked by the controller. The agent performs all cluster object mutation operations via the API Server, which performs additional authorization using the Kubernetes TokenReview API

### README headings

- Bottlerocket Update Operator
- Getting Started
- Version Support Policy
- Installation
- Add the cert-manager helm chart
- Update your local chart cache with the latest
- Install the cert-manager (including its CRDs)
- Add the bottlerocket-update-operator chart
- Update your local chart cache with the latest updates
- Create a namespace
- Install the brupop CRD
- Install the brupop operator
- Configuration
- Configure via Helm values yaml file
- Default values for bottlerocket-update-operator.
- The namespace to deploy the update operator into
- The image to use for brupop
- This defaults to the image built alongside a particular helm chart, but you can override it by uncommenting this line:
- image: "public.ecr.aws/bottlerocket/bottlerocket-update-operator:v1.8.0"
- Placement controls
- See the Kubernetes documentation about placement controls for more details:
- * https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
- * https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
- * https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity
- If testing against a private image registry, you can set the pull secret to fetch images.
- This can likely remain as `brupop` so long as you run something like the following:
- kubectl create secret docker-registry brupop \
- --docker-server 109276217309.dkr.ecr.us-west-2.amazonaws.com \
- --docker-username=AWS \
- --docker-password=$(aws --region us-west-2 ecr get-login-password) \

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 410,139 |
| Shell | 5,513 |
| Makefile | 5,231 |
| Dockerfile | 1,923 |
| Mustache | 1,735 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Dockerfile (capture: captured)
- Makefile (capture: captured)
- agent/Cargo.toml (capture: captured) — dependency clues: apiserver, chrono, futures, governor, http, k8s-openapi, kube, lazy_static, models, nonzero_ext, semver, serde, serde_json, snafu, tokio, tokio-retry, tracing
- apiserver/Cargo.toml (capture: captured) — dependency clues: actix-web, async-trait, awc, futures, governor, http, k8s-openapi, kube, lazy_static, log, maplit, mockall, models, nonzero_ext, opentelemetry, opentelemetry-instrumentation-actix-web, opentelemetry-prometheus, opentelemetry_sdk, prometheus, reqwest
- controller/Cargo.toml (capture: captured) — dependency clues: actix-web, chrono, cron, futures, http, k8s-openapi, kube, lazy_static, maplit, models, opentelemetry, opentelemetry-prometheus, opentelemetry_sdk, prometheus, regex, semver, serde, serde_plain, snafu, tokio

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 221
- Forks at capture: 51
- Last updated: 2026-10-22T08:28:27Z
- Last pushed: 2026-07-29T18:46:20Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-update-operator)
- [README](https://github.com/bottlerocket-os/bottlerocket-update-operator/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-update-operator/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-update-operator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
