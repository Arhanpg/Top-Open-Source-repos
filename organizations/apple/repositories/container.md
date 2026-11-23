# container

- **Company:** apple
- **Repository:** https://github.com/apple/container
- **README:** https://github.com/apple/container/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** 7077937f1c3d362ab32a6488cc9e2f9164b001c8

## What it does

A tool for creating and running Linux containers as lightweight virtual machines on Mac, written in Swift and optimized for Apple silicon.

## Features documented by the upstream README

- Consumes and produces OCI-compatible container images.
- Pulls and runs images from standard container registries and can push images built locally.
- Uses the Apple Containerization Swift package for low-level container, image and process management.
- Provides a command-line interface and lifecycle commands for starting, stopping, upgrading and running containers.

## Technology stack

Swift; macOS 26 or later; Apple silicon; Apple Containerization Swift package; OCI-compatible container images and registries.

## Notes and limitations

The README explicitly states the Mac / Apple-silicon requirement and macOS 26+ design target.

## Evidence

This record summarizes the upstream README linked above. Dependency manifests, source files, CI workflows and release artifacts were not exhaustively examined in this pass. Do not interpret this summary as a full source-code security or architecture audit.
