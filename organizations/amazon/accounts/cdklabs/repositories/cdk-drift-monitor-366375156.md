# cdklabs/cdk-drift-monitor

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-drift-monitor](https://github.com/cdklabs/cdk-drift-monitor)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-drift-monitor/blob/main/README.md)
- README blob SHA: 4f8a577ebc30750371439172ae328e2b2273aca8
- Repository ID: 366375156
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Monitors for CloudFormation stack drifts.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:39+00:00

### Short excerpt (up to 100 words)

> Monitors for CloudFormation stack drifts. By default, detects drifts for all stacks: new DriftMonitor(driftDetectStack, 'DriftMonitor'); You can also specify a list of stacks to detect drifts: new DriftMonitor(driftDetectStack, 'DriftMonitor', { stacks: [myStack1, myStack2], }); It can also be initialized by providing stack names: new DriftMonitor(driftDetectStack, 'DriftMonitor', { stackNames: ['myStack1', 'myStack2'], }); By default, the drift detection will run every hour. This can be customized: new DriftMonitor(driftDetectStack, 'DriftMonitor', { runEvery: Duration.hours(24), }); The construct creates an alarm with no actions. Here's an example for adding an alarm action: import * as sns from 'aws-cdk-lib/aws-sns'; import { SnsAction } from 'aws-cdk-lib/aws-cloudwatch-actions'; const

### README headings

- CDK Drift Monitor
- Lambda Runtime
- Roadmap
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 28,160 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, aws-sdk, cdklabs-projen-project-types, commit-and-tag-version, constructs, esbuild, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-each, jest-junit, jsii

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 54
- Forks at capture: 5
- Last updated: 2026-11-09T23:07:58Z
- Last pushed: 2026-11-23T18:45:14Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-drift-monitor)
- [README](https://github.com/cdklabs/cdk-drift-monitor/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-drift-monitor/issues)
- [Releases](https://github.com/cdklabs/cdk-drift-monitor/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
