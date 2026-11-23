# awslabs/amazon-denseclus

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-denseclus](https://github.com/awslabs/amazon-denseclus)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/amazon-denseclus/blob/main/README.md)
- README blob SHA: a5d63bbb94c95659adf0f6fdf403efd354dcc773
- Repository ID: 392481310
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Clustering for mixed-type data

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:27:22+00:00

### Short excerpt (up to 100 words)

> DenseClus is a Python module for clustering mixed type data using UMAP and HDBSCAN. Allowing for both categorical and numerical data, DenseClus makes it possible to incorporate all features in clustering. python3 -m pip install amazon-denseclus DenseClus requires a Panda's dataframe as input with both numerical and categorical columns. All preprocessing and extraction are done under the hood, just call fit and then retrieve the clusters! from denseclus import DenseClus from denseclus.utils import make_dataframe df = make_dataframe() clf = DenseClus(df) clf.fit(df) scores = clf.evaluate() print(scores[0:10]) DenseClus uses a `predict` method when `umap_combine_method` is set to `ensemble`. Results are return in

### README headings

- Amazon DenseClus
- Installation
- Quick Start
- Usage
- Prediction
- On Combination Method
- To Use with GPU with Ensemble
- Advanced Usage
- Examples
- Notebooks
- Blogs
- References

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Jupyter Notebook | 763,385 |
| Python | 49,633 |
| Makefile | 2,071 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured)
- requirements.txt (capture: captured) — dependency clues: hdbscan, numba, numpy, pandas, scikit_learn, seaborn, umap_learn
- setup.py (capture: captured)
- docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 101
- Forks at capture: 18
- Last updated: 2026-08-21T17:04:28Z
- Last pushed: 2024-07-29T22:54:49Z
- Topics: clustering, embedding, machinelearning-python, python

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-denseclus)
- [README](https://github.com/awslabs/amazon-denseclus/blob/main/README.md)
- [Issues](https://github.com/awslabs/amazon-denseclus/issues)
- [Releases](https://github.com/awslabs/amazon-denseclus/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
