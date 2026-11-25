# industrial-edge/Apache-Kafka-Connector

- Company: Siemens
- Account: industrial-edge
- Repository: https://github.com/industrial-edge/Apache-Kafka-Connector
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:52:11+00:00

## Project purpose

Connect Industrial Edge Device to Apache Kafka

## Why this project is used

The Apache Kafka Connector connects to the IE Databus and Apache Kafka.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: confluent-kafka, paho-mqtt
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/consumer/main.py, src/producer/main.py, src/consumer/globalconfig.py, src/consumer/kafka.py

## Setup and usage

- Installation: You can find the further information about the following steps in the docs
- Installation: - Upload application to Industrial Edge Management
- Installation: - Configure and install application to Industrial Edge Device
- Usage: Connect your Industrial Edge Device to a PLC as datasource over the network.
- Usage: Provide a Apache Kafka Broker (see Prerequisites) that is accessible for the Industrial Edge Device over the network
- Usage: Use e.g. Flow Creator to verify data exchange to and from Apache Kafka Broker.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/industrial-edge/Apache-Kafka-Connector/blob/main/README.md
- README SHA: 4f610d75ec74c9c6ddcd84f1d97b22a1f084039f
- Manifests: src/consumer/requirements.txt, src/producer/requirements.txt
- Sampled source files: src/consumer/main.py, src/producer/main.py, src/consumer/globalconfig.py, src/consumer/kafka.py
- Git tree state: captured
- Evidence fingerprint: 52deab61485837d4599291f8c9d5d8591c7b555241f28e90df63c7293ce00423

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
