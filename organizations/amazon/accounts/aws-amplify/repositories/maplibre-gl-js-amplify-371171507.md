# aws-amplify/maplibre-gl-js-amplify

- Company: Amazon
- GitHub account: [https://github.com/aws-amplify](https://github.com/aws-amplify)
- Mapping status: official-directory-listed
- Repository: [aws-amplify/maplibre-gl-js-amplify](https://github.com/aws-amplify/maplibre-gl-js-amplify)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-amplify/maplibre-gl-js-amplify/blob/main/README.md)
- README blob SHA: 138cac6968b1bad19ed4f01fe48b38cbc1b979a4
- Repository ID: 371171507
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:31:55+00:00

### Short excerpt (up to 100 words)

> A plugin for maplibre-gl-js for integration with Amplify Geo. yarn add maplibre-gl-js-amplify import { createMap } from "maplibre-gl-js-amplify"; import { Amplify } from "aws-amplify"; import awsconfig from './aws-exports'; Amplify.configure(awsconfig); ... const map = await createMap({ container: "map", // An HTML Element or HTML element ID to render the map in https://maplibre.org/maplibre-gl-js-docs/api/map/ center: [-123.1187, 49.2819], zoom: 11, region: "us-west-2" }) import { Amplify } from "aws-amplify"; import { AmplifyGeocoderAPI } from "maplibre-gl-js-amplify"; import awsconfig from './aws-exports'; import maplibregl from "maplibre-gl"; import MaplibreGeocoder from "@maplibre/maplibre-gl-geocoder"; import "@maplibre/maplibre-gl-geocoder/dist/maplibre-gl-geocoder.css"; Amplify.configure(awsconfig); ... const geocoder = createAmplifyGeocoder(); map.addControl(geocoder); import spiderManIcon from "./spiderman.svg" ... const icon =

### README headings

- Maplibre GL JS Amplify
- Reporting Bugs/Feature Requests
- Usage
- Using AmplifyMapLibreRequest to Display a Map
- Using AmplifyGeocoderAPI with [maplibre-gl-geocoder](https://github.com/maplibre/maplibre-gl-geocoder)
- Using Custom Icon with [drawPoints](https://github.com/aws-amplify/maplibre-gl-js-amplify/blob/main/API.md#drawpoints)
- Deeper dive
- API Documentation
- Examples
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 152,148 |
| CSS | 8,775 |
| JavaScript | 5,446 |
| Shell | 126 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-amplify/core, @aws-amplify/geo, @babel/preset-env, @commitlint/cli, @commitlint/config-conventional, @mapbox/mapbox-gl-draw, @maplibre/maplibre-gl-geocoder, @turf/along, @turf/circle, @turf/distance, @turf/helpers, @turf/length, @turf/line-slice, @types/debounce, @types/geojson, @types/jest, @types/mapbox__mapbox-gl-draw, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 14
- Forks at capture: 12
- Last updated: 2026-10-22T14:11:50Z
- Last pushed: 2026-10-22T13:54:59Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-amplify/maplibre-gl-js-amplify)
- [README](https://github.com/aws-amplify/maplibre-gl-js-amplify/blob/main/README.md)
- [Issues](https://github.com/aws-amplify/maplibre-gl-js-amplify/issues)
- [Releases](https://github.com/aws-amplify/maplibre-gl-js-amplify/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
