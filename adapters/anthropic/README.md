# Anthropic Adapter

## Overview
This adapter enables Big4Bot consulting skills to be exposed as tools within the Anthropic Claude agent ecosystem.

## Integration Approach
Each Big4Bot skill can be registered as a Claude tool by:

1. **Parsing the `SKILL.md`** to extract the skill's purpose, inputs, and diagnostic process.
2. **Using `schema.json`** to define the tool's input schema.
3. **Registering the skill** via the Anthropic Tool Use API.

## Implementation Pattern
```python
# Example: Register a Big4Bot skill as a Claude tool
tool_definition = {
    "name": "swot_analysis",
    "description": "Strategic diagnostic of strengths, weaknesses, opportunities and threats.",
    "input_schema": {
        "type": "object",
        "properties": {
            "company": {"type": "string", "description": "Company or organization to analyze"},
            "context": {"type": "string", "description": "Additional business context"}
        },
        "required": ["company"]
    }
}
```

## Status
Placeholder - adapter implementation pending.
