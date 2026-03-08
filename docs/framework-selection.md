# Framework Selection

Big4Bot assumes that human users and AI agents collaborate to select the appropriate diagnostic framework. There are four primary selection modes supported by the system's `usage_policy.yaml`:

## 1. Explicit User Request (Targeted Selection)
When a user asks directly for a specific consulting analysis (e.g., "Give me a Porter's Five Forces breakdown of the EV market"), the agent honors the request explicitly. 

The agent bypasses the broader `dependencies.yaml` graph, loads the requested skill directly, asks for any missing `input_schema.json` context, and executes. The user's explicit request overrides all other architectural suggestions.

## 2. Advisory Selection
When a user brings a vague or multifaceted business problem (e.g., "Revenues are dropping and I don't know why, what should we do?"), the agent refers to the **Entry Points** defined in the Reasoning Graph.

By mapping fuzzy language to predefined entry states (`financial_problem`, `market_problem`), the agent can propose a menu of 2-3 logical starting frameworks for the user to choose from. 

## 3. Graph-Guided Selection
Once an initial analysis is complete, the agent can proactively select or suggest downstream analysis based on the `dependencies.yaml` file. 

If the agent just finished a SWOT Analysis that highlighted severe "Threats" regarding corporate liability, the graph will natively suggest pivoting to the `risk-register` skill. The agent will propose this pre-mapped pathway to the user to continue the engagement.

## 4. Artifact-Driven Selection (Single-Artifact Use Case)
Users frequently engage consultants (or consulting AI) not to begin an analysis from scratch, but to review, audit, or expand upon an existing artifact.

**Example Scenario:** A user uploads a drafted Balanced Scorecard spreadsheet and asks: "Is this any good?"

In this scenario:
1. The agent intercepts the artifact and matches it to the `balanced-scorecard` skill.
2. The agent executes the analysis, using the provided artifact as the primary `input_schema.json` fulfillment.
3. The agent validates the artifact against the structured expectations of the `SKILL.md` methodology, highlighting gaps or flawed reasoning.
4. The agent honors the user's focus. It provides the structured output and stops, rather than forcing the user into a tangent mapping strategic initiatives (unless explicitly requested).

### Handling Missing Inputs Gracefully
Regardless of the selection mode, an agent will inevitably encounter a situation where it lacks the data required by an `input_schema.json`. 

**The Golden Rule:** The agent may suggest what missing data would improve its analysis, or suggest running upstream frameworks to generate that missing data, but it must **never** block execution. Agents are expected to synthesize the available data best-effort, explicitly calling out their assumptions within the `output_schema.json` confidence levels.
