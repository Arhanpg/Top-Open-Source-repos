# microsoft/AADConnectConfigDocumenter

- Company: Microsoft
- Account: microsoft
- Repository: https://github.com/microsoft/AADConnectConfigDocumenter
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:49:09+00:00

## Project purpose

AAD Connect configuration documenter is a tool to generate documentation of an Azure AD Connect installation. Currently, the documentation is only limited to the Azure AD Connect sync configuration.

## Why this project is used

AAD Connect configuration documenter is a tool to generate documentation of an AAD Connect installation.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C#, CSS, JavaScript, PowerShell, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/AzureADConnectSyncDocumenter/ActiveDirectoryConnectorDocumenter.cs, src/AzureADConnectSyncDocumenter/AzureActiveDirectoryConnectorDocumenter.cs, src/AzureADConnectSyncDocumenter/AzureADConnectSyncDocumenter.cs, src/AzureADConnectSyncDocumenter/DocumenterResources.Designer.cs

## Setup and usage

- **How to use the tool** (if you want to generate report for the current server installation):: 1. Download the latest release AzureADConnectSyncDocumenter.zip from the releases tab under the Code tab tab, UNBLOCK the downloaded zip file and extract the zip file to an empty local folder on a machine which has .NET Framework 4.5 installed.
- **How to use the tool** (if you want to generate report for the current server installation):: * This will extract the Documenter application binaries along with the sample data files for "Contoso".
- **How to use the tool** (if you want to generate report for the current server installation):: * Make sure that the tool runs by double-clicking on the cmd file AzureADConnectSyncDocumenter.cmd.
- **How to use the tool** (if you want to generate report for the current server installation):: * Upon successful execution, the generated report for "Contoso" will be found in the Documenter "Report" folder.
- **How to use the tool** (if you want to generate report for the current server installation):: 2. Export the Server Configuration of your Azure AD Connect sync server (named "AADC-SERVER01" in the example below) by running Get-ADSyncServerConfiguration cmdlet defined in ADSync module shipped with Azure AD Connect as in the example below.
- **How to use the tool** (if you want to generate report for the current server installation):: Get-ADSyncServerConfiguration -Path "C:\Temp\AADC-SERVER01-06JUN2022"
- **How to use the tool** (if you want to generate report for the current server installation):: 3. Copy the configuration export files folder produced in the previous step ("AADC-SERVER01-06JUN2022") to the "Data" directory of the Documenter tool.
- **How to use the tool** (if you want to generate report for the current server installation):: 4. Open a command prompt and change directory to AzureADConnectSyncDocumenter which should have AzureADConnectSyncDocumenterCmd.exe executable of the tool. Run the tool as follows to generate the report

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/microsoft/AADConnectConfigDocumenter/blob/master/README.md
- README SHA: d7d2473468b3c54694f07bac03dbe2a12b85aef8
- Manifests: none
- Sampled source files: src/AzureADConnectSyncDocumenter/ActiveDirectoryConnectorDocumenter.cs, src/AzureADConnectSyncDocumenter/AzureActiveDirectoryConnectorDocumenter.cs, src/AzureADConnectSyncDocumenter/AzureADConnectSyncDocumenter.cs, src/AzureADConnectSyncDocumenter/DocumenterResources.Designer.cs
- Git tree state: captured
- Evidence fingerprint: 5952c4bea45be7287971356b5877a67b08fb3ab1f4774a7f987739fc9e1d3cb3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
