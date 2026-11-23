# Collector reliability update — 24 November 2026

## Findings from the previous collector setup

A code review identified several mismatches between the documented collector, the GitHub Actions workflow and the verified account mapping:

1. The verified mapping rows use account_type=auto, while the older audit_org_repos.py accepted only org or user.
2. The Actions workflow passed --phase, --enrich-limit and --manifest-limit, but the older collector did not define those arguments.
3. The older collector stored its main resume state in .catalogue-state.json, which is ignored by Git. A fresh Actions runner therefore could not rely on that file being present.
4. Previously completed repositories were skipped for enrichment, while inventory output was rebuilt from current-run in-memory rows. That made cross-run inventory continuity difficult.
5. The root README linked the legacy collector while the workflow invoked a different loader.

## Changes made

- Replaced scripts/catalogue_audit.py with a readable, standard-library-only canonical implementation.
- Added automatic account-type resolution through the public GitHub profile endpoint.
- Added explicit inventory, enrichment, export and combined phases.
- Followed GitHub's pagination Link header rather than assuming one page or a search result represents a complete inventory.
- Persisted account pagination state and repository evidence to tracked inventory.json files after every page and each enrichment.
- Added bounded README excerpts, README heading capture, language-byte statistics and selected manifest-path capture.
- Kept automated evidence capture distinct from manual README review.
- Retained scripts/audit_org_repos.py as a compatibility wrapper to the canonical collector.
- Updated GitHub Actions and collector documentation to use the same CLI.

## Local verification performed

The replacement script passed Python bytecode compilation. Offline mocked tests passed for automatic organization detection, README/language/manifest evidence capture, dossier and account-index generation, skipping a fully paginated account when no refresh is requested, and stopping at a page cap before resuming from the saved next page through the final page.

These are local mocked tests, not a live GitHub Actions run. The workflow still needs an execution in the repository's Actions environment.

## Remaining work

The collector now provides a coherent base for large inventory runs, but company-wide completion still requires discovery and verification of secondary official GitHub accounts, full pagination for each verified account, repeated enrichment batches and eventual human interpretation of the captured evidence.


## Follow-on hardening

- Scheduled refreshes preserve and resume an interrupted scan's next-page checkpoint. A new scheduled scan begins only after the previous pagination run completed.
- Empty organizations remain complete after their first successful empty page and are not mistaken for uninitialized checkpoints.
- Selected small manifests are fetched with a 256 KB per-file cap, and conservative dependency-name clues are extracted for common package formats.
- Per-manifest errors create a partial evidence state instead of being represented as a successful manifest capture.
