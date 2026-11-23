# zx — JavaScript shell scripting utility

- **Company grouping:** Alphabet / Google
- **GitHub organization:** [google](https://github.com/google)
- **Repository:** [google/zx](https://github.com/google/zx)
- **Default branch:** master/main (verify from repository metadata)
- **README:** [Open upstream README](https://github.com/google/zx/blob/master/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `fa45dba2135b2488a228a896e60a6c10d6ba5199`

## Project overview

zx is a JavaScript package for writing shell scripts with more convenient abstractions than the raw Node.js child_process APIs. Its README describes cross-platform wrappers around child_process, argument escaping and sensible defaults.

## Features and capabilities

- Provides a tagged-template command helper for invoking shell commands from JavaScript.
- Escapes interpolated arguments and reduces common shell-quoting work.
- Supports asynchronous command execution and parallel command execution with Promise.all.
- Makes complex shell automation approachable in JavaScript while retaining access to shell commands.
- Links setup options, examples, a lite variant and TypeScript usage guidance.

## Technology stack

JavaScript package distributed through npm. The README lists Node.js 12.20+, Bun 1.0+, Deno 1.x/2.x, GraalVM Node.js and Electron 11+ compatibility. Both CommonJS and ESM modules are supported, with JavaScript/TypeScript usage guidance.

## Getting started

Install the zx package from npm and follow the README's setup instructions for the chosen module/runtime mode. The project documentation includes examples and a separate zx@lite option.

## Lifecycle and operational considerations

The README explicitly states that zx is not an officially supported Google product. Shell behaviour still depends on the available shell and installed command-line tools; interpolation escaping does not make arbitrary untrusted command design safe.

## Evaluation guidance

Check the exact release, manifests, supported platforms, licence and maintenance policy before adopting the project. This dossier is based on the upstream README, not a full source-code, vulnerability or performance audit.

## Upstream references

- [Repository](https://github.com/google/zx)
- [README](https://github.com/google/zx/blob/master/README.md)
- [Issues](https://github.com/google/zx/issues)
- [Releases](https://github.com/google/zx/releases)

*Evidence note: README blob SHA identifies the upstream version inspected. Technology claims are limited to the README's evidence; implementation details not established by that source are not inferred.*
