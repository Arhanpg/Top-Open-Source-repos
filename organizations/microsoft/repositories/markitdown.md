# MarkItDown

- **Company:** Microsoft
- **Repository:** https://github.com/microsoft/markitdown
- **README:** https://github.com/microsoft/markitdown/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** af858038fd380b187e2928cfbb8b9802c4912d5b

## What it does

A lightweight Python utility that converts many file types into Markdown while retaining useful document structure such as headings, lists, tables and links, for LLM and text-analysis workflows.

## Features documented by the upstream README

- Converts PDF, PowerPoint, Word, Excel, images, audio, HTML, text formats (CSV/JSON/XML), ZIP contents, YouTube URLs and EPUBs.
- Provides a command-line interface and a Python API.
- Offers optional dependency groups for individual formats and third-party plugins.
- Documents an OCR plugin and cloud-backed image-captioning / speech-transcription integrations.

## Technology stack

Python 3.10–3.14; Python package / pip; optional format-specific dependencies and plugins. Some captioning and transcription capabilities rely on web-hosted services.

## Notes and limitations

README warns that conversions perform I/O with the current process's privileges and recommends narrow conversion functions when processing untrusted inputs.

## Evidence

This summary is based on the upstream README linked above. Repository manifests, source code, CI workflows and release artifacts were not exhaustively audited in this pass; therefore the technology stack is limited to what the README explicitly supports.
