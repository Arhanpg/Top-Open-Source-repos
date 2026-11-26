# triton-inference-server/fil_backend

- Company: NVIDIA
- Account: triton-inference-server
- Repository: https://github.com/triton-inference-server/fil_backend
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:16:55+00:00

## Project purpose

-->

## Why this project is used

FIL backend for the Triton Inference Server

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Jupyter Notebook, Python, C, Shell, CMake, Dockerfile, Cuda
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration, Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/api.cc, src/cpu_forest_model.h, src/cpu_treeshap_model.h, src/detail/omp_helpers.h

## Setup and usage

- Usage Information: - [Introductory end-to-end
- Usage Information: example](https://nbviewer.org/github/triton-inference-server/fil_backend/blob/main/notebooks/categorical-fraud-detection/Fraud_Detection_Example.ipynb)
- Usage Information: notebook](https://nbviewer.org/github/triton-inference-server/fil_backend/blob/main/notebooks/faq/FAQs.ipynb) with code snippets for many common scenarios
- Usage Information: - Model Configuration
- Usage Information: - Explainability and Shapley value support
- Usage Information: - Scikit-Learn and cuML model support
- Usage Information: - Model support and limitations
- Quickstart: Deploying a tree model in 3 steps: 1. Copy your model into the following directory structure. In this

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/triton-inference-server/fil_backend/blob/main/README.md
- README SHA: 08f692616bdfaa1cd8d7ffb20ab7fa8b7e8838f5
- Manifests: CMakeLists.txt, pyproject.toml, ops/Dockerfile, rapids_triton_python/pyproject.toml, test/CMakeLists.txt
- Sampled source files: src/api.cc, src/cpu_forest_model.h, src/cpu_treeshap_model.h, src/detail/omp_helpers.h
- Git tree state: captured
- Evidence fingerprint: 1d42ddbd88790edf949800b35f251eddbed2a4d88d085a524d0a57ec68969a16

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
