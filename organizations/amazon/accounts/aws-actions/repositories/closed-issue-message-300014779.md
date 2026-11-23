# aws-actions/closed-issue-message

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/closed-issue-message](https://github.com/aws-actions/closed-issue-message)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-actions/closed-issue-message/blob/main/README.md)
- README blob SHA: 843bb570888b413b57c5dbc3d77edccdf560d3b4
- Repository ID: 300014779
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Github Action to set a default message to be commented on all issues when they get closed.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:18+00:00

### Short excerpt (up to 100 words)

> This action sets a default message to be commented on all issues or pull requests when they get closed. Add a YAML workflow file into your repository under `.github/workflows`. This workflow file follows the For a list of options and their description, see action.yml. name: Closed Issue Message on: issues: types: [closed] jobs: auto_comment: permissions: issues: write runs-on: ubuntu-latest steps: - uses: aws-actions/closed-issue-message@v2 with: repo-token: "${{ secrets.GITHUB_TOKEN }}" message: "Comments on closed issues are hard for our team to see." message: | Comments on closed issues are hard for our team to see. If you need more assistance, please either

### README headings

- "Closed Issue Message" Action for GitHub Actions
- Usage
- Example Workflow
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 812 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @actions/github, @biomejs/biome
- node_modules/before-after-hook/package.json (capture: captured) — dependency clues: browserify, gaze-cli, istanbul, istanbul-coveralls, mkdirp, prettier, rimraf, semantic-release, simple-mock, tap-min, tap-spec, tape, typescript, uglify-js
- node_modules/deprecation/package.json (capture: captured) — dependency clues: @pika/pack, @pika/plugin-build-node, @pika/plugin-build-types, @pika/plugin-build-web, @pika/plugin-standard-pkg, semantic-release
- node_modules/once/package.json (capture: captured) — dependency clues: tap, wrappy
- node_modules/tunnel/package.json (capture: captured) — dependency clues: mocha, should
- node_modules/undici/package.json (capture: captured) — dependency clues: @fastify/busboy, @sinonjs/fake-timers, @types/node, abort-controller, atomic-sleep, chai, chai-as-promised, chai-iterator, chai-string, concurrently, cronometro, delay, dns-packet, docsify-cli, form-data, formdata-node, https-pem, husky, import-fresh, jest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 5
- Last updated: 2025-04-21T21:18:53Z
- Last pushed: 2025-05-15T16:32:59Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/closed-issue-message)
- [README](https://github.com/aws-actions/closed-issue-message/blob/main/README.md)
- [Issues](https://github.com/aws-actions/closed-issue-message/issues)
- [Releases](https://github.com/aws-actions/closed-issue-message/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
