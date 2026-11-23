# NVIDIA cuGraph

- **Company:** NVIDIA
- **GitHub account:** [rapidsai](https://github.com/rapidsai)
- **Repository:** [rapidsai/cugraph](https://github.com/rapidsai/cugraph)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/rapidsai/cugraph/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `de6dc1db13871fb6fdb1d7070ba07b1600cf4a55`

## Project overview

A collection of GPU-accelerated graph analytics packages for creating and manipulating graphs and running scalable graph algorithms. The README positions cuGraph as part of the RAPIDS GPU data-science ecosystem.

## Features and capabilities documented by the README

- Provides graph creation/manipulation and scalable graph algorithms, with a README example computing PageRank from an edge-list dataframe.
- The high-level Python API works with GPU DataFrames from cuDF and offers an interface familiar to users of pandas-like dataframes and NetworkX.
- Supports importing data from pandas DataFrames, NetworkX graph objects and other formats.
- Provides `pylibcugraph`, a lower-level Python API intended for tighter integration with fewer dependencies.
- Provides `libcugraph` and `libcugraph_c` for C/C++/CUDA-oriented access to lower-level graph functionality.
- Links current algorithm support, package installation, source-build and API documentation.
- Lists ecosystem integrations and projects using cuGraph, including ArangoDB, CuPy, Memgraph, NetworkX via nx-cugraph, PyGraphistry and ScanPy.

## Technology stack

Python; C/C++; CUDA; RAPIDS; cuDF; cuML; pandas DataFrames; NetworkX; Dask and Apache Arrow references. The repository exposes Python, C and C++ API documentation. The README displays an Apache 2.0 licence badge.

## Getting started

Follow the official cuGraph installation guide for package installation or the source-build guide for a source build. The README's Python example loads an edge list into a cuDF DataFrame, constructs a `cugraph.Graph`, and calls `cugraph.pagerank`.

## Lifecycle, compatibility and operational considerations

cuGraph's high-level Python API and lower-level C/C++/CUDA APIs target different integration needs. The README itself warns readers to check the latest stable README/branch. Algorithm availability and supported GPU/software versions should be verified against the linked release documentation.

## Evaluation guidance

Review the release-specific installation documentation, exact software/hardware requirements, dependency manifests, licence terms and security guidance before using the project in production. Benchmark claims should be tested on the actual target hardware and workload. This dossier is based on the upstream README; it is not a full source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/rapidsai/cugraph)
- [README](https://github.com/rapidsai/cugraph/blob/main/README.md)
- [Issues](https://github.com/rapidsai/cugraph/issues)
- [Releases](https://github.com/rapidsai/cugraph/releases)

*Evidence note: the README blob SHA identifies the upstream version inspected. Details not supported by the README are left unspecified or directed to version-specific documentation.*
