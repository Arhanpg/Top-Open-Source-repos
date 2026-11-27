# NVIDIA/ContrastiveLosses4VRD

- Company: NVIDIA
- Account: NVIDIA
- Repository: https://github.com/NVIDIA/ContrastiveLosses4VRD
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:41:05+00:00

## Project purpose

Example results of RelDN with without and with our losses. "L0 only" means using only the original multi-class logistic loss (without our losses). The top row shows RelDN outputs and the bottom row visualizes the learned predicate CNN features of the two models. Red and green boxes highlight the wrong and right outputs (the first row) or feature saliency (the second row).

## Why this project is used

Implementation for the CVPR2019 paper "Graphical Contrastive Losses for Scene Graph Generation"

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Jupyter Notebook, Python, Dockerfile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/core/__init__.py, lib/core/config.py, lib/core/test_engine_rel.py, lib/core/test_rel.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/NVIDIA/ContrastiveLosses4VRD/blob/master/README.md
- README SHA: a61a79de31e82bd665a4381f5ecb23bfc4fd52c1
- Manifests: docker/Dockerfile, lib/setup.py
- Sampled source files: lib/core/config.py, lib/core/test_engine_rel.py, lib/core/test_rel.py
- Git tree state: captured
- Evidence fingerprint: c6c88df206fce1044491b4bb6c7b7763823b9738d6c15747a4e8bcab64db5418

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
