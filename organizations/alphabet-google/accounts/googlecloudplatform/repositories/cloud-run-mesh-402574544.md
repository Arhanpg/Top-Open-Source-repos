# GoogleCloudPlatform/cloud-run-mesh

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-run-mesh](https://github.com/GoogleCloudPlatform/cloud-run-mesh)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-run-mesh/blob/main/README.md)
- README blob SHA: f82d7a28fb812ccdcd15e12395490e8ec8feb635
- README bytes captured: 18429
- README truncated at capture limit: False
- Repository ID: 402574544
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:50:09+00:00

### Short excerpt (up to 300 words)

> In K8s, the mesh Requirements: For each region, The setup is similar

### README headings

- Running a CloudRun or docker image in a mesh environment
- Overview
- Architecture
- Before you begin
- Project where the Cloud Run workload will be deployed.
- Project to deploy cluster config resources to. Defaults to PROJECT_ID.
- Override for multi project configurations where the GKE clusters are in a separate project from the Cloud Run resources.
- CloudRun region
- Name of the service account running the CloudRun service. It is recommended to use a dedicated SA for each K8s namespace
- and keep permissions as small as possible.
- By default the namespace is extracted from the GSA name - if using a different SA or naming, WORKLOAD_NAMESPACE env
- is required when deploying the docker image.
- (This may change as we polish the UX)
- Name for the cloudrun service - will use the same as the workload.
- Note that the service must be unique for region, if you want the same name in multiple namespace you must
- use explicit config for WORKLOAD_NAME when deploying and unique cloudrun service name
- Install
- Cluster setup (once per cluster)
- Serverless connector setup (once per project / region / VPC network)
- Multi-project
- Namespace Setup
- Build a mesh-enabled docker image for the app
- Base image. You can create a custom 'golden' base, starting with ASM proxy image and adding the
- startup helper (krun) and other files or configs you need. This doc uses the image
- used for the CI/CD testing.
- Target image
- Deploy the image to CloudRun
- If you didn't build a custom docker image, you can use the prebuilt image:
- IMAGE=gcr.io/wlhe-cr/fortio-mesh:main
- Configure the CloudRun service in K8s

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> In K8s, the mesh

### Getting started and usage: Install

> Requirements: For each region,

### Architecture and design: How it works

> The setup is similar

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 225,382 |
| Makefile | 24,472 |
| Shell | 20,364 |
| Dockerfile | 1,417 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go, github.com/creack/pty, github.com/golang/groupcache, github.com/golang/protobuf, github.com/google/uuid, github.com/json-iterator/go, github.com/pkg/sftp, golang.org/x/crypto, golang.org/x/net, golang.org/x/oauth2, golang.org/x/text, google.golang.org/api, google.golang.org/genproto, google.golang.org/grpc, google.golang.org/protobuf, gopkg.in/yaml.v2, k8s.io/api, k8s.io/apimachinery, k8s.io/client-go, k8s.io/klog
- Makefile (capture: captured)
- samples/distroless/Dockerfile (capture: captured)
- samples/fortio/Dockerfile (capture: captured)
- samples/fortio/Makefile (capture: captured)
- tools/builder/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 35
- Forks at capture: 8
- Last updated: 2025-06-07T13:46:54Z
- Last pushed: 2026-09-02T00:09:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-run-mesh)
- [README](https://github.com/GoogleCloudPlatform/cloud-run-mesh/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-run-mesh/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-run-mesh/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
