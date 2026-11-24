# SAP/cf-cli-java-plugin

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/cf-cli-java-plugin](https://github.com/SAP/cf-cli-java-plugin)
- Default branch: master
- README: [Open upstream README](https://github.com/SAP/cf-cli-java-plugin/blob/master/README.md)
- README blob SHA: 14b0894a036f2c7ae961d80d29d9608fdcd6820e
- README bytes captured: 32751
- README truncated at capture limit: False
- Repository ID: 84809110
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Cloud Foundry CLI Plugin to troubleshoot Java apps

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T04:34:19+00:00

### Short excerpt (up to 300 words)

> Make sure you have Most commands work out The --args parameter passes

### README headings

- Cloud Foundry Command Line Java plugin
- Installation
- Installation via CF Community Repository
- Manual Installation
- on Mac arm64 (Apple Silicon only)
- on Windows amd64
- on Linux amd64
- on Linux arm64
- Manual Installation of Snapshot Release
- on Mac arm64 (Apple Silicon only)
- on Windows amd64
- on Linux amd64
- on Linux arm64
- Common Tasks
- My CF app is not responding — find what it is stuck on
- My CF app is using too much CPU
- Downloads an HTML flamegraph to your current directory
- reproduce the slow operation or wait 30–60 s
- Downloads $APP_NAME-asprof-<random>.jfr — open in JDK Mission Control
- My CF app crashed with OutOfMemoryError — take a heap dump
- Downloads $APP_NAME-heapdump-<random>.hprof to current directory
- Open report.html → "Leak Suspects" and "Top Consumers" tabs
- Usage
- Prerequisites
- Container Requirements
- JRE-only containers
- SSH Access
- Examples
- Basic — plain .hprof saved locally.
- On JDK 17+ containers, transfer is always gzip-compressed automatically (faster on slow connections).

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation via CF Community Repository

> Make sure you have

### Technology and requirements: Container Requirements

> Most commands work out

### Limitations and security: Security Note on `--args`

> The --args parameter passes

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 253,237 |
| Go | 146,325 |
| Shell | 36,087 |
| Java | 7,572 |
| Makefile | 4,583 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: code.cloudfoundry.org/bytefmt, code.cloudfoundry.org/cli, code.cloudfoundry.org/jsonry, code.cloudfoundry.org/tlsconfig, github.com/SermoDigital/jose, github.com/blang/semver/v4, github.com/bmatcuk/doublestar, github.com/charlievieth/fs, github.com/cloudfoundry/bosh-cli, github.com/cloudfoundry/bosh-utils, github.com/cppforlife/go-patch, github.com/fatih/color, github.com/google/shlex, github.com/google/uuid, github.com/jessevdk/go-flags, github.com/kr/pretty, github.com/lithammer/fuzzysearch, github.com/lunixbochs/vtclean, github.com/mattn/go-colorable, github.com/mattn/go-isatty
- Makefile (capture: captured)
- test/pyproject.toml (capture: captured) — dependency clues: colorama, pytest, pytest-html, pytest-xdist, python-Levenshtein, pyyaml
- test/requirements.txt (capture: captured) — dependency clues: black, click, colorama, flake8, isort, pytest, pytest-html, pytest-xdist, python-Levenshtein, pyyaml, tabulate

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 24
- Forks at capture: 15
- Last updated: 2026-11-02T13:15:39Z
- Last pushed: 2026-11-02T13:18:09Z
- Topics: cloudfoundry, java, open-source, profile

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/cf-cli-java-plugin)
- [README](https://github.com/SAP/cf-cli-java-plugin/blob/master/README.md)
- [Issues](https://github.com/SAP/cf-cli-java-plugin/issues)
- [Releases](https://github.com/SAP/cf-cli-java-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
