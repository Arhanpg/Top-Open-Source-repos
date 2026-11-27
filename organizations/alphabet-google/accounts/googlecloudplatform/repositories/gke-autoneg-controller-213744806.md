# GoogleCloudPlatform/gke-autoneg-controller

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/gke-autoneg-controller](https://github.com/GoogleCloudPlatform/gke-autoneg-controller)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/gke-autoneg-controller/blob/master/README.md)
- README blob SHA: ba9309526f65c62d5c80c3bb569d3ce5de104d9f
- README bytes captured: 15228
- README truncated at capture limit: False
- Repository ID: 213744806
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This GKE controller provides simple custom integration between GKE and GCLB.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:37:18+00:00

### Short excerpt (up to 300 words)

> First, set up the autoneg depends on the Since the GKE cluster

### README headings

- ![Autoneg GKE controller](assets/img/autoneg.png)
- How it works
- Using Autoneg
- Example annotations
- Autoneg Configuration
- Options
- Autoneg annotation options
- Controller parameters
- Automatic regional preference
- IAM considerations
- Security considerations
- Installation
- Installation via Terraform
- Installation via Helm charts
- helm install -n autoneg-system --create-namespace --set 'createNamespace=false' autoneg deploy/chart/
- Customizing your installation

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> First, set up the

### Architecture and design: How it works

> autoneg depends on the

### Limitations and security: Security considerations

> Since the GKE cluster

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 152,103 |
| HCL | 54,569 |
| Python | 18,695 |
| Makefile | 5,699 |
| Go Template | 3,050 |
| Shell | 1,411 |
| Dockerfile | 1,381 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, github.com/antlr4-go/antlr/v4, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/felixge/httpsnoop, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference
- Makefile (capture: captured)
- deploy/chart/Chart.yaml (capture: captured)
- terraform/test/requirements.txt (capture: captured) — dependency clues: google-auth, google-cloud-compute, google-cloud-logging, kubernetes, pyOpenSSL, termcolor, timelength

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 180
- Forks at capture: 68
- Last updated: 2026-11-11T16:53:32Z
- Last pushed: 2026-11-14T05:29:03Z
- Topics: gclb, gke

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/gke-autoneg-controller)
- [README](https://github.com/GoogleCloudPlatform/gke-autoneg-controller/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/gke-autoneg-controller/issues)
- [Releases](https://github.com/GoogleCloudPlatform/gke-autoneg-controller/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
