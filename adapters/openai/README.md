# OpenAI Adapter

## Overview
This adapter enables Big4Bot consulting skills to be exposed as tools within the OpenAI Agents ecosystem.

## Integration Approach
Each Big4Bot skill can be registered as an OpenAI function tool by:

1. **Parsing the `SKILL.md`** to extract the skill's purpose, inputs, and diagnostic process.
2. **Using `schema.json`** to define the function's structured output format.
3. **Registering the skill** as a tool in the OpenAI Assistants API or Agents SDK.

## Implementation Pattern
```python
# Example: Register a Big4Bot skill as an OpenAI tool
tool_definition = {
    "type": "function",
    "function": {
        "name": "swot_analysis",
        "description": "Strategic diagnostic of strengths, weaknesses, opportunities and threats.",
        "parameters": {
            "type": "object",
            "properties": {
                "company": {"type": "string", "description": "Company or organization to analyze"},
                "context": {"type": "string", "description": "Additional business context"}
            },
            "required": ["company"]
        }
    }
}
```

## Status
Placeholder - adapter implementation pending.
