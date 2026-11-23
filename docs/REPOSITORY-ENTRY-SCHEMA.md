# Repository documentation schema

Every repository entry must be evidence-backed. Keep unknown fields as `Unknown`.

| Field | Required evidence |
|---|---|
| Repository | Canonical upstream URL |
| README | Direct README URL on the default branch |
| Default branch | GitHub repository metadata |
| Description | Upstream GitHub description |
| Purpose | README explanation, summarized faithfully |
| Key features | README feature list / documented usage |
| Languages | GitHub Languages API; note it measures detected code bytes |
| Frameworks / libraries | README plus dependency manifests (package.json, pyproject.toml, pom.xml, Cargo.toml, etc.) |
| Infrastructure | README and deployment / infra configuration |
| License | Upstream license metadata and license file |
| Archived | GitHub repository metadata |
| Last updated | GitHub metadata |
| Status | README reviewed / metadata only / README unavailable |
| Reviewed on | Date of inspection |
| Evidence | Direct links to README sections and manifests |

Do not state that a repository uses a framework merely because a badge appears without further evidence. Separate programming languages from frameworks, libraries, build systems, and infrastructure.
