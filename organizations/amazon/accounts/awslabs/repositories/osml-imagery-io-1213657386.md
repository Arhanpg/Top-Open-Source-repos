# awslabs/osml-imagery-io

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/osml-imagery-io](https://github.com/awslabs/osml-imagery-io)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/osml-imagery-io/blob/main/README.md)
- README blob SHA: bcd1a33fc99c3a3e22b7047eb428d639fbe587db
- README bytes captured: 10566
- README truncated at capture limit: False
- Repository ID: 1213657386
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

High-performance read/write for NITF, GeoTIFF, JPEG 2000, and more. Rust core with Python bindings — pip install, no complex dependencies.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:57:30+00:00

### Short excerpt (up to 300 words)

> pip install osml-imagery-io from Please do not open

### README headings

- OversightML Imagery IO
- Why This Library
- What This Library is Not
- Quick Start
- Inspect metadata without reading pixels
- Read an image as a NumPy array, careful this is the whole image
- Read a single windowed region, much more practical
- Save to any supported format — inferred from extension
- Iterate over tiles for memory-efficient processing of large images
- Full Format Access
- Format Specific Features
- NITF / NSIF
- TIFF / GeoTIFF / COG
- DTED (Digital Terrain Elevation Data)
- Other Formats
- Cloud-Native Access
- Build a tile index (works for NITF, TIFF, JPEG 2000)
- Open tiles directly from S3 — only fetches the bytes you need
- Documentation
- Development
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Quick Start

> pip install osml-imagery-io from

### Limitations and security: Security

> Please do not open

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 4,098,567 |
| Python | 1,787,341 |
| Kaitai Struct | 530,261 |
| Shell | 13,003 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: criterion, memmap2, numpy, png, proptest, pyo3, rayon, serde, serde_json, serde_yaml, tempfile, thiserror
- pyproject.toml (capture: captured) — dependency clues: fsspec, furo, myst-parser, numpy, pyarrow, sphinx, sphinx-autodoc-typehints, sphinxcontrib-mermaid, virtualizarr, zarr
- docs/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 2
- Last updated: 2026-11-02T17:03:41Z
- Last pushed: 2026-09-21T15:22:59Z
- Topics: cloud-optimized-geotiff, geospatial, geotiff, jpeg2000, nitf, numpy, python, remote-sensing, rust, satellite-imagery, zarr

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/osml-imagery-io)
- [README](https://github.com/awslabs/osml-imagery-io/blob/main/README.md)
- [Issues](https://github.com/awslabs/osml-imagery-io/issues)
- [Releases](https://github.com/awslabs/osml-imagery-io/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
