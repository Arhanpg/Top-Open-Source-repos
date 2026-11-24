# Azure SDK for .NET

- Company association: Microsoft
- Upstream GitHub account: [Azure](https://github.com/Azure)
- Repository: [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net)
- Default branch: `main`
- README: [Open upstream README](https://github.com/Azure/azure-sdk-for-net/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: `ceb3627ab543aad5072d0206cd2d05128c8e6aba`
- Account relationship: Microsoft's official contributor documentation links the MicrosoftDocs, dotnet and Azure accounts as separate documentation/product project locations. The repository remains hosted under its actual GitHub owner.

## Project overview

The active development repository for Azure SDK client and management libraries for .NET. Its README groups packages by Azure service and distinguishes the newer Azure-prefixed client libraries from legacy package generations and management SDKs.

## Features and capabilities documented by the README

- Organizes service-specific libraries under the sdk directory, with each library's README providing service-level usage details.
- Provides client libraries for application code that interacts with Azure services at runtime.
- Provides management libraries for provisioning and managing Azure resources.
- Separates new Azure-prefixed packages that follow Azure SDK design guidelines from previous Microsoft.Azure package generations.
- Documents shared client-library capabilities such as HTTP retries, logging, transport protocols and authentication through Azure.Core.
- Provides build and test instructions for all services or a single service scope.
- Documents central package version management using eng/centralpackagemanagement/Directory.Packages.props.
- Provides security-reporting guidance and opt-out controls for telemetry.

## Technology stack

C#/.NET; .NET SDK; NuGet; Visual Studio; MSBuild/dotnet build; Azure.Core and Azure Identity; service-specific client and resource-management libraries; central NuGet package version management.

## Getting started

The README recommends using stable, non-preview packages where production readiness is required. For a package, inspect the service-specific README under sdk. The contribution guide lists Visual Studio 2026, .NET 10.0.401 SDK or a higher 10.0.* version, Git, and PowerShell 7 for some workflows. It documents dotnet build build.proj at repo root and scoped builds such as /p:Scope=servicebus.

## Lifecycle, compatibility and operational considerations

**Preview versus stable:** the README separates new client/management releases from previous stable versions and explicitly recommends stable, non-preview libraries when production readiness is required. **Telemetry:** collection is on by default; the README documents per-client IsTelemetryEnabled=false and global AZURE_TELEMETRY_DISABLED=true. **Security:** it directs vulnerability reports to Microsoft's Security Response Center rather than public issues.

## Evaluation guidance

Use the release-specific product documentation, contributor guidelines, licensing notices and security process before making changes or adopting packages. This dossier summarizes the inspected README and (where noted) contribution guidance; it is not a full code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/Azure/azure-sdk-for-net)
- [README](https://github.com/Azure/azure-sdk-for-net/blob/main/README.md)
- [Issues](https://github.com/Azure/azure-sdk-for-net/issues)
- [Releases](https://github.com/Azure/azure-sdk-for-net/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Documentation source, product code and SDK implementation are classified separately.
