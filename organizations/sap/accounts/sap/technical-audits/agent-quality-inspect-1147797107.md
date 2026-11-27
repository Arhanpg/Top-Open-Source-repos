# SAP/agent-quality-inspect

- Company: SAP
- Account: SAP
- Repository: https://github.com/SAP/agent-quality-inspect
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:23:17+00:00

## Project purpose

Paper Link: https://openreview.net/pdf?id=fHsVNklKOc

## Why this project is used

Evaluation package that allows benchmarking of agentic AIs from various sources and frameworks by producing statistical results which can be compared across different use cases and datasets.

## Core features

- **User personas**: User proxy simulating users with different levels of domain expertise (expert and non-expert).: **User personas**: User proxy simulating users with different levels of domain expertise (expert and non-expert).
  - Evidence: README.md#Features
- **Area Under the Curve (AUC)**: Measures the area under the progress curve and evaluates how quickly the agent makes progress toward the goal.: **Area Under the Curve (AUC)**: Measures the area under the progress curve and evaluates how quickly the agent makes progress toward the goal.
  - Evidence: README.md#Features
- **Progress Per Turn (PPT)**: Measures the average progress made by the agent in each turn.: **Progress Per Turn (PPT)**: Measures the average progress made by the agent in each turn.
  - Evidence: README.md#Features
- **Task success and reliability**: Metrics such as pass@k and pass^k.: **Task success and reliability**: Metrics such as pass@k and pass^k.
  - Evidence: README.md#Features
- **Error analysis**: Automatic categorization of failure modes to highlight where and why agents fail.: **Error analysis**: Automatic categorization of failure modes to highlight where and why agents fail.
  - Evidence: README.md#Features
- **Agent-runner support**: Supports and is extensible to different agent runners. This repository currently includes integrations for **Tau2Bench** and **Toolsan: **Agent-runner support**: Supports and is extensible to different agent runners. This repository currently includes integrations for **Tau2Bench** and **Toolsandbox** and provides a pattern to extend to other multi-turn benchmarks.
  - Evidence: README.md#Features

## Technology stack

- Languages: Python, Shell, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: PyYAML, addict, aiohappyeyeballs, aiohttp, aiosignal, annotated-types, anyio, appdirs, attrs, backoff, certifi, charset-normalizer, click, colorama, contourpy, cycler, deepdiff, distro, docstring-parser, fastapi, filelock, fonttools, frozenlist, fs, fsspec, h11, httpcore, httpx, huggingface-hub, idna, importlib-metadata, iniconfig, jinja2, jiter, joblib, jsonschema, jsonschema-specifications, kiwisolver, langfuse, litellm, loguru, markdown-it-py, markupsafe, matplotlib, mdurl, multidict, narwhals, numpy, openai, orderly-set, packaging, pandas, pillow, plotly, pluggy, propcache, psutil, pydantic, pydantic-argparse, pydantic-core, pygments, pyparsing, pytest, python-dateutil, python-dotenv, pytz, pyyaml, redis, referencing, regex, requests, rich, rpds-py, ruff, scikit-learn, scipy, seaborn, setuptools, six, sniffio, starlette, tabulate, tenacity, threadpoolctl, tiktoken, tokenizers, toml, tqdm, typing-extensions, tzdata, urllib3, uvicorn, watchdog, win32-setctime, wrapt, yarl, zipp
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: agent_runners/tau2-bench/src/tau2/cli.py, agent_runners/tau2-bench/src/tau2/environment/server.py, agent_runners/tau2-bench/fastapi_server/main.py, agent_runners/tau2-bench/src/tau2/__init__.py

## Setup and usage

- Quick Start: There are two primary ways to use this repository:
- Quick Start: 1. **As a metrics / evaluation package** inside your own code.
- Quick Start: 2. **Via the provided experiment runners** to reproduce paper results and run new evaluations.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/SAP/agent-quality-inspect/blob/main/README.md
- README SHA: 4578879a77eef73898ef763c15ebca5038e07ec0
- Manifests: pyproject.toml, docs/Makefile, agent_runners/tau2-bench/Makefile, agent_runners/tau2-bench/pyproject.toml, agent_runners/tau2-bench/requirements.txt
- Sampled source files: agent_runners/tau2-bench/src/tau2/cli.py, agent_runners/tau2-bench/src/tau2/environment/server.py, agent_runners/tau2-bench/fastapi_server/main.py, agent_runners/tau2-bench/src/tau2/__init__.py
- Git tree state: captured
- Evidence fingerprint: 27d5561af02848a334edb15cb46621d349ccf5868d465dc0f93afb45f6fac4bd

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
