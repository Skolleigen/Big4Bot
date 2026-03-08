import sys
import os
import json
from typing import Dict, Any, List

from big4bot.shared.big4bot_loader import Big4BotLoader
from big4bot.shared.schema_utils import to_openai_function

class Big4BotOpenAIAdapter:
    def __init__(self):
        self.loader = Big4BotLoader()
        self.skills = self.loader.get_all_skills()

    def get_tools(self) -> List[Dict[str, Any]]:
        """
        Returns all Big4Bot skills formatted dynamically as OpenAI Tool definitions.
        """
        tools = []
        for skill in self.skills:
            # Fallback description if the skill lacks one
            desc = skill.description if skill.description else f"Execute the {skill.skill_id} framework."
            
            tool = to_openai_function(
                schema=skill.input_schema,
                name=skill.skill_id,
                description=desc
            )
            tools.append(tool)
        return tools

    def handle_tool_call(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """
        Simulates parsing a tool call from OpenAI. Returns the methodology and the required output schema structure.
        The external application should then pass this result back into the OpenAI LLM Context.
        """
        # OpenAI tool names use underscores, Big4Bot uses hyphens
        skill_id = tool_name.replace("_", "-")
        skill = self.loader.get_skill(skill_id)
        
        if not skill:
            return json.dumps({"error": f"Skill {skill_id} not found."})
            
        return json.dumps({
            "skill_id": skill.skill_id,
            "methodology": skill.methodology,
            "output_schema": skill.output_schema,
            "instructions": "Use the methodology above to analyze the provided inputs. Return results strictly matching the output_schema."
        }, indent=2)
