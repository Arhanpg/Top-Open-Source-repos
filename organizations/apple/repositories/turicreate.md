# Turi Create

- **Company:** Apple
- **GitHub owner:** [apple](https://github.com/apple)
- **Repository:** [apple/turicreate](https://github.com/apple/turicreate)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/apple/turicreate/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `771c306591ba21343e3d0f04c740ef1721f1bd66`

## Project overview

Turi Create is a Python library designed to simplify development of custom machine-learning models for application use. The README describes task-oriented APIs for recommendations, image classification, object detection, sound classification, image similarity, activity classification and other common ML tasks.

## Features and capabilities documented by the README

- Provides task-specific model creation APIs so developers can focus on the ML task rather than implementing algorithms from scratch.
- Supports text, images, audio, video and sensor data according to the README.
- Includes streaming visualizations for exploring data.
- Documents model tasks including recommenders, image/drawing/sound classification, object detection, one-shot object detection, style transfer, activity classification, image similarity, text classification, regression and clustering.
- Exports trained models to Core ML for use in iOS, macOS, watchOS and tvOS apps.
- The README shows an image-classifier workflow using SFrame, image_classifier.create, predict and export_coreml.

## Technology stack

Python package distributed through pip; SFrame data API; task-specific ML model APIs; Core ML export. The README's listed supported Python versions are 2.7 and 3.5–3.8; supported platforms include macOS, Linux and Windows 10 via WSL.

## Getting started

The README recommends using a Python virtual environment and installing the turicreate package with pip. Consult the linked installation guide for Linux-specific setup and common installation issues.

## Lifecycle, compatibility and operational notes

The Python versions listed in this README are old (2.7 and 3.5–3.8). Treat this as a legacy compatibility signal and verify current package release, Python support and maintenance status before using it for a new project. Do not assume it supports modern Python releases based on current ML ecosystem norms.

## Evaluation guidance

Check the current release, upstream documentation, dependency manifests, supported platforms, licence and maintenance policy before adoption. This README-based dossier is not a complete source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/apple/turicreate)
- [README](https://github.com/apple/turicreate/blob/main/README.md)
- [Issues](https://github.com/apple/turicreate/issues)
- [Releases](https://github.com/apple/turicreate/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology and lifecycle claims are limited to the README evidence; additional manifest and source verification remains separate.*
