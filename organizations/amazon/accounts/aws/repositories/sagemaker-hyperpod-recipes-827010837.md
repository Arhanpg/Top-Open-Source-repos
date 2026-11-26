# aws/sagemaker-hyperpod-recipes

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/sagemaker-hyperpod-recipes](https://github.com/aws/sagemaker-hyperpod-recipes)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/sagemaker-hyperpod-recipes/blob/main/README.md)
- README blob SHA: 9bc17faa3d718b56b45f4e1d22bf7d43373f29ba
- README bytes captured: 23903
- README truncated at capture limit: False
- Repository ID: 827010837
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:20:00+00:00

### Short excerpt (up to 300 words)

> Amazon SageMaker HyperPod recipes Amazon SageMaker HyperPod recipes See CONTRIBUTING for more

### README headings

- Amazon SageMaker HyperPod Recipes
- Overview
- Version History
- Supported Models and Techniques
- Supported Models
- Supported Techniques
- Supported Accelerators
- Advanced Training Frameworks
- LLMFT (LLM Fine-Tuning Framework)
- VERL (Versatile Reinforcement Learning)
- Checkpointless Training
- Elastic Training
- Multi-Turn Reinforcement Learning (MTRL)
- Evaluation
- Logging Support
- Installation
- Usage Guide
- Container Images
- Running a recipe on a SageMaker HyperPod cluster orchestrated by Amazon EKS
- Running a recipe on a SageMaker HyperPod cluster orchestrated by Slurm
- Configuring the Recipe
- Running the Training Job
- Running a recipe on SageMaker training jobs
- install SageMaker SDK
- Override any recipe fields. Here we point the recipe's output at the standard
- SageMaker training-job container path so artifacts are uploaded to S3.
- Compute for the training job. instance_type is required for recipes and must be
- a GPU or Trainium instance type.
- (Optional) stream TensorBoard logs to S3.
- Running a recipe with SageMaker serverless model customization

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> Amazon SageMaker HyperPod recipes

### Getting started and usage: Installation

> Amazon SageMaker HyperPod recipes

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,029,713 |
| Shell | 1,013,470 |
| Dockerfile | 10,564 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: PyYAML, boto3, hydra-core, omegaconf, pathspec, pydantic, pynvml, pytest-cov, pytest-subtests, pytest-xdist, requests, ruamel.yaml, sagemaker, tensorboard, tqdm, zstandard
- requirements.txt (capture: captured) — dependency clues: PyYAML, boto3, hydra-core, omegaconf, pathspec, pydantic, pynvml, pytest-cov, pytest-subtests, pytest-xdist, requests, ruamel.yaml, tensorboard, tqdm, zstandard
- launcher/nemo/nemo_framework_launcher/Dockerfile (capture: captured)
- launcher/nemo/nemo_framework_launcher/requirements.txt (capture: captured) — dependency clues: hydra-core, omegaconf, pynvml, requests, tqdm, zstandard
- launcher/evaluation/k8s_templates/EVAL/Chart.yaml (capture: captured)
- launcher/nemo/k8s_templates/ray/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 100
- Forks at capture: 32
- Last updated: 2026-11-03T07:50:09Z
- Last pushed: 2026-11-17T21:50:00Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/sagemaker-hyperpod-recipes)
- [README](https://github.com/aws/sagemaker-hyperpod-recipes/blob/main/README.md)
- [Issues](https://github.com/aws/sagemaker-hyperpod-recipes/issues)
- [Releases](https://github.com/aws/sagemaker-hyperpod-recipes/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
