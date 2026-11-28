# microsoft/AEC-Challenge

- Company: Microsoft
- Account: microsoft
- Repository: https://github.com/microsoft/AEC-Challenge
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:52:50+00:00

## Project purpose

The ICASSP 2023 Acoustic Echo Cancellation Challenge is intended to stimulate research in acoustic echo cancellation (AEC), which is an important area of speech enhancement and is still a top issue in audio communication. This is the fourth AEC challenge and it is enhanced by adding a second track for personalized acoustic echo cancellation, reducing the algorithmic+buffering latency to 20ms, and including a full-band version of AECMOS. We open source two large datasets to train AEC models under both single talk and double talk scenarios. These datasets consist of recordings from more than 10,000 real audio devices and human speakers in real environments, as well as a synthetic dataset. We open source an online subjective test framework and provide an online objective metric service for researchers to quickly test their results. The winners of this challenge were selected based on the av

## Why this project is used

AEC Challenge

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: librosa, numpy, onnxruntime, soundfile, tqdm
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: AECMOS/aecmos.py, AECMOS/AECMOS_local/aecmos.py, baseline/icassp2022/enhance.py, baseline/interspeech2021/audio_utils.py

## Setup and usage

- Usage: 1. Set up Git Large File Storage (LFS) for faster download of the datasets. First, download and install the Git LFS client. Then, set up Git LFS for your user account by running:
- Usage: 2. Clone the repository.
- Usage: git clone https://github.com/microsoft/AEC-Challenge AEC-Challenge

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/microsoft/AEC-Challenge/blob/main/README.md
- README SHA: bbd846797b6ef13ad68717a15ea253f2023656de
- Manifests: baseline/icassp2022/requirements.txt, baseline/interspeech2021/requirements.txt
- Sampled source files: AECMOS/aecmos.py, AECMOS/AECMOS_local/aecmos.py, baseline/icassp2022/enhance.py, baseline/interspeech2021/audio_utils.py
- Git tree state: captured
- Evidence fingerprint: ee5774eeb79295aa95a1059a79d72cc015a748820746609307c45950152a2151

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
