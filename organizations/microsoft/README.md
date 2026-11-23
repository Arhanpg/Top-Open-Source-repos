# Microsoft — open-source organization profile

- **GitHub account:** [microsoft](https://github.com/microsoft)
- **Company mapping:** candidate account used for this catalogue; verify through Microsoft's official engineering / open-source pages before treating every associated repository as a corporate project.
- **Source group:** United States & Global
- **Directory status:** initialized; repository list not yet exhaustive
- **Detailed README records:** 16 project briefs currently linked below

## Why this directory matters

The Microsoft account contains a broad public engineering ecosystem spanning developer tools, programming languages, AI and machine learning, data platforms, Windows utilities, browser automation and research projects. This page acts as the entry point to the reviewed project briefs. The list is an initial selection, not a claim that these are the company's only or most important repositories.

## Reviewed projects by theme

| Theme | Projects | What they help explore |
|---|---|---|
| Document ingestion | [MarkItDown](repositories/markitdown.md) | Converting files and media into structured Markdown for downstream processing |
| Browser automation | [Playwright](repositories/playwright.md), [Playwright MCP](repositories/playwright-mcp.md) | Testing, browser scripting and agent-controlled browser workflows |
| Programming languages / editor tooling | [TypeScript](repositories/typescript.md), [Monaco Editor](repositories/monaco-editor.md) | Type-aware JavaScript development and browser-based code editing |
| Quantitative research | [Qlib](repositories/qlib.md) | Financial data processing, modelling and backtesting |
| LLM / retrieval research | [GraphRAG](repositories/graphrag.md) | Graph-based context construction for question answering |
| AI models / inference | [VibeVoice](repositories/vibevoice.md), [BitNet](repositories/bitnet.md) | Speech models and low-bit LLM inference |
| Windows productivity | [PowerToys](repositories/powertoys.md) | Desktop utilities and workflow improvements |
| AI agent development | [Semantic Kernel](repositories/semantic-kernel.md) | Tool-using and multi-agent application patterns; successor guidance included |

## Repository index

Open the [Microsoft repository catalogue](repositories/README.md) for the indexed project list and audit status.

## Reading the technical briefs

Each project page separates the maintainer-documented purpose and features from practical application ideas. It also captures platform requirements, relevant installation paths, lifecycle warnings and direct upstream references where these appear in the README. The technology table is deliberately evidence-limited: implementation details that have not been confirmed from manifests or source files are not guessed.

## Important lifecycle and adoption notes

A few of the reviewed pages contain material caveats:

- GraphRAG's README says the project is largely in maintenance mode and is not accepting feature work.
- Semantic Kernel's README directs new development toward Microsoft Agent Framework and links a migration guide.
- VibeVoice's README records the removal of TTS code from this repository in 2025; current model and code availability should be checked separately.
- Qlib's README contains migration notices for artifact loading and configuration changes in source builds.
- MarkItDown warns that conversion operations run with the privileges of the current process and that untrusted inputs must be handled carefully.

Always use the current upstream README, release notes and security guidance before adopting a project.

## Inventory completeness

The detailed pages below cover selected README-reviewed projects only. The public repository listing for the Microsoft account has not yet been exhaustively fetched and reconciled. The inventory collector can be run using the instructions in [docs/INVENTORY-COLLECTOR.md](../../docs/INVENTORY-COLLECTOR.md).

## Upstream

- [Microsoft GitHub account](https://github.com/microsoft)
- [Microsoft Open Source](https://opensource.microsoft.com/)
- [GitHub repository catalogue](repositories/README.md)


## Additional README-reviewed projects — 23 November 2026

Five additional Microsoft project briefs have been added: Visual Studio Code (Code - OSS), Windows Terminal, Generative AI for Beginners, Web Development for Beginners and AI Agents for Beginners. Their summaries distinguish learning materials from deployable software and retain important licensing, platform and provider lifecycle caveats. See the [repository index](repositories/README.md).
