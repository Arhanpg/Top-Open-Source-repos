# apple/apple_rules_lint

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/apple_rules_lint](https://github.com/apple/apple_rules_lint)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/apple_rules_lint/blob/main/README.md)
- README blob SHA: 65356fdf515afe2bc30cc32b5b3126e5eace6f1b
- Repository ID: 294468697
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A framework for adding lint checks to Bazel projects

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:00:26+00:00

### Short excerpt (up to 100 words)

> A linting framework for Bazel You must load and configure the linting framework before anything else. This is because later rulesets that depend on the linting framework will attempt to ensure that linters are configured by registering no-op implementations of lint configs. You can do this by: load("@apple_rules_lint//lint:repositories.bzl", "lint_deps") lint_deps() load("@apple_rules_lint//lint:setup.bzl", "lint_setup") lint_setup({ "java-checkstyle": "//your:checkstyle-config", }) Alternatively, using Bzlmod: bazel_dep(name = "apple_rules_lint", version = "0.4.0") linter = use_extension("@apple_rules_lint//lint:extensions.bzl", "linter") linter.configure(name = "java-checkstyle", config = "//your:checkstyle-config") use_repo(linter, "apple_linters") You may override specific lint configurations on a per-package basis by: load("@apple_rules_lint//lint:defs.bzl", "package_lint_config") package_lint_config({ "java-checkstyle": ":alternative-checkstyle-config", }) Bazel may report an error like

### README headings

- apple_rules_lint
- Users
- WORKSPACE
- MODULE.bazel
- BUILD.bazel
- Missing `@@apple_linters` error
- API Documentation
- Ruleset Authors
- WORKSPACE setup
- repositories.bzl
- setup.bzl
- Bzlmod setup
- MODULE.bazel
- Getting the configured config for a linter
- your_rules.bzl
- Integrating `apple_rules_lint` With Your Rulesets

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Starlark | 14,768 |
| Shell | 278 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 146
- Forks at capture: 19
- Last updated: 2026-10-07T10:45:55Z
- Last pushed: 2026-09-25T21:52:23Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/apple_rules_lint)
- [README](https://github.com/apple/apple_rules_lint/blob/main/README.md)
- [Issues](https://github.com/apple/apple_rules_lint/issues)
- [Releases](https://github.com/apple/apple_rules_lint/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
