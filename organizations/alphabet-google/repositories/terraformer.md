# Terraformer — Infrastructure-to-Code Import CLI

- Company association: Alphabet / Google
- Upstream GitHub account: [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Repository: [GoogleCloudPlatform/terraformer](https://github.com/GoogleCloudPlatform/terraformer)
- Default branch: `master`
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/terraformer/blob/master/README.md)
- Review status: README inspected and summarized
- README blob SHA: `adab1177e655a647ae262fa4ffd0fbd99d453c63`
- Account relationship: The repository is hosted under the separately inventoried GoogleCloudPlatform account, which Google Cloud documentation links for its cloud samples.

## Project overview

A Go command-line tool that generates Terraform configuration and state files from existing cloud and infrastructure resources (reverse Terraform), allowing teams to bring already-deployed infrastructure into an infrastructure-as-code workflow.

## Features and capabilities documented by the README

- Generates Terraform HCL or JSON configuration and Terraform state from resources discovered in provider APIs.
- Supports selecting providers, projects, regions and resource types, with include/exclude and identifier/attribute filters.
- Can write local state or upload remote state to a Google Cloud Storage bucket.
- Connects related resources using Terraform remote-state references and supports configurable output folder structures.
- Includes a plan step that generates a plan file for review and modification before import.
- Documents providers for major clouds, Kubernetes, networking, monitoring, identity and other infrastructure services.

## Technology stack

Go; Terraform provider plugins; Terraform state and HCL/JSON; provider APIs for Google Cloud, AWS, Azure and additional services. The README describes package-manager, release-binary and source-build installation paths.

## Getting started

The README describes installing Terraformer and the matching Terraform provider plugin, initializing provider plugins with terraform init, then running a provider-specific plan/import command. Resource selection and filters should be reviewed before applying imported configuration to a working Terraform project.

## Lifecycle, compatibility and operational considerations

**Lifecycle warning:** GitHub marks this repository archived, and the README says it was deprecated and archived on 16 March 2026. It is read-only and receives no further updates, security patches or support. The README also states it is not an official Google product. Document it for historical/reference use only; do not make it a new production dependency without an independently supported migration plan.

## Evaluation guidance

Check the exact upstream release/branch, environment prerequisites, licence and security guidance before adopting the project. For archived or superseded repositories, follow the stated successor path. This dossier summarizes the inspected README and repository metadata; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/GoogleCloudPlatform/terraformer)
- [README](https://github.com/GoogleCloudPlatform/terraformer/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/terraformer/issues)
- [Releases](https://github.com/GoogleCloudPlatform/terraformer/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Lifecycle statements are cross-checked against the current repository metadata where noted.
