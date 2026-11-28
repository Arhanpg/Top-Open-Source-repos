# microsoft/AzureFilesFUSE

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/AzureFilesFUSE](https://github.com/microsoft/AzureFilesFUSE)
- Default branch: master
- README: [Open upstream README](https://github.com/microsoft/AzureFilesFUSE/blob/master/README.md)
- README blob SHA: 92a95651da867b1288fb81e500782c318498cd0e
- README bytes captured: 3889
- README truncated at capture limit: False
- Repository ID: 99595747
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

I wanted to be able to use Shared Access Signature (SAS) Tokens for connecting to file shares. Microsoft Azure Files provides CIFS/SMB mounting but, unfortunately, only mounting via Account Key is supported.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:00:06+00:00

### Short excerpt (up to 300 words)

> I wanted to be sudo -H -u username The system needs Python

### README headings

- Azure Files FUSE Driver
- Enables using SAS Tokens for mounting Azure Files shares
- Motivation
- But why would I care about mounting via SAS instead of Account Primary/Secondary key?
- Using Azure Files FUSE Driver
- Quick Setup (Assumes Ubuntu 16.04 LTS or similar)
- System Requirements
- Ubuntu 16.04 LTS
- RHEL 6.3
- Python Dependencies
- Packages needed to run
- Packages needed to develop
- Example Usage
- Additional Notes
- Running Tests

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Motivation

> I wanted to be

### Getting started and usage: Example Usage

> sudo -H -u username

### Technology and requirements: System Requirements

> The system needs Python

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 49,126 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: azure, fusepy, ptvsd, python-dateutil, requests, vcrpy

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 19
- Forks at capture: 13
- Last updated: 2026-10-03T21:09:06Z
- Last pushed: 2023-08-31T11:00:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/AzureFilesFUSE)
- [README](https://github.com/microsoft/AzureFilesFUSE/blob/master/README.md)
- [Issues](https://github.com/microsoft/AzureFilesFUSE/issues)
- [Releases](https://github.com/microsoft/AzureFilesFUSE/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
