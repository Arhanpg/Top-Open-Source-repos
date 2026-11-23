# Megatron-LM

- **Company:** nvidia
- **Repository:** https://github.com/NVIDIA/Megatron-LM
- **README:** https://github.com/NVIDIA/Megatron-LM/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** deac1231bd747256eea778b021200265c3a9455e

## What it does

A GPU-optimized library for training transformer models at scale, combining Megatron-LM reference training scripts with the composable Megatron Core library.

## Features documented by the upstream README

- Megatron-LM provides reference examples and preconfigured training scripts for research and experimentation.
- Megatron Core supplies reusable transformer building blocks and GPU-optimized components.
- Supports tensor, pipeline, data, expert and context parallelism (TP, PP, DP, EP, CP).
- README documents mixed precision options including FP16, BF16, FP8 and FP4.
- Megatron Bridge provides bidirectional Hugging Face ↔ Megatron checkpoint conversion and training recipes.

## Technology stack

Python 3.12+; PyTorch 2.6.0+ recommended; NVIDIA GPU-oriented training; Megatron Core; optional NGC containers and uv/PyPI installation.

## Notes and limitations

README distinguishes the reference training repository from the composable Megatron Core library; choose the appropriate component for the use case.

## Evidence

This record summarizes the upstream README linked above. Dependency manifests, source files, CI workflows and release artifacts were not exhaustively examined in this pass. Do not interpret this summary as a full source-code security or architecture audit.
