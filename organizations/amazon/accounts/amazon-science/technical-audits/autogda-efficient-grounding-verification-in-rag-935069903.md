# amazon-science/AutoGDA-Efficient-Grounding-Verification-in-RAG

- Company: Amazon
- Account: amazon-science
- Repository: https://github.com/amazon-science/AutoGDA-Efficient-Grounding-Verification-in-RAG
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:07:46+00:00

## Project purpose

This repository contains code for the Automatic Generative Domain Adaption (Auto-GDA) framework published at ICLR 2025. It can be used to generate high-quality synthetic NLI data, which is useful for fine-tuning efficient NLI models to specific domains.

## Why this project is used

This repository contains code for the Automatic Generative Domain Adaption (Auto-GDA) framework published at ICLR 2025. It can be used to generate high-quality synthetic NLI data, which is useful for fine-tuning efficient NLI models to specific domains.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Jupyter Notebook, Python, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: accelerate, boto3, datasets, en-core-web-sm, evaluate, gensim, httpx, huggingface-hub, ipykernel, ipython, ipywidgets, jupyter, jupyterlab, jupyterlab_widgets, litellm, matplotlib, matplotlib-inline, multiprocess, nltk, notebook, numpy, openai, optuna, pandas, s3fs, scikit-learn, scipy, seaborn, sentence-transformers, sentencepiece, spacy, torch, tqdm, transformers
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/__init__.py, src/cross_encoder_model/__init__.py, src/cross_encoder_model/model_wrappers.py, src/cross_encoder_model/my_evaluator.py

## Setup and usage

- Installation: git clone git@github.com:amazon-science/AutoGDA-Efficient-Grounding-Verification-in-RAG.git
- Installation: cd AutoGDA-Efficient-Grounding-Verification-in-RAG
- Installation: Install mysql server which is used to manage hyperparameter configuration and venv or conda (if not already installed)
- Installation: sudo apt-get install mysql-server pkg-config default-libmysqlclient-dev build-essential python3.10-venv
- Usage: **Datasets.** First, download the datasets by exectuing the script ./src/scripts/download_datasets.sh from the main directory as working directory.
- Usage: **LLM APIs.** For using the LLM APIs either make sure you have valid credentials for Amazon Bedrock in your ~/.aws folder or set the OpenAI key in data/openai.json.
- Quickstart: We provide a simple example for running Auto-GDA on the LFQA-Verification dataset.
- Quickstart: We recommend first generating the initial data using the notebook notebooks/GenerateSync.ipynb. Second you can just launch a run of Auto-GDA by running

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-science/AutoGDA-Efficient-Grounding-Verification-in-RAG/blob/main/README.md
- README SHA: 3c778601b38067ec569d6f5526bebe7e7736bf23
- Manifests: pyproject.toml, requirements.txt
- Sampled source files: src/cross_encoder_model/model_wrappers.py, src/cross_encoder_model/my_evaluator.py
- Git tree state: captured
- Evidence fingerprint: 301d2f31c46f7ba088fb501da12dbcbbbc4b2fc6e15ecab279033e436989c6be

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
