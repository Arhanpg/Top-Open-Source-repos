# amazon-science/fact-check-summarization

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/fact-check-summarization](https://github.com/amazon-science/fact-check-summarization)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/fact-check-summarization/blob/main/README.md)
- README blob SHA: a0d823bc135256deb969ca86fd535c6224bf3b4f
- README bytes captured: 15787
- README truncated at capture limit: False
- Repository ID: 339465093
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T23:24:26+00:00

### Short excerpt (up to 300 words)

> The idea is to python==3.6: conda create -n

### README headings

- Improving Factual Consistency of Abstractive Text Summarization
- Requirements and setup
- [Entity-level Factual Consistency of Abstractive Text Summarization](https://www.aclweb.org/anthology/2021.eacl-main.235/)
- Data preprocessing:
- XSUM:
- CNNDM:
- NEWSROOM:
- Tokenize and binarize the data:
- JAENS: Joint Entity and Summary Generation
- 1. prepare the train/val data by generating entity augmented targets:
- 2. Fine-tune the BART-large model on the generated data:
- 3. Generate the summaries from the fine-tuned models:
- 4. To evaluate the generated summaries for ROUGE as well as entity level factual scores:
- Summary-worthy entity classification with summarization (multi-task learning)
- [Improving Factual Consistency of Abstractive Summarization via Question Answering](https://arxiv.org/abs/2105.04623)
- *QUALS* (QUestion Answering with Language model score for Summarization)
- 0. Prepare summaries into jsonl format
- 1. Generating question and answer pairs from summaries
- 2. Filter the generated question and answer for high quality pairs
- 3. Evaluate the generated question and answer pairs using the source document as input
- 4. Compute QUALS scores for each summary
- *CONSEQ* (CONtrastive SEQ2seq learning)
- Citations

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: JAENS: Joint Entity and Summary Generation

> The idea is to

### Technology and requirements: Requirements and setup

> python==3.6: conda create -n

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,926,948 |
| Cuda | 36,414 |
| C++ | 15,854 |
| Shell | 11,304 |
| Cython | 8,858 |
| Lua | 4,210 |
| Dockerfile | 1,993 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured)
- setup.py (capture: captured)
- docs/Makefile (capture: captured)
- docs/requirements.txt (capture: captured) — dependency clues: sphinx, sphinx-argparse
- fairseq/modules/dynamicconv_layer/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 78
- Forks at capture: 15
- Last updated: 2026-09-10T16:38:46Z
- Last pushed: 2024-05-03T20:26:28Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/fact-check-summarization)
- [README](https://github.com/amazon-science/fact-check-summarization/blob/main/README.md)
- [Issues](https://github.com/amazon-science/fact-check-summarization/issues)
- [Releases](https://github.com/amazon-science/fact-check-summarization/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
