# Azure/AzureKusto

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/AzureKusto](https://github.com/Azure/AzureKusto)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/AzureKusto/blob/master/README.md)
- README blob SHA: 3dccbd63f90ed9ebd98280e9a355e5e3aa181bbc
- README bytes captured: 10539
- README truncated at capture limit: False
- Repository ID: 187983887
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

R interface to Azure Data Explorer, aka Kusto

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:55:19+00:00

### Short excerpt (up to 300 words)

> AzureKusto is available on

### README headings

- AzureKusto <img src="man/figures/logo.png" align="right" width=150 />
- Installation
- Example usage
- Kusto endpoint interface
- (New in 1.1.0) Some other ways to call this that also work:
- Samples <- kusto_database_endpoint(server="help", database="Samples")
- Samples <- kusto_database_endpoint(cluster="help", database="Samples")
- No app ID supplied; using KustoClient app
- Waiting for authentication in browser...
- Press Esc/Ctrl + C to abort
- VSCode WebView only supports showing local http content.
- Opening in external browser...
- Browsing https://login.microsoftonline.com/common/oauth2/v2.0/authorize...
- Authentication complete.
- State EventCount
- 1        ALABAMA       1315
- 2         ALASKA        257
- 3 AMERICAN SAMOA         16
- 4        ARIZONA        340
- 5       ARKANSAS       1028
- 6 ATLANTIC NORTH        188
- dplyr Interface
- <KQL> database('Samples').['StormEvents']
- | summarize ['EventCount'] = count() by ['State']
- | order by ['State'] asc
- # A tibble: 67 x 2
- State          EventCount
- <chr>               <dbl>
- 1 ALABAMA              1315
- 2 ALASKA                257

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> AzureKusto is available on

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| R | 186,301 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- AzureKusto.sln (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 19
- Forks at capture: 11
- Last updated: 2025-09-09T18:19:57Z
- Last pushed: 2025-09-09T18:19:53Z
- Topics: azure, azure-data-explorer, azure-sdk-r, big-data-analytics, kusto, r

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/AzureKusto)
- [README](https://github.com/Azure/AzureKusto/blob/master/README.md)
- [Issues](https://github.com/Azure/AzureKusto/issues)
- [Releases](https://github.com/Azure/AzureKusto/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
