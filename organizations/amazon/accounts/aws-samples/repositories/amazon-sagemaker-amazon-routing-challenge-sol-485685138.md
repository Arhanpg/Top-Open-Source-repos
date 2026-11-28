# aws-samples/amazon-sagemaker-amazon-routing-challenge-sol

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-sagemaker-amazon-routing-challenge-sol](https://github.com/aws-samples/amazon-sagemaker-amazon-routing-challenge-sol)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-sagemaker-amazon-routing-challenge-sol/blob/main/README.md)
- README blob SHA: 12f848a90515dea492703767f4a4b3ee1521f874
- README bytes captured: 14291
- README truncated at capture limit: False
- Repository ID: 485685138
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Last Mile Route Sequence Optimization

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T03:10:41+00:00

### Short excerpt (up to 300 words)

> Our solution hierarchically integrates The Quick Start instructions See CONTRIBUTING for more

### README headings

- AWS Last Mile Route Sequence Optimization
- Method Overview
- Training
- Inference
- Folder structure
- Quick Start
- Step 1. Install
- Get the source code
- Setup Python Environment
- if on a SageMaker notebook instance, uncomment and execute the following command instead
- source activate aro
- Install the current version of the package
- Step 2. Obtain data
- Step 3. Preprocess data
- generate package information in Parquet file (training)
- generate travel time matrix for all stops in a route (training)
- generate zone information for each stop (training)
- generate ground-truth zone sequence for each route using the Parquet file generated from `gen_route` action
- generate package information in Parquet (evaluation)
- generate travel time matrix for all stops in a route (evaluation)
- generate zone information for each stop (evaluation)
- Step 4. Upload pre-processed data to S3
- Step 5. Train the PPM model locally
- train the PPM model
- Step 6. Upload the trained model to S3
- optional - set `${s3_model_prefix}` with your own S3 model prefix
- Step 7. Generate sequence locally as a test
- test inference locally
- Step 8. Run sequence generation as a SageMaker processing job
- please set environment variables (e.g. ${bucket_name})

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Method Overview

> Our solution hierarchically integrates

### Getting started and usage: Quick Start

> The Quick Start instructions

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 52,104 |
| Shell | 2,257 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: ortools
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 86
- Forks at capture: 20
- Last updated: 2026-11-02T13:28:43Z
- Last pushed: 2026-01-13T03:35:36Z
- Topics: dynamic-programming, last-mile-delivery, markov-decision-processes, markov-model, ppm, reinforcement-learning, sagemaker-processing, sequence-models

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-sagemaker-amazon-routing-challenge-sol)
- [README](https://github.com/aws-samples/amazon-sagemaker-amazon-routing-challenge-sol/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-sagemaker-amazon-routing-challenge-sol/issues)
- [Releases](https://github.com/aws-samples/amazon-sagemaker-amazon-routing-challenge-sol/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
