# industrial-edge/LEdgeBuffer-getting-started

- Company: Siemens
- Account: industrial-edge
- Repository: https://github.com/industrial-edge/LEdgeBuffer-getting-started
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:50:31+00:00

## Project purpose

This document will take you through the basic steps and configuration of components required to set up a PLC program with the SIEMENS library "LEdgeBuffer" to record and send high frequency signals' data to an edge computing application using MQTT and Node-RED or SIEMENS Industrial Flow Creator.

## Why this project is used

The SIMATIC library "LEdgeBuffer" allows creating a local buffer in the PLC to sample high speed signals. This buffer and the recording job can be accessed and controled via OPC-UA.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: node-red-contrib-opcua, node-red-contrib-ui-led, node-red-dashboard
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: none

## Setup and usage

- Installation Guide: 1. Firstly, the user must import the PLC library into their PLC application. see this link: Library SIMATIC: S7-1500 – LEdgeBuffer
- Installation Guide: 2. A fork of this github repository must be created
- Installation Guide: 3. Open *Node-Red Editor* with browser (authenticate if necessary)
- Installation Guide: 4. Press button on top-right corner, and go to Projects-->New (or ctrl-alt-n)
- Installation Guide: 5. Choose **Clone Repository**, and input the Git repository URL of your fork
- Installation Guide: 6. Authenticate using preconfigured SSH keys or HTTPS access tokens
- Installation Guide: 7. After the succcessful clone, **restart** *Node-Red* internally (refreshing the webpage or restarting flows is not enough)
- Installation Guide: 8. Go back to *Node-Red Editor*, press button on top-right corner, and go to Projects-->Project settings-->Dependencies

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/industrial-edge/LEdgeBuffer-getting-started/blob/main/README.md
- README SHA: f322381d35627c7dc56c01bfa06957133f1fd18f
- Manifests: package.json
- Sampled source files: none
- Git tree state: captured
- Evidence fingerprint: c41ca3e872711f4e7a1334d601d8a8217635d6c02a8ed1bd2e2d6eddf6455927

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
