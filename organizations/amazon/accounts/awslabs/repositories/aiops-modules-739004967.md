# awslabs/aiops-modules

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aiops-modules](https://github.com/awslabs/aiops-modules)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/aiops-modules/blob/main/README.md)
- README blob SHA: eced6424605df09bd4982322d71970ba1d632913
- Repository ID: 739004967
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AIOps modules is a collection of reusable Infrastructure as Code (IaC) modules for Machine Learning (ML), Foundation Models (FM), Large Language Models (LLM) and GenAI development and operations on AWS

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:46+00:00

### Short excerpt (up to 100 words)

> AIOps modules is a collection of reusable Infrastructure as Code (IAC) modules that works with SeedFarmer CLI. Please see the DOCS for all things seed-farmer. The modules in this repository are decoupled from each other and can be aggregated together using GitOps (manifest file) principles provided by `seedfarmer` and achieve the desired use cases. It removes the undifferentiated heavy lifting for an end user by providing hardended modules and enables them to focus on building business on top of them. The modules in this repository are / must be generic for reuse without affiliation to any one particular project in

### README headings

- AIOps Modules
- General Information
- Deployment
- Project Manifests
- Modules
- SageMaker Modules
- Mlflow Modules
- FMOps/LLMOps Modules
- Agent Modules
- MWAA Modules
- MLOps using Step Functions Module
- EKS Modules
- Example Modules
- Industry Data Framework (IDF) Modules
- Autonomous Driving Data Framework (ADDF) Modules

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 950,501 |
| TypeScript | 90,148 |
| HCL | 68,976 |
| Jupyter Notebook | 30,315 |
| Shell | 9,429 |
| Dockerfile | 3,590 |
| JavaScript | 3,526 |
| Go Template | 1,932 |
| Batchfile | 437 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: seed-farmer
- modules/eks/ray-cluster/pyproject.toml (capture: captured)
- modules/eks/ray-cluster/requirements.txt (capture: captured) — dependency clues: annotated-types, attrs, aws-cdk-asset-awscli-v1, aws-cdk-asset-kubectl-v20, aws-cdk-asset-node-proxy-agent-v6, aws-cdk-cloud-assembly-schema, aws-cdk-lambda-layer-kubectl-v29, aws-cdk-lib, cattrs, constructs, importlib-resources, jsii, publication, pydantic, pydantic-core, pydantic-settings, python-dateutil, python-dotenv, pyyaml, six
- modules/eks/ray-operator/pyproject.toml (capture: captured)
- modules/eks/ray-operator/requirements.txt (capture: captured) — dependency clues: annotated-types, attrs, aws-cdk-asset-awscli-v1, aws-cdk-asset-kubectl-v20, aws-cdk-asset-node-proxy-agent-v6, aws-cdk-cloud-assembly-schema, aws-cdk-lambda-layer-kubectl-v29, aws-cdk-lib, cattrs, constructs, importlib-resources, jsii, publication, pydantic, pydantic-core, pydantic-settings, python-dateutil, python-dotenv, pyyaml, six
- modules/eks/ray-orchestrator/pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 104
- Forks at capture: 36
- Last updated: 2026-11-02T09:41:02Z
- Last pushed: 2026-05-11T17:27:04Z
- Topics: aiops, aws, bedrock, fmops, genai, llmops, mlflow, mlops, sagemaker

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aiops-modules)
- [README](https://github.com/awslabs/aiops-modules/blob/main/README.md)
- [Issues](https://github.com/awslabs/aiops-modules/issues)
- [Releases](https://github.com/awslabs/aiops-modules/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
