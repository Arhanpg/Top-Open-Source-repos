# NVIDIA Container Toolkit

- **Company:** NVIDIA
- **GitHub owner:** [NVIDIA](https://github.com/NVIDIA)
- **Repository:** [NVIDIA/nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/NVIDIA/nvidia-container-toolkit/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `28f495e38d1c3ad5dfa6d5ab13cd319eb23bf92e`

## Project overview

NVIDIA Container Toolkit allows users to build and run GPU-accelerated containers. The README says it includes a container runtime library and utilities that automatically configure containers to use NVIDIA GPUs.

## Features and capabilities documented by the README

- Provides tools for running GPU-accelerated containers.
- Includes a container runtime library through the separate libnvidia-container project.
- Automatically configures containers to leverage NVIDIA GPUs.
- Provides documentation links for architecture, platform support, installation and usage.
- The user guide covers configuration and command-line options when running GPU containers with Docker.

## Technology stack

NVIDIA Container Toolkit; libnvidia-container runtime library; Linux NVIDIA driver; container runtime integration and Docker usage documented by the user guide. The README says the host does not need the CUDA Toolkit installed, but does require an NVIDIA driver.

## Getting started

Install the NVIDIA driver for the Linux distribution first, then follow the official NVIDIA Container Toolkit installation guide. The README explicitly notes that the CUDA Toolkit does not need to be installed on the host for the toolkit's basic setup.

## Lifecycle, compatibility and operational notes

This is the active replacement project linked by the archived nvidia-docker repository. Keep the NVIDIA driver and toolkit versions compatible and follow the current official installation guide for the target Linux distribution and container runtime.

## Evaluation guidance

Check the current release, upstream documentation, dependency manifests, supported platforms, licence and maintenance policy before adoption. This README-based dossier is not a complete source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/NVIDIA/nvidia-container-toolkit)
- [README](https://github.com/NVIDIA/nvidia-container-toolkit/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nvidia-container-toolkit/issues)
- [Releases](https://github.com/NVIDIA/nvidia-container-toolkit/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology and lifecycle claims are limited to the README evidence; additional manifest and source verification remains separate.*
