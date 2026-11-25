# amazon-science/iwslt-autodub-task

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/iwslt-autodub-task](https://github.com/amazon-science/iwslt-autodub-task)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/iwslt-autodub-task/blob/main/README.md)
- README blob SHA: 705dc516f902043e5903afb723824c99015d8c87
- README bytes captured: 14473
- README truncated at capture limit: False
- Repository ID: 590144513
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:13:18+00:00

### Short excerpt (up to 300 words)

> Copyright Amazon.com, Inc. or conda create -n fastspeech2

### README headings

- Introduction
- Setting up the environment
- Clone this repository (~1.1 GB)
- Create a conda environment
- Download Prism model for evaluation
- Downloads Prism model (~1.4 GB)
- Download and extract data
- Download and split CoVoST2 TSV files
- Compute the distribution of speech durations
- Build dataset
- text -> text. Used to generate references for automatic evaluation of translation quality.
- text and noised binned segments -> phones and durations. For the baseline model.
- Prepare target factor files
- Decode test set and evaluate using provided Sockeye baseline model
- Decoding using **baseline_factored_noised0.1**
- Check JSON file looks like this
- Evaluate **baseline_factored_noised0.1** output
- Reproduce Sockeye baseline models
- Set the number of GPUs for distributed training
- Adjust BATCH_SIZE and UPDATE_INTERVAL according to your GPU situation.
- For example, if you change N_GPU to 2, you should set update-interval to 8 to have the same effective batch size
- Generate test set dubs with Sockeye models
- Create separate environment for FastSpeech2 dependencies
- Download and extract pretrained model

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> Copyright Amazon.com, Inc. or

### Technology and requirements: Create separate environment for FastSpeech2 dependencies

> conda create -n fastspeech2

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 61,462 |
| Shell | 5,842 |

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
- Stars at capture: 21
- Forks at capture: 11
- Last updated: 2026-02-09T16:29:58Z
- Last pushed: 2024-03-04T22:36:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/iwslt-autodub-task)
- [README](https://github.com/amazon-science/iwslt-autodub-task/blob/main/README.md)
- [Issues](https://github.com/amazon-science/iwslt-autodub-task/issues)
- [Releases](https://github.com/amazon-science/iwslt-autodub-task/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
