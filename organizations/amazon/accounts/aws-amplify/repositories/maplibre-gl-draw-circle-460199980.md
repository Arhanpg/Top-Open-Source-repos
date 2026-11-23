# aws-amplify/maplibre-gl-draw-circle

- Company: Amazon
- GitHub account: [https://github.com/aws-amplify](https://github.com/aws-amplify)
- Mapping status: official-directory-listed
- Repository: [aws-amplify/maplibre-gl-draw-circle](https://github.com/aws-amplify/maplibre-gl-draw-circle)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-amplify/maplibre-gl-draw-circle/blob/main/README.md)
- README blob SHA: 98092073da93e76b5d7695ca3414bdd795180a1a
- Repository ID: 460199980
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Supports drawing/editing a circle on a Mapbox map.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:31:53+00:00

### Short excerpt (up to 100 words)

> This package was forked from mapbox-gl-draw-circle. We originally reached out to @iamanvesh about working together and received no response but are still open to doing so moving forward! Adds support for drawing and editing a circle feature using mapbox-gl-draw library. npm install maplibre-gl-draw-circle import { CircleMode, DragCircleMode, DirectMode, SimpleSelectMode } from 'maplibre-gl-draw-circle'; // userProperties has to be enabled const draw = new MapboxDraw({ defaultMode: "draw_circle", userProperties: true, modes: { ...MapboxDraw.modes, draw_circle : CircleMode, drag_circle : DragCircleMode, direct_select: DirectMode, simple_select: SimpleSelectMode } }); // Add this draw object to the map when map loads map.addControl(draw); The default radius units are in

### README headings

- mapbox-gl-draw-circle
- Demo
- Circle mode
- Drag Circle mode
- Usage
- Installation
- Changelog
- v1.1.0

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 44,982 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @mapbox/mapbox-gl-draw, @turf/along, @turf/circle, @turf/distance, @turf/helpers, @turf/length, jest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 17
- Forks at capture: 3
- Last updated: 2026-03-30T20:14:30Z
- Last pushed: 2025-11-17T22:49:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-amplify/maplibre-gl-draw-circle)
- [README](https://github.com/aws-amplify/maplibre-gl-draw-circle/blob/main/README.md)
- [Issues](https://github.com/aws-amplify/maplibre-gl-draw-circle/issues)
- [Releases](https://github.com/aws-amplify/maplibre-gl-draw-circle/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
