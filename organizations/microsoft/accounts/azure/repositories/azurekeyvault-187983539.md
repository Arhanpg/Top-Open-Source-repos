# Azure/AzureKeyVault

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/AzureKeyVault](https://github.com/Azure/AzureKeyVault)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/AzureKeyVault/blob/master/README.md)
- README blob SHA: c71b7a974f477ff0d17fd529d8aaf36415758cb0
- README bytes captured: 4515
- README truncated at capture limit: False
- Repository ID: 187983539
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

R interface to Azure Key Vault

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:54:19+00:00

### Short excerpt (up to 300 words)

> Cryptographic keys: Supports multiple key types and algorithms, and enables the use of Hardware Security Modules (HSM) for high value keys. Secrets: Provides secure storage

### README headings

- AzureKeyVault <img src="man/figures/logo.png" align="right" width=150 />
- Resource Manager interface
- create a key vault
- list current principals (by default includes logged-in user)
- get details for a service principal
- give the service principal read-only access to vault keys and secrets
- Client interface
- can also be done from the ARM resource object
- create a new secret
- printing the value won't display it; this is to help guard against shoulder-surfing
- create a new RSA key with 4096-bit key size
- encrypting and decrypting
- create a new self-signed certificate (will also create an associated key and secret)
- import a certificate from a PFX file
- OAuth authentication using a cert in Key Vault (requires AzureAuth >= 1.0.2)
- export the certificate as a PEM file
- (you should only export a cert if absolutely necessary)
- add a managed storage account
- Creating a new SAS definition

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: AzureKeyVault <img src="man/figures/logo.png" align="right" width=150 />

> Cryptographic keys: Supports multiple key types and algorithms, and enables the use of Hardware Security Modules (HSM) for high value keys. Secrets: Provides secure storage

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| R | 117,892 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 18
- Forks at capture: 13
- Last updated: 2026-06-02T15:59:33Z
- Last pushed: 2025-04-12T08:33:24Z
- Topics: azure, azure-key-vault, azure-sdk-r, r, security

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/AzureKeyVault)
- [README](https://github.com/Azure/AzureKeyVault/blob/master/README.md)
- [Issues](https://github.com/Azure/AzureKeyVault/issues)
- [Releases](https://github.com/Azure/AzureKeyVault/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
