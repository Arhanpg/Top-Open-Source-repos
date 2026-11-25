# rapidsai/blazingsql-release-staging

- Company: NVIDIA
- Account: rapidsai
- Repository: https://github.com/rapidsai/blazingsql-release-staging
- Default branch: branch-21.10
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:25:30+00:00

## Project purpose

> A lightweight, GPU accelerated, SQL engine built on the RAPIDS.ai ecosystem.

## Why this project is used

BlazingSQL is a lightweight, GPU accelerated, SQL engine for Python. Built on RAPIDS cuDF.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Python, Java, Shell, Cuda, Jupyter Notebook, CMake, Cython, Dockerfile, FreeMarker, CSS, Lua, Makefile, C, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: alabaster, blazingdb-calcite-parent, breathe, commonmark, exhale, jcl-over-slf4j, junit, maven-compiler-plugin, maven-javadoc-plugin, recommonmark, slf4j-api, slf4j-log4j12, sphinx, sphinx-book-theme, testng
- Build/package tools: CMake configuration, Docker build configuration, Maven project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/ApplicationContext.java, algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/CalciteApplication.java, algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/Chrono/Check.java, algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/Chrono/Chronometer.java

## Setup and usage

- Getting Started: Here's two copy + paste reproducable BlazingSQL snippets, keep scrolling to find example Notebooks below.
- Getting Started: Create and query a table from a cudf.DataFrame with progress bar:
- Getting Started: df = cudf.DataFrame()
- Getting Started: df['key'] = ['a', 'b', 'c', 'd', 'e']
- Getting Started: df['val'] = [7.6, 2.9, 7.1, 1.6, 2.2]
- Getting Started: from blazingsql import BlazingContext
- Getting Started: bc = BlazingContext(enable_progress_bar=True)
- Getting Started: bc.create_table('game_1', df)

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/rapidsai/blazingsql-release-staging/blob/branch-21.10/README.md
- README SHA: 536b54d2c02ce899413a4a9bff85a1ca2eb54918
- Manifests: Dockerfile, algebra/pom.xml, docsrc/Makefile, docsrc/requirements.txt, engine/CMakeLists.txt, engine/setup.py
- Sampled source files: algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/ApplicationContext.java, algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/CalciteApplication.java, algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/Chrono/Check.java, algebra/blazingdb-calcite-application/src/main/java/com/blazingdb/calcite/application/Chrono/Chronometer.java
- Git tree state: captured
- Evidence fingerprint: 59649fe90f40c82e652e493f17458ff802c9e8d06d6cbc370231d3c8f0343157

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
