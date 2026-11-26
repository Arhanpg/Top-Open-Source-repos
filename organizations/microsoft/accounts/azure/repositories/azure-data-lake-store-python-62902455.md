# Azure/azure-data-lake-store-python

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/azure-data-lake-store-python](https://github.com/Azure/azure-data-lake-store-python)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/azure-data-lake-store-python/blob/master/Readme.md)
- README blob SHA: b021a8bc4b9facc5f16cbba961af88c21201bf5e
- README bytes captured: 31143
- README truncated at capture limit: False
- Repository ID: 62902455
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Microsoft Azure Data Lake Store Filesystem Library for Python

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:05:36+00:00

### Short excerpt (up to 300 words)

> Using pip: pip install

### README headings

- azure-datalake-store
- Installation
- Auth
- Pythonic Filesystem
- alternatively, adl = core.AzureDLFileSystem()
- uses environment variables
- possible remote paths to use on API
- p1, p3, and p6 only work on Windows
- Performant up-/down-loading
- download the whole directory structure using 5 threads, 16MB chunks
- API
- class azure.datalake.store.core.AzureDLFileSystem(token=None, per_call_timeout_seconds=60, \*\*kwargs)
- Methods
- access(self, path, invalidate_cache=True)
- cat(self, path)
- chmod(self, path, mod)
- chown(self, path, owner=None, group=None)
- concat(self, outfile, filelist, delete_source=False)
- connect(self)
- cp(self, path1, path2)
- classmethod current()
- df(self, path)
- du(self, path, total=False, deep=False, invalidate_cache=True)
- exists(self, path, invalidate_cache=True)
- get(self, path, filename)
- get_acl_status(self, path)
- glob(self, path, details=False, invalidate_cache=True)
- head(self, path, size=1024)
- info(self, path, invalidate_cache=True, expected_error_code=None)
- invalidate_cache(self, path=None)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> Using pip: pip install

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 218,208 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- azure-data-lake-store-python.sln (capture: captured)
- setup.py (capture: captured)
- docs/Makefile (capture: captured)
- docs/requirements.txt (capture: captured) — dependency clues: cffi, numpydoc

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 75
- Forks at capture: 79
- Last updated: 2026-10-02T15:18:43Z
- Last pushed: 2025-06-03T23:02:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/azure-data-lake-store-python)
- [README](https://github.com/Azure/azure-data-lake-store-python/blob/master/Readme.md)
- [Issues](https://github.com/Azure/azure-data-lake-store-python/issues)
- [Releases](https://github.com/Azure/azure-data-lake-store-python/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
