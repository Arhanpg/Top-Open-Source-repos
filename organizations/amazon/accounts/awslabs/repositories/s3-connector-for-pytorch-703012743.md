# awslabs/s3-connector-for-pytorch

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/s3-connector-for-pytorch](https://github.com/awslabs/s3-connector-for-pytorch)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/s3-connector-for-pytorch/blob/main/README.md)
- README blob SHA: e49124fa80e54fedb7c12aec88ac33c0ad75b389
- README bytes captured: 21826
- README truncated at capture limit: False
- Repository ID: 703012743
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Amazon S3 Connector for PyTorch delivers high throughput for PyTorch training jobs that access and store data in Amazon S3.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:50:55+00:00

### Short excerpt (up to 300 words)

> bucket = item.bucket key pip install s3torchconnector Amazon Python 3.8-3.14 is supported. S3 Connector for PyTorch

### README headings

- Amazon S3 Connector for PyTorch
- Getting Started
- Prerequisites
- Installation
- Configuration
- Examples
- Sample Examples
- You need to update <BUCKET> and <PREFIX>
- Datasets are also iterators.
- S3MapDataset eagerly lists all the objects under the given prefix
- to provide support of random access.
- S3MapDataset builds a list of all objects at the first access to its elements or
- at the first call to get the number of elements, whichever happens first.
- This process might take some time and may give the impression of being unresponsive.
- Randomly access an item in map_dataset.
- Learn about bucket, key, and content of the object
- Save checkpoint to S3
- Load checkpoint from S3
- Distributed checkpoints
- Overview
- Prerequisites and Installation
- Sample Example
- Configuration
- Save distributed checkpoint to S3
- Load distributed checkpoint from S3
- S3StorageReader uses DCPOptimizedS3Reader by default for improved performance
- S3 Prefix Strategies for Distributed Checkpointing
- Available Strategies
- 1. RoundRobinPrefixStrategy
- Initialize with multiple prefixes and optional epoch tracking

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Learn about bucket, key, and content of the object

> bucket = item.bucket key

### Getting started and usage: Installation

> pip install s3torchconnector Amazon

### Technology and requirements: Prerequisites

> Python 3.8-3.14 is supported.

### Limitations and security: Compatibility with other storage services

> S3 Connector for PyTorch

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 553,637 |
| Rust | 45,980 |
| Shell | 6,289 |
| Jupyter Notebook | 6,220 |
| Batchfile | 787 |
| Makefile | 634 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- s3torchbenchmarking/pyproject.toml (capture: captured) — dependency clues: boto3, click, hydra-core, pandas, pillow, prefixed, psutil, pynvml, pytest, requests, s3fs, s3torchconnector, torchdata, torchvision, transformers
- s3torchconnector/pyproject.toml (capture: captured) — dependency clues: Pillow, black, boto3, flake8, fsspec, hypothesis, importlib_metadata, lightning, mypy, numpy, packaging, pytest, pytest-timeout, pytest-xdist, s3fs, s3torchconnector, s3torchconnectorclient, tenacity, torch, torchdata
- s3torchconnectorclient/Cargo.toml (capture: captured) — dependency clues: built, futures, log, mountpoint-s3-client, mountpoint-s3-crt-sys, nix, pyo3, rusty-fork, tracing, tracing-appender, tracing-subscriber
- s3torchconnectorclient/pyproject.toml (capture: captured) — dependency clues: Pillow, black, boto3, flake8, hypothesis, mypy, pytest, pytest-timeout
- s3torchconnector/docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 214
- Forks at capture: 37
- Last updated: 2026-09-25T11:49:36Z
- Last pushed: 2026-10-16T15:03:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/s3-connector-for-pytorch)
- [README](https://github.com/awslabs/s3-connector-for-pytorch/blob/main/README.md)
- [Issues](https://github.com/awslabs/s3-connector-for-pytorch/issues)
- [Releases](https://github.com/awslabs/s3-connector-for-pytorch/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
