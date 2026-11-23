# MarkItDown

<sub>Company: Microsoft · Repository: [microsoft/markitdown](https://github.com/microsoft/markitdown) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

MarkItDown is a Python package and command-line utility for converting documents and other media into Markdown. Its central design choice is to retain meaningful document structure—such as headings, lists, tables and links—instead of flattening everything into unstructured text. The resulting Markdown is intended primarily for indexing, language-model input and downstream text-analysis pipelines, rather than pixel-perfect document reproduction.

**Problem it addresses:** text and multimodal documents often need to be normalized before they can be searched, indexed, summarized or processed by an LLM. MarkItDown supplies a common conversion interface across several file formats.

## Supported inputs

The project README lists support for:

- **Office and document files:** PDF, PowerPoint, Word, Excel and EPUB.
- **Web and structured text:** HTML, CSV, JSON and XML.
- **Media:** images (including EXIF metadata and captioning) and audio (including metadata and speech transcription).
- **Other sources:** ZIP archives, whose contents are iterated, and YouTube URLs.

The exact conversion path and output fidelity depend on the format and optional integration being used. The README explicitly says that image captioning and speech transcription use web-hosted services.

## Main capabilities

### 1. Structure-aware Markdown conversion

The converter aims to preserve the information structure that is useful to downstream readers and models. Markdown is used as an intermediate representation because it is compact while retaining semantic boundaries such as headings, lists, tables and links.

### 2. CLI and Python API

A simple command-line workflow can redirect conversion output into a Markdown file:

```bash
markitdown report.pdf > report.md
```

The README also documents output-file arguments and piping input through standard input. In Python, the package exposes a `MarkItDown` object and a `convert(...)` method:

```python
from markitdown import MarkItDown

converter = MarkItDown()
result = converter.convert("report.xlsx")
print(result.markdown)
```

### 3. Optional dependency groups

The package does not require every format-specific dependency to be installed for every user. The README lists optional groups for PDF, DOCX, PPTX, XLSX, legacy XLS, Outlook, Azure Document Intelligence, Azure Content Understanding, audio transcription and YouTube transcription. This allows an installation to be limited to the formats and integrations actually needed.

### 4. Plugin extension points

Third-party plugins are supported and are disabled by default. The CLI can list available plugins and enable them for a conversion. The README gives an OCR plugin example for extracting text embedded in PDF, DOCX, PPTX and XLSX images using an LLM vision client.

### 5. Cloud-backed content understanding

The README describes Azure Content Understanding as an option for higher-quality multimodal extraction, structured field extraction and audio/video processing. It contrasts local format-specific converters, Azure Document Intelligence and Azure Content Understanding in terms of modalities, analyzers and service costs.

## Technology profile

| Area | README-supported details |
|---|---|
| Primary language / runtime | Python 3.10–3.14 |
| Distribution | Python package installed through `pip` |
| Interfaces | Command-line utility and Python API |
| Extension mechanism | Optional dependency groups and third-party plugins |
| Integrations | Optional Azure Document Intelligence / Content Understanding; LLM client integration for OCR / captioning examples |
| Output format | Markdown |
| Source layout reference | `packages/markitdown` |

The stack above is limited to the README and package documentation inspected for this entry; it is not a complete dependency-manifest audit.

## Getting started

The project README recommends a virtual environment. A broad installation is documented as:

```bash
pip install 'markitdown[all]'
```

For a smaller install, select only the optional groups needed, for example:

```bash
pip install 'markitdown[pdf, docx, pptx]'
```

The Python and CLI examples above are the quickest documented ways to test a conversion. See the upstream README for current supported formats, plugin setup and cloud integration configuration.

## Where it may be useful

- Preparing office documents and PDFs for RAG or semantic-search indexing.
- Converting heterogeneous business documents into a consistent text representation.
- Creating text-analysis pipelines that need tables, headings and links retained.
- Extracting structured content from supported documents before sending it to an LLM.
- Building ingestion workflows that need both a CLI and an embeddable Python API.

These are practical applications of the documented conversion features, not claims that the repository ships a complete RAG or document-management product.

## Security and operational considerations

The maintainers emphasize that MarkItDown performs I/O with the privileges of the current process. Inputs should therefore be sanitized in untrusted environments, and callers should choose the narrowest conversion function appropriate to the task (the README names `convert_stream()` and `convert_local()` as examples). Cloud-backed image/audio features and Azure integrations may require credentials, network access and billable service usage.

Markdown conversion is not presented as high-fidelity visual reconstruction. Validate output quality for complex layouts, scanned files and tables before relying on it in a production pipeline.

## Upstream references

- [Repository](https://github.com/microsoft/markitdown)
- [Primary README](https://github.com/microsoft/markitdown/blob/main/README.md)
- [Package README](https://github.com/microsoft/markitdown/blob/main/packages/markitdown/README.md)
- [Optional plugin example: markitdown-ocr](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-ocr)

**Evidence note:** README blob inspected: `af858038fd380b187e2928cfbb8b9802c4912d5b`; package README blob: `2ac98708d6febc7e39ffd95f0286eb89a7a3eaa2`.
