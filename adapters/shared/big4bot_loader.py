import json
import yaml
from pathlib import Path
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from . import config

class SkillDefinition(BaseModel):
    skill_id: str
    domain: str
    methodology: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    description: str = ""
    when_to_use: str = ""
    when_not_to_use: str = ""
    related_skills: List[str] = []
class Big4BotLoader:
    def __init__(self):
        self.skills: Dict[str, SkillDefinition] = {}
        self.dependencies: Dict[str, Any] = {}
        self.entry_points: Dict[str, List[str]] = {}
        
        self._load_registry()
        self._load_all_skills()

    def _load_registry(self):
        """Loads the registry metadata including dependencies and entry points."""
        if not config.DEPENDENCIES_PATH.exists():
            raise FileNotFoundError(f"Dependency graph not found at {config.DEPENDENCIES_PATH}")
            
        with open(config.DEPENDENCIES_PATH, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            
        self.dependencies = data.get("skills", {})
        self.entry_points = data.get("entry_points", {})

    def _load_all_skills(self):
        """Dynamically loads all skills listed in the skills-index.yaml"""
        if not config.SKILLS_INDEX_PATH.exists():
            raise FileNotFoundError(f"Skills index not found at {config.SKILLS_INDEX_PATH}")
            
        with open(config.SKILLS_INDEX_PATH, "r", encoding="utf-8") as f:
            index_data = yaml.safe_load(f)
            
        registered_skills = index_data.get("skills", [])
        
        for skill_entry in registered_skills:
            skill_id = skill_entry.get("id")
            domain = skill_entry.get("domain")
            
            if skill_id and domain:
                skill_def = self._parse_skill_directory(skill_id, domain)
                if skill_def:
                    self.skills[skill_id] = skill_def

    def _parse_skill_directory(self, skill_id: str, domain: str) -> Optional[SkillDefinition]:
        """Reads the files in a skill's directory and constructs the SkillDefinition."""
        skill_dir = config.DOMAINS_DIR / domain / skill_id
        
        if not skill_dir.exists() or not skill_dir.is_dir():
            print(f"Warning: Skill directory not found for {skill_id} at {skill_dir}")
            return None
            
        skill_md_path = skill_dir / "SKILL.md"
        input_schema_path = skill_dir / "input_schema.json"
        output_schema_path = skill_dir / "output_schema.json"
        
        try:
            with open(skill_md_path, "r", encoding="utf-8") as f:
                methodology = f.read()
                
            with open(input_schema_path, "r", encoding="utf-8") as f:
                input_schema = json.load(f)
                
            with open(output_schema_path, "r", encoding="utf-8") as f:
                output_schema = json.load(f)
                
            desc = self._extract_section(methodology, "Description")
            wtu = self._extract_section(methodology, "When to Use")
            wntu = self._extract_section(methodology, "When NOT to Use")
            
            rel_skills = []
            rel_text = self._extract_section(methodology, "Related Skills")
            for line in rel_text.split("\n"):
                line = line.strip()
                if line.startswith("-"):
                    item = line.replace("-", "").strip()
                    item = item.replace("[", "").replace("]", "").replace("`", "")
                    if "(" in item and ")" in item:
                        item = item.split("(")[0].strip()
                    if item:
                        rel_skills.append(item)
                
            return SkillDefinition(
                skill_id=skill_id,
                domain=domain,
                methodology=methodology,
                input_schema=input_schema,
                output_schema=output_schema,
                description=desc,
                when_to_use=wtu,
                when_not_to_use=wntu,
                related_skills=rel_skills
            )
        except Exception as e:
            print(f"Error loading skill {skill_id}: {e}")
            return None

    def get_skill(self, skill_id: str) -> Optional[SkillDefinition]:
        return self.skills.get(skill_id)
        
    def get_all_skills(self) -> List[SkillDefinition]:
        return list(self.skills.values())

    def _extract_section(self, text: str, section_title: str) -> str:
        lines = text.split("\n")
        in_section = False
        content = []
        for line in lines:
            line_stripped = line.strip()
            if line_stripped.startswith(f"## {section_title}"):
                in_section = True
                continue
            elif in_section and line_stripped.startswith("## "):
                break
                
            if in_section:
                content.append(line)
        return "\n".join(content).strip()

    def list_frameworks(self, domain_filter: Optional[str] = None, keyword: Optional[str] = None) -> Dict[str, List[Dict[str, str]]]:
        """Discovery tool: Lists frameworks with optional filtering."""
        results = []
        for skill in self.skills.values():
            if domain_filter and skill.domain != domain_filter:
                continue
            if keyword and keyword.lower() not in skill.description.lower() and keyword.lower() not in skill.skill_id.lower():
                continue
            results.append({
                "skill_id": skill.skill_id,
                "domain": skill.domain,
                "description": skill.description
            })
        return {"frameworks": results}

    def describe_framework(self, skill_id: str) -> Dict[str, Any]:
        """Discovery tool: Returns detailed metadata for a specific framework."""
        skill = self.get_skill(skill_id)
        if not skill:
            return {"error": f"Skill '{skill_id}' not found."}
            
        required_inputs = list(skill.input_schema.get("properties", {}).keys())
        
        return {
            "skill_id": skill.skill_id,
            "domain": skill.domain,
            "description": skill.description,
            "when_to_use": skill.when_to_use,
            "when_not_to_use": skill.when_not_to_use,
            "required_inputs": required_inputs,
            "related_skills": skill.related_skills
        }

    def suggest_frameworks(self, problem_type: str) -> List[str]:
        """Returns suggested starting frameworks based on entry_points."""
        # entry_points val is a dict with 'description' and 'start_with'
        entry = self.entry_points.get(problem_type, {})
        return entry.get("start_with", [])

    def suggest_next_framework(self, current_skill: str) -> List[Dict[str, str]]:
        """Returns downstream frameworks based on trigger relationships."""
        if current_skill in self.dependencies:
            return self.dependencies[current_skill].get("triggers", [])
        return []

    def get_related_frameworks(self, skill_id: str) -> List[str]:
        """Returns frameworks listed in Related Skills section."""
        skill = self.get_skill(skill_id)
        if not skill:
            return []
        return skill.related_skills

    def plan_consulting_analysis(self, problem_type: Optional[str] = None, current_skill: Optional[str] = None, max_depth: int = 4) -> Dict[str, List[Dict[str, Any]]]:
        """Planner Tool: Generates recommended chain of consulting frameworks."""
        plan = []
        visited = set()
        current_node = None
        
        if current_skill:
            current_node = current_skill
        elif problem_type:
            starts = self.suggest_frameworks(problem_type)
            if starts:
                current_node = starts[0]
                
        if not current_node:
            valid_problems = list(self.entry_points.keys())
            return {"error": f"Please provide a valid problem_type ({', '.join(valid_problems)}) or current_skill"}
            
        for step_num in range(1, max_depth + 1):
            if current_node in visited:
                break
            visited.add(current_node)
            skill = self.get_skill(current_node)
            if not skill:
                break
                 
            plan.append({
                "step": step_num,
                "framework": current_node,
                "reason": skill.description if skill.description else f"Execute {current_node}"
            })
             
            triggers = self.suggest_next_framework(current_node)
            if not triggers:
                break
                 
            # Sort triggers: high=1, medium=2, low=3
            relevance_order = {"high": 1, "medium": 2, "low": 3}
            sorted_triggers = sorted(triggers, key=lambda x: relevance_order.get(x.get("relevance", "low"), 4))
             
            next_node = None
            for t in sorted_triggers:
                candidate = t.get("skill")
                if candidate not in visited:
                    next_node = candidate
                    break
                     
            if not next_node:
                break
            current_node = next_node
             
        return {"analysis_plan": plan}
