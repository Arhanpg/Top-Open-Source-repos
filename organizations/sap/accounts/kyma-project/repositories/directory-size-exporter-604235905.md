# kyma-project/directory-size-exporter

- Company: SAP
- GitHub account: [https://github.com/kyma-project](https://github.com/kyma-project)
- Mapping status: official-directory-listed
- Repository: [kyma-project/directory-size-exporter](https://github.com/kyma-project/directory-size-exporter)
- Default branch: main
- README: [Open upstream README](https://github.com/kyma-project/directory-size-exporter/blob/main/README.md)
- README blob SHA: 0b47703cc5c5458013594f6446abe3113db0e95b
- Repository ID: 604235905
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sidecar for fluentbit to export file buffer metrics

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:49:04+00:00

### Short excerpt (up to 100 words)

> This repository has been deprecated and archived. The project moved as a sub-project into https://github.com/kyma-project/telemetry-manager/tree/main/dependencies/directory-size-exporter. The directory size exporter is a typical metrics exporter in the Prometheus format. It is meant to run as a sidecar to an application to watch a specific application file storage and export metrics about that storage. At the moment, it is used only as a sidecar for the `telemetry-fluent-bit` instances to watch the file buffer sizes. The following configuration options are available: - **log-format** - log format parameter for the logger (`json` or `text`) - **log-level** - log level parameter for the logger (`debug`,

### README headings

- Directory Size Exporter
- :warning: **Archived**
- Overview
- Development
- Available Commands
- Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 10,382 |
| Makefile | 3,537 |
| Dockerfile | 903 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/kr/text, github.com/munnerz/goautoneg, github.com/pmezard/go-difflib, github.com/prometheus/client_golang, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/procfs, github.com/rogpeppe/go-internal, github.com/stretchr/testify, golang.org/x/sys, google.golang.org/protobuf, gopkg.in/yaml.v3
- Makefile (capture: captured)
- internal/tools/go.mod (capture: captured) — dependency clues: 4d63.com/gocheckcompilerdirectives, 4d63.com/gochecknoglobals, codeberg.org/chavacava/garif, dev.gaijin.team/go/exhaustruct/v4, dev.gaijin.team/go/golib, github.com/4meepo/tagalign, github.com/Abirdcfly/dupword, github.com/AlwxSin/noinlineerr, github.com/Antonboom/errname, github.com/Antonboom/nilnil, github.com/Antonboom/testifylint, github.com/BurntSushi/toml, github.com/Djarvur/go-err113, github.com/Masterminds/semver/v3, github.com/OpenPeeDeeP/depguard/v2, github.com/alecthomas/chroma/v2, github.com/alecthomas/go-check-sumtype, github.com/alexkohler/nakedret/v2, github.com/alexkohler/prealloc, github.com/alfatraining/structtag

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 8
- Last updated: 2025-08-21T11:43:31Z
- Last pushed: 2025-08-21T11:43:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/kyma-project/directory-size-exporter)
- [README](https://github.com/kyma-project/directory-size-exporter/blob/main/README.md)
- [Issues](https://github.com/kyma-project/directory-size-exporter/issues)
- [Releases](https://github.com/kyma-project/directory-size-exporter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
