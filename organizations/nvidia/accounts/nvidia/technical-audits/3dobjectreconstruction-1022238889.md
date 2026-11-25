# NVIDIA/3DObjectReconstruction

- Company: NVIDIA
- Account: NVIDIA
- Repository: https://github.com/NVIDIA/3DObjectReconstruction
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:41:27+00:00

## Project purpose

1. We use Theseus optimizers for pose optimization to replace BundleFusion. 2. Add optional config for color fusion across views to handle varying lighting conditions. (See Configuration for usage) 3. We now use commercial version FoundationStereo ONNX weight from NVIDIA TAO Toolkit. Now could be enabled through FoundationStereo configuration. 4. Add multi-architecture Docker support with automatic detection: deployment now automatically detects x86_64 vs ARM64 (tested on Jetson Orin) and uses the appropriate Dockerfile (Dockerfile or Dockerfile.aarch64) and upgrade to pytorch 2.7.0 for better compatiblity especially for newer architechures. 5. Add USD Exporting, Now we will export USD and USDZ of the reconstructed object for further usage.

## Why this project is used

3D Object Reconstruction project is a workflow that takes a set of stereo images and camera info and outputs a textured mesh (i.e., .OBJ file). The purpose is to translate physical items into the digital world in a photorealistic way

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Jupyter Notebook, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Pillow, imageio, iopath, ipympl, joblib, libigl, numpy, omegaconf, onnxruntime-gpu, open3d, opencv-python, plyfile, pycuda, pyrender, pytest, pytest-html, pytest-timeout, python-multipart, pyyaml, ruamel.yaml, scikit-image, scikit-learn, scipy, torch, torchvision, tqdm, transformations, trimesh, typing-extensions, xatlas, xformers
- Build/package tools: Docker build configuration, Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/nvidia/objectreconstruction/cli/main.py, src/nvidia/__init__.py, src/nvidia/objectreconstruction/__init__.py, src/nvidia/objectreconstruction/cli/__init__.py

## Setup and usage

- Quick Start (Recommended): Get up and running in under 30 minutes with our Docker Compose deployment:
- Inside the container or after installation: nvidia-3d-reconstruct --help
- Basic usage: nvidia-3d-reconstruct \
- Basic usage: --config /path/to/config.yaml \
- Basic usage: --data-path /path/to/stereo/data \
- Basic usage: --output-path /path/to/output
- Reduce memory usage in config.yaml: batch_size: 16 # Reduce from default 32
- Reduce memory usage in foundation stereo: scale: 0.2 # Reduce from default 0.3

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/NVIDIA/3DObjectReconstruction/blob/main/README.md
- README SHA: 59c66fb870073f530ea14bfb4c2eb49679fa8956
- Manifests: docker/Dockerfile, src/pyproject.toml, src/requirements.txt
- Sampled source files: src/nvidia/objectreconstruction/cli/main.py, src/nvidia/__init__.py, src/nvidia/objectreconstruction/__init__.py, src/nvidia/objectreconstruction/cli/__init__.py
- Git tree state: captured
- Evidence fingerprint: fdf9580d57426a51119fec40bafe2834af65e2badaf919716c8b84f8c93c5363

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
