# SAP/business-partner-sample-app-s4hana-cloud

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/business-partner-sample-app-s4hana-cloud](https://github.com/SAP/business-partner-sample-app-s4hana-cloud)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/business-partner-sample-app-s4hana-cloud/blob/main/README.md)
- README blob SHA: 2787c2199a7fce2f1ee124ee0dac37cdbe87df20
- README bytes captured: 13921
- README truncated at capture limit: False
- Repository ID: 364516724
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

You can extend the functionality of your SAP S/4HANA Cloud system to manage your business partners. To do that, you can use the Sample Extension Application for Managing Business Partners, deploy it in a subaccount in SAP Business Technology Platform (SAP BTP) but have it fully integrated in your SAP S/4HANA Cloud system

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T04:33:14+00:00

### Short excerpt (up to 300 words)

> You can extend the There are several components

### README headings

- Business Partner Sample Application for SAP S/4HANA Cloud
- Introduction
- Prerequisites
- Process
- 1. Connect the SAP S/4HANA Cloud system you want to extend with the corresponding global account in SAP BTP
- 2. Trigger the Registration in the SAP S/4HANA Cloud Tenant
- 3. Make the SAP S/4HANA Cloud system accessible in the subaccount in SAP BTP in which you want to build your extension application.
- 4. Configure the Entitlements to the Cloud Foundry Runtime
- 5. Clone the Business Partner Sample Application for SAP S/4HANA Cloud from GitHub
- 6. Create a Destination Service Instance
- Cockpit
- CLI
- 7. Create an SAP S/4HANA Cloud Extensibility Service Instance to Consume the SAP S/4HANA Cloud APIs
- Cockpit
- CLI
- 8. Create a service instance of the Authorization and Trust Management (XSUAA) service
- Cockpit
- CLI
- 9. Build and Deploy the Application
- 10. Test the Application
- Licensing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> You can extend the

### Technology and requirements: Prerequisites

> There are several components

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 14,167 |
| JavaScript | 7,145 |
| HTML | 3,193 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: business-partner-parent, sdk-bom, spring-boot-starter-parent, spring-boot-starter-web, xsuaa-spring-boot-starter
- approuter/package.json (capture: captured) — dependency clues: @sap/approuter
- business-partner-app/pom.xml (capture: captured) — dependency clues: business-partner-app, business-partner-parent, s4hana-all, scp-cf, spring-boot-maven-plugin, spring-boot-starter-web

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 7
- Last updated: 2026-06-03T12:38:17Z
- Last pushed: 2026-06-03T12:38:11Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/business-partner-sample-app-s4hana-cloud)
- [README](https://github.com/SAP/business-partner-sample-app-s4hana-cloud/blob/main/README.md)
- [Issues](https://github.com/SAP/business-partner-sample-app-s4hana-cloud/issues)
- [Releases](https://github.com/SAP/business-partner-sample-app-s4hana-cloud/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
