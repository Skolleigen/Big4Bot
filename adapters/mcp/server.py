import json
import sys
import os
from pathlib import Path

from big4bot.shared.big4bot_loader import Big4BotLoader
from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing import Dict, Any, List

# Initialize the MCP Server
mcp = FastMCP("Big4Bot", dependencies=["mcp", "pyyaml", "pydantic"])

# Initialize the Loader which builds the in-memory registry
print("Loading Big4Bot Skills Registry...")
loader = Big4BotLoader()
all_skills = loader.get_all_skills()
print(f"Loaded {len(all_skills)} consulting skills.")

from pydantic import BaseModel, Field, create_model

# Helper function to dynamically construct Pydantic models from Big4Bot JSON Schemas
# This fully integrates Big4Bot schemas into FastMCP's native type inference.
def create_dynamic_model(skill: Any):
    fields = {}
    for prop_name, prop_data in skill.input_schema.get("properties", {}).items():
        prop_type = str
        if prop_data.get("type") == "number":
            prop_type = float
        elif prop_data.get("type") == "boolean":
            prop_type = bool
        elif prop_data.get("type") == "array":
            prop_type = list
            
        desc = prop_data.get("description", "")
        if prop_name in skill.input_schema.get("required", []):
            fields[prop_name] = (prop_type, Field(..., description=desc))
        else:
            fields[prop_name] = (prop_type, Field(None, description=desc))
            
    return create_model(f"Input_{skill.skill_id.replace('-', '_')}", **fields)

# --- 1. Exposing Skills as MCP Tools (Agent-Led Execution) ---

def create_tool(skill: Any):
    InputModel = create_dynamic_model(skill)
    
    # Tool description is cleanly truncated to not break context limits
    @mcp.tool(
        name=skill.skill_id.replace("-", "_"),
        description=f"Domain: {skill.domain}. {skill.description}"
    )
    def execute_skill(inputs: InputModel) -> str:
        """
        Executes the Big4Bot analytical framework.
        Note: Big4Bot itself does NOT perform the analysis. It returns the rigid constraints.
        The external Agent must synthesize the 'inputs' against these constraints.
        """
        provided_inputs = inputs.model_dump_json(indent=2)
        response = (
            f"BIG4BOT SKILL LOADED: {skill.skill_id}\n\n"
            f"You have provided the required input data. You must now act as the consulting analyst.\n"
            f"Synthesize your inputs exactly according to the following methodology:\n\n"
            f"--- METHODOLOGY START ---\n"
            f"{skill.methodology}\n"
            f"--- METHODOLOGY END ---\n\n"
            f"Your final response to the user must be structured EXACTLY matching the following JSON Output Schema. Do not include markdown blocks around the JSON if the host expects pure JSON.\n\n"
            f"--- OUTPUT SCHEMA START ---\n"
            f"{json.dumps(skill.output_schema, indent=2)}\n"
            f"--- OUTPUT SCHEMA END ---\n"
        )
        return response
    return execute_skill

# Dynamically Register all 46 Tools
for skill in all_skills:
    create_tool(skill)



# --- 2. Exposing Skills as MCP Prompts (User-Led Execution) ---

def create_prompt(skill: Any):
    @mcp.prompt(name=skill.skill_id.replace("-", "_"))
    def invoke_prompt() -> str:
        """
        Provides the Big4Bot methodology and schemas to the LLM directly via a User Prompt.
        """
        return (
            f"You are a top-tier management consultant executing the {skill.skill_id} module.\n"
            f"The user has requested you run this framework.\n\n"
            f"First, review the required Input Schema. If prompt input arguments did not provide this information, ask them for it:\n"
            f"{json.dumps(skill.input_schema, indent=2)}\n\n"
            f"Once you have the inputs, perform the analysis using this exact methodology:\n"
            f"{skill.methodology}\n\n"
            f"Finally, output your findings ONLY in this exact JSON structure (matching output_schema.json):\n"
            f"{json.dumps(skill.output_schema, indent=2)}\n"
        )
    return invoke_prompt

# Dynamically Register all 46 Prompts
for skill in all_skills:
    create_prompt(skill)


# --- 3. Navigation Tools (Graph Traversal) ---

@mcp.tool()
def suggest_logically_starting_frameworks(problem_type: str) -> str:
    """
    Returns suggested starting frameworks based on a general business problem type.
    Valid problem_types: strategic_problem, market_problem, product_problem, operational_problem, financial_problem, risk_problem, culture_problem.
    """
    suggestions = loader.suggest_frameworks(problem_type)
    if not suggestions:
        return f"No direct entry points found for '{problem_type}'. Check available problem classifications."
    return f"Suggested starting frameworks for {problem_type}: {', '.join(suggestions)}."

@mcp.tool()
def suggest_downstream_frameworks(completed_skill_id: str) -> str:
    """
    Given an already completed skill (e.g., 'swot-analysis'), returns logically connected downstream frameworks to analyze next.
    Use dashes (not underscores) for the skill_id (e.g. 'swot-analysis').
    """
    triggers = loader.suggest_next_framework(completed_skill_id)
    if not triggers:
        return f"No downstream triggers found for '{completed_skill_id}' in the dependency graph."
    
    formatted_triggers = []
    for t in triggers:
        formatted_triggers.append(f"- {t.get('skill')} (Relevance: {t.get('relevance')})")
    return f"Suggested downstream frameworks to run next:\n" + "\n".join(formatted_triggers)

@mcp.tool()
def get_related_framework_concepts(skill_id: str) -> str:
    """
    Returns the explicitly related adjacent skills mapped within the methodology file.
    Use dashes (not underscores) for the skill_id (e.g. 'swot-analysis').
    """
    related = loader.get_related_frameworks(skill_id)
    if not related:
        return f"No related skills documented for '{skill_id}'."
    return f"Related skills for {skill_id}: {', '.join(related)}"


# --- 4. Discoverability Tools ---

@mcp.tool()
def list_frameworks(domain: str = None, keyword: str = None) -> str:
    """
    Lists available Big4Bot consulting frameworks.
    Filters by optional domain or keyword to find specific methodologies.
    """
    results = loader.list_frameworks(domain_filter=domain, keyword=keyword)
    return json.dumps(results, indent=2)

@mcp.tool()
def describe_framework(skill_id: str) -> str:
    """
    Returns structured metadata about a specific consulting framework,
    including when to use it, required inputs, and related skills.
    Use dashes (not underscores) for the skill_id (e.g. 'swot-analysis').
    """
    metadata = loader.describe_framework(skill_id)
    return json.dumps(metadata, indent=2)


# --- 5. Consulting Reasoning Planner ---

@mcp.tool()
def plan_consulting_analysis(problem_type: str = None, current_skill: str = None, max_depth: int = 4) -> str:
    """
    Generates a recommended multi-step chain of consulting frameworks for a problem.
    Provide either a `problem_type` (e.g., 'strategic_problem', 'financial_problem') OR a `current_skill` (e.g., 'swot-analysis') to start from.
    Optional `max_depth` limits the number of steps (default 4).
    """
    plan = loader.plan_consulting_analysis(problem_type=problem_type, current_skill=current_skill, max_depth=max_depth)
    return json.dumps(plan, indent=2)


if __name__ == "__main__":
    # Start the FastMCP server when script is run directly
    mcp.run()
