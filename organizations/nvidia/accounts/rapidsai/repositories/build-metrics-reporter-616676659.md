# rapidsai/build-metrics-reporter

- Company: NVIDIA
- GitHub account: [https://github.com/rapidsai](https://github.com/rapidsai)
- Mapping status: official-project-linked
- Repository: [rapidsai/build-metrics-reporter](https://github.com/rapidsai/build-metrics-reporter)
- Default branch: v1
- README: [Open upstream README](https://github.com/rapidsai/build-metrics-reporter/blob/v1/README.md)
- README blob SHA: 3da11fe14576f011dd44c74978e4e2e146162679
- Repository ID: 616676659
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:16:34+00:00

### Short excerpt (up to 100 words)

> This repository contains the source code for `rapids-build-metrics-reporter.py`, which is a small Python script that can be used to generate a report that contains the compile times and cache hit rates for RAPIDS library builds. It is intended to be used in the `build.sh` script of any given RAPIDS repository like this: if ! rapids-build-metrics-reporter.py 2> /dev/null && [ ! -f rapids-build-metrics-reporter.py ]; then echo "Downloading rapids-build-metrics-reporter.py" curl -sO https://raw.githubusercontent.com/rapidsai/build-metrics-reporter/v1/rapids-build-metrics-reporter.py fi PATH=".:$PATH" rapids-build-metrics-reporter.py The logic in the excerpt above ensures that `rapids-build-metrics-reporter.py` can be used in CI (where it will be pre-installed in RAPIDS CI images) and local environments (where

### README headings

- build-metrics-reporter
- Summary
- Versioning

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 20,855 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 5
- Last updated: 2026-05-27T19:54:44Z
- Last pushed: 2026-05-27T19:54:55Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/rapidsai/build-metrics-reporter)
- [README](https://github.com/rapidsai/build-metrics-reporter/blob/v1/README.md)
- [Issues](https://github.com/rapidsai/build-metrics-reporter/issues)
- [Releases](https://github.com/rapidsai/build-metrics-reporter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
