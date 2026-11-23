# PaddleOCR

- Company association: Baidu
- Upstream GitHub account: [PaddlePaddle](https://github.com/PaddlePaddle)
- Repository: [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- Default branch: main
- README: [Open upstream README](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: d3a9c16b6b5672a872d6ad7473ff52aceb7712bb
- Account relationship: Baidu's verified profile lists this account under affiliated organizations; this is a project relationship, not blanket ownership of every repository.

## Project overview

An OCR and document-understanding toolkit covering text detection and recognition, multilingual OCR, document parsing and structured extraction. The README describes model families for scene-text OCR and document parsing, including PP-OCR, PP-StructureV3 and PaddleOCR-VL.

## Features and capabilities documented by the README

- Provides text detection and recognition pipelines for printed and scene text.
- PP-OCRv6 offers tiny, small and medium model tiers; the README describes a 50-language unified recognition model in its 2026 release notes.
- PaddleOCR-VL is a compact vision-language model for document parsing, with the README describing text, tables, formulas, charts and complex document elements across more than 100 languages.
- PP-StructureV3 supports document parsing and structured output; the README describes conversion of Word, Excel and PowerPoint content to Markdown and parsed results to DOCX.
- The PaddleOCR.js browser SDK runs PP-OCRv5 directly in the browser.
- Supports model conversion to ONNX and high-performance inference through OpenVINO, ONNX Runtime and TensorRT.
- Offers local Python pipelines, C++ local deployment, service-oriented deployment and HTTP invocation.

## Technology stack

PaddlePaddle deep-learning framework; Python (the README's supported environment table lists Python 3.8–3.12); C++ deployment; Paddle Inference; ONNX Runtime; Transformers backend; ONNX model conversion; OpenVINO; TensorRT; PaddleOCR.js for browser inference. The README lists Linux, Windows and macOS, and CPU/GPU plus XPU/NPU deployment paths.

## Getting started

Start with the installation guide and choose the pipeline that matches the use case: PP-OCR for text recognition, PaddleOCR-VL for document parsing, or PP-StructureV3 for structured document workflows. The README links the online Experience Center and local deployment guides; the 3.x release line separates core and optional dependencies.

## Lifecycle, compatibility and operational considerations

The repository has several independently evolving model families. The README's release notes include different language coverage for PP-OCRv6 and PaddleOCR-VL; do not collapse these into one guarantee for every model. Hardware acceleration depends on matching PaddlePaddle, CUDA and device versions. Performance and accuracy claims in release notes are upstream-reported, not independently reproduced.

## Evaluation guidance

Check the exact upstream release, source manifests, platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a complete source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/PaddlePaddle/PaddleOCR)
- [README](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)
- [Issues](https://github.com/PaddlePaddle/PaddleOCR/issues)
- [Releases](https://github.com/PaddlePaddle/PaddleOCR/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Technical claims are limited to README-supported material; details not established by the README are left unspecified.
