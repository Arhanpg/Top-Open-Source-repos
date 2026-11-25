# mindsphere/devops-demo

- Company: Siemens
- Account: mindsphere
- Repository: https://github.com/mindsphere/devops-demo
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:58:41+00:00

## Project purpose

Close interaction of development and operations is essential to accelerate delivery of applications. This is a demo across the whole DevOps cycle with MindSphere, by using well known and widely used open source tools.

## Why this project is used

DevOps demo code demonstrated during MindSphere Developer Days in Berlin (mirror of project on GitLab)

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, TypeScript, Shell, HTML, CSS
- Frameworks/libraries: Unknown / not established
- Dependency names: @angular-devkit/build-angular, @angular/animations, @angular/cli, @angular/common, @angular/compiler, @angular/compiler-cli, @angular/core, @angular/forms, @angular/language-service, @angular/platform-browser, @angular/platform-browser-dynamic, @angular/router, @commitlint/cli, @commitlint/config-conventional, @mindconnect/mindconnect-nodejs, @types/jasmine, @types/jasminewd2, @types/node, body-parser, bootstrap, chromedriver, codelyzer, core-js, cors, eclint, express, express-http-proxy, express-prom-bundle, font-awesome, helmet, http, https-proxy-agent, husky, jasmine-core, jasmine-reporters, jasmine-spec-reporter, jsonwebtoken, jwks-rsa, karma, karma-chrome-launcher, karma-coverage-istanbul-reporter, karma-jasmine, karma-jasmine-html-reporter, karma-junit-reporter, karma-webdriver-launcher, license-checker, lodash.includes, markdownlint-cli, mongoose, ngx-cookie-service, nyc, protractor, rxjs, superagent, swagger-ui-express, ts-node, tslint, typescript, zone.js
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: server/server.js, agent/index.js, devops/devopsadmin/index.js, devops/devopsadmin/services/index.js

## Setup and usage

No setup information established.

## Limitations and caveats

- Known Issues / Limitations: - The gitlab-ci integration requires manually setting
- Known Issues / Limitations: authentication with access and refresh tokens available as protected
- Known Issues / Limitations: CI/CD Gitlab Variables,
- Known Issues / Limitations: and they need to be renewed every 30 days. This can be copied directly from
- Known Issues / Limitations: your CloudFoundry CLI ~/.cf/config.json file after successful cf login.
- Known Issues / Limitations: - Storage for Prometheus is currently transient, pending
- Known Issues / Limitations: support for some kind of dynamic persistent storage for apps, or direct
- Known Issues / Limitations: support for Prometheus in MindSphere.

## Evidence and provenance

- README: https://github.com/mindsphere/devops-demo/blob/master/README.md
- README SHA: 3c8114e118553714db7e607f8e20f7f01bd73283
- Manifests: package.json, agent/package.json, server/package.json, devops/devopsadmin/package.json
- Sampled source files: server/server.js, agent/index.js, devops/devopsadmin/index.js, devops/devopsadmin/services/index.js
- Git tree state: captured
- Evidence fingerprint: 56c0d7a1f51786e81a643b1544c4fd3598b825ef573eee23430c4e860515d82e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
