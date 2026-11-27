# NVIDIA/UnsupervisedLandmarkLearning

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/UnsupervisedLandmarkLearning](https://github.com/NVIDIA/UnsupervisedLandmarkLearning)
- Default branch: master
- README: [Open upstream README](https://github.com/NVIDIA/UnsupervisedLandmarkLearning/blob/master/README.md)
- README blob SHA: 739207f8d4f4c594361b37ca74f2b91d2d9ec30e
- README bytes captured: 6816
- README truncated at capture limit: False
- Repository ID: 233710742
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Implementation for the unsupervised latent landmark learning work from NVIDIA Applied Deep Learning Research

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:48:06+00:00

### Short excerpt (up to 300 words)

> Aysegul Dundar, Kevin J. Shih, Animesh Garg, Robert Pottorf, Andrew Tao, Bryan Catanzaro This repository provides our implementation for learning unsupervised landmarks from video data,

### README headings

- Unsupervised Disentanglement of Pose, Appearance and Background from Images and Videos
- Setup
- Datasets
- BBC
- Landmark Training
- Single GPU Training
- Multi-GPU Training
- BBC Landmark Evaluation
- cache the gaussian landmarks for the training data
- landmarks will be stored in pkl files in the gauss_dumps directory
- opt.yaml is the configuration file holding all the options for the pretrained model. It will be automatically output during training
- WARNING: this might take 20-30 minutes, and requires a fair amount of RAM for the training set caching.
- map the landmarks to the annotated keypoints with linear regression (no intercept)
- load the test-set annotations and evaluate. This script should match the output provided by the matlab eval code in the BBC Pose code folder
- Acknowledgements

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Unsupervised Disentanglement of Pose, Appearance and Background from Images and Videos

> Aysegul Dundar, Kevin J. Shih, Animesh Garg, Robert Pottorf, Andrew Tao, Bryan Catanzaro This repository provides our implementation for learning unsupervised landmarks from video data,

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 96,221 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- docker/dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 48
- Forks at capture: 13
- Last updated: 2026-07-21T12:28:06Z
- Last pushed: 2020-02-12T00:13:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/UnsupervisedLandmarkLearning)
- [README](https://github.com/NVIDIA/UnsupervisedLandmarkLearning/blob/master/README.md)
- [Issues](https://github.com/NVIDIA/UnsupervisedLandmarkLearning/issues)
- [Releases](https://github.com/NVIDIA/UnsupervisedLandmarkLearning/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
