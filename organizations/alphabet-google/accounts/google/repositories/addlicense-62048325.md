# google/addlicense

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/addlicense](https://github.com/google/addlicense)
- Default branch: master
- README: [Open upstream README](https://github.com/google/addlicense/blob/master/README.md)
- README blob SHA: c74ccbf02ae3546ebed15014068c7f864a98fb2e
- Repository ID: 62048325
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A program which ensures source code files have copyright license headers by scanning directory patterns recursively

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:24:49+00:00

### Short excerpt (up to 100 words)

> The program ensures source code files have copyright license headers by scanning directory patterns recursively. It modifies all source files in place and avoids adding a license header to any file that already has one. addlicense requires go 1.16 or later. go install github.com/google/addlicense@latest addlicense [flags] pattern [pattern ...] -c copyright holder (default "Google LLC") -check check only mode: verify presence of license headers and exit with non-zero code if missing -f license file -ignore file patterns to ignore, for example: -ignore **/*.go -ignore vendor/** -l license type: apache, bsd, mit, mpl (default "apache") -s Include SPDX identifier in license

### README headings

- addlicense
- install
- usage
- Running in a Docker Container
- Running with pre-commit
- license

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 36,699 |
| Dockerfile | 345 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/bmatcuk/doublestar/v4, golang.org/x/sync
- testdata/expected/Gemfile (capture: captured)
- testdata/initial/Gemfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 890
- Forks at capture: 197
- Last updated: 2026-11-19T20:02:53Z
- Last pushed: 2025-10-28T18:50:02Z
- Topics: license, utility

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/addlicense)
- [README](https://github.com/google/addlicense/blob/master/README.md)
- [Issues](https://github.com/google/addlicense/issues)
- [Releases](https://github.com/google/addlicense/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
