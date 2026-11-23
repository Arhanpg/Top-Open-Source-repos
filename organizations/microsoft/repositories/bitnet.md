# BitNet

- **Company:** Microsoft
- **Repository:** https://github.com/microsoft/BitNet
- **README:** https://github.com/microsoft/BitNet/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** Not recorded

## What it does

The official inference framework for 1-bit large language models such as BitNet b1.58.

## Features documented by the upstream README

- Optimized kernels for CPU and GPU inference.
- README describes ternary / 1.58-bit model inference and an official 2.4B-parameter model release.
- Supports chat-style inference and published build/run instructions for CPU and GPU.
- README reports inference speed and energy reductions relative to full-precision baselines; those figures are project-reported benchmarks.

## Technology stack

BitNet b1.58 model inference; CPU/GPU optimized kernels; I2_S quantization support in model/embedding announcements. Source-language inventory requires source/manifest inspection.

## Notes and limitations

Benchmark values are claims reported by the project README and are not independently reproduced in this catalogue.

## Evidence

This summary is based on the upstream README linked above. Repository manifests, source code, CI workflows and release artifacts were not exhaustively audited in this pass; therefore the technology stack is limited to what the README explicitly supports.
