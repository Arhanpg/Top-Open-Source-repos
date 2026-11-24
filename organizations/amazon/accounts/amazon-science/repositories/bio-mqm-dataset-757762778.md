# amazon-science/bio-mqm-dataset

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/bio-mqm-dataset](https://github.com/amazon-science/bio-mqm-dataset)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/bio-mqm-dataset/blob/main/README.md)
- README blob SHA: 7c0647078b9bd3aec19996d30d3762a831873b74
- Repository ID: 757762778
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Dataset and codebase for "Fine-Tuned Machine Translation Metrics Struggle in Unseen Domains"

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:38:18+00:00

### Short excerpt (up to 100 words)

> Dataset and codebase for *Fine-Tuned Machine Translation Metrics Struggle in Unseen Domains* If you use the data or code, please cite: @article{zouhar2024finetuned, title={Fine-Tuned Machine Translation Metrics Struggle in Unseen Domains}, author={Vilém Zouhar and Shuoyang Ding and Anna Currey and Tatyana Badeka and Jenyuan Wang and Brian Thompson}, year={2024}, eprint={2402.18747}, archivePrefix={arXiv}, journal={arXiv preprint arXiv:2306.07899}, url={https://arxiv.org/abs/2402.18747} } The dataset is based on system submissions from 21 participants to the WMT21 bio translation shared task (Yeganova et al., 2021), which is in turn based on bilingual academic paper abstracts in the MEDLINE corpus retrieved from National Library of Medicine (NLM). Reference translations and

### README headings

- Biomedical MQM Dataset
- New Dataset
- Important Prerequisites
- Comet
- Bertscore
- Setting Up Data for Result Reproduction
- main set, for testing
- secondary set, for dev and "train"
- 2022 data, for testing
- <2022 data, for training
- Baseline Metric Evaluation
- example how to use the GEMBA scores
- all figures are stored locally
- check that figure was generated
- Adapting MQM
- Baseline DA and DA+MQM
- output is ${ADAPTATION_ROOT}/models/trained/da/main/checkpoints/*.ckpt
- output is ${ADAPTATION_ROOT}/models/trained/da/qe/checkpoints/*.ckpt
- output is ${ADAPTATION_ROOT}/models/trained/mqm/main/checkpoints/*.ckpt
- output is ${ADAPTATION_ROOT}/models/trained/mqm/qe/checkpoints/*.ckpt
- Finetuning on Bio
- mass-evaluate everything (the stars need to be in quotes)
- or feel free to paralelize in the following way:
- check that the eval logfiles exist, should be 348 lines
- NOTE: you may need to manually add DA and MQM+DA
- run the plotting
- check figures exist
- Training with Mixed Bio and General
- the evaluation can be parametrized by replacing `"*"`
- sanity check

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 214,728 |
| Shell | 65,183 |
| Jupyter Notebook | 26,629 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 6
- Last updated: 2026-08-02T01:36:35Z
- Last pushed: 2024-03-01T21:42:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/bio-mqm-dataset)
- [README](https://github.com/amazon-science/bio-mqm-dataset/blob/main/README.md)
- [Issues](https://github.com/amazon-science/bio-mqm-dataset/issues)
- [Releases](https://github.com/amazon-science/bio-mqm-dataset/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
