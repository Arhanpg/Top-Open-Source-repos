# amazonlinux/amazon-linux-supportinfo

- Company: Amazon
- GitHub account: [https://github.com/amazonlinux](https://github.com/amazonlinux)
- Mapping status: official-directory-listed
- Repository: [amazonlinux/amazon-linux-supportinfo](https://github.com/amazonlinux/amazon-linux-supportinfo)
- Default branch: main
- README: [Open upstream README](https://github.com/amazonlinux/amazon-linux-supportinfo/blob/main/README.md)
- README blob SHA: a52d7809a041763b64dc36a481e134fc0812bd5a
- Repository ID: 1270610174
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:37:53+00:00

### Short excerpt (up to 100 words)

> `supportinfo` is a Python library for parsing and querying Amazon Linux's package support metadata. It reads the `support_info.xml` documents Amazon Linux publishes and exposes the data through a typed Python API. It is the parsing engine used by to power `dnf supportinfo --pkg <name>` on Amazon Linux 2023. Two schemas are supported. The right handler is picked automatically from the root element's `schema_version` attribute. Both XSDs ship with the package under `supportinfo/schemas/`. * Python 3.9 or newer * `lxml` and `xmlschema` (installed automatically) The package is not yet on PyPI. Install from a checkout: pip install . Or for development:

### README headings

- amazon-linux-supportinfo
- Document formats
- Requirements
- Installation
- Usage
- Loading a document
- Looking up a single package
- Returns SupportStatement, or None if the package is not in the document.
- 1.0 only. Raises ValueError if the package is in more than one origin
- and origin= is not given.
- 1.0 only. Returns Dict[origin_name, SupportStatement].
- Listing every package in a document
- Bulk metadata
- Dict[id_or_lifecycle_name, SupportStatement]
- 1.0-only metadata
- Detecting the schema version
- Or get the raw string:
- Development
- Run the tests
- Lint and format
- Building an RPM (downstream packagers)
- Reporting security issues
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 101,205 |
| Makefile | 992 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: black, flake8, isort, lxml, mypy, pep8-naming, pytest, pytest-cov, xmlschema
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-06-16T06:21:59Z
- Last pushed: 2026-06-15T23:07:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazonlinux/amazon-linux-supportinfo)
- [README](https://github.com/amazonlinux/amazon-linux-supportinfo/blob/main/README.md)
- [Issues](https://github.com/amazonlinux/amazon-linux-supportinfo/issues)
- [Releases](https://github.com/amazonlinux/amazon-linux-supportinfo/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
