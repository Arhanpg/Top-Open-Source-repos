# NVIDIA/gpu-monitoring-tools

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/gpu-monitoring-tools](https://github.com/NVIDIA/gpu-monitoring-tools)
- Default branch: master
- README: [Open upstream README](https://github.com/NVIDIA/gpu-monitoring-tools/blob/master/README.md)
- README blob SHA: 5cdd9be6db80d833d0d7c7d2e36bef89d47b7506
- README bytes captured: 7910
- README truncated at capture limit: False
- Repository ID: 134182484
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Tools for monitoring NVIDIA GPUs on Linux 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T06:08:40+00:00

### Short excerpt (up to 300 words)

> You can find the To gather metrics on

### README headings

- FINAL UPDATE: August 2021 - This repository has been deprecated.
- The projects have been moved to their own repositories:
- This repository will exist for a time to allow for migration to the new repositories.
- NVIDIA GPU Monitoring Tools
- Bindings
- DCGM-Exporter
- Quickstart
- HELP DCGM_FI_DEV_SM_CLOCK SM clock frequency (in MHz).
- TYPE DCGM_FI_DEV_SM_CLOCK gauge
- HELP DCGM_FI_DEV_MEM_CLOCK Memory clock frequency (in MHz).
- TYPE DCGM_FI_DEV_MEM_CLOCK gauge
- HELP DCGM_FI_DEV_MEMORY_TEMP Memory temperature (in C).
- TYPE DCGM_FI_DEV_MEMORY_TEMP gauge
- Quickstart on Kubernetes
- Let's get the output of a random pod:
- HELP DCGM_FI_DEV_SM_CLOCK SM clock frequency (in MHz).
- TYPE DCGM_FI_DEV_SM_CLOCK gauge
- HELP DCGM_FI_DEV_MEM_CLOCK Memory clock frequency (in MHz).
- TYPE DCGM_FI_DEV_MEM_CLOCK gauge
- HELP DCGM_FI_DEV_MEMORY_TEMP Memory temperature (in C).
- TYPE DCGM_FI_DEV_MEMORY_TEMP gauge
- Building from Source
- HELP DCGM_FI_DEV_SM_CLOCK SM clock frequency (in MHz).
- TYPE DCGM_FI_DEV_SM_CLOCK gauge
- HELP DCGM_FI_DEV_MEM_CLOCK Memory clock frequency (in MHz).
- TYPE DCGM_FI_DEV_MEM_CLOCK gauge
- HELP DCGM_FI_DEV_MEMORY_TEMP Memory temperature (in C).
- TYPE DCGM_FI_DEV_MEMORY_TEMP gauge
- Changing Metrics
- Format,,

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: What about a Grafana Dashboard?

> You can find the

### Getting started and usage: Quickstart

> To gather metrics on

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 705,254 |
| Go | 257,661 |
| Shell | 6,956 |
| Makefile | 3,037 |
| Mustache | 1,907 |
| Dockerfile | 567 |
| HCL | 113 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver, github.com/NVIDIA/gpu-monitoring-tools/bindings/go/dcgm, github.com/gorilla/mux
- Makefile (capture: captured)
- pkg/Dockerfile (capture: captured)
- pkg/go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver, github.com/NVIDIA/gpu-monitoring-tools/bindings/go/dcgm, github.com/gorilla/mux, github.com/sirupsen/logrus, github.com/stretchr/testify, github.com/urfave/cli/v2, google.golang.org/grpc, k8s.io/kubelet, k8s.io/kubernetes
- deployment/dcgm-exporter/Chart.yaml (capture: captured)
- bindings/go/dcgm/go.mod (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1072
- Forks at capture: 299
- Last updated: 2026-11-05T18:21:11Z
- Last pushed: 2021-11-02T12:55:46Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/gpu-monitoring-tools)
- [README](https://github.com/NVIDIA/gpu-monitoring-tools/blob/master/README.md)
- [Issues](https://github.com/NVIDIA/gpu-monitoring-tools/issues)
- [Releases](https://github.com/NVIDIA/gpu-monitoring-tools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
