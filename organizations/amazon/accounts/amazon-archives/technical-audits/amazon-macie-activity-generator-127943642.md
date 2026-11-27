# amazon-archives/amazon-macie-activity-generator

- Company: Amazon
- Account: amazon-archives
- Repository: https://github.com/amazon-archives/amazon-macie-activity-generator
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:24:25+00:00

## Project purpose

**Anomaly detection systems** (i.e. Amazon Macie) often perform quantitative analytics over timeseries derived from activities on their monitored subjects. While the core anomaly detection algorithms can be tested in isolation using test vectors, testing and measuring end to end performance and accuracy of these systems remain a challenge. **activity generator** aims to address at least a subset of these challenges via providing a platform to facilitate **timeseries generation, noise addition, anomaly injection** and **execution on target subjects** over an extended period of time. This platform offers generating synthetic timeseries as well as replaying real timeseries gathered from monitoring subjects in the past.

## Why this project is used

A platform to help security researchers develop and test machine learning-based security services based on time-series data, with the ability to generate synthetic time-series, replay existing log time-series, and inject noise and anomalies.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: faker, numpy, scipy
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-archives/amazon-macie-activity-generator/blob/master/README.md
- README SHA: 534f72c43b6330a9d9b434ddb4b66d057158b08f
- Manifests: requirements.txt
- Sampled source files: src/main.py
- Git tree state: captured
- Evidence fingerprint: 3acec1d855a83e2866ec4e27b77aa9628104f0e285aef39b3268371c6a96aa21

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
