# NVIDIA/auto-ontology-eval

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/auto-ontology-eval](https://github.com/NVIDIA/auto-ontology-eval)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/auto-ontology-eval/blob/main/README.md)
- README blob SHA: fae7b9fd0c2878428f38678f86b07b9f5f3e98c4
- Repository ID: 1287342429
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

LLM-powered Text-to-SQL evaluation toolkit: schema ingestion, retrieval eval, and standalone SQL judge/re-scorer.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:41:05+00:00

### Short excerpt (up to 100 words)

> Measures how much an Auto-Ontology ontology improves text-to-SQL accuracy, on public benchmarks and on your own data. Auto-Ontology exists to help agents give fewer wrong answers on enterprise data. This repository measures whether it does. A trustworthy accuracy number needs a control. The eval asks one question: how much does Auto-Ontology's ontology add over the same model given only the database schema? Each run asks the same questions of the same model twice and scores the SQL from both arms with one deterministic verifier. The result is a single accuracy difference, plus the list of questions the ontology fixed and

### README headings

- Auto-Ontology Eval
- Why it matters
- How it works
- Benchmarks and datasets
- Quickstart
- Models
- Running benchmarks
- Reading the results
- Extra prompts
- Evaluate your own data
- Troubleshooting
- Reference
- Contributing
- License and security

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 741,069 |
| Shell | 13,012 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: auto-ontology-server, datasets, huggingface-hub, matplotlib, nemo-gym, sqlglot
- resources_servers/auto_ontology_sql/requirements.txt (capture: captured) — dependency clues: nemo-gym
- resources_servers/schema_only_sql/requirements.txt (capture: captured) — dependency clues: mysql-connector-python, nemo-gym, psycopg

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 192
- Forks at capture: 39
- Last updated: 2026-11-23T16:23:41Z
- Last pushed: 2026-11-23T13:00:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/auto-ontology-eval)
- [README](https://github.com/NVIDIA/auto-ontology-eval/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/auto-ontology-eval/issues)
- [Releases](https://github.com/NVIDIA/auto-ontology-eval/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
