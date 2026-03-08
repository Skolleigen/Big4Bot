# The Anatomy of a Big4Bot Skill

Big4Bot utilizes a "skills-first" architecture. Each framework stands alone as a discrete atomic unit, fully isolated and self-documenting. The framework logic dictates the constraints; the LLM intelligence provides the contextual synthesis.

Every skill directory within a `domains/` folder (e.g., `domains/finance-valuation/dcf-valuation/`) contains exactly five core files and directories.

## 1. `SKILL.md` (The Methodology Playbook)
This document is the cornerstone of the framework. It houses the human-readable explanation and the methodological diagnostic rails that the LLM must adopt.

- **Description & Purpose:** Clarifies what the skill achieves and why it is valuable to an enterprise.
- **Usage Guards:** Explicitly outlines `When to Use` and `When NOT to Use` boundaries, preventing the LLM from hallucinating an incorrect application for the framework.
- **Inputs Required:** A qualitative list of context required to run the module successfully.
- **Diagnostic Process:** The step-by-step procedural logic the agent must internally execute when reasoning. This translates an abstract business concept into a bounded LLM prompt methodology.
- **Related Skills:** A list of conceptually adjacent frameworks. 

## 2. `input_schema.json` (The Data Intake Bouncer)
A strict draft-07 JSON Schema outlining what data points the agent **must** have before it is allowed to confidently execute the skill. 

If the agent intercepts a `problem_statement` or `company_context` that is insufficient to meet the schema requirements, the agent is expected to ask the user clarifying questions or infer the data through upstream analysis.

## 3. `output_schema.json` (The Structural Bouncer)
A strict draft-07 JSON Schema outlining exactly how the agent must format its findings. 

There are no generic textual responses allowed. If a tool mandates an `analysis_summary` and a discrete `confidence_level` (High, Medium, Low), the agent produces exactly that. This eliminates conversational drift and guarantees that outputs can be programmatically chained to other software or downstream frameworks. 

## 4. `examples/` and `references/` (The Academic Grounding)
These sub-directories encode the professional standards required to combat LLM degradation and hallucination.
- **`examples/example.md`:** Provides a synthetic business scenario and a human-readable analytical walkthrough demonstrating how the framework is logically applied, teaching the agent the required reasoning progression (without strictly defining the final JSON payload).
- **`references/references.md`:** A list of academic citations, canonical industry textbooks, or whitepapers that ground the framework in recognized real-world management consulting standards (e.g., *McKinsey*, *Harvard Business Review*, *WorldatWork*).

## 5. Global Standards and Integration
While each skill is atomic, they are governed by global standards located in the `shared/` directory:
- **`shared/schemas/base_envelope.json`:** Every skill's output is wrapped or validated against this baseline to ensure consistency across the library.
- **`shared/evaluation/rubric.md`:** A universal set of criteria for assessing whether an agent's application of a methodology was successful.
- **`shared/taxonomies/`:** Centralized lists (like Industry Sectors) that skills reference to ensure data interoperability.

This decoupling allows individual skills to remain lightweight while still benefiting from a rigorous, centralized governance structure.
