# aws-actions/action-cloudwatch-metrics

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/action-cloudwatch-metrics](https://github.com/aws-actions/action-cloudwatch-metrics)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-actions/action-cloudwatch-metrics/blob/main/README.md)
- README blob SHA: e337af50b37f8d6c3f397bce493b1099e8cf94e0
- Repository ID: 246134234
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

[Unmaintained] Github Action to publish metrics to AWS CloudWatch

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:33:13+00:00

### Short excerpt (up to 100 words)

> This action publishes a single metric to [Amazon CloudWatch][amazon-cloudwatch]. You can use this action to report workflow metrics, such as completed builds, build failures, build times, or any other metric. Using Amazon CloudWatch, you can then setup a unified dashboard to monitor all your packages, and be alerted when builds fail. To access AWS from a GitHub Action workflow, consider using correctly. jobs: build: runs-on: ubuntu-latest name: 'Build' steps: - name: Checkout repo uses: actions/checkout@v2 - name: Build run: ./my-build-script.sh - name: Configure AWS Credentials uses: aws-actions/configure-aws-credentials@v1 with: aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }} aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }} aws-region: us-west-2 if: always()

### README headings

- Amazon CloudWatch Metrics Github Action
- Example Workflow
- CloudWatch Metrics format
- Inputs
- `metric-dimensions`
- `metric-name`
- `metric-value`
- `namespace`

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 2,521 |
| Shell | 701 |
| JavaScript | 246 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @actions/exec, @actions/github, @types/jest, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @zeit/ncc, aws-sdk, eslint, husky, jest, prettier, ts-jest, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 3
- Last updated: 2025-02-27T21:13:40Z
- Last pushed: 2022-01-28T18:57:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/action-cloudwatch-metrics)
- [README](https://github.com/aws-actions/action-cloudwatch-metrics/blob/main/README.md)
- [Issues](https://github.com/aws-actions/action-cloudwatch-metrics/issues)
- [Releases](https://github.com/aws-actions/action-cloudwatch-metrics/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
