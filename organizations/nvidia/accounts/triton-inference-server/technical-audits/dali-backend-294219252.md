# triton-inference-server/dali_backend

- Company: NVIDIA
- Account: triton-inference-server
- Repository: https://github.com/triton-inference-server/dali_backend
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:04:58+00:00

## Project purpose

This repository contains code for DALI Backend for Triton Inference Server.

## Why this project is used

The Triton backend that allows running GPU-accelerated data pre-processing pipelines implemented in DALI's python API.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Python, Shell, CMake, C
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/config_tools/config_tools.cc, src/config_tools/config_tools.h, src/config_tools/config_tools.test.cc, src/dali_backend.cc

## Setup and usage

No setup information established.

## Limitations and caveats

- Known limitations:: 1. DALI's ImageDecoder accepts data only from the CPU - keep this in mind when putting together your DALI pipeline.
- Known limitations:: 1. Triton accepts only homogeneous batch shape. Feel free to pad your batch of encoded images with zeros
- Known limitations:: 1. Due to DALI limitations, you might observe unnaturally increased memory consumption when
- Known limitations:: defining instance group for DALI model with higher count than 1. We suggest using default instance
- Known limitations:: group for DALI model.

## Evidence and provenance

- README: https://github.com/triton-inference-server/dali_backend/blob/main/README.md
- README SHA: d5d0248243b9a71dc419d208bdd4bd2b0e73c254
- Manifests: CMakeLists.txt, pyproject.toml, src/CMakeLists.txt, src/dali_executor/CMakeLists.txt
- Sampled source files: src/config_tools/config_tools.cc, src/config_tools/config_tools.h, src/config_tools/config_tools.test.cc, src/dali_backend.cc
- Git tree state: captured
- Evidence fingerprint: ed909743a0467813b39fcb497d1c3f3b933fe4ecae5130334d5601ffcce276ce

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
