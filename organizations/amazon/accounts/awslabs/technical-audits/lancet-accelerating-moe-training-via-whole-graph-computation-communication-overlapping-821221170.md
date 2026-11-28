# awslabs/Lancet-Accelerating-MoE-Training-via-Whole-Graph-Computation-Communication-Overlapping

- Company: Amazon
- Account: awslabs
- Repository: https://github.com/awslabs/Lancet-Accelerating-MoE-Training-via-Whole-Graph-Computation-Communication-Overlapping
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:57:36+00:00

## Project purpose

Official implementation for the paper Lancet: Accelerating Mixture-of-Experts Training via Whole Graph Computation-Communication Overlapping, published in MLSys'24.

## Why this project is used

Official implementation for the paper Lancet: Accelerating Mixture-of-Experts Training via Whole Graph Computation-Communication Overlapping, published in MLSys'24.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Python, Cuda, CMake, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: antlr4-python3-runtime, argparse, attrs, awscli, boto3, cloudpickle, cython, decorator, future, gitpython, numpy, orderedset, packaging, psutil, requests, rpyc, ruamel.yaml, scipy, setuptools, tornado, tqdm, typed_ast, xgboost
- Build/package tools: CMake configuration, Docker build configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: models/benchmark/__main__.py, src/analysis/dependency_graph.cc, src/analysis/dependency_graph.h, src/common/cuda_utils.h

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: **Note**: The evaluation Dockerfile automatically establishes password-less SSH connection between the containers to facilitate MPI usage. Please make sure that the code is only run in a secure environment.
- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/awslabs/Lancet-Accelerating-MoE-Training-via-Whole-Graph-Computation-Communication-Overlapping/blob/main/README.md
- README SHA: c496b7c4316cba8b258fcb52ff4ea3e7461bc2eb
- Manifests: CMakeLists.txt, docker/Dockerfile, python/setup.py, apps/include_raf/CMakeLists.txt, docker/resources/requirements.txt, tests/cpp/CMakeLists.txt
- Sampled source files: models/benchmark/__main__.py, src/analysis/dependency_graph.cc, src/analysis/dependency_graph.h, src/common/cuda_utils.h
- Git tree state: captured
- Evidence fingerprint: 8e7f1758392d7eeb1510fe6f4a94754cfaf44e51a7886de6d491ee2885ae06ba

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
