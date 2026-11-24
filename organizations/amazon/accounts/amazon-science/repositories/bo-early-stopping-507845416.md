# amazon-science/bo-early-stopping

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/bo-early-stopping](https://github.com/amazon-science/bo-early-stopping)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/bo-early-stopping/blob/main/README.md)
- README blob SHA: 0ac3017de60b526d153f0ae2b710ba50e17e7805
- Repository ID: 507845416
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:38:21+00:00

### Short excerpt (up to 100 words)

> This is the code repo to reproduce figures and tables in the paper It's recommended that users use Python3 and create a virtual environment first. Then one could simply run the following to install all the dependencies. ./install.sh To generate the figures and tables in the paper, one could open the notebook: jupyter notebook table_plot.ipynb To generate raw results in csv files: PYTHONPATH="." python bin/gen_csv.py The included termination results are: * `result_identity_cv_top0.5.csv`: for XGB and RF algorithms with cross validation on 19 tabular datasets. * `bore_results_xgboost_identity_top0.5_hpobench.csv`: for BORE optimizers on HPO-Bench. * `rs_results_identity_top0.5_hpobench.csv`: for Random Search on HPO-Bench. * `tpe_results_identity_top0.5_hpobench.csv`:

### README headings

- BO-early-stopping
- Install
- Generating artifacts
- Description
- Citing
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Jupyter Notebook | 16,995,576 |
| Python | 149,731 |
| Roff | 5,377 |
| Shell | 4,029 |
| JavaScript | 543 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- experiment_env/share/jupyter/labextensions/jupyterlab-plotly/package.json (capture: captured) — dependency clues: @jupyter-widgets/base, @jupyterlab/builder, @jupyterlab/rendermime-interfaces, @lumino/application, @lumino/messaging, @lumino/widgets, @types/plotly.js, @types/webpack-env, acorn, css-loader, fs-extra, lodash, mkdirp, npm-run-all, plotly.js, prettier, rimraf, source-map-loader, style-loader, ts-loader

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 3
- Last updated: 2025-04-09T08:06:54Z
- Last pushed: 2022-09-20T11:42:14Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/bo-early-stopping)
- [README](https://github.com/amazon-science/bo-early-stopping/blob/main/README.md)
- [Issues](https://github.com/amazon-science/bo-early-stopping/issues)
- [Releases](https://github.com/amazon-science/bo-early-stopping/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
