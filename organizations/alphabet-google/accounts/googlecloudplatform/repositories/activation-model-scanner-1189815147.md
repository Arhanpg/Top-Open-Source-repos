# GoogleCloudPlatform/activation-model-scanner

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/activation-model-scanner](https://github.com/GoogleCloudPlatform/activation-model-scanner)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/activation-model-scanner/blob/main/README.md)
- README blob SHA: d06b76378b1dad79feef372e143eb4cbe48653cd
- Repository ID: 1189815147
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Verify language model safety before deployment by analyzing activation patterns

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T21:21:29+00:00

### Short excerpt (up to 100 words)

> **Verify language model safety before deployment by analyzing activation patterns.** **Disclaimer:** This is not an officially supported Google product. This project is not eligible for the Google Open Source Software Vulnerability Rewards Program. AMS detects whether a model has intact safety training by measuring the separation of safety-relevant concepts in the model's activation space. Models with removed or degraded safety training (e.g., "uncensored" fine-tunes, abliterated models) show collapsed safety directions that AMS can detect in seconds. AMS requires a GPU for standard operation. Scan times of 10–40 seconds quoted in the paper are based on NVIDIA A100/L4 hardware. You can

### README headings

- AMS - Activation-based Model Scanner
- Platform Requirements
- Quick Start
- Install from PyPI with CLI tools
- Or clone and install from source
- Usage Examples
- Scan an ungated model (no authentication required)
- Scan a gated model (requires Hugging Face authentication — see below)
- Scan with identity verification against a baseline
- Hugging Face Authentication
- Security Considerations
- How It Works
- Core Insight
- Two-Tier Scanning
- Usage
- Basic Scan
- Standard scan (3 concepts: harmful_content, injection_resistance, refusal_capability)
- Quick scan (2 concepts, ~40% faster)
- Full scan (4 concepts including truthfulness)
- JSON output for CI/CD pipelines
- Identity Verification
- First, create a baseline from the official model
- Then verify an unknown model against it
- Baseline Management
- List available baselines
- Create baseline with custom ID
- Show baseline details
- Quantized Models
- Scan 8-bit quantized model
- Scan 4-bit quantized model

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 112,809 |
| Shell | 3,303 |
| Makefile | 1,800 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: accelerate, ams-scanner, bitsandbytes, black, einops, isort, mypy, numpy, protobuf, pytest, pytest-cov, rich, ruff, safetensors, sentencepiece, tiktoken, torch, transformers

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 36
- Forks at capture: 10
- Last updated: 2026-11-19T00:56:06Z
- Last pushed: 2026-11-04T23:30:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/activation-model-scanner)
- [README](https://github.com/GoogleCloudPlatform/activation-model-scanner/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/activation-model-scanner/issues)
- [Releases](https://github.com/GoogleCloudPlatform/activation-model-scanner/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
