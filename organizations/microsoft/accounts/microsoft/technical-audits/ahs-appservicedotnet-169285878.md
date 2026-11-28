# microsoft/AHS-AppServiceDotNet

- Company: Microsoft
- Account: microsoft
- Repository: https://github.com/microsoft/AHS-AppServiceDotNet
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:11:12+00:00

## Project purpose

The **Azure App Service** is a service for hosting web applications, REST APIs and mobile backend. We can develop applications using .NET, .NET Core, Java, Ruby, Node.js, PHP or Python. The Applications will run and scale with ease on the Windows-based environments. For Linux-based environments, the web apps add the power of Microsoft Azure to the applications such as security, load balancing, auto scaling and automated management.

## Why this project is used

Code for SmartHotel 360 Registration app for the AHS

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, C#, PowerShell, ASP, CSS
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: SmartHotel.Registration.WCF/Data/Booking.cs, SmartHotel.Registration.WCF/Data/BookingsDbContext.cs, SmartHotel.Registration.WCF/Data/BookingsDbContextInitializer.cs, SmartHotel.Registration.WCF/Data/Generators/AddressGenerator.cs

## Setup and usage

- Exercise 1: Getting Started: 1. You will need **Visual Studio 2017 Community and/or Enterprise** (Snapshot Debugger).
- Exercise 1: Getting Started: 2. Open the solution called **SmartHotel360.Registration**.
- Exercise 1: Getting Started: >**Talk Track**: In this demonstration, we will look at the example of SmartHotel360, a fictitious hospitality company planning to use the Microsoft Azure App Service to re-host its web application to Azure.

## Limitations and caveats

- Security and compliance: The Azure App Service is ISO, SOC and PCI compliant which is a requirement for App Modernization as it requires security and compliance. Create IP address restrictions, manage service identities, add custom domains and SSL for the apps. We can create restorable archive copies of our apps content, configuration and database.
- Security and compliance: 1. Click on the **Authentication / Authorization** option to setup identity provider or anonymous access.
- Security and compliance: >**Talk Track**: We can choose to authenticate users with the Azure Active Directory, or via other platforms such as Google, Facebook, Twitter and Microsoft.
- Security and compliance: 1. Click on the **Backups** option to configure the Snapshot and Backup configuration.
- Security and compliance: >**Talk Track**: Here we can take a snapshot of an OS or data disk VHD for backup or to troubleshoot VM issues. A snapshot is a full, read-only copy of a VHD. Here we can also backup and restore our data in Azure. Azure Backup replaces our existing on-premises or off-site backup solutions with a cloud-based solution which is reliable, secure and co
- Security and compliance: 1. Click on the **SSL settings** option to setup the certificates and TLS.
- Security and compliance: >**Talk Track**: Here we can configure the transport security layer (TLS), specify the certificates to be used when responding to requests to host a specific hostname over HTTPS and more.

## Evidence and provenance

- README: https://github.com/microsoft/AHS-AppServiceDotNet/blob/master/README.md
- README SHA: 090b46206df7fd10a35489420b423b9f9bbcb597
- Manifests: none
- Sampled source files: SmartHotel.Registration.WCF/Data/Booking.cs, SmartHotel.Registration.WCF/Data/BookingsDbContext.cs, SmartHotel.Registration.WCF/Data/BookingsDbContextInitializer.cs, SmartHotel.Registration.WCF/Data/Generators/AddressGenerator.cs
- Git tree state: captured
- Evidence fingerprint: 4270a75ad9800761532ca4fc788196c219553172d037502457c9376bebca0b73

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
