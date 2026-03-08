# DuPont Analysis

## Domain
Finance & Valuation

## Description
Financial decomposition framework that breaks Return on Equity (ROE) into three or five component drivers — profit margin, asset turnover, and financial leverage — to diagnose the root causes of ROE performance and change over time.

## Purpose
DuPont analysis transforms ROE from a single aggregate ratio into a structured diagnostic tool, allowing analysts to determine whether changes in shareholder returns are driven by operational improvements, asset efficiency gains, or changes in financial risk through leverage. The framework prevents misattribution of performance by forcing a systematic decomposition before drawing conclusions, and it directs management attention to the specific lever — margin, turnover, or leverage — with the greatest improvement opportunity. The 5-factor extension adds granularity by isolating the tax and interest burden effects from core operating margin.

## When to Use
- Diagnosing why a company's ROE has changed materially between periods or differs from peer benchmarks
- Evaluating whether a competitor's superior ROE is driven by genuine operational efficiency or elevated financial risk
- Identifying the primary performance lever for management focus or operational improvement programs
- Supporting strategy reviews, management presentations, or investor communications on profitability drivers

## When NOT to Use
- For companies with negative equity (the equity multiplier and ROE become meaningless)
- When comparing companies across different accounting frameworks (e.g., US GAAP vs. IFRS) without adjusting for material differences in asset recognition and leverage measurement
- As a standalone tool when the analysis requires cash-flow-based performance assessment rather than accrual-based metrics

## Inputs Required
- Net income for the period
- Total revenues for the period
- Total assets (average for the period)
- Total shareholders' equity (average for the period)
- Interest expense and pre-tax income (for 5-factor extension)

## Optional Inputs
- Tax expense (to isolate tax burden factor in the 5-factor model)
- Peer company financials for cross-sectional benchmarking

## Diagnostic Process
1. Calculate the headline ROE: Net Income divided by Average Shareholders' Equity; express as a percentage and note the year-over-year change.
2. Decompose ROE using the 3-factor DuPont model: Net Profit Margin (Net Income / Revenue) multiplied by Asset Turnover (Revenue / Average Total Assets) multiplied by Equity Multiplier (Average Total Assets / Average Shareholders' Equity); verify that the product of the three factors equals the calculated ROE.
3. Optionally expand to the 5-factor model: Tax Burden (Net Income / Pre-Tax Income) multiplied by Interest Burden (Pre-Tax Income / EBIT) multiplied by EBIT Margin (EBIT / Revenue) multiplied by Asset Turnover (Revenue / Assets) multiplied by Equity Multiplier (Assets / Equity); each factor isolates a distinct value driver.
4. Benchmark each factor against the same company in prior periods (minimum 3 years) and against direct industry peers to establish whether observed levels are above or below expectations.
5. Identify the primary driver of ROE change by calculating the contribution of each factor to the total ROE delta using period-over-period decomposition attribution.
6. Trace the identified driver to its operational or financial root cause: for example, margin compression traced to pricing pressure or input cost inflation; asset turnover decline traced to excess inventory buildup or receivables deterioration; leverage increase traced to debt-funded acquisitions or share buybacks.
7. Recommend targeted interventions matched to the root cause: operational efficiency programs for margin, working capital optimization for asset turnover, or capital structure review for leverage; quantify the ROE improvement achievable from each lever.

## Output
The analysis delivers a structured DuPont decomposition table for the current and prior periods, a factor-level peer comparison, a root-cause attribution narrative, and quantified improvement targets for the primary driver. A bridge chart showing ROE factor contributions over time is included where presentation is required.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- financial-ratio-analysis
- scenario-and-sensitivity-analysis
- unit-economics
- comparable-company-valuation

## References
- Donaldson Brown: *DuPont Corporation Internal Financial Reporting Framework* (1920)
- Stephen Penman: *Financial Statement Analysis and Security Valuation* (5th ed., 2013)
- Aswath Damodaran: *Investment Valuation* (3rd ed., 2012) — profitability and return analysis chapters
