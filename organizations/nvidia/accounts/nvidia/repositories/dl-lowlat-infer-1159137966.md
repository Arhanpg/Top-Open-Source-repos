# NVIDIA/dl-lowlat-infer

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/dl-lowlat-infer](https://github.com/NVIDIA/dl-lowlat-infer)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/dl-lowlat-infer/blob/main/README.md)
- README blob SHA: b7ffc3703fe79e22bd07b698d828e5ab1eb6f03a
- README bytes captured: 23016
- README truncated at capture limit: False
- Repository ID: 1159137966
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Low Latency inference for sliding window LSTMs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T01:15:06+00:00

### Short excerpt (up to 300 words)

> You may also specify

### README headings

- Low Latency inference for sliding window LSTMs
- Obtaining the Source Code
- Building with CMake
- Build Options
- Testing with CMake
- Installation
- Source Code Structure
- Structure within the Implementation
- Performance Tuning
- This benchmark is sensitive to CPU clock
- Set max clocks on GH200
- Isolate core IDs through grub
- E.g. to isolate 2 cores from the system
- Edit /etc/default/grub with
- Where 54-55 are multithreaded cores, if multithreading is enabled
- Then point the benchmark to those cores ids
- Run with numactl on multiple socket system
- Numa topology:
- Sample usage
- development in container exports
- Generate ONNX models for all three sizes (Optional)
- Convert lstm_s ONNX model to NumPy arrays (Optional). The weights will be dumped into
- $NVLSTM_DATA_DIR/models/lstm_s directory
- Generate lstm_s model weights
- Generate lstm_m model weights
- Generate lstm_l model weights
- Generate input distribution
- Generate the reference using cuBLAS based SingleStep implementation for a single model instance for 30 seconds:
- required parameters:                                    <model> <model_dir> <data_file> <nr_of_sec_to_run>
- Run the inference

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> You may also specify

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Cuda | 632,402 |
| C++ | 162,975 |
| Python | 29,505 |
| CMake | 17,280 |
| Shell | 5,582 |
| Makefile | 4,707 |
| Dockerfile | 4,330 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- pyproject.toml (capture: captured)
- docker/Dockerfile (capture: captured)
- docker/Makefile (capture: captured)
- src/python/CMakeLists.txt (capture: captured)
- src/python/requirements.txt (capture: captured) — dependency clues: numpy

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 18
- Forks at capture: 7
- Last updated: 2026-11-01T21:44:38Z
- Last pushed: 2026-11-16T10:05:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/dl-lowlat-infer)
- [README](https://github.com/NVIDIA/dl-lowlat-infer/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/dl-lowlat-infer/issues)
- [Releases](https://github.com/NVIDIA/dl-lowlat-infer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
