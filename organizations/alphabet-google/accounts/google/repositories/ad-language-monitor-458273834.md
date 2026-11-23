# google/ad_language_monitor

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/ad_language_monitor](https://github.com/google/ad_language_monitor)
- Default branch: main
- README: [Open upstream README](https://github.com/google/ad_language_monitor/blob/main/README.md)
- README blob SHA: ff34c8e3dfa98599e6ee6254cf30b8eacdceea98
- Repository ID: 458273834
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:24:39+00:00

### Short excerpt (up to 100 words)

> **This is not an officially supported Google product. It is a reference implementation.** A Cloud Function that uses Retext.js to monitor the inclusive language of ad copy. Run the command: gcloud functions deploy AdLanguageMonitor \ --runtime nodejs14 \ --memory 1GB \ --timeout 540s \ --trigger-http Install dependencies: yarn Run the tests: yarn test Run the development environment: yarn start Send a payload to the development function: curl -X POST http://localhost:8080/ -H "Content-Type:application/json" -d '{ "text": "He’s pretty set on beating your butt for sheriff." }' *Note: You can use either the HTTP query string or the JSON body to generate

### README headings

- Ad Language Monitor
- Overview
- Deploy
- Testing
- Development
- References

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 7,702 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @google-cloud/functions-framework, eslint, eslint-config-google, express, retext, retext-equality, vfile-reporter, vfile-reporter-json
- appsscript/package.json (capture: captured) — dependency clues: @babel/core, @babel/polyfill, @babel/preset-env, babel-loader, copy-webpack-plugin, eslint, eslint-config-google, retext, retext-equality, vfile-reporter-json, webpack, webpack-cli

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 0
- Last updated: 2026-07-21T09:23:22Z
- Last pushed: 2024-08-29T15:28:23Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/ad_language_monitor)
- [README](https://github.com/google/ad_language_monitor/blob/main/README.md)
- [Issues](https://github.com/google/ad_language_monitor/issues)
- [Releases](https://github.com/google/ad_language_monitor/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
