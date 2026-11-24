# siemens/continuous-clearing

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/continuous-clearing](https://github.com/siemens/continuous-clearing)
- Default branch: main
- README: [Open upstream README](https://github.com/siemens/continuous-clearing/blob/main/README.md)
- README blob SHA: fb26f1ac80943d5dc0d437244bd4120889317ec5
- Repository ID: 599993480
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Continuous Clearing Tool scans and collects third-party open-source components used in projects based on NPM, NuGet, Debian, Maven, Python, Conan, Alpine, and Cargo. It then uploads the collected data to SW360 and FOSSology for license clearing, using the respective project ID provided.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:59+00:00

### Short excerpt (up to 100 words)

> The Continuous Clearing Tool scans and collects the 3rd party OSS components used in a NPM/NuGet/Maven/Python/Debian and uploads it to SW360 and Fossology by accepting respective project ID for license clearing. The tool helps the developer/project manager to enable the clearing process faster by reducing the manual effort of creating SW360 and FOSSology workflows. To secure overall DevOps supply chain, we need to ensure that the coding is secure and other mandatory security aspects is integrated in Software development lifecycle from beginning to end. To ensure such practises are in place, we need to provide software bill of material (

### README headings

- Introduction
- Continuous Clearing Tool for SBOM :
- Package Installation
- Use container image
- Use Binary
- Development
- Prerequisite
- Building via .NET SDK
- Creating Docker image
- Contribute
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 3,888,787 |
| PowerShell | 3,752 |
| Dockerfile | 2,151 |
| Batchfile | 1,184 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- src/ContinuousClearingTool.sln (capture: captured)
- DemoProject/NPMProject/package.json (capture: captured) — dependency clues: charts, gettext, requirejs
- src/SIT.APICommunications.UTest/SIT.APICommunications.UTest.csproj (capture: captured)
- src/SIT.APICommunications/SIT.APICommunications.csproj (capture: captured)
- src/SIT.Common.UTests/SIT.Common.UTest.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 35
- Forks at capture: 15
- Last updated: 2026-11-16T01:50:19Z
- Last pushed: 2026-11-23T16:10:11Z
- Topics: alpine, conan, container, cyclonedx, docker, license-clearing, maven, npm, nuget, nuget-package, python, sbom

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/continuous-clearing)
- [README](https://github.com/siemens/continuous-clearing/blob/main/README.md)
- [Issues](https://github.com/siemens/continuous-clearing/issues)
- [Releases](https://github.com/siemens/continuous-clearing/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
