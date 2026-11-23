# amazon-science/adversarial-robustness-with-nonuniform-perturbations

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/adversarial-robustness-with-nonuniform-perturbations](https://github.com/amazon-science/adversarial-robustness-with-nonuniform-perturbations)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/adversarial-robustness-with-nonuniform-perturbations/blob/main/README.md)
- README blob SHA: 9323c316f76f46bb3c7c85aaf4d50ff3dc19714a
- Repository ID: 422618061
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:49+00:00

### Short excerpt (up to 100 words)

> This repository hosts the code to replicate experiments of the paper Adversarial Robustness with Non-uniform Perturbations for malware use-case. Please first refer to https://github.com/elastic/ember and follow the instructions to download 2018 version of EMBER dataset and install `ember` package. After installing `ember`, use `pip` to install the required packages for this project: pip install -r requirements.txt This file contains the following functions: - `get_clean_data(data_dir)` returns train and test sets of vectorized EMBER dataset features - `get_adversarial_examples(data_dir, num_features, attack_name="GreedyNN")` returns adversarial example set which is crafted by the specified problem space attack, e.g., Greedy attack (GreedyNN). - `omega(num_features, perturbation_constraint="Uniform")` computes the

### README headings

- Adversarial Robustness with Non-uniform Perturbations
- Installation
- Usage
- NonuniformRobustness.py
- Malware_demo.ipynb
- nonuniform_omega
- Adversarial_example_sets

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 12,222 |
| Jupyter Notebook | 5,966 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: lightgbm, numpy, pandas, scikit-learn, scipy, torch, torchvision, tqdm, xgboost

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 3
- Last updated: 2024-03-10T08:17:06Z
- Last pushed: 2026-11-12T00:55:36Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/adversarial-robustness-with-nonuniform-perturbations)
- [README](https://github.com/amazon-science/adversarial-robustness-with-nonuniform-perturbations/blob/main/README.md)
- [Issues](https://github.com/amazon-science/adversarial-robustness-with-nonuniform-perturbations/issues)
- [Releases](https://github.com/amazon-science/adversarial-robustness-with-nonuniform-perturbations/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
