# Technical-audit YAML schema

One YAML record and one Markdown dossier are generated per repository at:

`organizations/<company>/accounts/<account>/technical-audits/<repository-slug>-<repository-id>.yaml`

The YAML is the canonical structured record. The adjacent Markdown file is its reader-friendly companion. Current schema version: `1.0`.

```yaml
schema_version: "1.0"
audit_status: "llm_interpreted | evidence_only | insufficient_evidence | llm_error | manual_reviewed"
generated_at: "ISO-8601 UTC timestamp"
evidence_fingerprint: "sha256"
repository_metadata:
  company: ""
  account: ""
  full_name: "owner/repository"
  repository_id: 0
  url: "https://github.com/owner/repository"
  description: null
  default_branch: ""
  license_spdx: null
  archived: false
  fork: false
  disabled: false
  pushed_at: null
  stars: null
  readme_url: null
  readme_path: null
  readme_sha: null
  manifest_paths: []
  source_files_inspected: []
  repository_tree:
    status: "captured | unavailable_or_empty | unavailable | not_collected_for_manual_sample"
    sha: null
    truncated: false
  source_code_review: "Selected source files only; not exhaustive."
analysis:
  purpose: ""
  why_used: ""
  core_features:
    - name: ""
      description: ""
      evidence: []
  technology_stack:
    languages: []
    frameworks_and_libraries: []
    dependencies: []
    build_and_package_tools: []
    runtimes: []
    databases_and_storage: []
    infrastructure: []
    platforms: []
  architecture: ""
  setup_and_usage: []
  limitations: []
  unknowns: []
  confidence: "high | medium | low"
evidence_sources: []
```

Values shown as alternatives are illustrative. Each generated record contains concrete values or explicitly unknown fields. A language statistic is not evidence of a framework; a manifest filename is not proof that a particular framework is used.
