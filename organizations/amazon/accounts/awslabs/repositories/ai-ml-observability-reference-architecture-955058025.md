# awslabs/ai-ml-observability-reference-architecture

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/ai-ml-observability-reference-architecture](https://github.com/awslabs/ai-ml-observability-reference-architecture)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/ai-ml-observability-reference-architecture/blob/main/README.md)
- README blob SHA: 1178719ad32746ab4fe7190ac1ac0db6fcfca4b7
- Repository ID: 955058025
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:02:53+00:00

### Short excerpt (up to 100 words)

> This project provides a comprehensive monitoring solution for AI and ML workloads running on Kubernetes. This open source observability stack integrates three key components to deliver end-to-end visibility into AI/ML infrastructure and applications: * **Prometheus** serves as the core metrics collection and storage engine, gathering performance data from GPU utilization and memory metrics (via DCGM for NVIDIA GPUs), CPU, memory, network, and storage metrics from Kubernetes nodes, application-specific metrics from AI/ML workloads like Ray training jobs and vLLM inference servers, and Kubernetes cluster metrics and resource utilization. * **Grafana** functions as the primary visualization and dashboarding platform, providing pre-built dashboards

### README headings

- ai-ml-observability-reference-architecture
- About
- Why?
- Traditional observability
- Agent-augmented observability
- Deployment
- Getting started
- Prerequisites
- Deployment
- Option 1: Kustomize
- Option 2: Helm
- Download subchart dependencies
- Install with default settings (all core components enabled, MCP disabled)
- Components
- MCP Servers
- Enable MCP but only deploy the Prometheus server
- Helm Values Reference
- Component toggles
- Subchart configuration (passed through to upstream Helm charts)
- Security
- Grafana
- OpenSearch
- Example
- Setup
- Training
- Inference
- Repository Structure
- Support
- Roadmap
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 11,851 |
| Go Template | 804 |
| Dockerfile | 204 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- chart/Chart.yaml (capture: captured)
- deploy/agent/Dockerfile (capture: captured)
- deploy/agent/requirements.txt (capture: captured) — dependency clues: fastapi, mcp, pydantic, sse-starlette, strands-agents, strands-agents-tools, uvicorn

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 7
- Last updated: 2026-07-01T18:37:17Z
- Last pushed: 2026-03-18T17:58:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/ai-ml-observability-reference-architecture)
- [README](https://github.com/awslabs/ai-ml-observability-reference-architecture/blob/main/README.md)
- [Issues](https://github.com/awslabs/ai-ml-observability-reference-architecture/issues)
- [Releases](https://github.com/awslabs/ai-ml-observability-reference-architecture/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
