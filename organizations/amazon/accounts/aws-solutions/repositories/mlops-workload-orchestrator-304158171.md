# aws-solutions/mlops-workload-orchestrator

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/mlops-workload-orchestrator](https://github.com/aws-solutions/mlops-workload-orchestrator)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/mlops-workload-orchestrator/blob/main/README.md)
- README blob SHA: ef10dae3a9c0bb5005f1204d82bf7a7ac2850a75
- Repository ID: 304158171
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The MLOps Workload Orchestrator solution helps you streamline and enforce architecture best practices for machine learning (ML) model productionization. This solution is an extendable framework that provides a standard interface for managing ML pipelines for AWS ML services and third-party services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:36+00:00

### Short excerpt (up to 100 words)

> As of 06/10/2025, The MLOps Workload Orchestrator solution has been deprecated and will not be receiving any additional features or updates. We encourage customers to explore using Amazon SageMaker Unified Studio to manage their ML workloads. The machine learning (ML) lifecycle is an iterative and repetitive process that involves changing models over time and learning from new data. As ML applications gain popularity, organizations are building new and better applications for a wide range of use cases including optimized email campaigns, forecasting tools, recommendation engines, self-driving vehicles, virtual personal assistants, and more. While operational and pipelining processes vary greatly across

### README headings

- Deprecation Notice
- mlops-workload-orchestrator
- Benefits
- Architecture
- Template option 1: Single account deployment
- Template option 2: Multi-account deployment
- File Structure
- Creating a custom build
- Prerequisites
- 1. Clone the repository
- 2. Build the solution for deployment
- Uninstall the solution
- Collection of operational metrics
- Known Issues
- Image Builder Pipeline may fail due to Docker Hub rate limits

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,044,461 |
| Shell | 26,477 |
| JavaScript | 3,555 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, aws-cdk.aws-servicecatalogappregistry-alpha, aws-solutions-constructs.aws-apigateway-lambda, aws-solutions-constructs.aws-lambda-sagemakerendpoint, aws-solutions-constructs.core, constructs
- deployment/cdk-solution-helper/package.json (capture: captured) — dependency clues: fs
- source/lambdas/custom_resource/requirements.txt (capture: captured) — dependency clues: crhelper
- source/lambdas/custom_resource/setup.py (capture: captured)
- source/lambdas/pipeline_orchestration/setup.py (capture: captured)
- source/lambdas/solution_helper/requirements.txt (capture: captured) — dependency clues: crhelper, requests, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 157
- Forks at capture: 56
- Last updated: 2026-10-06T08:53:14Z
- Last pushed: 2025-06-10T18:28:29Z
- Topics: artificial-intelligence, machine-learning, mlops

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/mlops-workload-orchestrator)
- [README](https://github.com/aws-solutions/mlops-workload-orchestrator/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/mlops-workload-orchestrator/issues)
- [Releases](https://github.com/aws-solutions/mlops-workload-orchestrator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
