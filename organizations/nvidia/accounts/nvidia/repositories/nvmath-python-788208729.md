# NVIDIA/nvmath-python

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nvmath-python](https://github.com/NVIDIA/nvmath-python)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nvmath-python/blob/main/README.md)
- README blob SHA: 542e2adaa34787b22ed200dfc40f475fc77f29fa
- README bytes captured: 9988
- README truncated at capture limit: False
- Repository ID: 788208729
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA Math Libraries for the Python Ecosystem

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:02:36+00:00

### Short excerpt (up to 300 words)

> src="docs/sphinx/_static/nvmath-python-green-r4.svg" alt="A cube with Below are a few

### README headings

- nvmath-python: NVIDIA Math Libraries for the Python Ecosystem
- Some Examples
- Host APIs
- Prepare sample input data. nvmath-python accepts input tensors from pytorch, cupy, and
- numpy.
- Use the stateful Matmul object in order to perform multiple matrix multiplications
- without replanning. The nvmath API allows us to fine-tune our operations by, for
- example, selecting a mixed-precision compute type.
- Plan the matrix multiplication. Planning returns a sequence of algorithms that can be
- configured. We can also select epilog operations which are applied to the result of
- the multiplication without a separate function call.
- Execute the matrix multiplication.
- Remember to free the Matmul object when finished or use it as a context manager
- Synchronize the default stream, since by default the execution is non-blocking for
- GPU operands.
- Create the data for the batched 1-D FFT.
- Compute the normalization factor for unitary transforms
- Define the epilog function for the FFT.
- Compile the epilog to LTO-IR.
- Perform the forward FFT, applying the filter as a epilog...
- Finally, we can test that the fused FFT run result matches the result of separate
- calls
- Distributed Host APIs
- Initialize nvmath.distributed.
- The global 3-D FFT size is (512, 256, 512).
- In this example, the input data is distributed across processes according to
- the cuFFTMp Slab distribution on the X axis.
- cuFFTMp uses the NVSHMEM PGAS model for distributed computation, which requires GPU
- operands to be on the symmetric heap.
- a is a cupy ndarray and can be operated on using in-place cupy operations.

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> src="docs/sphinx/_static/nvmath-python-green-r4.svg" alt="A cube with

### Getting started and usage: Some Examples

> Below are a few

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Cython | 8,734,252 |
| Python | 5,767,016 |
| Jupyter Notebook | 816,024 |
| C++ | 44,139 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: cffi, cuda-bindings, cuda-core, cuda-pathfinder, cuda-toolkit, cutensor-cu12, cutensor-cu13, llvmlite, mkl, nccl4py, numba, numba-cuda, numba-cuda-mlir, numpy, nvidia-cublas-cu12, nvidia-cublasmp-cu12, nvidia-cublasmp-cu13, nvidia-cuda-cccl-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12
- setup.py (capture: captured)
- docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 603
- Forks at capture: 49
- Last updated: 2026-11-19T23:14:54Z
- Last pushed: 2026-07-14T17:52:55Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nvmath-python)
- [README](https://github.com/NVIDIA/nvmath-python/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nvmath-python/issues)
- [Releases](https://github.com/NVIDIA/nvmath-python/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
