# Playwright MCP

- **Company:** Microsoft
- **Repository:** https://github.com/microsoft/playwright-mcp
- **README:** https://github.com/microsoft/playwright-mcp/blob/main/README.md
- **Default branch:** main
- **Audit status:** README reviewed
- **README blob SHA at inspection:** 4b9fa171c615e6ace19011a04c28527449be0e46

## What it does

A Model Context Protocol server that provides browser automation to LLMs using Playwright and structured accessibility snapshots.

## Features documented by the upstream README

- Enables browser interaction through structured accessibility information rather than pixel-based screenshots.
- Designed to be LLM-friendly and deterministic.
- README documents integration with MCP clients including VS Code, Cursor and Claude Desktop.
- Discusses when MCP is useful relative to Playwright CLI for coding agents.

## Technology stack

Node.js 20+ runtime; Model Context Protocol; Playwright browser automation.

## Notes and limitations

README differentiates the MCP server from the CLI + skills approach for coding agents.

## Evidence

This summary is based on the upstream README linked above. Repository manifests, source code, CI workflows and release artifacts were not exhaustively audited in this pass; therefore the technology stack is limited to what the README explicitly supports.
