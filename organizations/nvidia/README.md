# NVIDIA — open-source organization profile

- **GitHub account:** [NVIDIA](https://github.com/NVIDIA)
- **Company mapping:** candidate account; project-specific NVIDIA organizations and related research groups may exist.
- **Source group:** United States & Global
- **Directory status:** initialized; public repository inventory not exhaustive
- **Detailed README records:** 7

## Reviewed projects

| Project | Focus | What the README documents |
|---|---|---|
| [Megatron-LM](repositories/megatron-lm.md) | Model training | GPU-optimized transformer training, parallelism strategies and composable Megatron Core components |
| [TensorRT-LLM](repositories/tensorrt-llm.md) | Model inference | Specialized kernels, an efficient runtime and a Python-facing framework for LLM and visual-generation inference |

## Engineering themes

The selected projects cover two major stages of a model lifecycle:

1. **Training:** Megatron-LM and Megatron Core provide components for distributed transformer training and precision / parallelism configurations.
2. **Inference:** TensorRT-LLM focuses on optimized execution and runtime performance for supported generative models.

They are complementary examples, not interchangeable frameworks. Training and inference have different hardware, performance and operational requirements.

## Technology snapshot

The inspected READMEs identify Python, PyTorch and NVIDIA GPU systems across these projects. Megatron-LM documents TP, PP, DP, EP and CP parallelism and FP16/BF16/FP8/FP4 precision. TensorRT-LLM's inspected README badges list Python, CUDA and PyTorch version information; confirm release-specific compatibility before installation.

## Inventory status and cautions

The two repository pages are README-based summaries, not benchmark reproductions or a complete source-code audit. Reported performance claims remain attributed to upstream documentation. The full public repository inventory for NVIDIA has not yet been retrieved.

## Upstream

- [NVIDIA GitHub account](https://github.com/NVIDIA)
- [NVIDIA developer resources](https://developer.nvidia.com/)
- [NVIDIA repository index in this catalogue](repositories/README.md)


## Additional README-reviewed projects — 23 November 2026

Five additional NVIDIA project briefs have been added: Linux Open GPU Kernel Modules, nvidia-docker, DeepLearningExamples, Cosmos and TensorRT OSS. The records preserve important lifecycle and compatibility findings, including the archived/deprecated state of nvidia-docker and TensorRT 11 migration notes. See the [repository index](repositories/README.md).
