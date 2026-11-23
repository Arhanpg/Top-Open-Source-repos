# amazon-science/Automating-Relational-Machine-Learning

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/Automating-Relational-Machine-Learning](https://github.com/amazon-science/Automating-Relational-Machine-Learning)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/Automating-Relational-Machine-Learning/blob/main/README.md)
- README blob SHA: 937467099a2d7c3dabe70cfc1174ca938b6f3ade
- Repository ID: 1167127630
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:44:34+00:00

### Short excerpt (up to 100 words)

> **Zhikai Chen, Han Xie, Jian Zhang, Jiliang Tang, Xiang Song, Huzefa Rangwala** Predictive modeling over relational databases (RDBs) powers applications in various domains, yet remains challenging due to the need to capture both cross-table dependencies and complex feature interactions. Recent Relational Deep Learning (RDL) methods automate feature engineering via message passing, while classical approaches like Deep Feature Synthesis (DFS) rely on predefined non-parametric aggregators. Despite promising performance gains, the comparative advantages of RDL over DFS and the design principles for selecting effective architectures remain poorly understood. We present a comprehensive study that unifies RDL and DFS in a shared design

### README headings

- (ICLR 2026) Relatron: Automating Relational Machine Learning over Relational Databases
- Abstract
- Environment Setup
- Install pixi
- Install dependencies
- Activate the environment
- Repository Structure
- Downloading Datasets and Generating DFS Features
- Download all datasets and generate DFS features
- Download a single dataset
- Download a single dataset-task pair
- Download only (skip DFS generation)
- Generate DFS only (assume datasets are already cached)
- Reproducing Experimental Results
- Figure 3-1: Rank Comparison (Classification vs. Regression)
- Table 4 & Table 5: Task Signal Evaluation and Meta-Selector
- Generating the Model Performance Bank
- Run on all tasks (uses all available GPUs)
- Customize parallelism and GPU memory threshold
- Debug mode (single process, no subprocess spawning)
- Run on all tasks
- Customize settings
- Debug mode
- configs/pyg/hpo/rel-f1.yaml
- Tasks requiring performance bank
- Baseline methods (Random, TPE, Hyperband) on a single task (--data_id selects task index)
- Ours (TPE + landscape post-hoc selection)
- Autotransfer baseline
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,249,342 |
| Rust | 129,264 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: Cython, GPUtil, GitPython, GraKeL, Mako, Markdown, PyPika, Pympler, SQLAlchemy, Werkzeug, absl-py, accelerate, adagio, aiohappyeyeballs, aiohttp, aiohttp-cors, aiosignal, alembic, annotated-types, antlr4-python3-runtime
- pytorch-frame/pyproject.toml (capture: captured) — dependency clues: Pillow, catboost, datasets, lightgbm, mpmath, mypy, numpy, optuna, optuna-integration, pandas, pre-commit, pyarrow, pytest, pytest-cov, pytorch-frame, scikit-learn, torchmetrics, tqdm, xgboost
- relbench/pyproject.toml (capture: captured) — dependency clues: datasets, duckdb, numpy, pandas, pooch, pre-commit, pyarrow, pytest, pytorch_frame, scikit-learn, sentence-transformers, torch_geometric, tqdm, typing-extensions
- rustler/Cargo.toml (capture: captured) — dependency clues: anyhow, chrono, clap, glob, half, indicatif, itertools, memmap2, ndarray, ndarray-npy, numpy, parquet, polars, pyo3, rand, rkyv, serde, serde_json, serde_yaml, xxhash-rust
- rustler/pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 5
- Forks at capture: 0
- Last updated: 2026-07-10T18:45:17Z
- Last pushed: 2026-05-09T04:19:37Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/Automating-Relational-Machine-Learning)
- [README](https://github.com/amazon-science/Automating-Relational-Machine-Learning/blob/main/README.md)
- [Issues](https://github.com/amazon-science/Automating-Relational-Machine-Learning/issues)
- [Releases](https://github.com/amazon-science/Automating-Relational-Machine-Learning/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
