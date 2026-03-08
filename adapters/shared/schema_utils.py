import jsonschema
from typing import Dict, Any

def validate_schema(instance: Dict[str, Any], schema: Dict[str, Any]) -> None:
    """
    Validates a JSON instance against a JSON schema to ensure compliance.
    Raises jsonschema.exceptions.ValidationError if invalid.
    """
    jsonschema.validate(instance=instance, schema=schema)


def to_openai_function(schema: Dict[str, Any], name: str, description: str) -> Dict[str, Any]:
    """
    Converts a standard JSON schema into an OpenAI Tool function definition.
    Strips out unsupported $schema or $id tags that sometimes cause validation errors.
    """
    cleaned_schema = {k: v for k, v in schema.items() if k not in ["$schema", "$id"]}
    
    return {
        "type": "function",
        "function": {
            "name": name.replace("-", "_"), # OpenAI requires alphanumeric/underscore names
            "description": description,
            "parameters": cleaned_schema,
            # For 2024 structured outputs, strict mode can optionally be added, 
            # though it requires additional constraints (like `additionalProperties: false`).
        }
    }


def to_anthropic_tool(schema: Dict[str, Any], name: str, description: str) -> Dict[str, Any]:
    """
    Converts a standard JSON schema into an Anthropic 'tool' object for Claude.
    """
    cleaned_schema = {k: v for k, v in schema.items() if k not in ["$schema", "$id"]}
    
    return {
        "name": name.replace("-", "_"),
        "description": description,
        "input_schema": cleaned_schema
    }


def to_gemini_function_declaration(schema: Dict[str, Any], name: str, description: str) -> Dict[str, Any]:
    """
    Converts a standard JSON schema into a Gemini FunctionDeclaration representation.
    """
    cleaned_schema = {k: v for k, v in schema.items() if k not in ["$schema", "$id"]}
    
    # In the google-genai SDK 2024+, Function Declarations expect parameters to use
    # standard OpenAPI 3 struct types, which are heavily based on JSON Schema.
    return {
        "name": name.replace("-", "_"),
        "description": description,
        "parameters": cleaned_schema
    }
