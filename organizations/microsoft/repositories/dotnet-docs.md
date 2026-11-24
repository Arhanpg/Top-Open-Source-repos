# .NET Documentation Source

- Company association: Microsoft
- Upstream GitHub account: [dotnet](https://github.com/dotnet)
- Repository: [dotnet/docs](https://github.com/dotnet/docs)
- Default branch: `main`
- README: [Open upstream README](https://github.com/dotnet/docs/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: `f453b0a248035c488b9bf5be1fc57af677af4e2b`
- Account relationship: Microsoft's official contributor documentation links the MicrosoftDocs, dotnet and Azure accounts as separate documentation/product project locations. The repository remains hosted under its actual GitHub owner.

## Project overview

The conceptual documentation source repository for .NET. Its README explains that the .NET documentation site is assembled from multiple repositories and that product API reference and language-specification content may be maintained in separate source repositories.

## Features and capabilities documented by the README

- Contains conceptual .NET documentation, while the public site is assembled from dotnet/docs and related documentation repositories such as ASP.NET Core, .NET Desktop, .NET MAUI, Entity Framework and community-toolkit docs.
- Separates conceptual docs from generated API reference repositories, including .NET, MAUI, Android, Entity Framework and Roslyn API reference content.
- Points language specification readers to the C# language design and C# specification repositories.
- Uses GitHub issues and pull requests with contributor workflows, maintainer review and abandoned-PR handling.
- Lists CI workflows for Markdown linting, documentation verification, snippets/build validation, branch protection and monthly supported-version sweeps.
- Routes article feedback from the published Learn pages to the relevant source repository.

## Technology stack

Documentation and samples source; Markdown and code snippets; GitHub Actions for Markdown lint, docs verification and snippet/build checks; Microsoft Learn publishing pipeline. Related API references and language specifications are hosted in separate repositories.

## Getting started

Begin with the Microsoft Learn .NET contributor guide referenced by the README. Use the published article's documentation-issue control or the relevant issue template to route a report. For a contribution, work in a fork/topic branch and submit a pull request; follow the site-wide Microsoft Docs contributor guidance.

## Lifecycle, compatibility and operational considerations

This repository is conceptual documentation, not the .NET runtime, SDK or compiler source. The README specifically says API reference documentation is published from separate repositories and that some are pass-through/generated sources. Do not assume every folder in this repository is the source of the corresponding API reference.

## Evaluation guidance

Use the release-specific product documentation, contributor guidelines, licensing notices and security process before making changes or adopting packages. This dossier summarizes the inspected README and (where noted) contribution guidance; it is not a full code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/dotnet/docs)
- [README](https://github.com/dotnet/docs/blob/main/README.md)
- [Issues](https://github.com/dotnet/docs/issues)
- [Releases](https://github.com/dotnet/docs/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Documentation source, product code and SDK implementation are classified separately.
