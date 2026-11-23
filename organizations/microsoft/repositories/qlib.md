# Qlib

<sub>Company: Microsoft · Repository: [microsoft/qlib](https://github.com/microsoft/qlib) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

Qlib is an open-source, AI-oriented quantitative investment platform. Its stated goal is to support quantitative investment research from idea exploration through production-oriented implementation. The README describes a full machine-learning workflow covering data processing, model training and backtesting, with components spanning alpha research, risk modelling, portfolio optimization and order execution.

**Problem it addresses:** quantitative research requires more than an isolated prediction model. Researchers need connected tooling for financial data preparation, modelling, experimentation, evaluation and portfolio-level decision support. Qlib brings those stages into one research platform.

## Research paradigms and workflow coverage

The README explicitly lists support for several modelling paradigms:

- **Supervised learning:** mining nonlinear patterns from heterogeneous financial data.
- **Market-dynamics modelling:** addressing changing market behaviour and concept drift.
- **Reinforcement learning:** modelling continuous investment decisions and assisting with trading-strategy optimization.

Its documented pipeline covers:

1. Financial data processing.
2. Model training.
3. Backtesting.
4. Alpha seeking and factor research.
5. Risk modelling.
6. Portfolio optimization.
7. Order execution workflows.

This is a broad research platform; the README does not imply that a user can skip data validation, execution controls or financial risk review.

## Notable project components and research directions

The README's release history and feature table reference a range of model and workflow areas, including:

- KRNN and Sandwich models.
- HIST and IGMTF models.
- Reinforcement-learning workflows.
- High-frequency data processing and examples.
- Online serving and automatic model rolling.
- Meta-learning and domain-adaptation work.
- Planning-based portfolio optimization.
- Nested decision workflows.
- Transformer, Localformer, TCN, ADARNN, TabNet and DoubleEnsemble model additions.

The README also points to **RD-Agent**, a related project for LLM-based autonomous evolving agents in industrial data-driven R&D. It describes quant factor mining and model optimization workflows and links the associated research paper. RD-Agent is a separate repository and should not be counted as a Qlib subdirectory.

## Technology profile

| Area | README-supported details |
|---|---|
| Main package | `pyqlib` |
| Primary programming ecosystem | Python |
| Platforms advertised | Linux, Windows and macOS |
| Modelling approaches | Supervised learning, market-dynamics modelling and reinforcement learning |
| Core pipeline | Data processing, training and backtesting |
| Research domains | Alpha, risk, portfolio optimization and order execution |
| Documentation | Read the Docs and repository tutorials |

The README includes a Python package version badge and platform badges. Exact dependency versions and framework integrations should be confirmed from the current project manifests and documentation rather than inferred from the model list.

## Installation and learning path

The project is distributed as the `pyqlib` Python package. The repository README links to:

- [Qlib documentation](https://qlib.readthedocs.io/en/latest/)
- [Tutorial notebooks](https://github.com/microsoft/qlib/tree/main/examples/tutorial)
- [Qlib research paper](https://arxiv.org/abs/2009.11189)

A practical evaluation should begin with the official tutorial and a supported data provider, then reproduce a small training/backtesting workflow before moving to custom datasets or high-frequency workloads.

## Important upgrade and safety note

The inspected README contains a prominent notice about **unreleased breaking changes** in source builds related to artifact loading. Saved model and dataset recorder loads are restricted by default in those source changes. Workflows that reload saved artifacts, resume online or delayed training, or use DDG-DA are instructed to review artifact writers and storage permissions before opting in with `trusted=True`. There are also configuration migration changes.

The README distinguishes changes merged into `main` from changes included in a tagged/PyPI release. Check the exact installed version and follow the [artifact migration guide](https://qlib.readthedocs.io/en/latest/start/artifact_migration.html) before upgrading; do not assume source-branch behaviour matches the currently installed package.

## Suitable research applications

- Developing and comparing quantitative alpha factors.
- Testing supervised or reinforcement-learning approaches on financial time series.
- Building repeatable financial data preparation and backtesting workflows.
- Studying portfolio construction and risk modelling.
- Experimenting with high-frequency data and online model-update strategies.

Qlib is a research and engineering toolkit, not investment advice or a guarantee of trading profitability. Real deployments require independent validation, execution controls and financial risk governance.

## Upstream references

- [Repository](https://github.com/microsoft/qlib)
- [Primary README](https://github.com/microsoft/qlib/blob/main/README.md)
- [Documentation](https://qlib.readthedocs.io/en/latest/)
- [Research paper](https://arxiv.org/abs/2009.11189)
- [RD-Agent](https://github.com/microsoft/RD-Agent)
- [Artifact loading migration guide](https://qlib.readthedocs.io/en/latest/start/artifact_migration.html)

**Evidence note:** README blob inspected: `a6963f6e40bd9ebee7dd2b5c88df94fe73a67dd4`.
