# amazon-science/background-summaries

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/background-summaries](https://github.com/amazon-science/background-summaries)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/background-summaries/blob/main/README.md)
- README blob SHA: 7def0e3767a46c4b4fe7d84f8dcb2f36aa850433
- Repository ID: 719806019
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Repository for "Background Summarization of Event Timelines"

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:44+00:00

### Short excerpt (up to 100 words)

> This is the repository for the EMNLP 2023 paper "Background Summarization of Event Timelines" by Adithya Pratapa, Kevin Small and Markus Dreyer. The image below provides an overview of the background summarization task. Background summarization dataset is available under data, as well as on Hugging Face datasets. We experiment with Flan-T5-XL and Long-T5-TGlobal-XL. For Flan-T5-XL, we explore both generic and query-focused setups. See configs/train.conf for supported model configurations. bash bash_scripts/t5/train.sh flan-t5-xl 8888 For inference, set the checkpoint path in configs/eval.conf and run the evaluation script. bash bash_scripts/t5/eval.sh flan-t5-xl We experiment with zero-shot inference with GPT-3.5. See configs/gpt.conf for supported model

### README headings

- Background Summarization of Event Timelines (EMNLP 2023)
- Dataset
- Training and inference
- T5-based systems
- example flan-t5-xl training using deepspeed
- example flan-t5-xl inference
- GPT-based systems
- Background Utility Score (BUS)
- Human and BUS evaluation data
- MTurk setup
- Model checkpoints and predictions
- Security
- License
- Reference

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 92,726 |
| HTML | 25,123 |
| Shell | 7,253 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: Unidecode, absl-py, accelerate, bert_score, bs4, datasets, deepspeed, evaluate, pyhocon, pyrouge, pytest, readability-lxml, rouge_score, seaborn, sentencepiece, spacy, transformers, ujson, wandb

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 5
- Forks at capture: 2
- Last updated: 2025-05-22T20:54:26Z
- Last pushed: 2023-12-21T07:27:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/background-summaries)
- [README](https://github.com/amazon-science/background-summaries/blob/main/README.md)
- [Issues](https://github.com/amazon-science/background-summaries/issues)
- [Releases](https://github.com/amazon-science/background-summaries/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
