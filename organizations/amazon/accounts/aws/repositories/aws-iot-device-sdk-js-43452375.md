# aws/aws-iot-device-sdk-js

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-iot-device-sdk-js](https://github.com/aws/aws-iot-device-sdk-js)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/aws-iot-device-sdk-js/blob/master/README.md)
- README blob SHA: 29d2ff7af384d1aa6d7a3fc663128a1a737a5a0c
- README bytes captured: 70333
- README truncated at capture limit: False
- Repository ID: 43452375
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SDK for connecting to AWS IoT from a device using JavaScript/Node.js

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T01:16:53+00:00

### Short excerpt (up to 300 words)

> This document provides instructions 1. The AWS SDK **NOTE:** AWS IoT Node.js temperature-control.js uses the blessed.js

### README headings

- New Version Available
- AWS IoT SDK for JavaScript
- Overview
- MQTT Connection
- Collection of Metrics
- Thing Shadows
- Jobs
- Installation
- Mac-Only TLS Behavior
- Examples
- Device Class
- Thing Shadow Class
- Jobs Class
- API Documentation
- awsIot.device(options)
- awsIot.device#updateWebSocketCredentials(accessKeyId, secretKey, sessionToken, expiration)
- awsIot.thingShadow(deviceOptions, thingShadowOptions)
- Event `'message'`
- Event `'status'`
- Event `'delta'`
- Event `'foreignStateChange'`
- Event `'timeout'`
- awsIot.thingShadow#register(thingName, [options], [callback] )
- awsIot.thingShadow#unregister(thingName)
- awsIot.thingShadow#update(thingName, stateObject)
- awsIot.thingShadow#get(thingName, [clientToken])
- awsIot.thingShadow#delete(thingName, [clientToken])
- awsIot.thingShadow#publish(topic, message, [options], [callback])
- awsIot.thingShadow#subscribe(topic, [options], [callback])
- awsIot.thingShadow#unsubscribe(topic, [callback])

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> This document provides instructions

### Features and capabilities: Eliminate unused features from the AWS SDK

> 1. The AWS SDK

### Getting started and usage: Installation

> **NOTE:** AWS IoT Node.js

### Technology and requirements: _Installing Dependencies_

> temperature-control.js uses the blessed.js

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 308,964 |
| Shell | 34,885 |
| Batchfile | 2,745 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @httptoolkit/websocket-stream, crypto-js, gulp, gulp-beautify, gulp-concat, gulp-coverage, gulp-jscs, gulp-jshint, gulp-mocha, jshint, jshint-stylish, minimist, mqtt, rewire, sinon
- browser/package.json (capture: captured) — dependency clues: aws-iot-device-sdk, aws-sdk
- examples/temperature-control/package.json (capture: captured) — dependency clues: blessed, blessed-contrib
- examples/browser/mqtt-webpack/package.json (capture: captured) — dependency clues: aws-iot-device-sdk, aws-sdk, webpack

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 966
- Forks at capture: 374
- Last updated: 2026-11-19T19:44:05Z
- Last pushed: 2026-07-07T18:51:58Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-iot-device-sdk-js)
- [README](https://github.com/aws/aws-iot-device-sdk-js/blob/master/README.md)
- [Issues](https://github.com/aws/aws-iot-device-sdk-js/issues)
- [Releases](https://github.com/aws/aws-iot-device-sdk-js/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
