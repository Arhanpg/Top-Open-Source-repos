# triton-inference-server/hugectr_backend

- Company: NVIDIA
- Account: triton-inference-server
- Repository: https://github.com/triton-inference-server/hugectr_backend
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:35:57+00:00

## Project purpose

-->

## Why this project is used

-->

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Jupyter Notebook, C++, CMake, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: jupyter, onnx, tensorflow, tf2onnx, torch
- Build/package tools: CMake configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: hps_backend/src/backend.cpp, hps_backend/src/hps.cc, hps_backend/src/model_instance_state.cpp, hps_backend/src/model_state.cpp

## Setup and usage

- Quick Start: You can build the HPS Backend from scratch and install to the specify path based on your own specific requirements using the NGC Merlin inference Docker images.
- Quick Start: We support the following compute capabilities for inference deployment:
- Quick Start: | Compute Capability | GPU | SM |
- Quick Start: |--------------------|----------------------|----|
- Quick Start: | 7.0 | NVIDIA V100 (Volta) | 70 |
- Quick Start: | 7.5 | NVIDIA T4 (Turing) | 75 |
- Quick Start: | 8.0 | NVIDIA A100 (Ampere) | 80 |
- Quick Start: | 8.6 | NVIDIA A10 (Ampere) | 72 |

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/triton-inference-server/hugectr_backend/blob/main/README.md
- README SHA: b0bf8a464e68908c884d313d9f7af9fbc52f4b51
- Manifests: hps_backend/CMakeLists.txt, hps_backend/samples/hps-triton-ensemble/requirements.txt
- Sampled source files: hps_backend/src/backend.cpp, hps_backend/src/hps.cc, hps_backend/src/model_instance_state.cpp, hps_backend/src/model_state.cpp
- Git tree state: captured
- Evidence fingerprint: c11b9ef88ebbb0a7b9eabf62cab1d2b6611da2313daf75b9b7ecd9e3333587b7

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
