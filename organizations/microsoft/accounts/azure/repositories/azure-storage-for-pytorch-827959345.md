# Azure/azure-storage-for-pytorch

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-storage-for-pytorch](https://github.com/Azure/azure-storage-for-pytorch)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/azure-storage-for-pytorch/blob/main/README.md)
- README blob SHA: 7a10ad4bb385a898f30a466452ada0d83eeee27e
- README bytes captured: 9889
- README truncated at capture limit: False
- Repository ID: 827959345
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure Storage Connector for PyTorch

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:03:07+00:00

### Short excerpt (up to 300 words)

> This section highlights core Install the library with Python 3.9 or later While the project is

### README headings

- Azure Storage Connector for PyTorch (`azstoragetorch`) (Preview)
- Documentation
- Backwards compatibility
- Getting started
- Prerequisites
- Installation
- Configuration
- Features
- Saving and loading PyTorch models (Checkpointing)
- Update URL with your own Azure Storage account and container name
- Model to save. Replace with your own model.
- Save trained model to Azure Blob Storage. This saves the model weights
- to a blob named "model_weights.pth" in the container specified by CONTAINER_URL.
- Load trained model from Azure Blob Storage.  This loads the model weights
- from the blob named "model_weights.pth" in the container specified by CONTAINER_URL.
- PyTorch Datasets
- Update URL with your own Azure Storage account and container name
- Create an iterable-style dataset by listing blobs in the container specified by CONTAINER_URL.
- Print the first blob in the dataset. Default output is a dictionary with
- the blob URL and the blob data. Use `transform` keyword argument when
- creating dataset to customize output format.
- List of blob URLs to create dataset from. Update with your own blob names.
- Create a map-style dataset from the list of blob URLs
- Create a DataLoader to load data samples from the dataset in batches of 32
- Additional resources
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> This section highlights core

### Getting started and usage: Installation

> Install the library with

### Technology and requirements: Prerequisites

> Python 3.9 or later

### Limitations and security: Backwards compatibility

> While the project is

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 227,379 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: azure-identity, azure-storage-blob, build, check-manifest, furo, mypy, pytest, ruff, sphinx, sphinx-copybutton, sphinx-design, torch, torchvision, typing-extensions
- doc/sphinx/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 10
- Forks at capture: 12
- Last updated: 2026-09-21T16:39:55Z
- Last pushed: 2026-09-21T20:48:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-storage-for-pytorch)
- [README](https://github.com/Azure/azure-storage-for-pytorch/blob/main/README.md)
- [Issues](https://github.com/Azure/azure-storage-for-pytorch/issues)
- [Releases](https://github.com/Azure/azure-storage-for-pytorch/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
