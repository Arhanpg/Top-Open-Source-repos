# LangExtract

- **Company:** alphabet-google
- **Repository:** https://github.com/google/langextract
- **README:** https://github.com/google/langextract/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** 7fdba9d5d447e20aeabbf58288ed523d8ef5c43b

## What it does

A Python library that uses LLMs to extract structured information from unstructured text according to user-defined instructions, while grounding extracted details back to the source text.

## Features documented by the upstream README

- Maps every extraction to its exact source location for traceability and visual highlighting.
- Uses few-shot examples to guide consistent structured outputs.
- Processes long documents with text chunking, parallel extraction and multiple passes.
- Generates a self-contained interactive HTML visualization to inspect extracted entities in context.
- README contents include support paths for Gemini, OpenAI models and local LLMs with Ollama.

## Technology stack

Python library / PyPI; LLM provider integrations documented for Gemini, OpenAI and local Ollama workflows; structured output and interactive HTML visualization.

## Notes and limitations

README describes extraction grounding and schema control as core design goals; model-provider compatibility details should be checked against current documentation.

## Evidence

This record summarizes the upstream README linked above. Dependency manifests, source files, CI workflows and release artifacts were not exhaustively examined in this pass. Do not interpret this summary as a full source-code security or architecture audit.
