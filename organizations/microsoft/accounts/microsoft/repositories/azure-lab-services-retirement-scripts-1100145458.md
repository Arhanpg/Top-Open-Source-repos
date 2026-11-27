# microsoft/Azure-Lab-Services-Retirement-Scripts

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/Azure-Lab-Services-Retirement-Scripts](https://github.com/microsoft/Azure-Lab-Services-Retirement-Scripts)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/Azure-Lab-Services-Retirement-Scripts/blob/main/README.md)
- README blob SHA: 4c8142ab41d2b0bacf10b746ec5a2173cc254bd5
- README bytes captured: 9140
- README truncated at capture limit: False
- Repository ID: 1100145458
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository provides a set of automation scripts to help Azure Lab Services customers efficiently prepare for and complete their service retirement workflows. The scripts are designed to streamline bulk cleanup, resource validation, and deprovisioning tasks, reducing manual effort and simplifying the overall offboarding process.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:28:31+00:00

### Short excerpt (up to 300 words)

> .\Get-AzLabServicesUsage.ps1 -DetailLevel 1 **Purpose**: Comprehensive reporting on All scripts require: PowerShell

### README headings

- Azure-Lab-Services-Retirement-Scripts
- Prerequisites
- Script Overview
- 1. Get-AzLabServicesUsage.ps1
- Basic usage overview
- Full detailed report
- Get data for further processing
- 2. Get-UnusedVMs.ps1
- Find VMs with less than 1 hour usage (default)
- Find VMs with less than 3 hours usage and save reports to specific folder
- 3. Get-HighlyUsedVMs.ps1
- Default threshold (40 hours)
- Custom threshold and output file
- 4. Get-Labs.ps1
- Default output file in current directory
- Custom output file
- 5. Get-AzLabServicesUsers.ps1
- Default output file in current directory
- Custom output file
- 6. Delete-Labs.ps1
- Delete labs listed in CSV with confirmation prompt
- Delete labs without confirmation (dangerous!)
- 7. Delete-AzLabServices.ps1
- Test run without making changes
- Delete with 5 concurrent jobs
- Custom output file
- 8. Resize-Labs.ps1
- Test run showing what would be resized
- Resize all labs (with confirmation)
- Resize specific lab without confirmation

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Basic usage overview

> .\Get-AzLabServicesUsage.ps1 -DetailLevel 1

### Getting started and usage: 1. Get-AzLabServicesUsage.ps1

> **Purpose**: Comprehensive reporting on

### Technology and requirements: Prerequisites

> All scripts require: PowerShell

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| PowerShell | 124,378 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 4
- Last updated: 2025-12-12T16:09:23Z
- Last pushed: 2025-12-12T16:09:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/Azure-Lab-Services-Retirement-Scripts)
- [README](https://github.com/microsoft/Azure-Lab-Services-Retirement-Scripts/blob/main/README.md)
- [Issues](https://github.com/microsoft/Azure-Lab-Services-Retirement-Scripts/issues)
- [Releases](https://github.com/microsoft/Azure-Lab-Services-Retirement-Scripts/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
