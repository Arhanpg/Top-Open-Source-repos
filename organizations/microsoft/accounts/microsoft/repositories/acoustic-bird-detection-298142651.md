# microsoft/acoustic-bird-detection

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/acoustic-bird-detection](https://github.com/microsoft/acoustic-bird-detection)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/acoustic-bird-detection/blob/main/README.md)
- README blob SHA: 29f63ebf66635ee839f01580c219d44d7b80e555
- Repository ID: 298142651
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Machine learning tools for acoustic bird detection

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:17+00:00

### Short excerpt (up to 100 words)

> The Araripe Manakin (<i>Antilophia bokermanni</i>) is one of the rarest birds in the world, found only in a tiny forested valley in Brazil at the base of the Araripe Plateau. This critically endangered species, first discovered in 1996, was pushed to the brink of extinction through habitat destruction as settlements encroach on the last remaining forested areas (for more info). AI-fueled automatic bird call recognition (bioacoustic monitoring) is an important new tool for locating and restoring the health of such elusive species populations, but the accuracy of such systems inherently suffers from a lack of sufficient audio examples of the

### README headings

- Tutorial: Accurate Bioacoustic Species Detection from Small Numbers of Training Clips Using the Biophony Model
- **Introduction**
- Araripe Manakin *Antilophia bokermanni*
- Passive Acoustic Monitoring for Conservation
- Getting Started
- Prepare your environment and launch the `Jupyter Notebook`
- Download the Starter Kit
- uncomment the lines below if you are running the notebook in a hosted environment
- such as Google Colab to collect the libraries and supporting scripts you need.
- Data Preparation and Exploration
- Download Sample Data
- Depending on your environment, you may need to modify this script,
- which is located in the root of the repository.
- Data Preview
- Audio Preview
- Spectrograms As Feature Data
- note that we have increased the contrast to highlight the calls.
- Mel-frequency spectrograms
- visualize seconds 1-3 of the previous audio file, using Mel-frequency filter bank energies
- Window Labels
- Final Steps and Data Review
- Train / Test Split, Filter Bank Creation
- split train / test data
- create mel-frequency energy spectrograms
- Data Review
- Model Building Part 1: PCA Features + SVM
- Principal Component Analysis
- flatten our test and training sets into 1-dimensional vectors.
- n_components is the size of the vector into which PCA will decompose its input.
- This is another hyperparameter that can be tuned to get better accuracy.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Jupyter Notebook | 34,493 |
| R | 21,182 |
| Python | 3,057 |
| Shell | 296 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: jupyter, matplotlib, pandas, python_speech_features, sklearn, soundfile, tensorflow

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 50
- Forks at capture: 20
- Last updated: 2026-11-09T00:35:23Z
- Last pushed: 2020-10-15T15:16:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/acoustic-bird-detection)
- [README](https://github.com/microsoft/acoustic-bird-detection/blob/main/README.md)
- [Issues](https://github.com/microsoft/acoustic-bird-detection/issues)
- [Releases](https://github.com/microsoft/acoustic-bird-detection/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
