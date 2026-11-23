# rapidsai/blazingsql-release-staging

- Company: NVIDIA
- GitHub account: [https://github.com/rapidsai](https://github.com/rapidsai)
- Mapping status: official-project-linked
- Repository: [rapidsai/blazingsql-release-staging](https://github.com/rapidsai/blazingsql-release-staging)
- Default branch: branch-21.10
- README: [Open upstream README](https://github.com/rapidsai/blazingsql-release-staging/blob/branch-21.10/README.md)
- README blob SHA: 536b54d2c02ce899413a4a9bff85a1ca2eb54918
- Repository ID: 406099264
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

BlazingSQL is a lightweight, GPU accelerated, SQL engine for Python. Built on RAPIDS cuDF.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:16:33+00:00

### Short excerpt (up to 100 words)

> BlazingSQL is a GPU accelerated SQL engine built on top of the RAPIDS ecosystem. RAPIDS is based on the Apache Arrow columnar memory format, and cuDF is a GPU DataFrame library for loading, joining, aggregating, filtering, and otherwise manipulating data. BlazingSQL is a SQL interface for cuDF, with various features to support large scale data science workflows and enterprise datasets. * **Query Data Stored Externally** - a single line of code can register remote storage solutions, such as Amazon S3. * **Simple SQL** - incredibly easy to use, run a SQL query and the results are GPU DataFrames (GDFs). *

### README headings

- Getting Started
- Examples
- Documentation
- Prerequisites
- Install Using Conda
- Stable Version
- Nightly Version
- Build/Install from Source (Conda Environment)
- Stable Version
- Install build dependencies
- Build
- Nightly Version
- Install build dependencies
- Build
- Storage plugins
- Disable all storage plugins
- Disable AWS S3 storage plugin
- Disable Google Cloud Storage plugin
- SQL providers
- Disable all SQL providers
- Disable MySQL provider
- Documentation
- Community
- Contributing
- Contact
- License
- RAPIDS AI - Open GPU Data Science
- Apache Arrow on GPU

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 2,161,228 |
| Python | 677,764 |
| Java | 216,098 |
| Shell | 88,030 |
| Cuda | 82,625 |
| Jupyter Notebook | 76,882 |
| CMake | 58,565 |
| Cython | 37,625 |
| Dockerfile | 13,275 |
| FreeMarker | 9,690 |
| CSS | 7,968 |
| Lua | 1,780 |
| Makefile | 1,035 |
| C | 917 |
| Batchfile | 795 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- algebra/pom.xml (capture: captured) — dependency clues: blazingdb-calcite-parent, jcl-over-slf4j, junit, maven-compiler-plugin, maven-javadoc-plugin, slf4j-api, slf4j-log4j12, testng
- docsrc/Makefile (capture: captured)
- docsrc/requirements.txt (capture: captured) — dependency clues: alabaster, breathe, commonmark, exhale, recommonmark, sphinx, sphinx-book-theme
- engine/CMakeLists.txt (capture: captured)
- engine/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: True
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 2
- Last updated: 2024-04-26T21:40:29Z
- Last pushed: 2021-10-07T00:37:56Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/rapidsai/blazingsql-release-staging)
- [README](https://github.com/rapidsai/blazingsql-release-staging/blob/branch-21.10/README.md)
- [Issues](https://github.com/rapidsai/blazingsql-release-staging/issues)
- [Releases](https://github.com/rapidsai/blazingsql-release-staging/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
