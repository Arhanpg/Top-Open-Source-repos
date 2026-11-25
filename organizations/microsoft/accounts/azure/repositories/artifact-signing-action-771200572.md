# Azure/artifact-signing-action

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/artifact-signing-action](https://github.com/Azure/artifact-signing-action)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/artifact-signing-action/blob/main/README.md)
- README blob SHA: e78dfa1a5407b6cbc0edf120a92d67581c982f1a
- README bytes captured: 20899
- README truncated at capture limit: False
- Repository ID: 771200572
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T07:00:44+00:00

### Short excerpt (up to 300 words)

> description: My signed content. Please review Common error This Action can only cache-dependencies: false

### README headings

- Artifact Signing
- Runner Requirements
- Example
- Usage
- Authentication
- App Registration
- The Azure Active Directory tenant (directory) ID.
- The client (application) ID of an App Registration in the tenant.
- A client secret that was generated for the App Registration.
- Azure Active Directory
- The username, also known as upn, of an Azure Active Directory user account.
- The password of the Azure Active Directory user account. Note this does not support accounts with MFA enabled.
- Exclude Credentials
- Exclude the "EnvironmentCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "WorkloadIdentity" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "ManagedIdentity" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "SharedTokenCacheCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "VisualStudioCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "VisualStudioCodeCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "AzureCliCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "AzurePowerShellCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "AzureDeveloperCliCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is false.
- Exclude the "InteractiveBrowserCredential" type from being considered when authenticating with "DefaultAzureCredential". The default value is true.
- Account Details
- The Artifact Signing Account endpoint. The URI value must have a URI that aligns to the region your Artifact Signing Account and Certificate Profile you are specifying were created in during the setup of these resources.
- The Artifact Signing Account name.
- The Certificate Profile name.
- File Specification
- Files List
- A comma or newline separated list of absolute paths to the files being signed. Can be combined with the files-folder and file-catalog inputs.

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: A description of the signed content.

> description: My signed content.

### Getting started and usage: Usage

> Please review Common error

### Technology and requirements: Runner Requirements

> This Action can only

### Limitations and security: A boolean value (true/false) that indicates if the dependencies for this action should be cached by GitHub or not. The default value is false because GitHub Actions caches are not a security boundary and these dependencies contain executable code. Only enable caching after ensuring that untrusted contributors cannot write cache entries readable by signing workflows, including through pull_request_target, workflow_run, or issue_comment workflows. When using self-hosted runners, caches from workflow runs are stored on GitHub-owned cloud storage. A customer-owned storage solution is only available with GitHub Enterprise Server. More info: https://docs.github.com/actions/using-workflows/caching-dependencies-to-speed-up-workflows

> cache-dependencies: false

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Unknown | Not captured |

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
- Stars at capture: 142
- Forks at capture: 26
- Last updated: 2026-11-22T11:09:26Z
- Last pushed: 2026-11-16T19:31:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/artifact-signing-action)
- [README](https://github.com/Azure/artifact-signing-action/blob/main/README.md)
- [Issues](https://github.com/Azure/artifact-signing-action/issues)
- [Releases](https://github.com/Azure/artifact-signing-action/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
