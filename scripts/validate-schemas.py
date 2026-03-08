"""
Big4Bot Schema Validation Script
Validates all output_schema.json and input_schema.json files.

Usage: python scripts/validate-schemas.py
"""
import json
import os
import sys

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "domains")
DRAFT07_SCHEMA_URI = "http://json-schema.org/draft-07/schema#"


def validate_json_syntax(filepath):
    """Validate that a file contains valid JSON."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, data, None
    except json.JSONDecodeError as e:
        return False, None, str(e)


def validate_json_schema_structure(data, filepath):
    """Validate that a JSON file follows JSON Schema draft-07 conventions."""
    errors = []
    
    # Must have $schema
    if "$schema" not in data:
        errors.append("Missing $schema declaration")
    elif data["$schema"] != DRAFT07_SCHEMA_URI:
        errors.append(f"Invalid $schema: {data['$schema']}")
    
    # Must have title
    if "title" not in data:
        errors.append("Missing title")
    
    # Must have type
    if "type" not in data:
        errors.append("Missing root type")
    
    # Must have properties
    if "properties" not in data:
        errors.append("Missing properties")
    
    # Must have required
    if "required" not in data:
        errors.append("Missing required array")
    
    return errors


def validate_output_schema(data, skill_id, filepath):
    """Validate output schema specific requirements."""
    errors = validate_json_schema_structure(data, filepath)
    
    props = data.get("properties", {})
    
    # Must have skill_id
    if "skill_id" not in props:
        errors.append("Missing skill_id property")
    elif props["skill_id"].get("const") != skill_id:
        errors.append(f"skill_id const mismatch: expected '{skill_id}', got '{props['skill_id'].get('const')}'")
    
    # Must have domain
    if "domain" not in props:
        errors.append("Missing domain property")
    
    # Must have output
    if "output" not in props:
        errors.append("Missing output property")
    else:
        output = props["output"]
        output_props = output.get("properties", {})
        
        # Output must have analysis_summary
        if "analysis_summary" not in output_props:
            errors.append("Missing output.analysis_summary")
        
        # Output must have confidence_level
        if "confidence_level" not in output_props:
            errors.append("Missing output.confidence_level")
        else:
            cl = output_props["confidence_level"]
            if "enum" not in cl:
                errors.append("confidence_level missing enum constraint")
    
    return errors


def validate_input_schema(data, skill_id, filepath):
    """Validate input schema specific requirements."""
    errors = validate_json_schema_structure(data, filepath)
    
    props = data.get("properties", {})
    required = data.get("required", [])
    
    # Must have problem_statement
    if "problem_statement" not in props:
        errors.append("Missing problem_statement property")
    elif "problem_statement" not in required:
        errors.append("problem_statement not in required")
    
    # Must have company_context
    if "company_context" not in props:
        errors.append("Missing company_context property")
    elif "company_context" not in required:
        errors.append("company_context not in required")
    
    return errors


def main():
    total_skills = 0
    total_errors = 0
    skills_with_errors = []
    missing_output = []
    missing_input = []
    
    for domain in sorted(os.listdir(BASE)):
        domain_path = os.path.join(BASE, domain)
        if not os.path.isdir(domain_path):
            continue
        for skill in sorted(os.listdir(domain_path)):
            skill_path = os.path.join(domain_path, skill)
            if not os.path.isdir(skill_path):
                continue
            
            skill_md = os.path.join(skill_path, "SKILL.md")
            if not os.path.exists(skill_md):
                continue
            
            total_skills += 1
            skill_errors = []
            
            # Check output_schema.json
            output_path = os.path.join(skill_path, "output_schema.json")
            if not os.path.exists(output_path):
                missing_output.append(skill)
                skill_errors.append("output_schema.json NOT FOUND")
            else:
                valid, data, parse_err = validate_json_syntax(output_path)
                if not valid:
                    skill_errors.append(f"output_schema.json JSON parse error: {parse_err}")
                else:
                    errs = validate_output_schema(data, skill, output_path)
                    skill_errors.extend([f"output_schema: {e}" for e in errs])
            
            # Check input_schema.json
            input_path = os.path.join(skill_path, "input_schema.json")
            if not os.path.exists(input_path):
                missing_input.append(skill)
                skill_errors.append("input_schema.json NOT FOUND")
            else:
                valid, data, parse_err = validate_json_syntax(input_path)
                if not valid:
                    skill_errors.append(f"input_schema.json JSON parse error: {parse_err}")
                else:
                    errs = validate_input_schema(data, skill, input_path)
                    skill_errors.extend([f"input_schema: {e}" for e in errs])
            
            # Check no old schema.json remains
            old_schema = os.path.join(skill_path, "schema.json")
            if os.path.exists(old_schema):
                skill_errors.append("OLD schema.json STILL EXISTS")
            
            if skill_errors:
                emoji = "[FAIL]"
                skills_with_errors.append({"skill": skill, "errors": skill_errors})
                total_errors += len(skill_errors)
            else:
                emoji = "[PASS]"
            
            print(f"  {emoji} {skill}")
            for err in skill_errors:
                print(f"     ERROR: {err}")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Schema Validation Report")
    print(f"{'='*60}")
    print(f"Schemas validated: {total_skills} / {total_skills}")
    print(f"Output schemas present: {total_skills - len(missing_output)} / {total_skills}")
    print(f"Input schemas present: {total_skills - len(missing_input)} / {total_skills}")
    print(f"Errors detected: {total_errors}")
    
    if total_errors == 0:
        print(f"\nResult: ALL PASS")
        return 0
    else:
        print(f"\nResult: {len(skills_with_errors)} skills with errors")
        return 1


if __name__ == "__main__":
    sys.exit(main())
