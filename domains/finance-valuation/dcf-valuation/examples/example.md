# DCF Valuation — Example

## Scenario
A strategic acquirer is evaluating a $160M cash offer for a B2B logistics software company that provides transportation management and route optimization software to mid-market freight operators. The target has $40M in trailing revenue growing at 25% annually with an 18% EBITDA margin. The acquirer's corporate development team has been asked to conduct a DCF valuation to assess whether the $160M offer represents fair value or undervalues the business.

## Inputs
- **Base year revenue:** $40M (TTM)
- **Revenue growth rate (Years 1–5):** 25% declining to 15% by Year 5
- **EBITDA margin (Year 1):** 18%, expanding to 28% by Year 5
- **Capital expenditure (% of revenue):** 4% annually
- **Change in net working capital (% of revenue growth):** 8%
- **Depreciation & amortization:** $1.2M in Year 1, scaling with revenue
- **Tax rate:** 25%
- **WACC:** 11%
- **Terminal growth rate:** 3%
- **Current acquisition offer:** $160M

## Analysis

**Step 1 — Revenue and EBITDA Projection (5-Year Explicit Period):**
Year-by-year revenue and EBITDA projections based on stated growth and margin assumptions:
- Year 1: Revenue $50.0M (+25%), EBITDA margin 18.0%, EBITDA $9.0M
- Year 2: Revenue $61.5M (+23%), EBITDA margin 21.0%, EBITDA $12.9M
- Year 3: Revenue $74.4M (+21%), EBITDA margin 23.5%, EBITDA $17.5M
- Year 4: Revenue $88.2M (+18.5%), EBITDA margin 25.5%, EBITDA $22.5M
- Year 5: Revenue $101.4M (+15%), EBITDA margin 28.0%, EBITDA $28.4M

**Step 2 — Free Cash Flow to Firm (FCFF) Calculation:**
FCFF = EBITDA × (1 − tax rate) + D&A tax shield − Capex − Change in NWC

Simplified FCFF calculation using unlevered net income approach:
- Year 1: EBIT $7.8M (EBITDA $9.0M − D&A $1.2M), NOPAT $5.85M, Capex ($2.0M), NWC change ($0.8M), D&A +$1.2M, FCFF = $4.25M
- Year 2: EBIT $11.5M, NOPAT $8.63M, Capex ($2.46M), NWC change ($0.92M), D&A +$1.5M, FCFF = $6.75M
- Year 3: EBIT $15.6M, NOPAT $11.7M, Capex ($2.98M), NWC change ($1.04M), D&A +$1.85M, FCFF = $9.53M
- Year 4: EBIT $20.2M, NOPAT $15.15M, Capex ($3.53M), NWC change ($1.1M), D&A +$2.2M, FCFF = $12.72M
- Year 5: EBIT $25.4M, NOPAT $19.05M, Capex ($4.06M), NWC change ($1.05M), D&A +$2.5M, FCFF = $16.44M

**Step 3 — Discount Factors and PV of Explicit Period FCFFs:**
Discount factor at WACC = 11%:
- Year 1: 1 / (1.11)^1 = 0.901 → PV of FCFF = $3.83M
- Year 2: 1 / (1.11)^2 = 0.812 → PV of FCFF = $5.48M
- Year 3: 1 / (1.11)^3 = 0.731 → PV of FCFF = $6.97M
- Year 4: 1 / (1.11)^4 = 0.659 → PV of FCFF = $8.38M
- Year 5: 1 / (1.11)^5 = 0.593 → PV of FCFF = $9.75M

Sum of PV of explicit period FCFFs = $34.41M

**Step 4 — Terminal Value Calculation:**
Terminal year FCFF (Year 6 steady-state) = Year 5 FCFF × (1 + terminal growth rate) = $16.44M × 1.03 = $16.93M. Terminal value (Gordon Growth Model) = $16.93M / (0.11 − 0.03) = $16.93M / 0.08 = $211.6M. PV of terminal value = $211.6M × 0.593 (Year 5 discount factor) = $125.5M.

**Step 5 — Enterprise Value and Equity Value:**
Total DCF enterprise value = PV of explicit period FCFFs + PV of terminal value = $34.41M + $125.5M = $159.9M, approximately $160M. Adjusting for net debt (assume target is debt-free with $4M cash on hand): equity value = $160M + $4M = $164M intrinsic equity value. The terminal value represents 79% of total enterprise value, typical for high-growth software companies.

**Step 6 — Sensitivity Analysis on WACC and Terminal Growth Rate:**
Cross-referencing WACC (9%–13%) against terminal growth rate (2%–4%):
- WACC 9%, TGR 4%: EV = $231M (acquirer significantly underpaying)
- WACC 11%, TGR 3%: EV = $160M (base case, offer is at fair value)
- WACC 11%, TGR 2%: EV = $138M (offer is above intrinsic value)
- WACC 13%, TGR 3%: EV = $122M (offer is well above bear case)

The $160M offer is at or near intrinsic value under base case assumptions but requires the full 25% growth trajectory and margin expansion to materialize. There is limited upside for the acquirer without synergies at this price.

**Step 7 — Valuation Comparison:**
DCF intrinsic value (base case): ~$160M enterprise value. Current offer: $160M. Implied EV/Revenue (TTM): 4.0x. Implied EV/EBITDA (TTM): 22.2x. The offer is at the low end of the comparable company valuation range for logistics software peers (EV/Revenue 4x–7x), suggesting the target may be undervalued on a relative basis if market multiples hold, but the DCF analysis indicates the offer is at fair value on a standalone intrinsic basis.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
