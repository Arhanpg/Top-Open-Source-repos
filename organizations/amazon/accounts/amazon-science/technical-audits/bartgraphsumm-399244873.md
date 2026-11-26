# amazon-science/BartGraphSumm

- Company: Amazon
- Account: amazon-science
- Repository: https://github.com/amazon-science/BartGraphSumm
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:31:09+00:00

## Project purpose

This is the implementation of the paper Efficiently Summarizing Text and Graph Encodings of Multi-Document Clusters.

## Why this project is used

Implementation of the paper "Efficiently Summarizing Text and Graph Encodings of Multi-Document Clusters (NAACL 2021)"

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Shell, Cuda, C++, Makefile, Cython, Lua, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: sphinx, sphinx-argparse
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/bart_decode_parallel.py, src/convert_model_to_long.py, src/fairseq/eval_lm.py, src/fairseq/fairseq/__init__.py

## Setup and usage

- Pre-installations: 1. This code is tested using Python 3.6, Pytorch 1.4, and CUDA 10.1
- Pre-installations: - cd ~; git clone https://github.com/NVIDIA/apex
- Pre-installations: - pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" --global-option="--deprecated_fused_adam" ./
- Pre-installations: - cd ~; git clone https://github.com/NVIDIA/nccl.git
- Pre-installations: - make -j10 src.build CUDA_HOME=/usr/local/cuda-10.1
- Pre-installations: - sudo apt install build-essential devscripts debhelper fakeroot
- Pre-installations: - make -j10 pkg.debian.build CUDA_HOME=/usr/local/cuda-10.1
- Pre-installations: - sudo apt install ./build/pkg/deb/*.deb

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/amazon-science/BartGraphSumm/blob/main/README.md
- README SHA: c3bbb29db2ae49b7a6d8cc0626611bd3cdb55020
- Manifests: src/fairseq/pyproject.toml, src/fairseq/setup.py, src/fairseq/docs/Makefile, src/fairseq/docs/requirements.txt, src/fairseq/fairseq/modules/dynamicconv_layer/setup.py, src/fairseq/fairseq/modules/lightconv_layer/setup.py
- Sampled source files: src/bart_decode_parallel.py, src/convert_model_to_long.py, src/fairseq/eval_lm.py, src/fairseq/fairseq/__init__.py
- Git tree state: captured
- Evidence fingerprint: 53faf0a503352bcba2c6ed8cc7cfb0aef00a26eb63a0a13d3e3108de58d95c8d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
