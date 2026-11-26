# amazon-science/XplainRecommendation

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/XplainRecommendation](https://github.com/amazon-science/XplainRecommendation)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/XplainRecommendation/blob/main/README.md)
- README blob SHA: 2f217d3b1f5f8d956c9d5ad3eff3d364a8a4ed63
- README bytes captured: 18201
- README truncated at capture limit: False
- Repository ID: 1353867861
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Code accompanying "Pairwise Ranking Outperforms Single-Action RL for Offline Explanation Selection: A Practical Lesson" (Tanay Chowdhury, Saeideh Shahrokh Esfahani — RecSys 2026, Research & Practice Notes track).

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:49:47+00:00

### Short excerpt (up to 300 words)

> Arguments: --variants ppo,grpo,dpo,distillation (default: python3 movielens/pipeline/build_tables.py Files that must exist

### README headings

- XplainRecommendation
- 0. What's in here
- 1. Prerequisites
- 2. Running the data-prep pipeline
- 3. Evaluating baselines
- 4. Training and evaluating our methods
- 4a. LambdaRank
- → LambdaRank F1 = 0.5003 ± 0.0947 (n=2958)
- 4b. PPO (single seed, baseline reward)
- 4c. GRPO
- 4d. DPO
- 4e. Distillation
- 4f. Full 5-seed sweep (all four methods)
- Results: results/experiments/<variant>/seed{42..46}.json
- Rollup:  results/experiments/summary.json
- 4g. MovieLens pipeline
- Stage 1: build features + tables + LambdaRank (~30 min CPU, uses cached pool)
- Stage 2: 5-seed RL sweep (4 variants)
- Stage 3: BART + USR scoring for all methods
- 5. Results summary
- 5.1 Google Local results
- BERTScore-F1 (primary metric)
- All three metrics (Google Local)
- 5.2 MovieLens-1M results
- BERTScore-F1 (primary metric)
- All three metrics (MovieLens)
- 6. Reproduction sanity check
- Split integrity
- Baselines
- LambdaRank

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Rollup:  results/experiments/summary.json

> Arguments: --variants ppo,grpo,dpo,distillation (default:

### Features and capabilities: Stage 1: build features + tables + LambdaRank (~30 min CPU, uses cached pool)

> python3 movielens/pipeline/build_tables.py

### Technology and requirements: 1. Prerequisites

> Files that must exist

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 344,652 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: bert-score, boto3, evaluate, lightgbm, numpy, pandas, scikit-learn, sentence-transformers, torch, tqdm, transformers, xgboost

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-09-01T18:34:59Z
- Last pushed: 2026-09-01T18:34:29Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/XplainRecommendation)
- [README](https://github.com/amazon-science/XplainRecommendation/blob/main/README.md)
- [Issues](https://github.com/amazon-science/XplainRecommendation/issues)
- [Releases](https://github.com/amazon-science/XplainRecommendation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
