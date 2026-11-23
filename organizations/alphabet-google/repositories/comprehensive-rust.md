# Comprehensive Rust

- **Company grouping:** Alphabet / Google
- **GitHub organization:** [google](https://github.com/google)
- **Repository:** [google/comprehensive-rust](https://github.com/google/comprehensive-rust)
- **Default branch:** master/main (verify from repository metadata)
- **README:** [Open upstream README](https://github.com/google/comprehensive-rust/blob/master/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `cc4b760db424d5c5c8bc8ba39fc4a244e571d679`

## Project overview

The source repository for a multi-day Rust course developed by Google's Android team. It teaches Rust from basic syntax through generics and error handling, with deeper material for Android, Chromium, bare-metal programming and concurrency.

## Features and capabilities

- Classroom-oriented course designed for experienced software engineers, often with C++ or Java backgrounds.
- Includes exercises, code examples and specialist deep dives for Android, Chromium, bare-metal programming and concurrency.
- Course content is published as a browsable book through GitHub Pages.
- Provides commands to install build tools, serve the course locally, run Rust snippet tests, run web-driver tests and build static course content.
- Includes translation workflows and separate code/documentation licensing notes.

## Technology stack

Rust toolchain; mdBook; mdbook-svgbob; mdbook-i18n-helpers; mdbook-exerciser; mdbook-course; mdbook-linkcheck2; Bazel/Bazelisk; Cargo xtask command runner.

## Getting started

Install Rust via rustup and Bazel via Bazelisk, clone the repository and run cargo xtask install-tools. The README lists cargo xtask serve, rust-tests, web-tests and build as common project commands.

## Lifecycle and operational considerations

The maintainers say the course is less ideal for self-study because classroom discussion and compiler-error walkthroughs are part of the teaching method. Source code and embedded code examples are Apache 2.0; documentation, Markdown and images are CC BY 4.0.

## Evaluation guidance

Check the exact release, manifests, supported platforms, licence and maintenance policy before adopting the project. This dossier is based on the upstream README, not a full source-code, vulnerability or performance audit.

## Upstream references

- [Repository](https://github.com/google/comprehensive-rust)
- [README](https://github.com/google/comprehensive-rust/blob/master/README.md)
- [Issues](https://github.com/google/comprehensive-rust/issues)
- [Releases](https://github.com/google/comprehensive-rust/releases)

*Evidence note: README blob SHA identifies the upstream version inspected. Technology claims are limited to the README's evidence; implementation details not established by that source are not inferred.*
