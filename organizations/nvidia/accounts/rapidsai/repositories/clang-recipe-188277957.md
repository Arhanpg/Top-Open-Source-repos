# rapidsai/clang-recipe

- Company: NVIDIA
- GitHub account: [https://github.com/rapidsai](https://github.com/rapidsai)
- Mapping status: official-project-linked
- Repository: [rapidsai/clang-recipe](https://github.com/rapidsai/clang-recipe)
- Default branch: master
- README: [Open upstream README](https://github.com/rapidsai/clang-recipe/blob/master/README.md)
- README blob SHA: 961a20096e9ca2b732f112c2b3cbb484855c2ed6
- Repository ID: 188277957
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Clang build recipe for anaconda

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:32:28+00:00

### Short excerpt (up to 100 words)

> This repo contains recipe for building clang library, clang-format, clang-tidy and also the python wrapper for clang library. conda install -c teju85 clang libclang If you want to build your package and upload it to anaconda cloud, continue reading... * docker * git git clone https://github.com/teju85/clang-recipe cd clang-recipe docker build -t conda:dev . docker run --rm -it conda:dev /bin/bash inside-container# anaconda login inside-container# conda build lib inside-container# anaconda upload /path/to/libclang/package.tar.gz inside-container# conda build py inside-container# anaconda upload /path/to/clang/package.tar.gz

### README headings

- Introduction
- Downloading built recipes
- Building my own recipe?
- Pre-reqs
- Usage
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Dockerfile | 726 |
| Shell | 558 |
| Python | 341 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- py/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: True
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 0
- Forks at capture: 2
- Last updated: 2022-11-17T20:32:21Z
- Last pushed: 2019-05-28T18:10:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/rapidsai/clang-recipe)
- [README](https://github.com/rapidsai/clang-recipe/blob/master/README.md)
- [Issues](https://github.com/rapidsai/clang-recipe/issues)
- [Releases](https://github.com/rapidsai/clang-recipe/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
