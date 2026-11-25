# Azure/AzBulkSetBlobTier

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/AzBulkSetBlobTier](https://github.com/Azure/AzBulkSetBlobTier)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/AzBulkSetBlobTier/blob/main/README.md)
- README blob SHA: 8d6353b56a806d52b2f0c97ace87c206d5a5b758
- README bytes captured: 21301
- README truncated at capture limit: False
- Repository ID: 358026969
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sample Application to Call Set Blob Tier in a Bulk & Multithreaded Fashion

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:04:22+00:00

### Short excerpt (up to 300 words)

> page_type: sample name: AzBulkSetBlobTier az monitor app-insights component This sample requires the

### README headings

- AzBulkSetBlobTier
- Considerations
- Listing the files to be moved
- Cost of data retrieval
- PowerShell Option
- .NET Docker Container Option
- Prerequisites
- Build, Deploy & Run the sample
- Shared Variables used for all deployment steps
- the region you want to deploy to
- this should match the region the storage account is in if you already have a storage account
- the name of the resource group that you want to deploy the resources to
- the sample assumes everything is in the same resource group, your situation might differ
- the name of the storage account you want to rehydrate from/to
- the name of the container in the storage account you want to rehydrate from/to
- the name you want to use for your Azure Container Registry
- the name you want to use for your Application Insights Instance
- the name you want to use for the ACI instance
- Deploy the Infrastructure, Build the sample, and publish it to ACR
- Create the Resource Group
- Create Storage Account if you dont already have one
- If you already have one filled with your archived blobs, skip this step
- Create Container Registry
- Create Application Insights
- If you don't have the AI extension installed in your shell you will be prompted to install it when you run this command
- Package the sample into a docker container and publish it to ACR
- Here we are building with the published sample code from GitHub
- If you are changing the code alter this command to point to where you put your code
- Run the sample
- Request authentication information from container registry

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> page_type: sample name: AzBulkSetBlobTier

### Getting started and usage: If you don't have the AI extension installed in your shell you will be prompted to install it when you run this command

> az monitor app-insights component

### Technology and requirements: Prerequisites

> This sample requires the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 20,058 |
| Dockerfile | 454 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- AzBulkSetBlobTier.sln (capture: captured)
- AzBulkSetBlobTier/AzBulkSetBlobTier.csproj (capture: captured)
- AzBulkSetBlobTier/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 4
- Forks at capture: 8
- Last updated: 2026-06-11T21:34:09Z
- Last pushed: 2023-01-09T22:57:53Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/AzBulkSetBlobTier)
- [README](https://github.com/Azure/AzBulkSetBlobTier/blob/main/README.md)
- [Issues](https://github.com/Azure/AzBulkSetBlobTier/issues)
- [Releases](https://github.com/Azure/AzBulkSetBlobTier/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
