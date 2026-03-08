# Financial Ratio Analysis

## Domain
Finance & Valuation

## Description
Systematic evaluation of financial statements using standardized ratios across liquidity, solvency, profitability, efficiency, and market valuation dimensions. It translates raw financial data into comparable, actionable metrics that reveal the financial health and performance trajectory of a business.

## Purpose
Financial ratio analysis converts the three financial statements into a diagnostic framework that identifies strengths, weaknesses, and anomalies in a company's financial position relative to its own history and industry peers. It serves as the entry point for more targeted analyses — such as DuPont decomposition, cash conversion cycle review, or DCF modeling — by flagging the areas that require deeper investigation. The multi-dimensional coverage ensures that a strong result in one area (e.g., high profitability) is not evaluated in isolation from risks in another (e.g., high leverage or poor liquidity).

## When to Use
- Conducting initial financial due diligence on a target company for M&A, investment, or lending purposes
- Performing annual or quarterly performance reviews comparing a company against itself over time and against industry peers
- Identifying financial warning signs such as liquidity deterioration, leverage creep, or margin compression
- Supporting credit analysis, covenant compliance monitoring, or lender presentations

## When NOT to Use
- For companies that have undergone major structural changes (acquisitions, divestitures, restatements) within the analysis period that make historical comparisons misleading without adjustment
- When industry-specific regulatory accounting standards (e.g., insurance, banking) render standard ratios non-comparable without specialist restatement
- As the sole basis for investment or credit decisions without supplementing with cash flow analysis and qualitative assessment

## Inputs Required
- Income statement for the current period and at least two prior periods
- Balance sheet as of the end of the current period and at least two prior periods
- Cash flow statement for the current period and at least two prior periods
- Industry median ratio benchmarks (from Damodaran, IBISWorld, or S&P Capital IQ)

## Optional Inputs
- Segment-level financial data for multi-division companies
- Analyst consensus revenue and earnings forecasts (for forward multiple calculations)

## Diagnostic Process
1. Collect and quality-check income statements, balance sheets, and cash flow statements for at least three fiscal years; normalize for non-recurring items, accounting policy changes, and M&A events.
2. Calculate liquidity ratios: Current Ratio (Current Assets / Current Liabilities) and Quick Ratio ((Current Assets - Inventory) / Current Liabilities); assess whether the company can meet short-term obligations.
3. Calculate solvency and leverage ratios: Debt-to-Equity (Total Debt / Equity), Net Debt-to-EBITDA (Net Debt / EBITDA), and Interest Coverage Ratio (EBIT / Interest Expense); assess long-term financial risk and debt serviceability.
4. Calculate profitability ratios: Gross Margin (Gross Profit / Revenue), EBITDA Margin (EBITDA / Revenue), Net Profit Margin (Net Income / Revenue), Return on Assets (Net Income / Average Total Assets), and Return on Equity (Net Income / Average Equity).
5. Calculate efficiency ratios: Asset Turnover (Revenue / Average Total Assets), Inventory Turnover (COGS / Average Inventory), and Accounts Receivable Turnover (Revenue / Average Accounts Receivable); these feed directly into the cash conversion cycle analysis.
6. Benchmark all ratios against industry medians and the two prior periods; flag any ratio that deviates by more than one standard deviation from the peer median or shows a directionally adverse three-year trend.
7. Synthesize findings into a structured commentary identifying the top three financial strengths and the top three risks or areas requiring further investigation; prioritize by materiality and urgency.

## Output
The analysis produces a ratio summary table organized by category (liquidity, solvency, profitability, efficiency), a peer comparison column, a three-year trend column, and a traffic-light rating (green / amber / red) for each ratio. A narrative summary identifies the most material findings and directs follow-on analysis.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- dupont-analysis
- cash-conversion-cycle
- unit-economics
- scenario-and-sensitivity-analysis
- comparable-company-valuation

## References
- Eugene Brigham, Joel Houston: *Fundamentals of Financial Management* (15th ed.)
- Aswath Damodaran: *Investment Valuation* (3rd ed., 2012)
- CFA Institute: *CFA Program Curriculum* — Financial Reporting and Analysis volumes
