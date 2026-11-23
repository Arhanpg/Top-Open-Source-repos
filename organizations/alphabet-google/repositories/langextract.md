# LangExtract

<sub>Company: Alphabet / Google · Repository: [google/langextract](https://github.com/google/langextract) · Default branch: `main` · Review status: **README and package manifest reviewed**</sub>

## At a glance

LangExtract is a Python library that uses large language models to extract structured information from unstructured text based on user-defined instructions. Its distinguishing feature is source grounding: extracted values are associated with their exact locations in the original document, allowing users to trace and visually verify the output.

**Problem it addresses:** LLM extraction can generate a plausible structured response, but users also need to know where each extracted value came from. LangExtract combines instruction-driven extraction with source-span grounding and visual review.

## Main capabilities

### 1. Source-grounded extraction

The README says that each extraction is mapped to its exact source location. The visualization can highlight the original text span so a reviewer can inspect the context rather than relying only on the generated output.

### 2. Schema-consistent structured output

The library uses user instructions and few-shot examples to guide a consistent extraction schema. The README highlights controlled generation in supported models, including Gemini, as a way to produce structured results.

### 3. Long-document processing

The README describes an approach using text chunking, parallel processing and multiple passes to address long-document extraction and improve recall. This is relevant when a source is too long to handle as one undifferentiated prompt.

### 4. Interactive HTML visualization

The library can generate a self-contained interactive HTML file for reviewing extracted entities in their original context. The README describes visualization of large sets of extracted entities, which makes the result more auditable for human reviewers.

### 5. Model-provider flexibility

The README and package manifest show provider paths for Gemini, Ollama and OpenAI. The README also links examples for cloud models and local LLMs, allowing the extraction workflow to be evaluated across different model-serving choices.

## Typical workflow

A documented high-level workflow is:

1. Define the information to extract in natural-language instructions.
2. Provide few-shot examples that clarify the expected output.
3. Pass the source document to the library.
4. Let the configured LLM provider identify candidate structured information.
5. Review the output and its grounded character spans.
6. Export or use the structured extraction in a downstream application.

This workflow description follows the README's stated functionality. The exact extraction configuration, provider setup and long-document parameters should be taken from the current usage documentation.

## Technology profile

| Area | Evidence from README / `pyproject.toml` |
|---|---|
| Primary language | Python |
| Minimum Python version | Python 3.10+ |
| Packaging | setuptools / wheel; PyPI package `langextract` |
| Core data / validation dependencies | NumPy, Pandas, Pydantic, PyYAML |
| Provider integrations | Gemini (`google-genai`), Ollama and optional OpenAI |
| HTTP / async utilities | aiohttp, async-timeout, requests |
| Developer tooling | pytest, pyink, isort, pylint, pytype and pre-commit |
| Visualization output | Self-contained interactive HTML |
| License in manifest | Apache-2.0 |

The provider entry points are explicitly registered in `pyproject.toml` for Gemini, Ollama and OpenAI. OpenAI is also exposed as an optional dependency group. The manifest separates runtime dependencies from development and test tooling.

## Installation and provider configuration

The README presents LangExtract as an installable Python package and documents setup for cloud model credentials, custom providers and local LLMs with Ollama. Consult the [current README](https://github.com/google/langextract/blob/main/README.md) for exact installation commands and provider-specific configuration, because environment variables and provider options can evolve.

## Good fit

- Extracting structured fields from reports, notes and long text documents.
- Creating traceable entity extraction pipelines.
- Reviewing extraction output with visual links back to the source text.
- Building document processing systems where provenance matters.
- Comparing cloud and local model providers for a common extraction task.

## Evaluation and limitations

Source grounding improves traceability but does not prove that an extraction is correct. Review the extracted values, schema, source span and model behaviour. Long-document processing can also require more model calls and compute than a single short prompt. Evaluate recall, precision, consistency and cost on representative documents before using the output for high-impact workflows.

## Upstream references

- [Repository](https://github.com/google/langextract)
- [Primary README](https://github.com/google/langextract/blob/main/README.md)
- [Python package manifest](https://github.com/google/langextract/blob/main/pyproject.toml)
- [PyPI package](https://pypi.org/project/langextract/)
- [Interactive demo](https://google-langextract.hf.space/)

**Evidence note:** README blob inspected: `7fdba9d5d447e20aeabbf58288ed523d8ef5c43b`; `pyproject.toml` inspected: `3bbfe286d5cb5d7e3f5dca9909400a337c032f7d`.
