# Gemini Adapter

## Overview
This adapter enables Big4Bot consulting skills to be exposed as function declarations within the Google Gemini ecosystem.

## Integration Approach
Each Big4Bot skill can be registered as a Gemini function by:

1. **Parsing the `SKILL.md`** to extract the skill's purpose, inputs, and diagnostic process.
2. **Using `schema.json`** to define the function's response schema.
3. **Registering the skill** as a function declaration in the Gemini API.

## Implementation Pattern
```python
# Example: Register a Big4Bot skill as a Gemini function
from google.generativeai.types import FunctionDeclaration

swot_tool = FunctionDeclaration(
    name="swot_analysis",
    description="Strategic diagnostic of strengths, weaknesses, opportunities and threats.",
    parameters={
        "type": "object",
        "properties": {
            "company": {"type": "string", "description": "Company or organization to analyze"},
            "context": {"type": "string", "description": "Additional business context"}
        },
        "required": ["company"]
    }
)
```

## Status
Placeholder - adapter implementation pending.
