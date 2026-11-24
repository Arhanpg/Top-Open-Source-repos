# amazon-science/BartGraphSumm

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/BartGraphSumm](https://github.com/amazon-science/BartGraphSumm)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/BartGraphSumm/blob/main/README.md)
- README blob SHA: c3bbb29db2ae49b7a6d8cc0626611bd3cdb55020
- Repository ID: 399244873
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Implementation of the paper "Efficiently Summarizing Text and Graph Encodings of Multi-Document Clusters (NAACL 2021)"

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:38:08+00:00

### Short excerpt (up to 100 words)

> This is the implementation of the paper Efficiently Summarizing Text and Graph Encodings of Multi-Document Clusters. 1. This code is tested using Python 3.6, Pytorch 1.4, and CUDA 10.1 2. Install Apex: - ```cd ~; git clone https://github.com/NVIDIA/apex``` - ```cd apex``` - ```pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" --global-option="--deprecated_fused_adam" ./``` 3. Install nccl: - ```cd ~; git clone https://github.com/NVIDIA/nccl.git``` - ```cd nccl``` - ```make -j10 src.build CUDA_HOME=/usr/local/cuda-10.1``` - ```sudo apt install build-essential devscripts debhelper fakeroot``` - ```make -j10 pkg.debian.build CUDA_HOME=/usr/local/cuda-10.1``` - ```sudo apt install ./build/pkg/deb/*.deb``` 4. Setup fairSeq and import some files: - ```cd ~``` - ```pip uninstall -y enum34```

### README headings

- Efficiently Summarizing Text and Graph Encodings of Multi-Document Clusters (NAACL 2021)
- Pre-installations
- Prepare Multi-News Data
- Code Setup
- Train and Evaluate
- BART baseline
- BART-Long
- BART-Long-Graph
- Security
- License
- Reference

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,337,118 |
| Shell | 43,404 |
| Cuda | 36,414 |
| C++ | 15,854 |
| Makefile | 13,594 |
| Cython | 8,858 |
| Lua | 4,210 |
| Batchfile | 805 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/fairseq/pyproject.toml (capture: captured)
- src/fairseq/setup.py (capture: captured)
- src/fairseq/docs/Makefile (capture: captured)
- src/fairseq/docs/requirements.txt (capture: captured) — dependency clues: sphinx, sphinx-argparse
- src/fairseq/fairseq/modules/dynamicconv_layer/setup.py (capture: captured)
- src/fairseq/fairseq/modules/lightconv_layer/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 29
- Forks at capture: 2
- Last updated: 2026-06-26T02:15:34Z
- Last pushed: 2025-09-04T08:56:57Z
- Topics: abstractive-summarization

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/BartGraphSumm)
- [README](https://github.com/amazon-science/BartGraphSumm/blob/main/README.md)
- [Issues](https://github.com/amazon-science/BartGraphSumm/issues)
- [Releases](https://github.com/amazon-science/BartGraphSumm/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
