# How Big4Bot Works

Big4Bot defines the operational execution flow between an external agent orchestrator (e.g., your custom Python script, an MCP server, or an AutoGen graph) and its machine-readable consulting skill sets. 

The core interaction loop follows three main usage modes, moving a user's problem from ambiguity to a structured Output Schema. 

---

## 1. Targeted Execution
The most common and straightforward operational model. The user knows exactly what analysis they need completed.

**Context:** The agent receives explicit instructions to execute a specific organizational framework.
- **Example request:** "Run a SWOT analysis on this competitor's recent SEC filing."
- **Execution Loop:**
  1. **Identify Framework:** The agent locates the `swot-analysis` skill in the registry.
  2. **Gather Context:** The agent reviews the text payload for required context to satisfy the skill's `input_schema.json`.
  3. **Run Skill:** The agent uses its LLM intelligence to apply the constraints of `SKILL.md` diagnostics against the data.
  4. **Structure Findings:** The agent produces exactly what the `output_schema.json` dictates, delivering the findings.
  5. **Completion:** The agent halts execution and returns the response to the user. No graphing transversals occur.

## 2. Framework Advisory
The user has identified an organizational problem, but does not know which diagnostic reasoning model to apply.

**Context:** The agent uses Big4Bot's Entry Point structures to suggest the best starting framework.
- **Example request:** "I need to figure out why our customer churn spiked 20% this quarter."
- **Execution Loop:**
  1. **Classify Problem:** The agent uses the problem description to identify `market_problem` mapping in `registry/dependencies.yaml`.
  2. **Suggest Frameworks:** The agent queries the registry and proposes logical starting points (e.g., Customer Journey Mapping, Market Segmentation).
  3. **Confirm Selection:** The user confirms a single starting framework.
  4. **Run Selected Skill:** The agent gathers the correct `input_schema.json` data and proceeds as in a Targeted Execution loop.

## 3. Guided Analysis
The user requires deeper, sequential insights derived from multiple interconnected frameworks.

**Context:** The agent leverages the Reasoning Graph explicitly, following triggered dependencies downstream.
- **Example request:** "We need an end-to-end strategic audit prior to fundraising."
- **Execution Loop:** 
  1. **Start Framework:** The agent begins at an agreed-upon entry point (e.g., `pestle-analysis`).
  2. **Run Skill:** The agent parses inputs and produces the required `output_schema.json` artifact.
  3. **Navigate Graph:** The agent references `dependencies.yaml` to identify downstream targets (e.g., `pestle-analysis` triggers `swot-analysis`).
  4. **Suggest Continuation:** The agent asks the user if they wish to proceed down the suggested path, leveraging the previous skill's outputs as input context.
  5. **Iterate:** The analysis loop continues until the graph is exhausted, or the user is satisfied.
