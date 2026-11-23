# microsoft/acc-vm-engine

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/acc-vm-engine](https://github.com/microsoft/acc-vm-engine)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/acc-vm-engine/blob/main/README.md)
- README blob SHA: 6a58000b0fc712c264dc2bad95923089f6feedf4
- Repository ID: 307846249
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ACC VM template generator

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:24:27+00:00

### Short excerpt (up to 100 words)

> - Confidential VM (CVM) If you want to build on Linux or MacOS, make sure you have golang installed. If not, you can download it by following these instructions: sudo apt update sudo apt upgrade wget https://dl.google.com/go/go1.15.5.linux-amd64.tar.gz sudo tar -C /usr/local/ -xzf go1.15.5.linux-amd64.tar.gz cd /usr/local/ echo $PATH sudo nano $HOME/.profile inside your profile, append the following: export PATH=$PATH:/usr/local/go/bin save and apply changes: source $HOME/.profile check that it installed correctly: go version On Linux or MacOS, execute: make build Alternatively, you can build with a Docker container: docker run \ -v $PWD:/go/src/github.com/microsoft/acc-vm-engine \ -w /go/src/github.com/microsoft/acc-vm-engine \ golang:1.15-alpine go build ./cmd/acc-vm-engine A

### README headings

- Azure template generator for ACC VMs
- Supported VMs
- Pre-Requisite
- update your system
- download the go binary
- extract binaries tarball
- set the right path
- Build
- Generate template
- Deploy the VM

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 88,881 |
| Raku | 13,410 |
| Makefile | 582 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/Jeffail/gabs, github.com/alecthomas/template, github.com/alecthomas/units, github.com/blang/semver, github.com/ghodss/yaml, github.com/go-playground/universal-translator, github.com/leodido/go-urn, github.com/onsi/gomega, github.com/pkg/errors, github.com/sirupsen/logrus, github.com/stretchr/testify, golang.org/x/crypto, gopkg.in/alecthomas/kingpin.v2, gopkg.in/go-playground/assert.v1, gopkg.in/go-playground/validator.v9
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 9
- Forks at capture: 10
- Last updated: 2026-10-03T21:25:27Z
- Last pushed: 2023-12-18T21:56:44Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/acc-vm-engine)
- [README](https://github.com/microsoft/acc-vm-engine/blob/main/README.md)
- [Issues](https://github.com/microsoft/acc-vm-engine/issues)
- [Releases](https://github.com/microsoft/acc-vm-engine/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
