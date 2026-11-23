# kyma-project/cp-mod-migrator

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/cp-mod-migrator](https://github.com/kyma-project/cp-mod-migrator)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/cp-mod-migrator/blob/main/README.md)
- README blob SHA: 1970d683be4fe5d6adb13213fa313a7799c9a650
- Repository ID: 745385822
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:58+00:00

### Short excerpt (up to 100 words)

> This repository contains the source code of components that are necessary to perform the migration from the legacy Kyma Connectivity Proxy component (currently in version 2.9.3) into the new Kyma Connectivity Proxy module. The migration is designed as a three-step process where each step is executed by a separate component. The migrator components are: - **Configuration Migrator** - Go Application that performs the main migration operation - **Backup** - Bash script that performs the backup of the user configuration - **Cleaner** - Bash script that performs the cleanup of the old CP Kubernetes objects They are built as separate Docker

### README headings

- Connectivity Proxy Migrator
- Overview
- Configuration Migrator
- Backup
- Cleaner
- Migration process
- Prerequisites
- Implementation details
- Troubleshooting
- Restoring old installation
- Fixing operator Pod
- Restore user configuration from backup
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 32,113 |
| Shell | 12,672 |
| Makefile | 1,118 |
| Dockerfile | 887 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/go-logr/logr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/go-task/slim-sprig, github.com/gogo/protobuf, github.com/golang/protobuf, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/gofuzz, github.com/google/pprof, github.com/google/uuid, github.com/imdario/mergo, github.com/josharian/intern, github.com/json-iterator/go, github.com/mailru/easyjson, github.com/modern-go/concurrent
- Makefile (capture: captured)
- images/backup/Dockerfile (capture: captured)
- images/cleaner/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 5
- Last updated: 2024-09-04T12:04:28Z
- Last pushed: 2024-09-04T09:40:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/cp-mod-migrator)
- [README](https://github.com/kyma-project/cp-mod-migrator/blob/main/README.md)
- [Issues](https://github.com/kyma-project/cp-mod-migrator/issues)
- [Releases](https://github.com/kyma-project/cp-mod-migrator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
