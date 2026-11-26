# mindsphere/mindconnect-mqtt

- Company: Siemens
- Account: mindsphere
- Repository: https://github.com/mindsphere/mindconnect-mqtt
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:18:30+00:00

## Project purpose

Sample python code for getting started to securely connect your MindConnect MQTT on-site devices in a scaleable manner to Insights Hub.

## Why this project is used

MindConnect MQTT - Example for getting started to securely connect your on-site devices in a saleable manner to Insights Hub. By cloning or downloading this repository, you accept the Development License Agreement, which can be found at https://documentation.mindsphere.io/MindSphere/license.html

## Core features

- Use MQTT certificates to connect to Insights Hub.: Use MQTT certificates to connect to Insights Hub.
  - Evidence: README.md#Features
- Define Asset Model and publish for model creation and instantiation.: Define Asset Model and publish for model creation and instantiation.
  - Evidence: README.md#Features
- Ingesting timeseries data, events and uploading files to Insights Hub.: Ingesting timeseries data, events and uploading files to Insights Hub.
  - Evidence: README.md#Features

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: PyJWT, PySimpleGUI, certifi, charset-normalizer, idna, oauthlib, paho-mqtt, requests, schedule, urllib3
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/config_parser.py, AssetModelPublisher.py, MindConnectClient.py

## Setup and usage

- Installation: Install latest Python version and install the dependencies using below command.
- Installation: run pip install -r requirements.txt
- Installation: Verify the valid certificates in the agent_cert folder and mqtt-config.json file is updated with the correct values.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/mindsphere/mindconnect-mqtt/blob/main/README.md
- README SHA: db9f7c75026c93d998152237e00fb4999c5f671c
- Manifests: requirements.txt
- Sampled source files: lib/config_parser.py, AssetModelPublisher.py, MindConnectClient.py
- Git tree state: captured
- Evidence fingerprint: b3240e3188aa5d31b87b60f982cfe4a07381c245040f7ffa66e676b5fe5a6334

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
