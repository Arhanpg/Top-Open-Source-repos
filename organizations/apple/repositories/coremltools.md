# Core ML Tools

- **Company:** Apple
- **GitHub organization:** [apple](https://github.com/apple)
- **Repository:** [apple/coremltools](https://github.com/apple/coremltools)
- **Default branch:** main
- **README:** [Open upstream README](https://github.com/apple/coremltools/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `2e12b0a22523e2c10bb34cef86327adac3a506df`

## Project overview

Core ML Tools is a Python package for converting trained machine-learning models from third-party frameworks into the Core ML format, so they can be integrated into Apple applications.

## Features and capabilities

- Converts models from TensorFlow 1.x/2.x and PyTorch.
- Supports conversion of models from scikit-learn, XGBoost and LibSVM non-neural frameworks.
- Can read, write and optimize Core ML models.
- Can verify conversion/creation on macOS by running predictions using Core ML.
- Produces Core ML models that can be integrated into apps through Xcode.

## Technology stack

Python package distributed through PyPI; model-conversion integrations include TensorFlow, PyTorch, scikit-learn, XGBoost and LibSVM. The target model format is Apple's Core ML model representation.

## Getting started

Install coremltools through pip. Use the official documentation's installation guide and framework-specific conversion examples for setup and verification.

## Platform, lifecycle and operational considerations

The README distinguishes Core ML Tools (model conversion and manipulation) from Core ML itself (the Apple framework used by apps). Core ML runs models on-device and can use CPU, GPU and Neural Engine resources; conversion verification is documented for macOS.

## Evaluation guidance

Check release-specific documentation, manifests, supported hardware/OS versions, licence and security guidance before adopting the project. This dossier summarizes the upstream README and is not a full source-code, security or performance audit.

## Upstream references

- [Repository](https://github.com/apple/coremltools)
- [README](https://github.com/apple/coremltools/blob/main/README.md)
- [Issues](https://github.com/apple/coremltools/issues)
- [Releases](https://github.com/apple/coremltools/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology claims are limited to the README; additional manifest and source-level verification remains a separate step.*
