# Contributing to Big4Bot

First off, thank you for considering contributing to Big4Bot! 

Big4Bot relies on the community to build out new consulting frameworks, refine schemas, and improve the orchestration adapters.

## Contribution Guidelines

All contributions must respect the "skills-first" methodology architecture.

### 1. Adding New Skills
When proposing a new consulting framework to a `domains/` folder:
- Ensure you provide exactly five components: `SKILL.md`, `input_schema.json`, `output_schema.json`, `examples/example.md`, and a `references/` citations file.
- The `SKILL.md` MUST contain a definitive step-by-step diagnostic process. Do not rely on "vibes" or generic instruction sets.
- Do not use verbose string sentences as JSON property keys. Use concise `snake_case` keys and lean heavily on the `"description"` parameter to enforce LLM boundaries.

### 2. Updating the Reasoning Graph
If your skill introduces a new analytical chain:
- Modify `registry/dependencies.yaml`.
- Ensure you do not create massive bottleneck nodes where too many frameworks point to a single outcome arbitrarily. Focus on actionable downstream paths.

### 3. Modifying Adapters
Do not modify `adapters/shared/` utilities unless absolutely standardizing logic across all SDK endpoints. If building a new provider adapter natively, refer to the `adapters/openai/client.py` structure as the canonical implementation.

## Pull Request Process
1. Fork the repository and create your branch from `main`.
2. Ensure you have tested your skill output schemas using the provided validation utilities.
3. Update the `README.md` and `registry/skills-index.yaml` if you added a new framework.
4. Issue a PR with a clear description of the business problem your framework solves.
