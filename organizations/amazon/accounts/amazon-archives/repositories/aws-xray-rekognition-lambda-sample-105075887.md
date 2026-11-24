# amazon-archives/aws-xray-rekognition-lambda-sample

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-xray-rekognition-lambda-sample](https://github.com/amazon-archives/aws-xray-rekognition-lambda-sample)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-xray-rekognition-lambda-sample/blob/master/README.md)
- README blob SHA: c72fed50841d21c737be3699d6087789cb7f3889
- README bytes captured: 9807
- README truncated at capture limit: False
- Repository ID: 105075887
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sample demonstrating AWS X-Ray instrumentation on Amazon Rekognition apps written on AWS Lambda

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T22:39:38+00:00

### Short excerpt (up to 300 words)

> 1. User uses photoform.html Run the following command

### README headings

- AWS X-Ray with Amazon Rekognition
- Before you begin
- Overview
- Setup instructions
- a. Deploy the resources from Cloudformation template
- b. Get the Cognito Identity Pool Id and update
- c. Copy contents of the Client folder to the public S3 bucket
- Testing
- Analyzing app using AWS X-Ray
- Analyzing AWS Lambda and Amazon Rekognition performance using AWS X-Ray
- AWS Lambda initializing time analysis
- AWS Lambda initializing time:
- AWS Lambda on subsequent runs:
- Amazon Rekognition time to analyze images
- Amazon Rekognition time to analyze images with many faces
- Rekognition for image with 15 faces
- Rekognition for image with 10 faces
- Average response time for the whole function
- No correlation on the number of times a celebrity face appears and time taken by Rekognition
- Amazon Rekognition image recognition errors
- Trace with error:
- Trace with exception shown:
- Delete resources and uninstall app

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> 1. User uses photoform.html

### Getting started and usage: Delete resources and uninstall app

> Run the following command

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 18,281 |
| Python | 4,525 |
| CSS | 1,526 |
| HTML | 950 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Lambda/package.json (capture: captured) — dependency clues: async, aws-sdk, aws-xray-sdk-core, fs, http
- Lambda/node_modules/async-listener/package.json (capture: captured) — dependency clues: semver, shimmer, tap
- Lambda/node_modules/async/package.json (capture: captured) — dependency clues: babel-cli, babel-core, babel-plugin-add-module-exports, babel-plugin-istanbul, babel-plugin-transform-es2015-modules-commonjs, babel-preset-es2015, babel-preset-es2017, babelify, benchmark, bluebird, chai, cheerio, coveralls, es6-promise, eslint, fs-extra, gh-pages-deploy, jsdoc, karma, karma-browserify
- Lambda/node_modules/aws-sdk/package.json (capture: captured) — dependency clues: @types/node, browserify, buffer, chai, codecov, coffee-script, coffeeify, crypto-browserify, cucumber, eslint, events, insert-module-globals, istanbul, jasmine, jasmine-core, jmespath, json-loader, karma, karma-jasmine, karma-phantomjs-launcher
- Lambda/node_modules/aws-xray-sdk-core/package.json (capture: captured) — dependency clues: chai, continuation-local-storage, eslint, grunt, grunt-contrib-clean, grunt-jsdoc, mocha, moment, nock, pkginfo, semver, sinon, sinon-chai, underscore, winston
- Lambda/node_modules/base64-js/package.json (capture: captured) — dependency clues: benchmark, browserify, standard, tape, uglify-js

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 17
- Forks at capture: 6
- Last updated: 2023-01-28T08:31:37Z
- Last pushed: 2020-01-09T04:42:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-xray-rekognition-lambda-sample)
- [README](https://github.com/amazon-archives/aws-xray-rekognition-lambda-sample/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-xray-rekognition-lambda-sample/issues)
- [Releases](https://github.com/amazon-archives/aws-xray-rekognition-lambda-sample/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
