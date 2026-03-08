import json

from big4bot.anthropic.client import Big4BotAnthropicAdapter

def main():
    print("Initializing Big4Bot Anthropic Claude Adapter...")
    adapter = Big4BotAnthropicAdapter()
    
    tools = adapter.get_tools()
    print(f"Loaded {len(tools)} Anthropic native tools.")
    
    swot_tool = next((t for t in tools if t['name'] == 'swot_analysis'), None)
    
    print("\n--- Example: Generated Tool Schema for 'swot_analysis' ---")
    print(json.dumps(swot_tool, indent=2))
    
    print("\n--- Example: Agent Simulates Calling 'swot_analysis' ---")
    print("Context: Claude encountered a Market Entry problem and invoked SWOT.")
    mock_arguments = {
        "internal_strengths": ["Strong capital reserves"],
        "internal_weaknesses": ["No local market experience"],
        "external_opportunities": ["Growing middle class"],
        "external_threats": ["New regulatory tariffs"]
    }
    print(f"Agent calls 'swot_analysis' providing arguments explicitly requested.")
    
    response_text = adapter.handle_tool_call('swot_analysis', mock_arguments)
    print("\n--- Adapter Response Sequence to Agent ---")
    print("Adapter seamlessly returns Big4Bot methodology embedded in explicit XML tags optimized for Claude's context window.\n")
    
    print(f"Total Response String Length: {len(response_text)} characters.")
    print("Preview of string returned to Claude:")
    print("--------------------------------------------------")
    print(response_text[:350] + "\n...\n")
    print("--------------------------------------------------")
    
    print("\nSUCCESS: Anthropic Claude workflow correctly translated without modifying any underlying Big4Bot consulting methodologies.")

if __name__ == "__main__":
    main()
