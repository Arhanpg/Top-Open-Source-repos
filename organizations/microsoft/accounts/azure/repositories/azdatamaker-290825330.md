# Azure/AzDataMaker

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/AzDataMaker](https://github.com/Azure/AzDataMaker)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/AzDataMaker/blob/master/README.md)
- README blob SHA: aeba6ce4f73e5f52022d93a76334338fed608121
- README bytes captured: 13568
- README truncated at capture limit: False
- Repository ID: 290825330
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

It is a sample .NET Core app that runs in a Linux Azure Container Instance that generates files and uploads them to Azure Blob Storage.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:25:58+00:00

### Short excerpt (up to 300 words)

> page_type: sample name: AzDataMaker

### README headings

- AzDataMaker
- Repository Content
- Deploying AzDataMaker
- login
- show the current subscriptions
- change the default subscription (if needed)
- the region you want to deploy to
- this should match the region the storage account is in if you already have a storage account
- the name of the resource group that you want to deploy the resources to
- the sample assumes everything is in the same resource group, your situation might differ
- the name of the storage account you want to load data to
- the name you want to use for your Azure Container Registry
- the name prefix you want to use for the ACI instance(s)
- the number of ACI instances you want to use
- Create the Resource Group
- Create Storage Account if you dont already have one
- Create Container Registry
- Package the sample into a docker container and publish it to ACR
- PICK ONE OPTION
- Here we are building with the published sample code directly from GitHub
- To build using a copy of the code you downloaded use this command
- You will need to be in the AzDataMaker directory for this to work
- Request authentication information from container registry
- Request authentication information from the storage account
- Find the number of currently running instances
- Get the storage account blob endpoint URI
- Create a user-assigned managed identity in the deployment resource group
- Grant the identity blob data access before the container starts
- If the storage account is in a different resource group, replace $RG below with that resource group name.
- Get the storage account blob endpoint URI

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> page_type: sample name: AzDataMaker

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 21,857 |
| Dockerfile | 492 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/AzDataMaker/AzDataMaker.sln (capture: captured)
- src/AzDataMaker/AzDataMaker/AzDataMaker.csproj (capture: captured)
- src/AzDataMaker/AzDataMaker/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1
- Forks at capture: 9
- Last updated: 2026-08-18T15:54:49Z
- Last pushed: 2026-08-18T15:46:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/AzDataMaker)
- [README](https://github.com/Azure/AzDataMaker/blob/master/README.md)
- [Issues](https://github.com/Azure/AzDataMaker/issues)
- [Releases](https://github.com/Azure/AzDataMaker/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
