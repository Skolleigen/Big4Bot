import os
import sys

# Ensure big4bot can be imported if running locally without pip install
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from big4bot.shared.big4bot_loader import Big4BotLoader

def main():
    print("==================================================")
    print("  Big4Bot Consulting Methodology Agent Example   ")
    print("==================================================\n")

    # Step 1 — Problem Statement
    # The agent receives a real-world business context
    problem = """
    Our SaaS startup is experiencing declining customer retention
    and we suspect our pricing model may not align with customer value.
    """
    print("Problem:")
    print(f"{problem.strip()}\n")

    # Step 2 — Problem Classification & Planning
    # The agent classifies this as a 'strategic_problem' and uses Big4Bot
    # to dynamically generate a loop-free chain of frameworks to diagnose it.
    print("Initializing Big4Bot Reasoning Planner...")
    loader = Big4BotLoader()
    
    plan_data = loader.plan_consulting_analysis(problem_type="strategic_problem")
    if "error" in plan_data:
        print(f"Planning failed: {plan_data['error']}")
        return
        
    execution_plan = plan_data.get("analysis_plan", [])

    # Step 3 — Display the Planned Framework Chain
    print("\nConsulting Analysis Plan:")
    for step in execution_plan:
        print(f"{step['step']}. {step['framework']}")
        
    print("\n" + "-"*50 + "\n")

    # Step 4 — Simulated Framework Execution
    # Normally, an LLM would parse the 'input_schema' for each tool, ingest the 'methodology', 
    # and strictly emit JSON matching the 'output_schema'.
    # For this example, we mock the results to demonstrate data accumulation.
    
    mock_llm_responses = {
        "pestle-analysis": "Identified high inflation affecting customer IT budgets.",
        "swot-analysis": "Customer churn driven by price/value mismatch.",
        "market-segmentation": "Mid-market tier requires more flexible packaging.",
        "value-proposition-canvas": "Features are overbuilt vs. customer willingness to pay."
    }

    analysis_results = []

    for step in execution_plan:
        skill_id = step["framework"]
        print(f"Executing framework: {skill_id}")
        
        # Simulated agent synthesis
        simulated_insight = mock_llm_responses.get(skill_id, "Standard analysis completed.")
        
        result = {
            "framework": skill_id,
            "insight": simulated_insight
        }
        
        analysis_results.append(result)

    # Step 5 — Accumulate Insights
    # The agent strings together the structured outputs to form a final synthesized deliverable.
    
    print("\n==================================================")
    print("             Final Analysis Summary               ")
    print("==================================================\n")
    
    for result in analysis_results:
        # Standardize formatting for display
        friendly_name = result["framework"].replace('-', ' ').title()
        print(f"Framework: {friendly_name}")
        print(f"Insight: {result['insight']}")
        print()
        
    print("--------------------------------------------------")
    print("Note: Big4Bot provided the consulting methodology.")
    print("The reasoning planner proposed the logical chain.")
    print("The LLM (mocked here) executed the structured analysis.")

if __name__ == "__main__":
    main()
