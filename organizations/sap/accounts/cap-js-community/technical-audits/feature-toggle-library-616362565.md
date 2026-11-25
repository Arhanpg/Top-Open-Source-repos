# cap-js-community/feature-toggle-library

- Company: SAP
- Account: cap-js-community
- Repository: https://github.com/cap-js-community/feature-toggle-library
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:26:02+00:00

## Project purpose

SAP BTP feature toggle library enables Node.js applications using the SAP Cloud Application Programming Model to maintain live-updatable feature toggles via Redis.

## Why this project is used

SAP BTP feature toggle library enables Node.js applications using the SAP Cloud Application Programming Model to maintain live-updatable feature toggles via Redis.

## Core features

- Set up project with @sap/cds.: Set up project with @sap/cds.
  - Evidence: README.md#Getting Started (CAP Feature Toggles)
- Install library:: Install library:
  - Evidence: README.md#Getting Started (CAP Feature Toggles)
- For CAP Feature Toggles everything is configured automatically.: For CAP Feature Toggles everything is configured automatically.
  - Evidence: README.md#Getting Started (CAP Feature Toggles)
- The library acts as a CDS-Plugin and registers a FeatureService, which can be used to check and update toggles.: The library acts as a CDS-Plugin and registers a FeatureService, which can be used to check and update toggles.
  - Evidence: README.md#Getting Started (CAP Feature Toggles)
- For details see Example CAP Server.: For details see Example CAP Server.
  - Evidence: README.md#Getting Started (CAP Feature Toggles)
- Maintain feature toggle states consistently across multiple app instances.: Maintain feature toggle states consistently across multiple app instances.
  - Evidence: README.md#Features
- Feature toggle changes are published from Redis to subscribed app instances with publish/subscribe pattern PUB/SUB.: Feature toggle changes are published from Redis to subscribed app instances with publish/subscribe pattern PUB/SUB.
  - Evidence: README.md#Features
- Horizontal app scaling is supported and new app instances will start with the correct state, or fallback values, if they cannot connect to Redis.: Horizontal app scaling is supported and new app instances will start with the correct state, or fallback values, if they cannot connect to Redis.
  - Evidence: README.md#Features
- Feature toggle values can be changed specifically for accessors with certain scopes, e.g., for specific tenants, users,...: Feature toggle values can be changed specifically for accessors with certain scopes, e.g., for specific tenants, users,...
  - Evidence: README.md#Features
- Users can register change handler callbacks for specific toggles.: Users can register change handler callbacks for specific toggles.
  - Evidence: README.md#Features
- Users can register custom input validation callbacks for specific toggles.: Users can register custom input validation callbacks for specific toggles.
  - Evidence: README.md#Features
- Works as a CDS-Plugin and provides a REST service to read and manipulate toggles.: Works as a CDS-Plugin and provides a REST service to read and manipulate toggles.
  - Evidence: README.md#Features

## Technology stack

- Languages: JavaScript, CAP CDS
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js-community/feature-toggle-library, @cap-js/cds-test, @eslint/js, @redis/client, @sap/cds, @sap/cds-mtxs, eslint, eslint-config-prettier, eslint-plugin-jest, express, globals, jest, jsdoc, prettier, verror, yaml
- Build/package tools: Bundler manifest, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/index.js, example-cap-server/srv/feature/index.js, example-cap-server/srv/server.js, src/feature-toggles.js

## Setup and usage

- Getting Started (CAP Feature Toggles): - Set up project with @sap/cds.
- Getting Started (CAP Feature Toggles): npm install --save @cap-js-community/feature-toggle-library
- Getting Started (CAP Feature Toggles): - For CAP Feature Toggles everything is configured automatically.
- Getting Started (CAP Feature Toggles): - The library acts as a CDS-Plugin and registers a FeatureService, which can be used to check and update toggles.
- Getting Started (CAP Feature Toggles): - For details see Example CAP Server.
- Getting Started (Custom Configuration): - Same as previous section.
- Getting Started (Custom Configuration): - Write toggles.yaml configuration file:

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/cap-js-community/feature-toggle-library/blob/main/README.md
- README SHA: e310afdbba6986e5453f8c5a9ade206910ac5836
- Manifests: package.json, docs/Gemfile, example-cap-server/package.json, test-cap-server/package.json
- Sampled source files: src/index.js, example-cap-server/srv/feature/index.js, example-cap-server/srv/server.js, src/feature-toggles.js
- Git tree state: captured
- Evidence fingerprint: eb4f2b7973abc44c8ef5130e2e1fd2b3648660d06b5f64494dadaad431f7752c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
