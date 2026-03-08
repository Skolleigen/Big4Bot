# Scenario and Sensitivity Analysis

## Domain
Finance & Valuation

## Description
Quantitative modeling technique that evaluates the impact of changes in key assumptions on financial outcomes, stress-testing projections under multiple scenarios. It transforms a single-point financial model into a probabilistic range of outcomes that supports more robust decision-making.

## Purpose
Scenario and sensitivity analysis makes the uncertainty embedded in financial projections explicit and quantifiable, replacing false precision with a structured range of outcomes tied to specific assumption changes. It identifies which input variables have the greatest leverage on value or cash flow, directing management and investor attention to the risks and opportunities that matter most. The framework also tests whether a proposed strategy or investment is robust — generating acceptable returns even under adverse conditions — or fragile to plausible downside scenarios.

## When to Use
- Stress-testing a DCF, LBO, or business plan model before presenting to an investment committee, board, or lender
- Evaluating strategic options where outcomes depend heavily on uncertain market or competitive assumptions
- Preparing for due diligence or investor presentations where questions about downside scenarios are expected
- Setting financial covenants, credit limits, or contingency reserves based on quantified downside exposure

## When NOT to Use
- When the base model itself is unreliable or built on data of questionable quality, such that scenario analysis adds false rigor to a structurally flawed foundation
- When the variable being stressed is not actually uncertain (e.g., a contractually fixed revenue stream)
- As a substitute for Monte Carlo simulation when the joint probability distribution of multiple interacting variables is required and sufficient data exists to parameterize it

## Inputs Required
- Base case financial model with all key assumptions explicitly labeled
- Identified set of key value drivers and sensitivity variables (revenue growth rate, EBITDA margin, churn rate, WACC, capex intensity)
- Range definitions for each variable: bear case (pessimistic), base case, and bull case values
- Target output metric (NPV, equity value, IRR, EBITDA, free cash flow, or payback period)

## Optional Inputs
- Probability weights for each scenario (bear / base / bull) to support probability-weighted valuation
- Correlated variable pairs where joint movement is economically meaningful (e.g., revenue growth and gross margin)

## Diagnostic Process
1. Identify the key value drivers and assumptions underlying the base case model by reviewing all inputs and calculating their individual impact on the output metric; prioritize the top 5-8 variables by impact.
2. Define the sensitivity range for each selected variable: set the bear case at a level consistent with a historical stress scenario or the 10th percentile of observed outcomes, and the bull case at the 90th percentile or a plausible upside scenario.
3. Construct a one-variable sensitivity table for each key driver by holding all other assumptions at base case and varying the target variable across its bear-to-bull range; record the output metric at each interval.
4. Build a scenario matrix combining the bear, base, and bull values for all key variables simultaneously to produce at least three named scenarios: downside (all bear inputs), base (all base inputs), and upside (all bull inputs); optionally add a stress scenario using the most adverse plausible combination.
5. Calculate the output metric (e.g., NPV, EBITDA, or equity value) for each scenario and document the delta versus the base case in both absolute and percentage terms.
6. Construct a tornado chart ranking each sensitivity variable by its absolute impact on the output metric across its defined range; the top three variables typically explain 60-80% of total output variance and are the primary risk management focus.
7. Recommend decisions that are robust across scenarios — actions that generate acceptable outcomes under both base and bear conditions — and specify the trigger conditions or monitoring metrics that would indicate a scenario shift requiring a management response.

## Output
The analysis delivers a one-variable sensitivity table for each key driver, a multi-scenario summary table with output metrics for each named scenario, a tornado chart ranking variables by impact, and a narrative identifying the key risk exposures and recommended mitigation actions. A probability-weighted output is included when scenario probabilities are assigned.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- dcf-valuation
- unit-economics
- financial-ratio-analysis
- dupont-analysis
- break-even-analysis

## References
- McKinsey & Company: *Financial Modeling Standards and Best Practices* (internal practitioner framework)
- Aswath Damodaran: *Investment Valuation* (3rd ed., 2012) — chapters on uncertainty and risk in valuation
- CFA Institute: *CFA Program Curriculum Level 2* — Equity Valuation: Applications and Processes
