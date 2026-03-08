import os
import json
import glob
from pathlib import Path

DOMAINS_DIR = Path("e:/Big4Bot/domains")

STOP_WORDS = {"of", "and", "or", "in", "the", "to", "against", "their", "from", "with", "for", "representing", "multiple", "a", "an"}

def shorten_key(key: str) -> str:
    words = key.split('_')
    # Filter stop words
    filtered = [w for w in words if w not in STOP_WORDS]
    
    # Specific overrides
    if "historical_income_statements" in key:
        return "historical_financials"
    if "discount_rate" in key:
        return "discount_rate"
    if "benchmarking_data" in key:
        return "benchmarking_data"
    if "capital_expenditure" in key:
        return "capex_forecasts"
        
    if len(filtered) > 3:
        # Take first 2-3 meaningful words
        return "_".join(filtered[:3])
    elif len(filtered) > 0:
        return "_".join(filtered)
    return key
    
def infer_type(key: str, description: str, current_type: str) -> dict:
    if current_type != "string":
        return {} # Leave alone if it's already an array/number
        
    combined = (key + " " + description).lower()
    
    # Heuristics for typing
    array_keywords = ["list", "inventory", "peers", "competitors", "metrics", "opportunities", "threats", "strengths", "weaknesses", "factors", "segments", "risks", "initiatives", "stakeholders"]
    number_keywords = ["rate", "cost", "price", "revenue", "margin", "score", "percentage", "ratio", "financial_results", "expenditure", "budget", "value", "capex"]
    boolean_keywords = ["is_", "has_", "boolean", "flag", "whether"]
    
    for kw in array_keywords:
        if kw in combined:
            return {"type": "array", "items": {"type": "string"}}
            
    for kw in number_keywords:
        if kw in combined:
            return {"type": "number"}
            
    for kw in boolean_keywords:
        if kw in combined:
            return {"type": "boolean"}
            
    return {"type": "string"}

def refactor_schema(filepath: Path):
    if not filepath.exists():
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        schema = json.load(f)
        
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    
    new_properties = {}
    new_required = []
    
    for old_key, val in properties.items():
        # 1. Verbose naming (CRITICAL-3)
        new_key = shorten_key(old_key)
        
        # Ensure uniqueness
        original_new_key = new_key
        counter = 2
        while new_key in new_properties:
            new_key = f"{original_new_key}_{counter}"
            counter += 1
            
        desc = val.get("description", "")
        # Move the old key text into description if it got truncated
        if old_key != new_key and new_key not in old_key:
             pass # just trust the new key
             
        # 2. Input/Output Typing (CRITICAL-2)
        type_updates = infer_type(new_key, desc, val.get("type", "string"))
        
        new_val = dict(val)
        if type_updates:
            new_val.update(type_updates)
            
        if "description" not in new_val or not new_val["description"]:
            new_val["description"] = old_key.replace('_', ' ').capitalize()
            
        new_properties[new_key] = new_val
        
        if old_key in required:
            new_required.append(new_key)
            
    schema["properties"] = new_properties
    schema["required"] = new_required
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)

def main():
    print("Starting schema refactor...")
    domains = [f for f in DOMAINS_DIR.iterdir() if f.is_dir()]
    count = 0
    for domain in domains:
        skills = [f for f in domain.iterdir() if f.is_dir()]
        for skill in skills:
            input_schema = skill / "input_schema.json"
            output_schema = skill / "output_schema.json"
            
            refactor_schema(input_schema)
            refactor_schema(output_schema)
            count += 2
            
    print(f"Successfully processed {count} schema files.")

if __name__ == "__main__":
    main()
