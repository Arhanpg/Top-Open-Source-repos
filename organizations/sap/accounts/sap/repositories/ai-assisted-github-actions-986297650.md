# SAP/ai-assisted-github-actions

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/ai-assisted-github-actions](https://github.com/SAP/ai-assisted-github-actions)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/ai-assisted-github-actions/blob/main/README.md)
- README blob SHA: 5e87eb6f165da241904fc9b8e1e42ec0da5b8ad4
- Repository ID: 986297650
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Automate your PR workflow with GitHub Actions powered by SAP AI Core. Get instant summaries and reviews—no more manual grunt work.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:41:55+00:00

### Short excerpt (up to 100 words)

> _Automate your PR workflow with GitHub Actions powered by SAP AI Core. Get instant summaries and reviews—no more manual grunt work._ The following GitHub Actions are available to assist with pull requests: - **Pull Request Summary** This action calls SAP AI Core to create a comment with a summary of the pull request. Usage: `SAP/ai-assisted-github-actions/pr-summary@v3` - **Pull Request Review** This action calls SAP AI Core to create a review of the pull request (as comment). Usage: `SAP/ai-assisted-github-actions/pr-review@v3` These actions access models available via _SAP AI Core Orchestration_ service. To get started, you'll need to configure both _GitHub Actions_ and _SAP

### README headings

- AI-assisted GitHub Actions
- Available Actions
- Requirements and Setup
- Usage
- Support, Feedback, Contributing
- Security / Disclosure
- SAP-internal Usage
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 48,775 |
| JavaScript | 2,990 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pr-review/package.json (capture: captured) — dependency clues: @actions/core, @actions/github, @eslint/js, @octokit/action, @octokit/plugin-retry, @octokit/plugin-throttling, @octokit/webhooks, @sap-ai-sdk/ai-api, @sap-ai-sdk/orchestration, @types/node, @vercel/ncc, axios, eslint, eslint-plugin-import, eslint-plugin-sonarjs, eslint-plugin-unicorn, minimatch, mollitia, octokit, parse-diff
- pr-summary/package.json (capture: captured) — dependency clues: @actions/core, @actions/github, @eslint/js, @octokit/plugin-retry, @octokit/plugin-throttling, @octokit/webhooks, @sap-ai-sdk/ai-api, @sap-ai-sdk/orchestration, @types/node, @vercel/ncc, axios, eslint, eslint-plugin-import, eslint-plugin-sonarjs, eslint-plugin-unicorn, minimatch, mollitia, octokit, parse-diff, prettier

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 5
- Last updated: 2026-08-02T12:43:07Z
- Last pushed: 2026-11-21T14:16:39Z
- Topics: github-actions, sap-ai-core

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/ai-assisted-github-actions)
- [README](https://github.com/SAP/ai-assisted-github-actions/blob/main/README.md)
- [Issues](https://github.com/SAP/ai-assisted-github-actions/issues)
- [Releases](https://github.com/SAP/ai-assisted-github-actions/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
