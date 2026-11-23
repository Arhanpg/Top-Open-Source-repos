# cap-js/cap-operator-plugin

- Company: SAP
- GitHub account: [https://github.com/cap-js](https://github.com/cap-js)
- Mapping status: official-directory-listed
- Repository: [cap-js/cap-operator-plugin](https://github.com/cap-js/cap-operator-plugin)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js/cap-operator-plugin/blob/main/README.md)
- README blob SHA: 19ae47ddb0ab03815d27dbdfe64b5de203e2c6f2
- Repository ID: 762314628
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The CAP Operator Plugin offers a simple method for generating CAP Operator resources, which are essential for deploying multi-tenant CAP Applications.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:35:39+00:00

### Short excerpt (up to 100 words)

> The CAP Operator Plugin offers a simple method for generating CAP Operator resources, which are essential for deploying multi-tenant CAP Applications. The CAP Operator plugin requires `@sap/cds-dk: ">=9"`. If you've installed @sap/cds-dk globally, ensure that the installed version is `9` or higher. To integrate the CAP Operator Plugin into your project, follow these steps: 1. Add the plugin package to your project as a dev dependency: npm add @cap-js/cap-operator-plugin -D 2. After installation, execute the following command to add the CAP Operator Helm chart to your project: cds add cap-operator This creates a `chart` folder in your directory with three

### README headings

- CAP Operator Plugin
- Before You Start
- Set Up the Plugin
- Configure Your Chart
- Deploy Your Application
- Converting to Configurable Templates Chart
- Example
- ❗Things to Note
- CAP Operator Skill
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 138,466 |
| Handlebars | 13,524 |
| Go Template | 7,584 |
| Go | 7,042 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @sap/cds, @sap/cds-dk, @sap/cds-foss, chai, enquirer, mocha, mustache, nyc, sinon
- hack/go.mod (capture: captured) — dependency clues: github.com/SAP/sap-btp-service-operator, github.com/bahlo/generic-list-go, github.com/beorn7/perks, github.com/buger/jsonparser, github.com/cert-manager/cert-manager, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-openapi/swag/cmdutils, github.com/go-openapi/swag/conv, github.com/go-openapi/swag/fileutils, github.com/go-openapi/swag/jsonutils, github.com/go-openapi/swag/loading
- test/files/expectedChart/Chart.yaml (capture: captured)
- test/files/expectedConfigurableTemplatesChart/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 3
- Last updated: 2026-09-22T20:36:30Z
- Last pushed: 2026-11-17T21:50:05Z
- Topics: cap-operator, k8s-operator, plugin, sap-cns

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js/cap-operator-plugin)
- [README](https://github.com/cap-js/cap-operator-plugin/blob/main/README.md)
- [Issues](https://github.com/cap-js/cap-operator-plugin/issues)
- [Releases](https://github.com/cap-js/cap-operator-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
