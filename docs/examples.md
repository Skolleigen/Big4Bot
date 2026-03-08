# Example Implementation: Consulting Reasoning Loop

Big4Bot is more than a list of tools; it is a system for orchestration. To demonstrate how an AI agent can dynamically traverse the library, we provide a complete reasoning loop example.

## Location
The implementation can be found in `examples/consulting_loop_example.py`.

## Core Logic: The Loop
The example demonstrates a three-stage "Consulting Reasoning Loop":

### 1. Discovery & Classification
The agent starts with a fuzzy business problem (e.g., "Our revenue is declining").
- It uses the `suggest_logically_starting_frameworks` tool.
- The system maps the problem to a category (e.g., `financial_problem`) and returns appropriate entry points like `financial-ratio-analysis` or `dupont-analysis`.

### 2. Planning
Once a starting point is selected, the agent uses the `plan_consulting_analysis` tool.
- This queries the `registry/dependencies.yaml` reasoning graph.
- It returns a multi-step chain of frameworks (e.g., `DuPont Analysis` -> `Scenario Analysis` -> `Strategic Initiative Mapping`).

### 3. Execution
The agent iterates through the plan.
- For each step, it "executes" the skill via the adapter.
- The adapter returns the specific **Methodology** and **Output Schema**.
- The agent performs the actual reasoning based on these constraints and produces a structured result.

## Running the Example
To run the demo, ensure you have the required dependencies installed:

```bash
pip install big4bot openai
```

Then execute the script:
```bash
python examples/consulting_loop_example.py
```

## Key Architectural Takeaway
The example highlights that **Big4Bot does not perform the analysis**. The script shows how Big4Bot provides the "diagnostic rails" while the LLM provides the "intellectual engine." The example successfully bridges the gap between static methodology files and a dynamic AI consulting agent.
