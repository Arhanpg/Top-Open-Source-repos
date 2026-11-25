# triton-inference-server/TensorRT-LLM

- Company: NVIDIA
- Account: triton-inference-server
- Repository: https://github.com/triton-inference-server/TensorRT-LLM
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:50:37+00:00

## Project purpose

TensorRT LLM ===========================

## Why this project is used

TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, C++, Cuda, Groovy, Shell, CMake, Jinja, C, Makefile, JavaScript, Standard ML
- Frameworks/libraries: Unknown / not established
- Dependency names: PyNvVideoCodec, StrEnum, accelerate, aenum, anyio, apache-tvm-ffi, backoff, blake3, blobfile, build, cache-dit, claude-agent-sdk, click, click_option_group, colored, cuda-core, cuda-python, cuda-tile, datasets, diffusers, einops, etcd-sdk-python, evaluate, fastapi, filelock, fla-core, flash-attn-4, flashinfer-python, ftfy, graphviz, grpcio, grpcio-health-checking, h5py, jinja2, jsonschema, lark, lazy_loader, librosa, llguidance, llist, matplotlib, mcp, meson, mistral-common, mooncake-transfer-engine-cuda13, mpi4py, mpmath, msgpack, msgspec, nccl4py, ninja, numexpr, numpy, nvidia-cuda-nvrtc, nvidia-cuda-tileiras, nvidia-cudnn-frontend, nvidia-cutlass-dsl, nvidia-matmul-heuristics, nvidia-ml-py, nvidia-nccl-cu13, nvtx, omegaconf, openai, openai-codex, openai-harmony, optimum, ordered-set, packaging, pandas, partial_json_parser, patchelf, peft, pillow, plotly, polygraphy, prometheus_client, prometheus_fastapi_instrumentator, protobuf, psutil, pulp, pydantic, pydantic-settings, python-multipart, pyyaml, pyzmq, quack-kernels, rich, safetensors, sentencepiece, setuptools, soundfile, starlette, tiktoken, torch, torch-c-dlpack-ext, torchao, torchvision, transformers, triton, uvicorn, uvloop, xgrammar
- Build/package tools: CMake configuration, Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: scripts/attribution/sbom/src/trtllm_sbom/cli.py, agent-flow/agent_flow/workflows/agent_team/cli.py, agent-flow/agent_flow/workflows/modeling_bringup/cli.py, agent-flow/agent_flow/workflows/perf_analyze/cli.py

## Setup and usage

- Getting Started: To get started with TensorRT-LLM, visit our documentation:
- Getting Started: - Supported Hardware, Models, and other Software
- Getting Started: - Benchmarking Performance

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/triton-inference-server/TensorRT-LLM/blob/main/README.md
- README SHA: 4414e19fc01a00d74a245d8948aec6db7d279778
- Manifests: pyproject.toml, requirements.txt, setup.py, 3rdparty/CMakeLists.txt, agent-flow/pyproject.toml, cpp/CMakeLists.txt
- Sampled source files: scripts/attribution/sbom/src/trtllm_sbom/cli.py, agent-flow/agent_flow/workflows/agent_team/cli.py, agent-flow/agent_flow/workflows/modeling_bringup/cli.py, agent-flow/agent_flow/workflows/perf_analyze/cli.py
- Git tree state: captured
- Evidence fingerprint: a12bbfca7ead3af3e9d2f7060e8db64564f188716c2a0e980a567079751e21dd

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
