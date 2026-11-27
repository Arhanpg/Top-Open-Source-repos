# triton-inference-server/perf_analyzer

- Company: NVIDIA
- Account: triton-inference-server
- Repository: https://github.com/triton-inference-server/perf_analyzer
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:22:10+00:00

## Project purpose

Copyright (c) 2020-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

## Why this project is used

Copyright (c) 2020-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

## Core features

- Sequence Models,: Sequence Models,
  - Evidence: README.md#Other Features
- Input Data to model inferences can be auto-generated or: Input Data to model inferences can be auto-generated or
  - Evidence: README.md#Other Features
- TorchServe can be used as the: TorchServe can be used as the
  - Evidence: README.md#Other Features

## Technology stack

- Languages: Python, C++, CMake
- Frameworks/libraries: Unknown / not established
- Dependency names: fastparquet, jinja2, kaleido, numpy, optuna, orjson, pandas, perf-analyzer, pillow, plotly, pyarrow, pytest, pytest-mock, pyyaml, responses, rich, soundfile, statsmodels, transformers
- Build/package tools: CMake configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/perf_analyzer/cli.py, genai-perf/genai_perf/main.py, src/base_queue_ctx_id_tracker.h, src/client_backend/client_backend.cc

## Setup and usage

- Quick Start: The steps below will guide you on how to start using Perf Analyzer.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/triton-inference-server/perf_analyzer/blob/main/README.md
- README SHA: 9751dd0b4894f8fe9ef692ccf10898616c446679
- Manifests: CMakeLists.txt, pyproject.toml, genai-perf/pyproject.toml, src/CMakeLists.txt, src/client_backend/CMakeLists.txt, src/client_backend/dynamic_grpc/CMakeLists.txt
- Sampled source files: src/perf_analyzer/cli.py, genai-perf/genai_perf/main.py, src/base_queue_ctx_id_tracker.h, src/client_backend/client_backend.cc
- Git tree state: captured
- Evidence fingerprint: 14dcf9aaeb0edce703e6367defdfb284a84398fe4e87a1463739886e423105ca

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
