# nvidia-cosmos/cosmos-dependencies

- Company: NVIDIA
- GitHub account: [https://github.com/nvidia-cosmos](https://github.com/nvidia-cosmos)
- Mapping status: official-project-linked
- Repository: [nvidia-cosmos/cosmos-dependencies](https://github.com/nvidia-cosmos/cosmos-dependencies)
- Default branch: main
- README: [Open upstream README](https://github.com/nvidia-cosmos/cosmos-dependencies/blob/main/README.md)
- README blob SHA: b194b5bf068868b6bb0a68d813fcd9e11f62bc89
- Repository ID: 1041087655
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:16:12+00:00

### Short excerpt (up to 100 words)

> Repository for building and publishing Cosmos dependencies. Install system dependencies: export XDG_BIN_HOME="${XDG_BIN_HOME:-$HOME/.local/bin}" curl -LsSf https://astral.sh/uv/install.sh | sh source $XDG_BIN_HOME/env pushd "$XDG_BIN_HOME" && curl https://zyedidia.github.io/eget.sh | sh && popd eget casey/just --to="$XDG_BIN_HOME" If uploading wheels, gh: eget cli/cli --asset=.tar.gz --to="$XDG_BIN_HOME" gh auth login Run the docker container: just docker-<cuda_version> Optionally, test the environment: just build-dummy Build a single package: just build <package_name> <package_version> <python_version> <torch_version> Example: just docker-cu128 just build-dummy just build natten 0.21.1 3.12 2.9 On the host, fix file permissions: just fix-permissions 1. Upload wheels just upload "build/**/*.whl" 1. Create and locally host the package index just index-serve 1.

### README headings

- Cosmos Dependencies
- Setup
- Build Wheels
- Upload Wheels
- Bump Version
- Version Constraints
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 25,755 |
| Python | 11,877 |
| Dockerfile | 5,238 |
| Just | 3,394 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: cmake, ninja, numpy, packaging, pip, setuptools, wheel
- packages/apex/pyproject.toml (capture: captured) — dependency clues: cosmos-dependencies
- packages/cosmos-dummy/pyproject.toml (capture: captured) — dependency clues: cosmos-dependencies
- packages/decord/pyproject.toml (capture: captured) — dependency clues: cosmos-dependencies
- packages/flash-attn-3-nv/pyproject.toml (capture: captured) — dependency clues: cosmos-dependencies, psutil

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 13
- Last updated: 2026-09-07T01:48:08Z
- Last pushed: 2026-07-28T02:08:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/nvidia-cosmos/cosmos-dependencies)
- [README](https://github.com/nvidia-cosmos/cosmos-dependencies/blob/main/README.md)
- [Issues](https://github.com/nvidia-cosmos/cosmos-dependencies/issues)
- [Releases](https://github.com/nvidia-cosmos/cosmos-dependencies/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
