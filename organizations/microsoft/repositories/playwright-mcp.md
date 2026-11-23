# Playwright MCP

<sub>Company: Microsoft · Repository: [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

Playwright MCP is a Model Context Protocol server that exposes Playwright browser automation to LLM-based agents. Instead of asking an agent to interpret every page through screenshots, the server provides structured accessibility snapshots that describe page elements and their relationships.

**Problem it addresses:** agents need a reliable way to locate and manipulate page controls. Screenshot-only automation can be ambiguous and can require visual models. The MCP server exposes structured page information that can be referenced by tools and agent workflows.

## How the interaction model works

At a high level, an MCP client launches the server. The agent requests browser actions, the server uses Playwright to interact with the page, and the page is represented to the agent through an accessibility-oriented structure. Element references can then be used for actions such as clicking and typing.

The README illustrates a page represented through headings, textboxes, list items and element references. This is intended to reduce uncertainty about which page element an action targets.

## Key capabilities

- **Accessibility-tree interaction:** operates on structured accessibility information rather than pixel coordinates.
- **LLM-friendly representation:** the README describes the approach as avoiding a requirement for vision models to interpret the page.
- **Deterministic tool application:** structured element references can reduce ambiguity in browser actions.
- **Browser automation via Playwright:** builds on Playwright's navigation and interaction capabilities.
- **Broad MCP-client configuration:** the README documents setup examples for clients such as VS Code, Cursor, Claude Desktop and other agent environments.

The repository README also compares MCP with Playwright CLI. It suggests CLI plus skills for high-throughput coding-agent workflows where compact commands are preferred, while MCP may suit longer-running agent loops that benefit from persistent state and page introspection.

## Technology profile

| Area | README-supported details |
|---|---|
| Runtime | Node.js 20 or newer |
| Protocol | Model Context Protocol (MCP) |
| Browser automation | Playwright |
| Page representation | Structured accessibility snapshots |
| Configuration | MCP server JSON / client-specific configuration |
| Client examples | VS Code, Cursor, Windsurf, Claude Desktop, Goose, Grok, Junie and others |

## Installation / configuration

The README shows the standard configuration pattern below for an MCP client that supports command-based servers:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Some clients use their own configuration file or UI. Follow the current installation instructions for the client you use, and check the README for client-specific examples.

## Good fit

- Agent-assisted web testing and exploratory QA.
- Web research tasks that require navigation and form interaction.
- Long-running browser sessions where the agent needs to inspect page structure repeatedly.
- Self-healing test experiments that inspect live DOM/accessibility information.
- Controlled browser automation within an MCP-compatible agent ecosystem.

## Boundaries and cautions

The MCP server is a browser-control interface, not a guarantee that an agent understands the page correctly. Accessibility quality varies across websites. Actions can still fail because of authentication, dynamic content, permissions, anti-automation controls or site changes. Use only on sites and accounts where automation is authorized, and protect session credentials.

For coding agents that need compact, high-throughput commands, evaluate the companion [Playwright CLI](https://github.com/microsoft/playwright-cli) as the README recommends.

## Upstream references

- [Repository](https://github.com/microsoft/playwright-mcp)
- [Primary README](https://github.com/microsoft/playwright-mcp/blob/main/README.md)
- [Playwright documentation](https://playwright.dev/)
- [MCP introduction](https://playwright.dev/mcp/introduction)
- [Playwright CLI](https://github.com/microsoft/playwright-cli)

**Evidence note:** README blob inspected: `4b9fa171c615e6ace19011a04c28527449be0e46`.
