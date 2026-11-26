# MicrosoftDocs/Azure-Sphere-Developer-Learning-Path

- Company: Microsoft
- Account: MicrosoftDocs
- Repository: https://github.com/MicrosoftDocs/Azure-Sphere-Developer-Learning-Path
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:08:22+00:00

## Project purpose

**Follow** me on **Twitter** @dglover

## Why this project is used

The Azure Sphere Developer Learning Path is a set of libraries and a series of labs designed to ease you into the world of Azure Sphere development with the Avnet and Seeed Studio Azure Sphere development boards. The labs cover Azure Sphere security concepts, secure bi-directional cloud communications, how to integrate Real-Time applications with the Azure, and over the air updates, with more labs to follow.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C, Assembly, CMake, Makefile, PowerShell, Python, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: Lab_1_Visual_Studio_and_Azure_Sphere/main.c, Lab_2_Send_Telemetry_to_Azure_IoT/main.c, Lab_3_Device_Twins/main.c, Lab_4_Direct_Methods/main.c

## Setup and usage

No setup information established.

## Limitations and caveats

- Why you should care about IoT security: Almost a day doesn't go by without some newsworthy IoT security attack happening, and those are just the ones that make the news cycle. IoT security is fundamental and at the same time often absent from many conversations in the rush to get products to market.
- Why you should care about IoT security: The Seven Properties of Highly Secure Devices is highly recommended to help you understand what is required to mitigate exposure to IoT security issues. This IoT Security whitepaper draws from industry and Microsoft experience.
- Why you should care about IoT security: Here is one of the most unconventional: a fish tank. Not just an ordinary fish tank, mind you, but a high-tech one that featured Internet connectivity. That connection allowed the tank to be remotely monitored, automatically adjust temperature and salinity, and automate feedings.
- Why you should care about IoT security: It also allowed hackers to swipe 10 gigabytes of data from the North American casino that just installed it, according to a report from the threat intelligence experts at Darktrace.
- Why you should care about IoT security: Criminals Hacked A Fish Tank To Steal Data From A Casino
- Security: * Applications on Azure Sphere are locked down by default and you must grant capabilities to the application. This is key to Azure Sphere security and is also known as the Principle of least privilege.
- Security: * Capabilities, such as access to GPIO pins and network endpoint must be granted to both High Level and Real Time applications. This defends against application bugs and malicious code attacks.
- Security: * The chip includes a Memory Management Unit (MMU) to provide protected memory address spaces.

## Evidence and provenance

- README: https://github.com/MicrosoftDocs/Azure-Sphere-Developer-Learning-Path/blob/master/README.md
- README SHA: cdfae94f43bd5ea667ac7151329aef88d6b2a44e
- Manifests: Lab_1_Visual_Studio_and_Azure_Sphere/CMakeLists.txt, Lab_2_Send_Telemetry_to_Azure_IoT/CMakeLists.txt, Lab_3_Device_Twins/CMakeLists.txt, Lab_4_Direct_Methods/CMakeLists.txt, Lab_5_FreeRTOS_Environment/CMakeLists.txt, Lab_6_AzureRTOS_Environment/CMakeLists.txt
- Sampled source files: Lab_1_Visual_Studio_and_Azure_Sphere/main.c, Lab_2_Send_Telemetry_to_Azure_IoT/main.c, Lab_3_Device_Twins/main.c, Lab_4_Direct_Methods/main.c
- Git tree state: captured
- Evidence fingerprint: 1f2a0012cd21747c488aba065e0e63613284abe898dc7ad599a8e977ed4b5525

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
