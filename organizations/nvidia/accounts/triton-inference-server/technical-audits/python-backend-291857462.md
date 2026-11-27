# triton-inference-server/python_backend

- Company: NVIDIA
- Account: triton-inference-server
- Repository: https://github.com/triton-inference-server/python_backend
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:28:42+00:00

## Project purpose

-->

## Why this project is used

Triton backend that enables pre-process, post-processing and other logic to be implemented in Python.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Python, Shell, CMake, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration, Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/correlation_id.cc, src/correlation_id.h, src/gpu_buffers.cc, src/gpu_buffers.h

## Setup and usage

- Quick Start: 1. Run the Triton Inference Server container.
- Quick Start: docker run --shm-size=1g --ulimit memlock=-1 -p 8000:8000 -p 8001:8001 -p 8002:8002 --ulimit stack=67108864 -ti nvcr.io/nvidia/tritonserver: -py3
- Quick Start: Replace \ with the Triton version (e.g. 21.05).
- Quick Start: 2. Inside the container, clone the Python backend repository.
- Quick Start: git clone https://github.com/triton-inference-server/python_backend -b r
- Quick Start: 3. Install example model.
- Quick Start: mkdir -p models/add_sub/1/
- Quick Start: cp examples/add_sub/model.py models/add_sub/1/model.py

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/triton-inference-server/python_backend/blob/main/README.md
- README SHA: c7c20e9b2c64b6177b6f9d73b94aae25e1ae3846
- Manifests: CMakeLists.txt, pyproject.toml, .devcontainer/Dockerfile, src/shm_monitor/CMakeLists.txt
- Sampled source files: src/correlation_id.cc, src/correlation_id.h, src/gpu_buffers.cc, src/gpu_buffers.h
- Git tree state: captured
- Evidence fingerprint: 712fe58061e7f73c7f76a5606f459f313c1eeceb7f48cc1ed6cefa5e83b2e29f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
