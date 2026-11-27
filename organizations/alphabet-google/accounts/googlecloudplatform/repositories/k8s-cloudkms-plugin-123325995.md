# GoogleCloudPlatform/k8s-cloudkms-plugin

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/k8s-cloudkms-plugin](https://github.com/GoogleCloudPlatform/k8s-cloudkms-plugin)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/k8s-cloudkms-plugin/blob/main/README.md)
- README blob SHA: 6b08b54f83b7e3b144d28ed786fd276282d5149c
- README bytes captured: 9032
- README truncated at capture limit: False
- Repository ID: 123325995
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

K8S KMS Plugin for Google CloudKMS

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:19:19+00:00

### Short excerpt (up to 300 words)

> This repo contains an implementation of a [Kubernetes KMS Plugin][k8s-kms-plugin] for [Cloud KMS][gcp-kms]. **If you are running on Kubernetes Engine (GKE), you do not need

### README headings

- Kubernetes KMS Plugin for Cloud KMS
- Use with Compute Engine
- Assumptions
- Set environment variables
- The ID of the project. Please note that this is the ID, not the NAME of the
- project. In some cases they are the same, but they can be different. Run
- `gcloud projects list` and choose the value in "project id" column.
- The FQDN email of the service account that will be attached to the VMs which
- run the Kubernetes master nodes.
- These values correspond to the KMS key. KMS crypto keys belong to a key ring
- which belong to a location. For a full list of locations, run
- `gcloud kms locations list`.
- Create Cloud KMS key
- Enable the Cloud KMS API (this only needs to be done once per project
- where KMS is being used).
- Create the Cloud KMS key ring in the specified location.
- Create the Cloud KMS crypto key inside the key ring.
- Grant Service Account key permissions
- Deploy the KMS plugin
- Pull image onto master VMs
- Pick a tag and pin to that tag
- Test the interaction between KMS Plugin and Cloud KMS
- Configure kube-apiserver
- Learn more

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Kubernetes KMS Plugin for Cloud KMS

> This repo contains an implementation of a [Kubernetes KMS Plugin][k8s-kms-plugin] for [Cloud KMS][gcp-kms]. **If you are running on Kubernetes Engine (GKE), you do not need

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 104,841 |
| Shell | 2,548 |
| Makefile | 1,261 |
| Dockerfile | 923 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go/compute/metadata, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/gogo/protobuf, github.com/golang/glog, github.com/golang/groupcache, github.com/golang/protobuf, github.com/google/go-cmp, github.com/google/go-tpm, github.com/google/gofuzz, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, github.com/json-iterator/go, github.com/modern-go/concurrent
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 57
- Forks at capture: 17
- Last updated: 2026-05-14T21:35:26Z
- Last pushed: 2026-07-25T01:34:59Z
- Topics: google-cloudkms, kms, kubernetes

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/k8s-cloudkms-plugin)
- [README](https://github.com/GoogleCloudPlatform/k8s-cloudkms-plugin/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/k8s-cloudkms-plugin/issues)
- [Releases](https://github.com/GoogleCloudPlatform/k8s-cloudkms-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
