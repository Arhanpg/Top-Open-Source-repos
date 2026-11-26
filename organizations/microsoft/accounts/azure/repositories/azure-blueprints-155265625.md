# Azure/azure-blueprints

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-blueprints](https://github.com/Azure/azure-blueprints)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/azure-blueprints/blob/master/README.md)
- README blob SHA: 218e08a0956b28e34cad5fe91deff03211edfd18
- README bytes captured: 18260
- README truncated at capture limit: False
- Repository ID: 155265625
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A library of sample Blueprints that can be easily imported via API or PowerShell

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:20:35+00:00

### Short excerpt (up to 300 words)

> Version 2.0 Last edited: Push a sample blueprint This doc assumes you

### README headings

- Managing Blueprints as Code
- Table of Contents
- Next steps to operationalize blueprints
- Prerequisites
- How to use this guide
- Quickstart
- Get the blueprint we just created
- Publish version 1.0
- Get the version of the blueprint you want to assign, which we will pas to New-AzBlueprintAssignment
- Each resource group artifact in the blueprint will need a hashtable for the actual RG name and location
- all other (non-rg) parameters are listed in a single hashtable, with a key/value pair for each parameter
- All of the resource group artifact hashtables are themselves grouped into a parent hashtable
- the 'key' for each item in the table should match the RG placeholder name in the blueprint
- Assign the new blueprint to the specified subscription (Assignment updates should use Set-AzBlueprintAssignment
- Structure of blueprint artifacts
- Blueprint folder
- Functions
- Blueprint
- Resource Group properties
- Artifacts
- How Parameters work
- How blueprint parameters display during assignment in the Azure Portal
- Passing values between artifacts
- Sequencing the deployment of artifacts
- Push the Blueprint definition to Azure
- Next steps
- Contributing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> Version 2.0 Last edited:

### Getting started and usage: Quickstart

> Push a sample blueprint

### Technology and requirements: Prerequisites

> This doc assumes you

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| PowerShell | 7,313 |

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
- Stars at capture: 261
- Forks at capture: 151
- Last updated: 2026-10-05T12:32:45Z
- Last pushed: 2026-08-19T17:51:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-blueprints)
- [README](https://github.com/Azure/azure-blueprints/blob/master/README.md)
- [Issues](https://github.com/Azure/azure-blueprints/issues)
- [Releases](https://github.com/Azure/azure-blueprints/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
