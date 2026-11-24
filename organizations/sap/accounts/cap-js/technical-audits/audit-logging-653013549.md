# cap-js/audit-logging

- **Company:** SAP
- **Repository:** https://github.com/cap-js/audit-logging
- **Default branch:** main
- **Audit status:** manual_reviewed
- **Evidence confidence:** high

## Project purpose

A CDS plugin for SAP CAP applications that integrates with SAP Audit Log service and provides annotation-driven audit logging for personal-data-related changes.

## Why this project is used

CAP application developers can record auditable changes to annotated personal-data fields and route audit records to the console, a REST endpoint, SAP Audit Log service or a custom store.

## Core features

- **SAP Audit Log service integration:** integrates CAP applications with the SAP Audit Log service.
- **Annotation-driven personal-data logging:** uses CDS @PersonalData annotations to identify data subjects and personal or sensitive fields.
- **Configurable audit-log handlers:** package configuration declares console, REST v2 and SAP Audit Log service handler variants.
- **Outbox configuration:** the package's CDS configuration declares outbox enabled for the audit-log requirement.

Evidence: [README](https://github.com/cap-js/audit-logging/blob/main/README.md), [package.json](https://github.com/cap-js/audit-logging/blob/main/package.json).

## Technology stack

- **Languages:** JavaScript, CDS
- **Frameworks/libraries:** SAP Cloud Application Programming Model, @sap/cds
- **Dependencies:** @sap/cds peer dependency >=9; development dependencies include @cap-js/cds-test, @cap-js/sqlite, express and jest
- **Build/package tools:** npm, Jest, ESLint, Prettier
- **Runtime:** Node.js package ecosystem
- **Infrastructure:** SAP Audit Log service for the documented production integration
- **Storage:** README says an application-provided custom audit-log store is possible

## Architecture

A CDS plugin discovered and configured through cds.requires.audit-log. The package manifest declares handler variants and outbox configuration. Runtime internals were not exhaustively inspected.

## Setup and usage

- Install using npm add @cap-js/audit-logging.
- Annotate CDS entities and fields with documented @PersonalData semantics.
- The README demonstrates running an example using cds watch.

## Limitations and caveats

- The README describes its quick-start guide as incomplete and directs users to the full CAP data-privacy documentation.
- The README says the out-of-the-box production integration requires a paid SAP Audit Log service for customers; a custom store can also be provided.
- The inspected package manifest declares @sap/cds as a peer dependency but does not declare a Node.js engines range.

## Evidence and provenance

- [README](https://github.com/cap-js/audit-logging/blob/main/README.md)
- [package.json](https://github.com/cap-js/audit-logging/blob/main/package.json)

**Review boundary:** README and package.json checked; runtime implementation and tests were not exhaustively reviewed. No test suite was executed.
