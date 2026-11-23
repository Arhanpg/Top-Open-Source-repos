# TypeScript

<sub>Company: Microsoft · Repository: [microsoft/TypeScript](https://github.com/microsoft/TypeScript) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

TypeScript is a language for application-scale JavaScript. It adds optional types to JavaScript and compiles to readable, standards-based JavaScript. The README emphasizes that it is intended to work across browsers, hosts and operating systems rather than being tied to one runtime.

**Problem it addresses:** large JavaScript applications benefit from explicit type information and tooling support, while still needing to run in ordinary JavaScript environments. TypeScript provides a type-aware development layer and emits JavaScript as its compilation output.

## Main capabilities

### Optional static type information

Developers can express types in application code while retaining JavaScript as the emitted language. This is especially relevant when many modules, developers or interfaces need to agree on the shape of data and function contracts.

### JavaScript output

The README states that TypeScript compiles to readable, standards-based JavaScript. That output model lets projects adopt TypeScript within established JavaScript toolchains and runtime environments.

### Developer learning and feedback loop

The project links an interactive TypeScript Playground, a five-minute introduction, a programming handbook and a roadmap. These are the primary learning and discovery resources referenced by the maintainers.

### Stable and nightly package channels

The README documents installation of the latest stable compiler package as well as the `next` nightly build. Teams should choose the release channel deliberately rather than mixing prerelease builds into a production toolchain without testing.

## Installation

For a stable development dependency:

```bash
npm install -D typescript
```

For the nightly channel:

```bash
npm install -D typescript@next
```

The repository README points contributors to the project contribution guide and recommends the handbook and Playground for learning the language.

## Technology profile

| Area | README-supported details |
|---|---|
| Language model | JavaScript superset / typed authoring language |
| Compiler output | Standards-based JavaScript |
| Package manager | npm |
| Package | `typescript` |
| Developer tooling | TypeScript Playground, handbook and compiler |
| Ecosystem | Browser, host and operating-system agnostic JavaScript environments |

This entry intentionally describes the public product model rather than guessing the language mix of the compiler's internal implementation. A source-level stack inventory would require a separate inspection of repository manifests and build configuration.

## Where it fits

TypeScript is commonly selected for projects that need stronger contracts across modules, editor/tooling support and safer refactoring while continuing to deploy JavaScript. The README's application-scale framing makes it relevant to front-end applications, Node.js services, libraries and shared packages, provided the target environment can run the emitted JavaScript.

## Useful upstream documentation

- [TypeScript Playground](https://www.typescriptlang.org/play/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript in 5 minutes](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
- [Roadmap](https://github.com/microsoft/TypeScript/wiki/Roadmap)
- [Contribution guide](https://github.com/microsoft/TypeScript/blob/main/CONTRIBUTING.md)
- [Repository README](https://github.com/microsoft/TypeScript/blob/main/README.md)

**Evidence note:** README blob inspected: `7b8798935325f17edb0c2cb3a6efd372490dc798`.
