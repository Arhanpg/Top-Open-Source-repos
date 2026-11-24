# Repository technical-audit pipeline

## Purpose

Repository inventory and repository technical interpretation are separate activities. An account-level repository count proves that the configured public repository listing was paginated; it does not prove that each project has been technically understood.

The technical-audit runner consumes the committed account checkpoints at:

`organizations/<company>/accounts/<github-account>/inventory.json`

For every processed repository, it writes two companion files under:

`organizations/<company>/accounts/<github-account>/technical-audits/`

- `<repository-slug>-<repository-id>.yaml`: structured, machine-readable technical record.
- `<repository-slug>-<repository-id>.md`: human-readable project dossier.
- `TECHNICAL-AUDIT-INDEX.md`: per-account dossier links and audit status counts.

It also maintains [the global progress file](TECHNICAL-AUDIT-PROGRESS.md). Existing inventory records and curated company-level README briefs are preserved.

## Evidence gathered

For each repository, the runner reads the inventory record and then:

1. Resolves the default branch and obtains its Git tree, recording the tree SHA and truncated flag.
2. Retrieves the README from the recorded path or a README found in the repository tree.
3. Locates up to six build/dependency manifests (for example, package.json, pyproject.toml, go.mod, Cargo.toml, pom.xml and CMakeLists.txt).
4. Extracts conservative dependency-name clues from supported manifest formats.
5. Selects up to four representative source files, prioritizing common entry points and source folders. Their paths and blob SHAs are recorded.
6. Uses the README, manifest contents, language statistics and sampled source excerpts to produce the audit record.

Source sampling is bounded for scale. It is not a line-by-line review of the entire repository.

## Semantic interpretation setting

The workflow can call an OpenAI-compatible chat-completions endpoint to interpret purpose, usage, features, stack categories, architecture, setup and limitations. To enable it, configure these settings in the repository:

- Secret `AUDIT_LLM_API_KEY` (or `OPENROUTER_API_KEY`).
- Repository variable `AUDIT_LLM_MODEL`, set to an exact model identifier supported by the provider.
- Optional repository variable `AUDIT_LLM_BASE_URL`; default is `https://openrouter.ai/api/v1`.

Without both the secret and model variable, the runner generates evidence-only dossiers. It extracts documented purpose text, feature bullets in feature-labelled README sections, language statistics, selected dependencies and setup/limitation excerpts. It deliberately leaves framework, database, runtime, infrastructure and architecture claims unknown when they are not established by deterministic evidence.

A model-generated record is labelled `llm_interpreted`; this does not mean that a human has verified it or that the code was built, tested, security-scanned or reviewed exhaustively. Model errors are recorded as `llm_error`, not mislabelled as successful audits. The model prompt treats upstream repository content as untrusted data and ignores instructions that appear inside source files.

## YAML contents

The schema is versioned in [TECHNICAL-AUDIT-SCHEMA.md](TECHNICAL-AUDIT-SCHEMA.md). Each record includes:

- Project purpose and why the project is used.
- Core features, descriptions and evidence references.
- Technology stack separated into languages, frameworks/libraries, dependencies, build tools, runtimes, databases/storage, infrastructure and platforms.
- Architecture, setup/usage and documented limitations.
- Unknowns, confidence, audit status and evidence fingerprint.
- Repository lifecycle metadata, README SHA, manifest paths, sampled source files and upstream provenance.

Unsupported details are recorded as unknown rather than inferred from a repository name or programming language.

## Status meanings

- `llm_interpreted`: structured model interpretation generated from the supplied upstream evidence.
- `evidence_only`: upstream evidence and deterministic extracts recorded; semantic interpretation remains pending.
- `insufficient_evidence`: no usable README or meaningful description was found.
- `llm_error`: model call failed; deterministic evidence output is retained.
- `manual_reviewed`: a curated dossier was checked manually.

Both the YAML and Markdown file must exist for a repository to be considered already generated. A missing companion file causes the record to be queued again. Unchanged complete model/evidence records are skipped; when a model is configured, eligible evidence-only records are upgraded to model interpretation. An `llm_error` requires a deliberate forced retry.

## Scheduling and resume behaviour

The catalogue Actions workflow runs four times each day. Each run processes a default maximum of 200 technical-audit dossiers, interleaved round-robin across the configured account queues. A run can be narrowed to one company or account, and can force regeneration. Successful outputs are committed together with the collector's inventory checkpoints.

At the default cap, the theoretical upper bound is 800 dossiers per day. Processing 33,522 repository records at that rate would take about 42 days in an ideal uninterrupted run. This is a capacity calculation, not a completion promise: API retries, missing evidence, model latency, provider limits, and workflow queueing can extend it.

The workflow adds pull-request CI that installs PyYAML, compiles the collector and technical-audit scripts, and runs offline unit tests. It skips inventory writes and audit generation for pull requests.

## Important scope limits

- The inventory covers the configured, eligible GitHub accounts. It does not prove that every relevant secondary organization for all 151 source companies has been discovered.
- README claims describe what maintainers document; a bounded source sample cannot prove that every advertised feature is fully implemented or working.
- The runner does not execute projects, build them, run tests, scan vulnerabilities, assess license compliance or perform an exhaustive source-code review.
- Model-generated technical records require spot-checking against the cited upstream evidence before being treated as authoritative.
