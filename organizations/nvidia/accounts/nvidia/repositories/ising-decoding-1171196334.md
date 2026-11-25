# NVIDIA/Ising-Decoding

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/Ising-Decoding](https://github.com/NVIDIA/Ising-Decoding)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/Ising-Decoding/blob/main/README.md)
- README blob SHA: 536cd10824fc401b3f2091faeade2c0a54509b71
- README bytes captured: 61155
- README truncated at capture limit: False
- Repository ID: 1171196334
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A set of training recipes for AI Quantum Error Correction Decoders

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T07:46:09+00:00

### Short excerpt (up to 300 words)

> From the repo root: Target Python versions: **3.11, The narrow conf/config_public.yaml covers

### README headings

- Ising Decoding
- Table of Contents
- Publication
- High-level workflow
- Quick start (train + inference)
- Dependencies
- Optional: create and activate a virtual environment
- Optional: install CUDA-enabled PyTorch (example: pick any available cuXXX)
- Pick one that matches your CUDA runtime; cu130 is known to work.
- Inference-only (training install is a superset)
- Training (includes inference deps, adjust to cu13 as appropriate).
- The cu12 file takes PyTorch from the cu128 wheel index.
- Train (reads conf/config_public.yaml)
- Inference (loads a saved model from outputs/<exp>/models/*)
- Troubleshooting
- Inference (pre-trained models)
- Model export and downstream tools
- Converting .pt checkpoints to SafeTensors (optional, post-training)
- ONNX export and quantization (optional, post-training)
- Export ONNX only (no TensorRT)
- Export ONNX + apply INT8 quantization + run TensorRT inference
- Export ONNX + apply FP8 quantization + run TensorRT inference
- Use a pre-built TensorRT engine (skip export)
- Generating data for CUDA-Q QEC realtime predecoder test application
- Offline decoding from Stim detector samples
- File contract
- Bring your own detector samples
- Generate local reference files
- Decode the files
- Smoke script

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quick start (train + inference)

> From the repo root:

### Technology and requirements: Dependencies

> Target Python versions: **3.11,

### Limitations and security: Color-code limitations in this release

> The narrow conf/config_public.yaml covers

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,474,266 |
| Jupyter Notebook | 1,818,307 |
| Shell | 53,981 |
| Dockerfile | 2,647 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 124
- Forks at capture: 54
- Last updated: 2026-11-22T14:50:22Z
- Last pushed: 2026-11-23T18:14:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/Ising-Decoding)
- [README](https://github.com/NVIDIA/Ising-Decoding/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/Ising-Decoding/issues)
- [Releases](https://github.com/NVIDIA/Ising-Decoding/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
