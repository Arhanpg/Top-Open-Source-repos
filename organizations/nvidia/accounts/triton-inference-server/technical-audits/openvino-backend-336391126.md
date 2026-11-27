# triton-inference-server/openvino_backend

- Company: NVIDIA
- Account: triton-inference-server
- Repository: https://github.com/triton-inference-server/openvino_backend
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:16:08+00:00

## Project purpose

-->

## Why this project is used

OpenVINO backend for Triton.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Python, CMake
- Frameworks/libraries: Unknown / not established
- Dependency names: pytest, requests, tritonclient
- Build/package tools: CMake configuration, Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/openvino.cc, src/openvino_utils.cc, src/openvino_utils.h, tools/gen_openvino_dockerfile.py

## Setup and usage

No setup information established.

## Limitations and caveats

- Known Issues: * Models with the scalar on the input (shape without any dimension are not supported)
- Known Issues: * Reshaping using dimension ranges is not supported.
- Known Issues: * Models without output names are not supported. Models must be saved with names assigned.

## Evidence and provenance

- README: https://github.com/triton-inference-server/openvino_backend/blob/main/README.md
- README SHA: 98211ee86805189528fc20f32259f41b62b822b9
- Manifests: CMakeLists.txt, pyproject.toml, tests/requirements.txt
- Sampled source files: src/openvino.cc, src/openvino_utils.cc, src/openvino_utils.h, tools/gen_openvino_dockerfile.py
- Git tree state: captured
- Evidence fingerprint: a6c36a6d118766b45d43118a4764435bb2a874048a7de59f781a41314ae300af

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
