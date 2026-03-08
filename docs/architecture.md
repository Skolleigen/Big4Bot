# Repository Architecture

Big4Bot is designed to be cleanly integrated with any external AI agent orchestration system. To maintain a strict separation of concerns, the repository architecture is divided into three distinct conceptual layers.

## 1. The Skill Layer (Consulting Frameworks)

The Skill Layer is the foundation of the repository. It houses the 46 individual consulting methodologies, divided among 7 core professional domains (Strategy, Finance & Valuation, Market & Customer, Product & Innovation, Execution, Risk & Governance, Organization & Culture).

**Components:**
The `domains/` directory contains folders for each specific skill (e.g., `domains/strategy/swot-analysis/`). Everything an agent needs to execute that specific analytical framework is localized in this directory, including:
- `SKILL.md`: The natural language description, methodology context, and diagnostic logic.
- `input_schema.json`: What data the agent must extract or infer from the user to run the analysis.
- `output_schema.json`: The strict JSON structure the agent must generate to complete the analysis.
- `examples/` and `references/`: Context for grounding the LLM in real-world application and academic rigor.

## 2. The Reasoning Layer (Dependency Graph)

The Reasoning Layer defines how the individual skills connect to form cohesive, multi-step diagnostic investigations. 

**Components:**
The core of this layer is the `registry/dependencies.yaml` file. It operates as the "map" for the agent, defining:
- **Entry Points:** High-level problem classifications (e.g., `market_problem`, `financial_problem`) mapped to the best starting frameworks.
- **Skill Triggers:** Explicit, directed edges connecting skills (e.g., `financial-ratio-analysis` triggers `dupont-analysis`). Each trigger carries a `relevance` rating (high, medium, low) to assist the agent in prioritizing its suggestions to the user.

*Note: The metadata regarding available skills and domain configurations is managed by `registry/skills-index.yaml` and `registry/domains.yaml` respectively.*

## 3. The Execution Policy (Usage Policy)

The Execution Policy dictates the behavioral interface between the external agent framework and the Big4Bot repository. It answers the question: *"How strictly should an agent enforce the Reasoning Layer?"*

**Components:**
The `registry/usage_policy.yaml` file natively encodes these behavioral constraints. It explicitly defines the system as **"skills first, graph advisory,"** meaning:
- Agents may follow the dependency graph deeply if the user relies on them for guidance.
- Agents **must** break from the graph to execute targeted, single-framework commands if the user requests them.
- Agents are permitted to suggest upstream frameworks to gather missing data, but are explicitly forbidden from making upstream execution a hard, blocking requirement.

## Interaction Flow

When an external agent loads Big4Bot:
1. It reads the **Execution Policy** to understand the operating boundaries.
2. It uses the **Reasoning Layer** (dependencies/entry points) to help the user navigate to a specific framework.
3. It loads the **Skill Layer** for the chosen framework, applying the `input_schema` to the user's data and generating the highly structured insight defined in the `output_schema`.
