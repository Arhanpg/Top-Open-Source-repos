# GoogleCloudPlatform/healthcare-api-dicomweb-cli

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/healthcare-api-dicomweb-cli](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli/blob/master/README.md)
- README blob SHA: 8994361b9841a918be6879ff9247796d90f81a59
- README bytes captured: 6138
- README truncated at capture limit: False
- Repository ID: 207584723
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A command line tool for interacting with a DICOMweb server

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:44:31+00:00

### Short excerpt (up to 300 words)

> **search** python (3.5+) pip

### README headings

- DICOMweb command line tool
- Requirements
- Installation
- Using GitHub:
- Interface
- dcmweb [-m] \<host> \<store|retrieve|search|delete> [parameters]
- Examples
- will return json list of instances in dicomstore with date==1994.10.13
- will return list of studies without any filter
- will parse StudyUIDs/PatientNames for each study in search results
- will parse StudyUIDs for each study in search results
- and count lines of jq output by wc
- will upload list of files generated from current folder by shell
- will upload list of files generated from current folder by python
- will upload list of files generated from current folder recursively by python
- will upload list of files in parallel
- will download all instances from dicomstore into current folder
- will download all instances from dicomstore into current folder in parallel
- will download all instances from dicomstore into ./data folder
- will download all instances from dicomstore into ./data folder as png images,
- in instance is multiframe, frames will be saved as separate files
- will download all instances from study 1 into ./data folder
- will delete study 1
- Build
- Run tests
- Developing
- Running on machine with Python2
- Using pip local install
- Using virtualenv
- Apache License 2.0

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Examples

> **search**

### Technology and requirements: Requirements

> python (3.5+) pip

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 55,650 |
| Shell | 4,486 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: fire, google.auth, httpretty, hurry.filesize, pytest, pytest-check, requests, validators
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 42
- Forks at capture: 7
- Last updated: 2026-08-13T06:09:56Z
- Last pushed: 2025-06-09T21:33:28Z
- Topics: dicom, dicomweb, google-cloud, google-cloud-healthcare-api

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli)
- [README](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli/issues)
- [Releases](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
