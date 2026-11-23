# Repository documentation schema

Every repository entry must be evidence-backed. Keep unknown fields as Unknown.

| Field | Required evidence |
|---|---|
| Repository | Canonical upstream URL and stable GitHub repository ID |
| README | Direct README URL on the default branch and README blob SHA |
| Default branch | GitHub repository metadata |
| Description | Upstream GitHub description; do not treat it as an independent assessment |
| Purpose | README explanation, summarized faithfully by a human reviewer |
| Key features | README feature list / documented usage |
| Languages | GitHub Languages API; note that it measures detected code bytes |
| Frameworks / libraries | README plus dependency manifests (package.json, pyproject.toml, pom.xml, Cargo.toml, go.mod, etc.) |
| Infrastructure | README and deployment / infrastructure configuration |
| License | Upstream license metadata and, when needed, license file |
| Archived / fork / disabled | GitHub repository metadata |
| Last updated / pushed | GitHub repository metadata with retrieval timestamp |
| Evidence capture status | Metadata only / evidence captured / README unavailable / capture incomplete |
| Manual review status | Pending / README reviewed |
| Reviewed on | Date of human inspection |
| Evidence | Direct links to README sections and manifests |

Do not state that a repository uses a framework merely because a badge or filename exists. Separate programming languages from frameworks, libraries, build systems, model runtimes and infrastructure.
