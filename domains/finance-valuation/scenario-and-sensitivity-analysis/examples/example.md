# Scenario & Sensitivity Analysis — Example

## Scenario
A regional e-commerce company specializing in outdoor and sporting goods ($85M revenue, 12% EBITDA margin) is evaluating a $14M investment in a new 180,000 sq. ft. fulfillment warehouse in the Mid-Atlantic region. The expansion is intended to reduce last-mile delivery costs and support anticipated revenue growth. The CFO has asked for a scenario and sensitivity analysis to present to the board before approving the capital expenditure, with particular focus on the payback period and IRR under different market conditions.

## Inputs
- **Capital investment:** $14M (warehouse fit-out and automation equipment)
- **Base case revenue growth rate:** 22% per year (Years 1–3), moderating to 15% thereafter
- **Base case EBITDA margin:** 15% (improved from 12% due to fulfillment cost savings)
- **Bear case revenue growth rate:** 8% per year (market softens, competition intensifies)
- **Bear case EBITDA margin:** 10% (fulfillment savings partially offset by volume-based fixed cost absorption)
- **Bull case revenue growth rate:** 35% per year (strong market share capture)
- **Bull case EBITDA margin:** 18% (full automation efficiency realized)
- **Discount rate (WACC):** 10%
- **Incremental EBITDA from warehouse (% of total EBITDA):** 40% attributed to new capacity
- **Analysis horizon:** 5 years
- **Depreciation of warehouse investment:** straight-line over 10 years ($1.4M/year)

## Analysis

**Step 1 — Base Case Financial Projection:**
Revenue trajectory (base case, $85M starting point):
- Year 1: $103.7M (+22%), EBITDA margin 15%, EBITDA $15.6M
- Year 2: $126.5M (+22%), EBITDA $19.0M
- Year 3: $154.3M (+22%), EBITDA $23.1M
- Year 4: $177.4M (+15%), EBITDA $26.6M
- Year 5: $204.0M (+15%), EBITDA $30.6M

Incremental EBITDA attributable to warehouse investment (40% of total EBITDA):
- Year 1: $6.2M, Year 2: $7.6M, Year 3: $9.2M, Year 4: $10.6M, Year 5: $12.2M

Cumulative incremental EBITDA over 5 years: $45.8M. Against a $14M investment, simple payback = $14M / ($45.8M / 5 years average) = $14M / $9.16M = 1.53 years. Discounted payback calculation: Year 1 PV ($6.2M / 1.10 = $5.6M), Year 2 PV ($7.6M / 1.21 = $6.3M). Cumulative discounted cash flow crosses $14M early in Year 3. Base case discounted payback: approximately 3.2 years.

**Step 2 — Bear Case Financial Projection:**
Revenue trajectory (8% growth):
- Year 1: $91.8M, EBITDA margin 10%, EBITDA $9.2M
- Year 2: $99.1M, EBITDA $9.9M
- Year 3: $107.0M, EBITDA $10.7M
- Year 4: $115.6M, EBITDA $11.6M
- Year 5: $124.8M, EBITDA $12.5M

Incremental EBITDA (40%): Year 1 $3.7M, Year 2 $4.0M, Year 3 $4.3M, Year 4 $4.6M, Year 5 $5.0M.
Cumulative 5-year discounted incremental EBITDA: approximately $16.7M.
Bear case discounted payback: approximately 5.8 years. The investment barely justifies itself on a discounted basis within a standard 5-year planning horizon.

**Step 3 — Bull Case Financial Projection:**
Revenue trajectory (35% growth):
- Year 1: $114.8M, EBITDA margin 18%, EBITDA $20.7M
- Year 2: $155.0M, EBITDA $27.9M
- Year 3: $209.2M, EBITDA $37.7M
- Year 4: $282.4M, EBITDA $50.8M
- Year 5: $381.2M, EBITDA $68.6M

Incremental EBITDA (40%): Year 1 $8.3M, Year 2 $11.2M, Year 3 $15.1M, Year 4 $20.3M, Year 5 $27.4M.
Bull case discounted payback: approximately 2.1 years. 5-year IRR approximately 68%.

**Step 4 — Scenario Summary Comparison:**

| Metric | Bear Case | Base Case | Bull Case |
|---|---|---|---|
| Revenue growth | 8% | 22% | 35% |
| EBITDA margin | 10% | 15% | 18% |
| Discounted payback | 5.8 years | 3.2 years | 2.1 years |
| 5-year IRR | 8% | 32% | 68% |
| 5-year NPV (incremental) | $2.7M | $31.8M | $68.4M |

**Step 5 — Sensitivity Analysis (Single-Variable):**
Holding all other assumptions at base case values, the payback period responds to individual driver changes as follows:

Revenue growth rate sensitivity:
- 8% growth: 5.8-year payback
- 15% growth: 4.1-year payback
- 22% growth (base): 3.2-year payback
- 30% growth: 2.5-year payback
- 35% growth: 2.1-year payback

EBITDA margin sensitivity (at 22% revenue growth):
- 10% margin: 4.8-year payback
- 12% margin: 4.0-year payback
- 15% margin (base): 3.2-year payback
- 18% margin: 2.7-year payback
- 20% margin: 2.4-year payback

Capital cost sensitivity (at base case growth and margin):
- $10M investment: 2.3-year payback
- $14M investment (base): 3.2-year payback
- $18M investment: 4.1-year payback
- $22M investment: 5.0-year payback

**Step 6 — Tornado Chart Analysis (Variance Attribution):**
Ranking the impact of each input variable on NPV variance across the defined bear-to-bull range:
1. Revenue growth rate: drives $65.7M of the $65.7M total NPV range (68% of total variance) — largest single driver
2. EBITDA margin: drives $18.3M of NPV variance (19% of total variance)
3. Capital expenditure amount: drives $8.2M of NPV variance (8% of total variance)
4. WACC / discount rate: drives $3.1M of NPV variance (3% of total variance)
5. Attribution percentage (40% incremental): drives $2.8M of NPV variance (2% of total variance)

Revenue growth rate accounts for 68% of total outcome variance, making it the primary risk and opportunity driver. The board should focus due diligence on the revenue growth forecast assumptions rather than debating capital cost or margin assumptions.

**Step 7 — Decision Framework:**
The investment has a positive NPV in the base and bull cases but barely positive in the bear case (5.8-year discounted payback on a 5-year investment horizon). The critical assumption is a minimum revenue growth rate of approximately 13% to achieve the board's stated 4-year payback hurdle. Given the company's trailing 3-year growth rate of 28%, achieving 13% is considered conservative. The probability-weighted expected NPV (25% bear, 55% base, 20% bull) = (0.25 × $2.7M) + (0.55 × $31.8M) + (0.20 × $68.4M) = $0.7M + $17.5M + $13.7M = $31.9M, strongly favoring investment approval.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
