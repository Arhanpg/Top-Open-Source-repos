# siemens/mod_auth_mellon

- Company: Siemens
- GitHub account: [https://github.com/Siemens](https://github.com/Siemens)
- Mapping status: verified
- Repository: [siemens/mod_auth_mellon](https://github.com/siemens/mod_auth_mellon)
- Default branch: master
- README: [Open upstream README](https://github.com/siemens/mod_auth_mellon/blob/master/README.md)
- README blob SHA: 4f793371e9be5e96667ecb49fea84e7e9e761dbd
- README bytes captured: 40642
- README truncated at capture limit: False
- Repository ID: 195278404
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An Apache module with a simple SAML 2.0 service provider

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T21:56:37+00:00

### Short excerpt (up to 300 words)

> Require valid-user AuthType "Mellon" mod_auth_mellon uses autoconf, and mod_auth_mellon has four dependencies: For reporting security vulnerabilities

### README headings

- mod_auth_mellon
- Dependencies
- Installing mod_auth_mellon
- Configuring mod_auth_mellon
- Global configuration for mod_auth_mellon. This configuration is shared by
- every virtual server and location in this instance of apache.
- MellonCacheSize sets the maximum number of sessions which can be active
- at once. When mod_auth_mellon reaches this limit, it will begin removing
- the least recently used sessions. The server must be restarted before any
- changes to this option takes effect.
- Default: MellonCacheSize 100
- MellonCacheEntrySize sets the maximum size for a single session entry in
- bytes. When mod_auth_mellon reaches this limit, it cannot store any more
- data in the session and will return an error. The minimum entry size is
- 65536 bytes, values lower than that will be ignored and the minimum will
- be used.
- Default: MellonCacheEntrySize 196608
- MellonLockFile is the full path to a file used for synchronizing access
- to the session data. The path should only be used by one instance of
- apache at a time. The server must be restarted before any changes to this
- option takes effect.
- Default: MellonLockFile "/var/run/mod_auth_mellon.lock"
- MellonPostDirectory is the full path of a directory where POST requests
- are saved during authentication. This directory must writable by the
- Apache user. It should not be writable (or readable) by other users.
- Default: None
- Example: MellonPostDirectory "/var/cache/mod_auth_mellon_postdata"
- MellonPostTTL is the delay in seconds before a saved POST request can
- be flushed.
- Default: MellonPostTTL 900 (15 mn)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: about them.

> Require valid-user AuthType "Mellon"

### Getting started and usage: Installing mod_auth_mellon

> mod_auth_mellon uses autoconf, and

### Technology and requirements: Dependencies

> mod_auth_mellon has four dependencies:

### Limitations and security: Reporting security vulnerabilities

> For reporting security vulnerabilities

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 429,558 |
| M4 | 3,697 |
| Shell | 2,701 |
| Makefile | 1,965 |
| Emacs Lisp | 76 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2020-02-13T13:33:56Z
- Last pushed: 2020-02-13T13:33:52Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/siemens/mod_auth_mellon)
- [README](https://github.com/siemens/mod_auth_mellon/blob/master/README.md)
- [Issues](https://github.com/siemens/mod_auth_mellon/issues)
- [Releases](https://github.com/siemens/mod_auth_mellon/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
