# Tencent/ActionDetection-DBG

- Company: Tencent
- Account: Tencent
- Repository: https://github.com/Tencent/ActionDetection-DBG
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:50:56+00:00

## Project purpose

In this repo, we propose a novel and unified action detection framework, named DBG, with superior performance over the state-of-the-art action detectors BSN and BMN. You can use the code to evaluate our DBG for action proposal generation or action detection. For more details, please refer to our paper Fast Learning of Temporal Action Proposal via Dense Boundary Generator!

## Why this project is used

Code for AAAI2020 paper "Fast Learning of Temporal Action Proposal via Dense Boundary Generator"

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, C++, Cuda, Shell, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: tensorflow/custom_op/src/prop_tcfg.h, tensorflow/custom_op/src/prop_tcfg_op.cc, tensorflow/custom_op/src/prop_tcfg_op.cu.cc, config_loader.py

## Setup and usage

- Installation: Clone the github repository. We will call the cloned directory as $DBG_ROOT.
- Installation: Firstly, you should compile our proposal feature generation layers.
- Installation: Please compile according to the framework you need.
- Installation: Compile **tensorflow-version** proposal feature generation layers:
- Installation: cd tensorflow/custom_op
- Installation: Compile **pytorch-version** proposal feature generation layers:
- Installation: python setup.py install

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/Tencent/ActionDetection-DBG/blob/master/README.md
- README SHA: 33b4752329292fb8c14b504cd8806000cb06782f
- Manifests: pytorch/custom_op/setup.py, tensorflow/custom_op/Makefile
- Sampled source files: tensorflow/custom_op/src/prop_tcfg.h, tensorflow/custom_op/src/prop_tcfg_op.cc, tensorflow/custom_op/src/prop_tcfg_op.cu.cc, config_loader.py
- Git tree state: captured
- Evidence fingerprint: 17364accdfa7258794f075535b53f652336aa5e180523718bffa1d4dcce48b9c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
