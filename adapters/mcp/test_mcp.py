import json
from server import list_frameworks, describe_framework, plan_consulting_analysis

print("--- list_frameworks(domain='strategy') ---")
print(list_frameworks(domain="strategy"))

print("\n--- describe_framework('swot-analysis') ---")
print(describe_framework('swot-analysis'))

print("\n--- plan_consulting_analysis(problem_type='strategic_problem') ---")
print(plan_consulting_analysis(problem_type='strategic_problem'))
