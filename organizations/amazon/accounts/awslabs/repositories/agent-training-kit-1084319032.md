# awslabs/agent-training-kit

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/agent-training-kit](https://github.com/awslabs/agent-training-kit)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/agent-training-kit/blob/main/README.md)
- README blob SHA: 7272ac2bf229efeabecbf978e2f02e5f6b934374
- Repository ID: 1084319032
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:02:32+00:00

### Short excerpt (up to 100 words)

> Agent Training Kit (ATK) makes Strands Agents trainable — agents learn from their tool usage and task execution results, improving through experience. ATK adapts rLLM for Strands Agents, handling agent execution, trajectory collection, and reinforcement learning. *Figure 1: Agent Training Kit training workflow and data flow* Python file names match the component labels shown in Figure 1. ├── agentboost │ ├── agents │ │ ├── strands_agent.py # strands agent wrapper │ │ ├── strands_process_pool.py # parallel process execution of agents │ │ └── strands_worker.py # agent worker managed by the process pool │ ├── environments │ │ └── strands_env.py #

### README headings

- Agent Training Kit
- Agent Training Kit lets developers build trainable Strands Agents in just a few lines of code.
- Code structure
- Installation
- Create constraints file to lock Pytorch version
- Verify CUDA setup
- Verify vLLM
- Verify Flash Attention
- Quick Start - DeepCoder 🎯
- Prepare the dataset for coding
- Run the coding example
- Quick Start - Tau2-Bench
- Install tau2-bench
- Prepare the dataset for tau2-bench
- Run the Tau2-bench example
- Preliminary Results
- Tool Usage  🔧
- Stats from training 20 steps
- Tool calling Breakdown
- Coding Trajectories 🔄
- Tau2-Bench Trajectories
- [Airline Example](examples/tau2/exp_traj_airline_4_steps.json)
- [Retail Example](examples/tau2/exp_traj_retail_3_steps.json)
- Contributing
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 253,796 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 31
- Forks at capture: 4
- Last updated: 2026-08-15T07:10:41Z
- Last pushed: 2025-12-15T06:13:30Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/agent-training-kit)
- [README](https://github.com/awslabs/agent-training-kit/blob/main/README.md)
- [Issues](https://github.com/awslabs/agent-training-kit/issues)
- [Releases](https://github.com/awslabs/agent-training-kit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
