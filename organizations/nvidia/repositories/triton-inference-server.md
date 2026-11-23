# NVIDIA Triton Inference Server

- **Company:** NVIDIA
- **GitHub account:** [triton-inference-server](https://github.com/triton-inference-server)
- **Repository:** [triton-inference-server/server](https://github.com/triton-inference-server/server)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/triton-inference-server/server/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `f6f159df03d13ff7234f42e2444ff5a93abbec1d`

## Project overview

Open-source inference-serving software for deploying models from multiple deep-learning and machine-learning frameworks across cloud, datacenter, edge and embedded environments.

## Features and capabilities documented by the README

- Supports models from TensorRT, PyTorch, ONNX, OpenVINO, Python, RAPIDS FIL and additional framework backends.
- Supports NVIDIA GPUs, x86 and ARM CPUs, and AWS Inferentia according to the README.
- Supports real-time, batched, ensemble and audio/video streaming inference workloads.
- Provides concurrent model execution, dynamic batching, sequence batching and implicit state management for stateful models.
- Exposes a backend API for custom backends and pre/post-processing operations, including Python-based backends.
- Supports model pipelines through ensembles and Business Logic Scripting.
- Provides HTTP/REST and gRPC inference protocols based on the KServe v2 protocol, plus C and Java in-process APIs.
- Publishes metrics such as GPU utilization, server throughput and latency.

## Technology stack

Inference server with backends for TensorRT, PyTorch, ONNX, OpenVINO, Python and RAPIDS FIL; HTTP/REST, gRPC, C and Java APIs; Docker/NGC deployment; Kubernetes and Helm deployment examples. The README recommends Docker images for building and using Triton. The README shows a BSD 3-Clause licence badge.

## Getting started

The README's quickstart clones the server repository at a release branch, fetches example models and starts the Triton server from an NVIDIA NGC container with a model repository mounted into it. It also links a CPU-only quickstart, custom build/deployment guides and Kubernetes/Helm deployment examples.

## Lifecycle, compatibility and operational considerations

The inspected README says the `main` branch tracks under-development progress toward the next release; it identifies release 2.75.0 as corresponding to the 26.11 container release. Check release-specific container tags, driver/runtime compatibility and backend support before deployment. It links NVIDIA AI Enterprise as an enterprise support option.

## Evaluation guidance

Review the release-specific installation documentation, exact software/hardware requirements, dependency manifests, licence terms and security guidance before using the project in production. Benchmark claims should be tested on the actual target hardware and workload. This dossier is based on the upstream README; it is not a full source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/triton-inference-server/server)
- [README](https://github.com/triton-inference-server/server/blob/main/README.md)
- [Issues](https://github.com/triton-inference-server/server/issues)
- [Releases](https://github.com/triton-inference-server/server/releases)

*Evidence note: the README blob SHA identifies the upstream version inspected. Details not supported by the README are left unspecified or directed to version-specific documentation.*
