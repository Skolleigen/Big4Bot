# Quickstart Guide

Big4Bot allows you to equip your AI agent with professional consulting methodologies in under five minutes. 

You do not need to install complex libraries or adopt a new orchestration engine. Big4Bot is fundamentally a repository of instructions and JSON schemas that you feed to your existing LLM setup.

## Installation

For the fastest implementation, install the Big4Bot runtime:

```bash
pip install big4bot
export BIG4BOT_HOME="/path/to/your/big4bot/repo"
```

## Start Consulting in 6 Steps

### Step 1: Understand the Concept
Big4Bot provides the structural "playbook"; your agent (OpenAI, Claude, custom LangChain build) brings the intelligence. When a user asks a business question, your agent locates the corresponding Big4Bot skill and uses it as the system prompt and structural constraint.

### Step 2: Choose Usage Mode
Determine how your agent operates:
1. **Targeted Execution:** A user specifically asks for "SWOT Analysis."
2. **Framework Advisory:** A user states "We are losing market share." The agent recommends a starting framework like "Competitive Positioning."
3. **Guided Reasoning:** The agent strings together multiple frameworks using the `dependencies.yaml` graph to perform deep diagnostic audits.

### Step 3: Pick a Skill
Navigate to the `domains/` directory and select a framework. For this quickstart, let's select `domains/strategy/swot-analysis`.

### Step 4: Gather Input Context
Feed the `SKILL.md` to your agent as its system instructions. Review the `input_schema.json` to see what context the agent needs from the user (e.g., `company_context`, `industry_overview`). If the user hasn't provided this context, the agent must ask for it or infer it.

### Step 5: Execute & Return Structured Output
Have the agent use its LLM capabilities to synthesize the input data against the logic constraints found in `SKILL.md`. The agent must format its final response precisely according to the matching `output_schema.json`. You now have a machine-readable, robust strategic insight.

### Step 6: Optionally Chain Frameworks (Guided Reasoning)
Check `registry/dependencies.yaml`. You will see that `swot-analysis` triggers `risk-register` with a `medium` relevance. Your agent can ask the user: *"Would you like me to translate the identified Threats into a formalized Risk Register to mitigate organizational exposure?"* 

---

## 3 Quick Execution Examples

### Example A: Single Framework Execution
**User:** "Can you build a DCF Valuation for Acme Corp?"  
**Agent Action:** The agent pulls context, loads the `dcf-valuation` skill directly, calculates the valuation, formats it precisely to the output schema, and halts execution.

### Example B: Framework Advisory
**User:** "Why are our employees quitting? We pay well!"  
**Agent Action:** The agent identifies an `organization_culture` problem. It presents options from the registry: *"We can use the `ocai-culture-assessment` to map friction, or the `total-rewards-strategy` to ensure compensation matches strategic goals. Where should we start?"*

### Example C: Guided Reasoning Chain
**Agent Action:** The agent just finished a `financial-ratio-analysis`. It checks the graph and sees a high-relevance trigger linking to `dupont-analysis`. It proactively initiates the DuPont framework to break down Return on Equity (ROE) using the ratios it just calculated, deepening the engagement seamlessly.
