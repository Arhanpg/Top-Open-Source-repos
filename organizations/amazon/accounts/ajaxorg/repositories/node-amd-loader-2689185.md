# ajaxorg/node-amd-loader

- Company: Amazon
- GitHub account: [https://github.com/ajaxorg](https://github.com/ajaxorg)
- Mapping status: official-directory-listed
- Repository: [ajaxorg/node-amd-loader](https://github.com/ajaxorg/node-amd-loader)
- Default branch: master
- README: [Open upstream README](https://github.com/ajaxorg/node-amd-loader/blob/master/README.md)
- README blob SHA: 82d7c06050bc49f509d437a42152b910c9e0b243
- Repository ID: 2689185
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Load AMD modules directly from node.js

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:35:46+00:00

### Short excerpt (up to 100 words)

> AMD loader for node.js ====================== node-amd-loader adds the capability to load unmodified AMD (Asynchronous Module DefinitionAsynchronous Module Definition) from node.js applications. Installation `node-amd-loader` can be easily installed using npm. npm install amd-loader Before being able to load AMD modules the `amd-loader` module has to be required. require("amd-loader"); This needs to be done only once. Features Load modules which are written using AMD define from node.js node. amd.js define(function(require, exports, module) { exports.B = "B"; }); main.js require("amd-loader"); var amd = require("./amd"); From within an AMD modules the async require syntax introduced by requireJS can be used. require(["fs"], function(fs) { fs.readFile(...);

### README headings

- load modules which use AMD define() ###
- support requireJS asyncronous loading syntax ###
- support requireJS text plugin ###

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 3,557 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 76
- Forks at capture: 21
- Last updated: 2026-04-24T16:21:34Z
- Last pushed: 2018-07-05T04:26:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ajaxorg/node-amd-loader)
- [README](https://github.com/ajaxorg/node-amd-loader/blob/master/README.md)
- [Issues](https://github.com/ajaxorg/node-amd-loader/issues)
- [Releases](https://github.com/ajaxorg/node-amd-loader/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
