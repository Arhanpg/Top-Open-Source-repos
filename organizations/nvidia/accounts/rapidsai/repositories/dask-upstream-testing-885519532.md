# rapidsai/dask-upstream-testing

- Company: NVIDIA
- GitHub account: [https://github.com/rapidsai](https://github.com/rapidsai)
- Mapping status: official-project-linked
- Repository: [rapidsai/dask-upstream-testing](https://github.com/rapidsai/dask-upstream-testing)
- Default branch: main
- README: [Open upstream README](https://github.com/rapidsai/dask-upstream-testing/blob/main/README.md)
- README blob SHA: 24f49eaf494449988166dc47b5f0f988838d2c32
- Repository ID: 885519532
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:49+00:00

### Short excerpt (up to 100 words)

> This repository contains the scripts to run Dask's `gpu`-marked tests on a schedule and dask-dependent tests from some downstream libraries. The primary goal here is to quickly identify breakages in tests defined in `dask/dask` and `dask/distributed`, so we'll use the latest `main` from each of those. When breakages occur, they'll generally be fixed either in Dask or in the the nightly versions of the downstream packages (rapids, cupy, numba, etc.). And so we install the nightly (rather than `latest`) version of the downstream packages. This repository uses workflow dispatch to enable running tests against a specific version of Dask. Navigate

### README headings

- Dask Upstream Testing
- Version Policy
- Workflow Dispatch
- Version Upgrades
- RAPIDS version update

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 10,571 |
| Python | 932 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 2
- Forks at capture: 6
- Last updated: 2026-10-27T19:34:40Z
- Last pushed: 2026-11-18T21:39:36Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/rapidsai/dask-upstream-testing)
- [README](https://github.com/rapidsai/dask-upstream-testing/blob/main/README.md)
- [Issues](https://github.com/rapidsai/dask-upstream-testing/issues)
- [Releases](https://github.com/rapidsai/dask-upstream-testing/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
