# google/docker-explorer

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/docker-explorer](https://github.com/google/docker-explorer)
- Default branch: main
- README: [Open upstream README](https://github.com/google/docker-explorer/blob/main/README.md)
- README blob SHA: 4d8a5de08ee093a4f6f701bac7b97e923d9ef12e
- README bytes captured: 7596
- README truncated at capture limit: False
- Repository ID: 133632679
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A tool to help forensicate offline docker acquisitions

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T03:25:42+00:00

### Short excerpt (up to 300 words)

> When analyzing a system For the forensicator, this

### README headings

- Docker Explorer
- Overview
- Installation
- PPA
- PyPI
- Source
- Usage
- List the running containers
- docker ps
- de.py -r /mnt/root/var/lib/docker list running_containers
- Mount the container's filesystem:
- find ID of your running container:
- create image (snapshot) from container filesystem
- explore this filesystem using bash (for example)
- de.py -r /tmp/ mount 7b02fb3e8a665a63e32b909af5babb7d6ba0b64e10003b2d9534c7d5f2af8966 /tmp
- apt install aufs-tools
- de.py -r /tmp/ mount 7b02fb3e8a665a63e32b909af5babb7d6ba0b64e10003b2d9534c7d5f2af8966 /tmp/test
- Show a container's image history
- docker history 7968321274dc6b6171697c33df7815310468e694ac5be0ec03ff053bb135e768
- de.py -r /mnt/root/var/lib/docker history 7b02fb3e8a665a63e32b909af5babb7d6ba0b64e10003b2d9534c7d5f2af8966
- Troubleshooting
- Maintainer notes
- Gift PPA push
- Upload to PyPi

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> When analyzing a system

### Getting started and usage: Usage

> For the forensicator, this

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 124,389 |
| Shell | 2,890 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 553
- Forks at capture: 45
- Last updated: 2026-11-19T20:57:01Z
- Last pushed: 2024-10-04T07:44:31Z
- Topics: docker, forensics

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/docker-explorer)
- [README](https://github.com/google/docker-explorer/blob/main/README.md)
- [Issues](https://github.com/google/docker-explorer/issues)
- [Releases](https://github.com/google/docker-explorer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
