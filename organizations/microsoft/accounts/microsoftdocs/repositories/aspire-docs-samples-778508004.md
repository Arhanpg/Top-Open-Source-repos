# MicrosoftDocs/aspire-docs-samples

- Company: Microsoft
- GitHub account: [https://github.com/MicrosoftDocs](https://github.com/MicrosoftDocs)
- Mapping status: official-project-linked
- Repository: [MicrosoftDocs/aspire-docs-samples](https://github.com/MicrosoftDocs/aspire-docs-samples)
- Default branch: main
- README: [Open upstream README](https://github.com/MicrosoftDocs/aspire-docs-samples/blob/main/README.md)
- README blob SHA: 936714c315f08961edcb255534c107fdfbd01c35
- Repository ID: 778508004
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Samples used in .NET Aspire documentation

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:33:38+00:00

### Short excerpt (up to 100 words)

> This repository contains sample projects referenced by the Aspire documentation. A sample Aspire application demonstrating Entity Framework Core migrations with a separate migration service. The solution consists of: - .NET 10 SDK - Docker Desktop (for the SQL Server container) - Aspire CLI aspire run The AppHost will: 1. Start a SQL Server container. 2. Run the **MigrationService** to apply migrations and seed data. 3. Start the **API** only after the migration service completes (`WaitForCompletion`). cd SupportTicketApi/SupportTicketApi.MigrationService dotnet ef migrations add <MigrationName> --startup-project . --project . This project welcomes contributions and suggestions. Most contributions require you to agree to a

### README headings

- Aspire docs samples
- SupportTicketApi
- Prerequisites
- Running the sample
- Adding a new migration
- Contributing
- Legal Notices

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 14,316 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- SupportTicketApi/SupportTicketApi.Api/SupportTicketApi.Api.csproj (capture: captured)
- SupportTicketApi/SupportTicketApi.AppHost/SupportTicketApi.AppHost.csproj (capture: captured)
- SupportTicketApi/SupportTicketApi.Data/SupportTicketApi.Data.csproj (capture: captured)
- SupportTicketApi/SupportTicketApi.MigrationService/SupportTicketApi.MigrationService.csproj (capture: captured)
- SupportTicketApi/SupportTicketApi.ServiceDefaults/SupportTicketApi.ServiceDefaults.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: CC-BY-4.0
- Stars at capture: 11
- Forks at capture: 9
- Last updated: 2026-08-14T12:31:25Z
- Last pushed: 2026-11-11T01:19:37Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/MicrosoftDocs/aspire-docs-samples)
- [README](https://github.com/MicrosoftDocs/aspire-docs-samples/blob/main/README.md)
- [Issues](https://github.com/MicrosoftDocs/aspire-docs-samples/issues)
- [Releases](https://github.com/MicrosoftDocs/aspire-docs-samples/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
