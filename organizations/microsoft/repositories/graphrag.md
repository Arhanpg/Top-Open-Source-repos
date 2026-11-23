# GraphRAG

<sub>Company: Microsoft · Repository: [microsoft/graphrag](https://github.com/microsoft/graphrag) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

GraphRAG is a research project exploring how graph structures can form targeted context for question answering. The repository describes a data pipeline and transformation suite that uses large language models to extract meaningful structured data from unstructured text. The intended direction is to improve reasoning over private or organization-specific information by using knowledge-graph memory structures as part of the context supplied to an LLM.

**Problem it explores:** retrieving isolated text fragments is not always enough for questions that depend on relationships, entities or broader themes spread across a document collection. GraphRAG investigates graph-based context construction as a way to support those questions.

## What the repository provides

The README describes the project at a high level as:

- A pipeline for transforming unstructured text into structured data with LLM assistance.
- A methodology using knowledge-graph memory structures to enhance LLM outputs.
- A command-line quickstart and supporting documentation.
- Prompt-tuning guidance for adapting the approach to a particular dataset.
- Responsible-AI documentation describing intended uses, evaluation, limitations and operational considerations.

The repository README is a project overview rather than a full architecture specification. Detailed indexing stages, storage components, prompts and query modes should be taken from the linked documentation for the exact version being deployed.

## Workflow concepts

A typical use of the system, at the level described by the maintainers, involves preparing a corpus, running the GraphRAG indexing pipeline, and using the resulting graph-derived context to support question answering. The README emphasizes that indexing can be expensive and asks users to read the documentation and begin with a small dataset.

Prompt tuning is also called out as important: using the supplied approach without adapting prompts to the user's data may not produce the best results. This means domain-specific evaluation and prompt iteration are part of practical adoption, not optional afterthoughts.

## Technology profile

| Area | README-supported details |
|---|---|
| Core approach | LLM-assisted text transformation and knowledge-graph context |
| Distribution | Python package on PyPI (`graphrag`) |
| Interface | Command-line quickstart |
| Main data type | Unstructured text transformed into structured data |
| Reasoning pattern | Graph-based context for question answering |
| Documentation | Project docs, prompt-tuning guide and responsible-AI FAQ |

The README does not provide a complete technology bill of materials. Database engines, model providers and deployment architecture should be recorded only after inspecting the version-specific documentation and configuration files.

## Getting started and evaluation

The maintainers recommend beginning with the [command-line quickstart](https://microsoft.github.io/graphrag/get_started/). Before indexing a large private corpus:

1. Read the configuration and prompt-tuning documentation.
2. Test on a small, representative dataset.
3. Measure indexing cost and query quality.
4. Evaluate whether graph-derived context is actually improving the target question-answering tasks.
5. Review the responsible-AI FAQ and limitations before handling sensitive or consequential data.

The repository also documents version and configuration migrations. The README says to reinitialize configuration between minor version changes and provides a migration notebook for major version changes; because initialization can overwrite configuration and prompts, back them up first.

## Lifecycle and support status

The README contains an explicit warning that GraphRAG is **largely in maintenance mode**. The maintainers state that they are not accepting new pull requests or implementing new features, while bug fixes and dependency updates may still be considered, particularly for CVEs. This lifecycle information is important when evaluating the project for a long-lived production dependency.

The README also clarifies that the code is a research demonstration and is not an officially supported Microsoft offering. Treat this distinction as part of any risk assessment.

## Potential applications

- Exploring relationships across large private document collections.
- Question answering where entity or topic relationships may matter.
- Research into graph-augmented context construction for LLMs.
- Evaluating structured extraction and retrieval approaches on internal corpora.

These are use cases suggested by the repository's stated research goals; they are not a guarantee of accuracy, suitability or support for any particular dataset.

## Upstream references

- [Repository](https://github.com/microsoft/graphrag)
- [Primary README](https://github.com/microsoft/graphrag/blob/main/README.md)
- [Documentation and quickstart](https://microsoft.github.io/graphrag/)
- [Prompt-tuning guide](https://microsoft.github.io/graphrag/prompt_tuning/overview/)
- [Microsoft Research overview](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)
- [Responsible-AI FAQ in the repository](https://github.com/microsoft/graphrag/blob/main/RAI_TRANSPARENCY.md)
- [Research paper](https://arxiv.org/abs/2404.16130)

**Evidence note:** README blob inspected: `eb7d564ece1b898600feec8261a96e7d9e1d1d88`.
