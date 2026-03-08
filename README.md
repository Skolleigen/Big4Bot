# Big4Bot

**An open-source consultive AI agent framework that encodes professional consulting methodologies as reusable, model-agnostic skills.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Project Vision

Big4Bot transforms established consulting frameworks — SWOT analysis, Balanced Scorecard, DuPont financial decomposition, Design Thinking, and many more — into **structured reasoning modules** that AI agents can invoke programmatically.

Instead of treating AI agents as generic chat interfaces, Big4Bot provides a **library of cognitive playbooks** that enable agents to diagnose businesses, analyze strategy, evaluate financial health, assess organizational structure, and recommend transformations using proven consulting methodologies.

## Why Consulting Frameworks Matter for AI Agents

Traditional consulting relies on structured frameworks to analyze complex organizations. These frameworks function as **algorithms for reasoning about business systems**.

By encoding these methodologies as machine-readable skills, AI agents gain:

- **Structured diagnostic reasoning** instead of open-ended generation
- **Consistent analytical outputs** that can be chained across workflows
- **Domain expertise** grounded in established consulting practice
- **Reproducible analysis** that follows proven methodologies

## Documentation

Big4Bot provides a comprehensive [documentation library](docs/introduction.md) detailing the system's architecture and usage. 

Agents interact with the 46-skill library through three primary **Usage Modes**:
1. **Targeted Execution:** Running a specific user-requested framework.
2. **Framework Advisory:** Suggesting starting frameworks based on problem classification.
3. **Guided Analysis:** Proposing downstream frameworks natively using the dependency graph.

For a 5-minute implementation guide, see the [Quickstart Guide](docs/quickstart.md).

## Repository Structure

```
big4bot/
├── domains/            # Consulting skill modules organized by domain
│   ├── strategy/
│   ├── product-innovation/
│   ├── market-customer/
│   ├── execution/
│   ├── organization-culture/
│   ├── finance-valuation/
│   └── risk-governance/
├── shared/             # Shared schemas, taxonomies, and evaluation rubrics
│   ├── schemas/
│   ├── taxonomies/
│   ├── evaluation/
│   └── references/
├── adapters/           # Platform-specific integration adapters
│   ├── openai/
│   ├── anthropic/
│   ├── gemini/
│   └── mcp/
└── registry/           # Skill index, domain catalog, and dependency maps
    ├── skills-index.yaml
    ├── domains.yaml
    └── dependencies.yaml
```

## Domain Overview

| Domain | Directory | Skills |
|--------|-----------|--------|
| Strategy | `domains/strategy/` | 6 |
| Product & Innovation | `domains/product-innovation/` | 6 |
| Market & Customer | `domains/market-customer/` | 5 |
| Execution | `domains/execution/` | 7 |
| Organization & Culture | `domains/organization-culture/` | 9 |
| Finance & Valuation | `domains/finance-valuation/` | 9 |
| Risk & Governance | `domains/risk-governance/` | 4 |


## How Skills Work

Each skill is a self-contained directory following a consistent structure:

```
skill-name/
├── SKILL.md            # Complete skill definition and diagnostic process
├── input_schema.json   # Input parameters schema for agent validation
├── output_schema.json  # Structured output schema for agent interoperability
├── examples/           # Example scenarios and walkthroughs
│   └── example.md
└── references/         # Authoritative sources and citations
```

### SKILL.md

The core definition file contains:

- **Purpose** — What business problem the framework solves
- **When to Use / When NOT to Use** — Decision criteria for the agent
- **Inputs Required** — Data needed for execution
- **Diagnostic Process** — Step-by-step reasoning workflow
- **Output Schema** — Reference to the structured output format
- **Related Skills** — Cross-references for skill chaining

### input_schema.json and output_schema.json

Two standardized schemas enabling:

- Consistent structured outputs across all skills
- Skill chaining — output of one skill feeds into another
- Platform-agnostic data exchange

## Platform Compatibility

Big4Bot is designed to be **model-agnostic** and compatible with:

| Platform | Adapter | Status |
|----------|---------|--------|
| OpenAI Agents | `adapters/openai/` | Planned |
| Anthropic Claude | `adapters/anthropic/` | Planned |
| Google Gemini | `adapters/gemini/` | Planned |
| Model Context Protocol | `adapters/mcp/` | Planned |

Platform-specific logic lives in adapters, while the core reasoning remains platform-neutral.

## How to Contribute

We welcome contributions! Here's how you can help:

1. **Enhance skill definitions** — Expand the diagnostic processes, add decision rules, and improve the reasoning workflows in `SKILL.md` files.
2. **Add examples** — Create real-world scenario walkthroughs in the `examples/` directories.
3. **Build adapters** — Implement platform-specific adapters for OpenAI, Anthropic, Gemini, or MCP.
4. **Improve schemas** — Refine `input_schema.json` and `output_schema.json` files to better capture the analytical outputs.
5. **Add new skills** — Propose and implement additional consulting frameworks.
6. **Documentation** — Improve documentation, add references, and enhance the knowledge base.

### Contribution Guidelines

- Follow the existing skill folder structure
- Ensure all skills have complete `SKILL.md`, `input_schema.json`, and `output_schema.json` files
- Use consistent naming conventions (lowercase, hyphen-separated)
- Focus on structured reasoning, not prompt engineering
- Reference authoritative sources in the `references/` directories

## Future Roadmap

- [ ] Complete all 46 skill diagnostic processes with detailed reasoning workflows
- [ ] Build adapter implementations for OpenAI, Anthropic, Gemini, and MCP
- [ ] Create shared evaluation rubrics for skill output quality
- [ ] Implement skill chaining and dependency resolution
- [ ] Add consulting taxonomy and terminology standards
- [ ] Build a skill discovery and recommendation engine
- [ ] Create interactive example walkthroughs
- [ ] Develop automated testing for skill outputs
- [ ] Community-contributed skills and extensions

## Consulting Reasoning Graph

Big4Bot frameworks are designed to be chained using a structured consulting analysis pathway. The dependency graph defined in `registry/dependencies.yaml` enables AI agents to move through consulting domains and skills in logical diagnostic sequences.

### Domain Progression

```
Strategy → Market & Customer → Product & Innovation → Execution → Finance & Valuation → Risk & Governance → Organization & Culture
```

This flow represents a typical top-down consulting engagement: starting with strategic context, moving through market and product analysis, then validating through financial and risk lenses, and concluding with organizational implications.

### How Agents Use the Graph

- **Agents may start at any domain** depending on the presenting problem — a cost-reduction brief begins at Finance, a go-to-market question begins at Market & Customer
- **Domain dependencies guide progression** — each domain declares which domains logically follow, including feedback loops (e.g. Risk → Strategy, Organization → Execution)
- **Skill triggers enable deeper chaining** — within and across domains, individual frameworks declare which skills are typically invoked next, forming a micro-diagnostic path

### Example Reasoning Chain

```
swot-analysis
  → market-segmentation → value-proposition-canvas → business-model-canvas → unit-economics
  → competitive-positioning → pricing-and-packaging-strategy
  → product-discovery → product-market-fit-diagnostics → scenario-and-sensitivity-analysis
```

The full dependency map is machine-parsable and lives at `registry/dependencies.yaml`.

## Diagnostic Entry Layer

Big4Bot includes a **starting point selector** that allows AI agents to classify a problem before applying frameworks. Instead of randomly invoking skills, agents first determine the nature of the problem and select the most appropriate initial frameworks.

The entry layer supports seven problem categories:

| Category | Starting Frameworks |
|----------|-------------------|
| `strategic_problem` | PESTLE Analysis, SWOT Analysis, Balanced Scorecard, OKR Design |
| `market_problem` | Market Segmentation, Competitive Positioning, Customer Journey Mapping |
| `product_problem` | Product Discovery, Value Proposition Canvas, Product Market Fit Diagnostics |
| `operational_problem` | Process Mapping, Agile Operating Model, RACI / DACI Governance |
| `financial_problem` | Financial Ratio Analysis, DuPont Analysis, Unit Economics |
| `risk_problem` | Risk Register, Capability Maturity Assessment |
| `culture_problem` | OCAI Culture Assessment, Competing Values Framework, Pulse Surveys |

### Two-Stage Reasoning Process

Agents perform a two-stage reasoning process:

1. **Problem classification** → `entry_points` determines the starting frameworks
2. **Framework chaining** → the dependency graph determines subsequent frameworks

### Example

**Problem:** Declining revenue despite strong traffic

**Stage 1 — Entry classification:** `financial_problem`

**Stage 2 — Starting frameworks:**
- Financial Ratio Analysis
- DuPont Analysis
- Unit Economics

**Stage 3 — Dependency chain continues:**
```
financial-ratio-analysis → dupont-analysis → scenario-and-sensitivity-analysis → strategy reassessment
```

Once the initial frameworks are executed, the skill-level dependency graph in `registry/dependencies.yaml` determines which frameworks to invoke next, enabling a complete diagnostic reasoning flow.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

**Big4Bot** — *Structured consulting intelligence for AI agents.*
