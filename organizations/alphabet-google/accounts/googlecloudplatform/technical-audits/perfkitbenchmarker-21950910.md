# GoogleCloudPlatform/PerfKitBenchmarker

- Company: Alphabet (Google)
- Account: GoogleCloudPlatform
- Repository: https://github.com/GoogleCloudPlatform/PerfKitBenchmarker
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:55:29+00:00

## Project purpose

PerfKit Benchmarker is an open effort to define a canonical set of benchmarks to measure and compare cloud offerings. It's designed to operate via vendor provided command line tools. The benchmark default settings are not tuned for any particular platform or instance type. These settings are recommended for consistency across services. Only in the rare case where there is a common practice like setting the buffer pool size of a database do we change any settings.

## Why this project is used

PerfKit Benchmarker (PKB) contains a set of benchmarks to measure and compare cloud offerings. The benchmarks use default settings to reflect what most users will see. PerfKit Benchmarker is licensed under the Apache 2 license terms. Please make sure to read, understand and agree to the terms of the LICENSE and CONTRIBUTING files before proceeding.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Jinja, HTML, Shell, Lua, PowerShell, Dockerfile, Tcl, HCL, R, BitBake, TSQL
- Frameworks/libraries: Unknown / not established
- Dependency names: PyYAML, absl-py, anthropic, beautifulsoup4, blinker, colorlog, google-api-core, google-cloud-core, google-cloud-monitoring, google-genai, immutabledict, jinja2, numpy, openai, packaging, pandas, pint, python-dotenv, pytz, pywinrm, requests, rsa, scipy, seaborn, setuptools, six, timeout-decorator
- Build/package tools: Docker build configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: perfkitbenchmarker/data/docker/agentic/adk-agent/main.py, perfkitbenchmarker/data/llm_eval/main.py, perfkitbenchmarker/scripts/messaging_service_scripts/common/app.py, hooks/lib/check-boilerplate.sh

## Setup and usage

- Getting Started: To quickly get started running PKB, follow one of our tutorials:
- Getting Started: - Beginner tutorial for an in-depth but
- Getting Started: beginner friendly look at PKB's architectures, flags, and even data
- Getting Started: visualization, using GCP's Cloud Shell & netperf benchmarks.
- Getting Started: - Docker tutorial to run PKB in just a few
- Getting Started: steps, using GCP & docker.
- Getting Started: - Continue reading below for installation & setup on all Clouds + discussion
- Getting Started: of many topics like flags, configurations, preprovisioned data, & how to

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/GoogleCloudPlatform/PerfKitBenchmarker/blob/master/README.md
- README SHA: 1dee4f1cc48ca94634b03673481878a95d11c6b9
- Manifests: Dockerfile, requirements.txt, setup.py, tools/docker_images/Dockerfile, perfkitbenchmarker/data/llm_eval/requirements.txt, perfkitbenchmarker/providers/alicloud/requirements.txt
- Sampled source files: perfkitbenchmarker/data/docker/agentic/adk-agent/main.py, perfkitbenchmarker/data/llm_eval/main.py, perfkitbenchmarker/scripts/messaging_service_scripts/common/app.py, hooks/lib/check-boilerplate.sh
- Git tree state: captured
- Evidence fingerprint: 2a653e14d22cd7cc01415d7ff7eaaa070d10d2212c500c4ced0d0e7c919d635a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
