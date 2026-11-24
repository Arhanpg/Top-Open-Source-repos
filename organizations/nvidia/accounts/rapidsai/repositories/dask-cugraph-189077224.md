# rapidsai/dask-cugraph

- Company: NVIDIA
- GitHub account: [https://github.com/rapidsai](https://github.com/rapidsai)
- Mapping status: official-project-linked
- Repository: [rapidsai/dask-cugraph](https://github.com/rapidsai/dask-cugraph)
- Default branch: branch-0.9
- README: [Open upstream README](https://github.com/rapidsai/dask-cugraph/blob/branch-0.9/README.md)
- README blob SHA: 2535da1421891958080f6cea61464dc95e10c0bd
- Repository ID: 189077224
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:44+00:00

### Short excerpt (up to 100 words)

> Dask cuGraph contains parallel graph analytics algorithms that can make use of multiple GPUs on a single host. It is able to play nicely with other projects in the Dask ecosystem, as well as other RAPIDS projects, such as Dask cuDF and Dask cuML. As an example, the following Python snippet loads input from a csv file into a Dask cuDF Dataframe and finds the Pagerank in parallel, on multiple GPUs: from dask_cuda import LocalCUDACluster cluster = LocalCUDACluster() import dask_cudf df = dask_cudf.read_csv("/path/to/csv") import dask_cugraph pagerank = dask_cugraph.mg_pagerank(df) Clusters of Dask workers can be started in several different ways. One

### README headings

- <div align="left"><img src="img/rapids_logo.png" width="90px"/>&nbsp;Dask cuGraph - Multi-GPU Graph Analytics Algorithms</div>
- Use
- Create a Dask CUDA cluster w/ one worker per device
- Read CSV file in parallel across workers
- Find PageRank
- Dask CUDA Clusters
- Using the LocalCUDACluster()
- Using the dask-worker command
- Supported Algorithms
- Installation
- Conda
- Contact
- <div align="left"><img src="img/rapids_logo.png" width="265px"/></div> Open GPU Data Science

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 85,883 |
| Shell | 9,628 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- setup.py (capture: captured)
- docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 8
- Forks at capture: 5
- Last updated: 2024-09-17T08:41:48Z
- Last pushed: 2019-07-19T19:45:32Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/rapidsai/dask-cugraph)
- [README](https://github.com/rapidsai/dask-cugraph/blob/branch-0.9/README.md)
- [Issues](https://github.com/rapidsai/dask-cugraph/issues)
- [Releases](https://github.com/rapidsai/dask-cugraph/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
