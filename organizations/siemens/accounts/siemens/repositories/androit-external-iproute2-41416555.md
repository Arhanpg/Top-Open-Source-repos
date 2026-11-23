# siemens/androit_external_iproute2

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/androit_external_iproute2](https://github.com/siemens/androit_external_iproute2)
- Default branch: cm-10.2-androit
- README: [Open upstream README](https://github.com/siemens/androit_external_iproute2/blob/cm-10.2-androit/README)
- README blob SHA: 7d54bd2d4d7c81ed20f968c4b81391fd85574450
- Repository ID: 41416555
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Androit: slightly extended tc tool

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:26:26+00:00

### Short excerpt (up to 100 words)

> Primary site is: http://developer.osdl.org/dev/iproute2 Original FTP site is: ftp://ftp.inr.ac.ru/ip-routing/ How to compile this. 1. Look at start of Makefile and set correct values for: KERNEL_INCLUDE should point to correct linux kernel include directory. Default (/usr/src/linux/include) is right as rule. arpd needs to have the db4 development libraries. For debian users this is the package with a name like libdb4.x-dev. DBM_INCLUDE points to the directory with db_185.h which is the include file used by arpd to get to the old format Berkely database routines. Often this is in the db-devel package. 2. make The makefile will automatically build a file Config

### README headings

- No headings captured

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 1,205,209 |
| Groff | 19,018 |
| Makefile | 16,838 |
| Shell | 10,064 |
| Yacc | 6,984 |
| Lex | 3,396 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- doc/Makefile (capture: captured)
- genl/Makefile (capture: captured)
- ip/Makefile (capture: captured)
- lib/Makefile (capture: captured)
- misc/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: GPL-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2015-08-26T09:19:21Z
- Last pushed: 2015-08-26T09:24:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/androit_external_iproute2)
- [README](https://github.com/siemens/androit_external_iproute2/blob/cm-10.2-androit/README)
- [Issues](https://github.com/siemens/androit_external_iproute2/issues)
- [Releases](https://github.com/siemens/androit_external_iproute2/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
