# Megatron-LM and Megatron Core

<sub>Company: NVIDIA · Repository: [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

Megatron-LM and Megatron Core form a GPU-optimized software stack for training transformer models at scale. The README distinguishes two components: Megatron-LM as a reference repository with training examples and preconfigured scripts, and Megatron Core as a composable library of optimized building blocks for custom training frameworks.

**Problem it addresses:** training large transformer models across multiple GPUs and nodes requires coordinated partitioning of computation, data and model state. Megatron provides reusable implementations of parallelism strategies and transformer building blocks for these workloads.

## Two related components

### Megatron-LM: reference workflows

The README describes Megatron-LM as a reference example that includes Megatron Core plus preconfigured training scripts. It is presented as useful for research teams, learning distributed training and performing quick experiments.

### Megatron Core: composable training library

Megatron Core provides GPU-optimized building blocks that framework developers and ML engineers can assemble into custom training pipelines. The README identifies it as the reusable foundation for more specialized training systems.

## Parallelism strategies

The README explicitly lists the following parallelism dimensions:

- **Tensor Parallelism (TP):** partitions tensor operations.
- **Pipeline Parallelism (PP):** distributes model stages through a pipeline.
- **Data Parallelism (DP):** distributes training data and corresponding computation.
- **Expert Parallelism (EP):** supports models with expert-based architectures.
- **Context Parallelism (CP):** partitions context-related work.

These labels are the strategy families advertised by the project. Their correct combinations depend on model architecture, hardware topology, memory constraints and workload characteristics; use the official parallelism guide for configuration details.

## Precision and model support

The README identifies mixed-precision support for FP16, BF16, FP8 and FP4. It also describes transformer building blocks and model architectures intended for high-performance training.

The repository links Megatron Bridge for bidirectional Hugging Face-to-Megatron checkpoint conversion and production-oriented recipes. The README notes that this project is planned to be merged into the Megatron-LM repository; check the latest migration and release notes when working with the Bridge component.

## Technology profile

| Area | README-supported details |
|---|---|
| Primary ecosystem | Python |
| Recommended baseline | Python 3.12+ and PyTorch 2.6.0+ |
| Core library | Megatron Core |
| Training target | NVIDIA GPU systems |
| Parallelism | TP, PP, DP, EP and CP |
| Precision modes | FP16, BF16, FP8 and FP4 |
| Installation | PyPI package `megatron-core` or source installation |
| Container guidance | NVIDIA GPU Cloud (NGC) setup documentation |

## Getting started

The README provides installation through the `uv` package manager:

```bash
uv pip install megatron-core
```

It also documents installation from source:

```bash
git clone https://github.com/NVIDIA/Megatron-LM.git
cd Megatron-LM
uv pip install -e .
```

The maintainers warn that source builds can use substantial memory. They show `MAX_JOBS` as a way to limit parallel compilation jobs when the build runs out of memory.

For a first training run, the README links a full quickstart that includes data preparation. The NGC installation guide documents container setup and additional installation paths.

## Where it is useful

- Pretraining transformer models across multiple GPUs.
- Studying and benchmarking distributed training strategies.
- Building custom training frameworks using reusable transformer components.
- Experimenting with mixed precision and parallelism configurations.
- Converting checkpoints between Hugging Face and Megatron formats through the related Bridge tooling.

## Operational considerations

This is a systems-heavy project. Successful use depends on matching Python, PyTorch, CUDA, container and GPU environments. Distributed runs also need careful planning for memory, communication topology, checkpointing and reproducibility. Treat the README's recommended software versions as a starting compatibility baseline and verify the current installation guide before a large training run.

## Upstream references

- [Repository](https://github.com/NVIDIA/Megatron-LM)
- [Primary README](https://github.com/NVIDIA/Megatron-LM/blob/main/README.md)
- [Megatron Core documentation](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
- [First training run](https://docs.nvidia.com/megatron-core/developer-guide/latest/get-started/quickstart.html)
- [Parallelism guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html)
- [Megatron Bridge](https://github.com/NVIDIA-NeMo/Megatron-Bridge)

**Evidence note:** README blob inspected: `deac1231bd747256eea778b021200265c3a9455e`.
