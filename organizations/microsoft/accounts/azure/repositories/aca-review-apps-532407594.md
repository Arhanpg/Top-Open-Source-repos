# Azure/aca-review-apps

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/aca-review-apps](https://github.com/Azure/aca-review-apps)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/aca-review-apps/blob/main/README.md)
- README blob SHA: fc6ebd6452f7f50706d39ef1db6122fba4e41630
- Repository ID: 532407594
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Enable GitHub developers to create a new revision of Azure Container App for review by using GitHub Actions

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:34:40+00:00

### Short excerpt (up to 100 words)

> **aca-review-app** can be used to automate the workflow of creating a new revision of Azure Container App for review. This action runs the code contained in the GitHub pull request as an app in the Container App. The review application is then created as a new revision with a Weight of 0, each with a unique URL that can be shared. This is a great way to review and test code changes. This action allows deactivating an app for review that has been created, triggered by the close of a pull request. **aca-review-app** can also be configured to launch automatically

### README headings

- GitHub Action for Creating Azure Container App Revision
- End-to-End Sample Workflows
- Dependencies on other GitHub Actions
- Azure Service Principal for RBAC
- Integration to leave comments on Pull Request
- Sample Snipet for the Review Revision Creation
- Sample Snipet for the Review Revision Deactivation
- How to Develop/Test this Action
- Debug with breakpoints on Visual Studio Code
- Check workflow behavior without pushing to GitHub
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 17,450 |
| TypeScript | 10,775 |
| Dockerfile | 2,215 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @azure/arm-appcontainers, @azure/identity, @types/node, azure-actions-webclient, debug, typescript
- .devcontainer/Dockerfile (capture: captured)
- example/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 52
- Forks at capture: 18
- Last updated: 2026-09-01T04:37:18Z
- Last pushed: 2026-11-04T14:58:22Z
- Topics: actions, azure, azure-container-apps, cicd, container, github, github-actions

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/aca-review-apps)
- [README](https://github.com/Azure/aca-review-apps/blob/main/README.md)
- [Issues](https://github.com/Azure/aca-review-apps/issues)
- [Releases](https://github.com/Azure/aca-review-apps/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
