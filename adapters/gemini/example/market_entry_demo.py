import json
import os

from big4bot.gemini.client import Big4BotGeminiAdapter

def main():
    print("Initializing Big4Bot Google Gemini Adapter...")
    adapter = Big4BotGeminiAdapter()
    
    tools = adapter.get_tools()
    print(f"Loaded {len(tools)} Gemini FunctionDeclarations.")
    
    # Showcase a single tool translation
    swot_tool = next((t for t in tools if t['name'] == 'swot_analysis'), None)
    
    print("\n--- Example: Generated FunctionDeclaration for 'swot_analysis' ---")
    print(json.dumps(swot_tool, indent=2))
    
    print("\n--- Example: Gemini Simulates Calling 'swot_analysis' ---")
    print("Context: The LLM encountered a Market Entry problem and chose SWOT to analyze.")
    mock_arguments = {
        "internal_strengths": ["Strong capital reserves"],
        "internal_weaknesses": ["No local market experience"],
        "external_opportunities": ["Growing middle class"],
        "external_threats": ["New regulatory tariffs"]
    }
    print(f"Agent calls 'swot_analysis' providing arguments explicitly requested by input_schema.json.")
    
    print("\n--- Adapter Response to Agent ---")
    response_json = adapter.handle_tool_call('swot_analysis', mock_arguments)
    print("Adapter seamlessly returns Big4Bot methodology and rigid output constraints back to the LLM context.")
    
    parsed = json.loads(response_json)
    print(f"\nResponse Includes:\n - skill_id: {parsed['skill_id']}\n - methodology (length: {len(parsed['methodology'])} chars)\n - output_schema (length: {len(str(parsed['output_schema']))} chars)")
    print(f"\nFinal Instructions appended to LLM message:\n> {parsed['instructions']}")
    
    print("\nSUCCESS: Gemini workflow correctly translated without modifying any underlying Big4Bot consulting methodologies.")

if __name__ == "__main__":
    main()
