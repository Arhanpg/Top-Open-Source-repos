# NVIDIA Dynamo

- **Company:** NVIDIA
- **GitHub account:** [ai-dynamo](https://github.com/ai-dynamo)
- **Repository:** [ai-dynamo/dynamo](https://github.com/ai-dynamo/dynamo)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/ai-dynamo/dynamo/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `45bdcc01f334ef168f3aeaf79dbf029480b682f1`

## Project overview

An open-source datacenter-scale inference orchestration stack. The README describes Dynamo as a coordination layer above inference engines that turns multiple GPUs/nodes into a distributed inference system rather than replacing engines such as SGLang, TensorRT-LLM or vLLM.

## Features and capabilities documented by the README

- Disaggregates prefill and decode into independently scalable GPU pools.
- Uses KV-aware routing based on worker load and KV-cache overlap to avoid redundant prefill computation.
- ModelExpress streams model weights GPU-to-GPU using NIXL/NVLink to accelerate cold starts.
- Planner provides an SLA-driven autoscaler that profiles workloads and right-sizes serving pools.
- Grove provides a Kubernetes operator for topology-aware gang scheduling.
- AISimulate predicts serving behavior and searches deployment configurations offline.
- Fault-tolerance capabilities include health checks and in-flight request migration.
- The README describes multimodal, tool-calling, agentic inference and OpenAI-compatible request paths across multiple backends.

## Technology stack

Rust for performance and Python for extensibility; Kubernetes; Docker/NGC runtime containers; NIXL/NVLink; SGLang, TensorRT-LLM and vLLM backends; PyPI package distribution; Apache 2.0 licence.

## Getting started

The README provides container-based quickstarts for vLLM and SGLang, a PyPI installation option and a Kubernetes deployment path. It recommends using Dynamo when serving across multiple GPUs/nodes or when disaggregated serving, KV-aware routing, SLA-driven autoscaling or fault tolerance are required.

## Lifecycle, compatibility and operational considerations

The README reports project-specific performance claims such as 7x throughput per GPU, 7x faster startup and 2x faster time-to-first-token in linked benchmark contexts. Treat these as upstream-reported, workload/hardware-specific results, not universal guarantees. The README notes that a single model on a single GPU may not need Dynamo.

## Evaluation guidance

Review the release-specific installation documentation, exact software/hardware requirements, dependency manifests, licence terms and security guidance before using the project in production. Benchmark claims should be tested on the actual target hardware and workload. This dossier is based on the upstream README; it is not a full source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/ai-dynamo/dynamo)
- [README](https://github.com/ai-dynamo/dynamo/blob/main/README.md)
- [Issues](https://github.com/ai-dynamo/dynamo/issues)
- [Releases](https://github.com/ai-dynamo/dynamo/releases)

*Evidence note: the README blob SHA identifies the upstream version inspected. Details not supported by the README are left unspecified or directed to version-specific documentation.*
