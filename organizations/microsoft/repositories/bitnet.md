# bitnet.cpp

<sub>Company: Microsoft · Repository: [microsoft/BitNet](https://github.com/microsoft/BitNet) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

The project branded **bitnet.cpp** is described as an official inference framework for 1-bit large language models, including BitNet b1.58. It provides optimized inference kernels intended to run these models efficiently on CPUs and GPUs.

**Problem it addresses:** ordinary full-precision LLM inference can be demanding in memory, compute and energy. BitNet explores ternary / very-low-bit model weights and optimized kernels to make inference more practical on local compute, including CPU-only environments.

## What is included

The README presents several connected components:

- An inference framework for BitNet-family 1-bit / 1.58-bit LLMs.
- CPU inference paths with architecture-specific kernel variants.
- An official GPU inference kernel.
- Conversion and inference guidance for I2_S-quantized models and embeddings.
- Model releases and links to Hugging Face weights, demos and technical reports.

The project should be treated as an inference/runtime repository. Model weights are linked as separate Hugging Face artifacts.

## Model family described by the README

| Model | Approximate parameters | Purpose described |
|---|---:|---|
| BitNet-b1.58-2B-4T | 2.4B | Conversational / general LLM inference |
| BitNet-embedding-0.6B | 0.6B | Text embedding |
| BitNet-embedding-270M | 270M | Smaller embedding model for more constrained environments |

The README also lists community models and a compatibility table showing supported CPU architectures and kernel variants. Support differs by model and architecture, so consult that table before selecting a weight file.

## CPU and GPU execution

The README describes optimized CPU inference on x86 and ARM systems and provides an official GPU kernel. It names kernel variants such as I2_S, TL1 and TL2, with compatibility depending on the specific model and CPU architecture.

The project README reports speedups and energy reductions relative to full-precision baselines. These are project-reported benchmark results, not independently reproduced measurements in this catalogue. Real performance depends on the exact model, instruction set, CPU/GPU, thread count, build configuration and workload.

## Technology profile

| Area | README-supported details |
|---|---|
| Project / runtime | `bitnet.cpp` inference framework |
| Model format / method | BitNet b1.58 / ternary-weight LLMs |
| Execution targets | CPU and GPU |
| CPU architectures mentioned | x86 and ARM |
| Kernel families | I2_S, TL1 and TL2 |
| Model distribution | Hugging Face |
| Documentation | Build-from-source guide, CPU/GPU guides and embedding conversion guide |
| License badge | MIT |

The README's project naming and build material indicate a C/C++-oriented inference runtime, but a complete language and compiler matrix has not been extracted here. Confirm compiler versions and platform support from the build documentation.

## Evaluation considerations

- Confirm that the desired model is listed as supported for the target architecture and kernel.
- Benchmark the exact CPU/GPU and thread configuration that will be used in deployment.
- Compare output quality and task performance as well as latency and memory.
- Inspect model licences and usage terms on the corresponding model pages.
- Treat README benchmark numbers as claims to reproduce, not guarantees for another device.

## Upstream references

- [Repository](https://github.com/microsoft/BitNet)
- [Primary README](https://github.com/microsoft/BitNet/blob/main/README.md)
- [CPU source / inference guide](https://github.com/microsoft/BitNet/blob/main/src/README.md)
- [GPU kernel guide](https://github.com/microsoft/BitNet/blob/main/gpu/README.md)
- [Embedding conversion guide](https://github.com/microsoft/BitNet/blob/main/docs/bitnet-embeddings-i2s-guide.md)
- [BitNet b1.58 2B model](https://huggingface.co/microsoft/BitNet-b1.58-2B-4T)
- [Technical report](https://arxiv.org/abs/2502.11880)

**Evidence note:** README blob inspected: `952ba3efbcd8f46be258f1b6229c6a1ea55f25d0`.
