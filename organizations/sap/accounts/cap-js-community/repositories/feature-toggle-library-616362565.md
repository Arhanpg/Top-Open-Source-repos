# cap-js-community/feature-toggle-library

- Company: SAP
- GitHub account: [https://github.com/cap-js-community](https://github.com/cap-js-community)
- Mapping status: official-directory-listed
- Repository: [cap-js-community/feature-toggle-library](https://github.com/cap-js-community/feature-toggle-library)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js-community/feature-toggle-library/blob/main/README.md)
- README blob SHA: e310afdbba6986e5453f8c5a9ade206910ac5836
- Repository ID: 616362565
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SAP BTP feature toggle library enables Node.js applications using the SAP Cloud Application Programming Model to maintain live-updatable feature toggles via Redis.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:36:23+00:00

### Short excerpt (up to 100 words)

> SAP BTP feature toggle library enables Node.js applications using the SAP Cloud Application Programming Model to maintain live-updatable feature toggles via Redis. - Set up project with `@sap/cds`. - Install library: npm install --save @cap-js-community/feature-toggle-library - For CAP Feature Toggles everything is configured automatically. - The library acts as a CDS-Plugin and registers a `FeatureService`, which can be used to check and update toggles. - For details see Example CAP Server. - Same as previous section. - Write `toggles.yaml` configuration file: /check/priority: type: number fallbackValue: 0 validations: - scopes: [user, tenant] - regex: '^\d+$' - Add configuration path to `package.json`:

### README headings

- SAP BTP Feature Toggle Library
- Getting Started (CAP Feature Toggles)
- Getting Started (Custom Configuration)
- Features
- Peers
- Documentation
- Support, Feedback, Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 306,077 |
| CAP CDS | 927 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/cds-test, @eslint/js, @redis/client, @sap/cds, @sap/cds-mtxs, eslint, eslint-config-prettier, eslint-plugin-jest, globals, jest, jsdoc, prettier, verror, yaml
- docs/Gemfile (capture: captured)
- example-cap-server/package.json (capture: captured) — dependency clues: @cap-js-community/feature-toggle-library, @sap/cds, @sap/cds-mtxs, express
- test-cap-server/package.json (capture: captured) — dependency clues: @cap-js-community/feature-toggle-library, @sap/cds-mtxs

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 4
- Last updated: 2026-11-11T15:23:39Z
- Last pushed: 2026-11-11T14:23:33Z
- Topics: cloud-foundry, feature-flags, feature-toggles, plugin, redis, sap-btp, sap-cap

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js-community/feature-toggle-library)
- [README](https://github.com/cap-js-community/feature-toggle-library/blob/main/README.md)
- [Issues](https://github.com/cap-js-community/feature-toggle-library/issues)
- [Releases](https://github.com/cap-js-community/feature-toggle-library/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
