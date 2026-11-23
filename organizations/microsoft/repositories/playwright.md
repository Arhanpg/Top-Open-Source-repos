# Playwright

<sub>Company: Microsoft · Repository: [microsoft/playwright](https://github.com/microsoft/playwright) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

Playwright is a browser automation and testing framework. It provides one programming interface for driving Chromium, Firefox and WebKit, and the README positions it for end-to-end tests, standalone browser scripts and AI-agent workflows.

**Problem it addresses:** browser behaviour differs across engines and test automation is often fragile when it relies on fixed sleeps, low-level selectors or manual setup. Playwright provides browser-aware waiting, resilient locators, isolated contexts and debugging traces to make automated browser work more repeatable.

## Project surfaces

The upstream README describes several related ways to use Playwright:

| Surface | Best fit described in the README |
|---|---|
| Playwright Test | End-to-end testing with a dedicated test runner |
| Playwright CLI | Browser automation from coding-agent workflows |
| Playwright MCP | LLM agents interacting with pages through the Model Context Protocol |
| Playwright Library | Programmatic browser automation scripts |
| VS Code extension | Test authoring, running and debugging in the editor |

These are complementary interfaces around the Playwright browser-automation ecosystem; they should not be confused with separate browser engines.

## Core capabilities

### Cross-browser automation

The same API can drive Chromium, Firefox and WebKit. The test runner can execute a suite across configured browser projects, which is useful when behaviour needs to be checked beyond a single browser.

### Auto-waiting and web-first assertions

The test runner waits for an element to become actionable and assertions retry until the expected condition is met. This reduces the need for arbitrary fixed delays and helps tests synchronize with real page state.

### Resilient locators

The README recommends locators that reflect how a user perceives the interface, such as roles, labels, placeholders and test IDs. Example locator patterns include `getByRole`, `getByLabel`, `getByPlaceholder` and `getByTestId`.

### Test isolation and authentication reuse

Each test receives a separate browser context, equivalent to a clean browser profile. The README also demonstrates saving authentication state and reusing it in later tests, avoiding the need to repeat interactive login in every test.

### Tracing and diagnosis

Playwright can capture traces, screenshots and videos on failure. Its Trace Viewer exposes actions, DOM snapshots, network requests and console messages, helping developers understand why a browser test failed.

### Parallel execution

Tests run in parallel by default across configured browsers. This is designed to improve suite throughput while preserving context isolation.

## Typical test workflow

A minimal test from the README navigates to a page, checks its title, follows a link and asserts that a target heading appears:

```typescript
import { test, expect } from "@playwright/test";

test("opens the installation guide", async ({ page }) => {
  await page.goto("https://playwright.dev/");
  await page.getByRole("link", { name: "Get started" }).click();
  await expect(
    page.getByRole("heading", { name: "Installation" })
  ).toBeVisible();
});
```

The README's documented setup is:

```bash
npm init playwright@latest
npx playwright test
```

## Library use beyond testing

The library can also be used without the test runner. The README gives examples for:

- Capturing page screenshots.
- Generating PDFs from pages.
- Emulating a mobile device profile.
- Intercepting and aborting matching network requests.

That makes Playwright applicable to browser-based data collection, report generation and controlled web-workflow automation, subject to the target site's terms and access rules.

## Technology profile

| Area | README-supported details |
|---|---|
| Package ecosystem | npm |
| Main API examples | TypeScript |
| Browser engines | Chromium, Firefox and WebKit |
| Test runner | `@playwright/test` |
| Automation interfaces | CLI, MCP server, library and VS Code extension |
| Debugging | Trace Viewer, screenshots, videos and browser/network traces |

The project is TypeScript/JavaScript-oriented in its documented examples. Other language bindings or implementation details should be recorded only after examining the relevant package and source files.

## Practical use cases

- Regression testing of a web application's user journeys.
- Cross-browser compatibility checks.
- Generating screenshots and PDFs in an automated backend job.
- Reproducing and diagnosing UI failures with trace artifacts.
- Browser-based research or extraction workflows where a real browser is necessary.
- Giving a controlled browser interface to an AI agent through CLI or MCP.

## Important design considerations

Use stable, user-facing locators wherever possible instead of depending on brittle CSS structure. Keep browser contexts isolated when test state must not leak between cases. Store authentication state securely, especially in CI environments. Network interception and page interaction should be used only where the operator is authorized to automate the target site.

## Upstream references

- [Repository](https://github.com/microsoft/playwright)
- [Primary README](https://github.com/microsoft/playwright/blob/main/README.md)
- [Playwright documentation](https://playwright.dev/docs/intro)
- [API reference](https://playwright.dev/docs/api/class-playwright)
- [Trace Viewer](https://playwright.dev/docs/trace-viewer)
- [Playwright CLI](https://github.com/microsoft/playwright-cli)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)

**Evidence note:** README blob inspected: `d22da6f2f507fd793d9d463401d7fbf66eec3275`.
