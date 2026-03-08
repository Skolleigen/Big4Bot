# Cash Conversion Cycle — Example

## Scenario
A mid-market B2B manufacturer with $95M in annual revenue is seeking a credit facility refinancing. The lender's due diligence team flags the company's working capital efficiency as a concern. The company's cash conversion cycle of 67 days is nearly double the industry median of 38 days for comparable industrial manufacturers, suggesting $4.2M in excess working capital that could be unlocked through operational improvements. Management is asked to present a remediation plan alongside the financing request.

## Inputs
- **Days Inventory Outstanding (DIO):** 45 days (industry median: 28 days)
- **Days Sales Outstanding (DSO):** 38 days (industry median: 32 days)
- **Days Payable Outstanding (DPO):** 16 days (industry median: 22 days)
- **Annual revenue:** $95M
- **Cost of goods sold (COGS):** $67M annually
- **Industry median CCC:** 38 days

## Analysis

**Step 1 — CCC Calculation:**
CCC = DIO + DSO − DPO = 45 + 38 − 16 = 67 days. The company takes 67 days from the point of paying for inventory to collecting cash from customers. Against the industry median of 38 days, the company is 29 days slower at converting its operating cycle into cash, placing it in approximately the 75th percentile of inefficiency relative to peers.

**Step 2 — Working Capital Trapped (Excess CCC Cost):**
Excess CCC days = 67 − 38 = 29 days. Daily revenue = $95M / 365 = $260,274. Excess working capital tied up = 29 × $260,274 = approximately $7.5M. An alternative calculation using COGS-based daily spend: excess inventory cost = (45 − 28) days × ($67M / 365) = 17 × $183,562 = $3.12M in excess inventory. Combined with the DSO and DPO gaps, total excess working capital approximates $4.2M to $7.5M depending on the method used, with the COGS-based inventory calculation being more conservative and appropriate for lender discussions.

**Step 3 — Component Decomposition:**
- DIO gap: 45 vs. 28 days = 17-day excess. Root cause assessment: the company carries safety stock above industry norms due to single-source supplier relationships and long lead times from overseas vendors. Estimated excess inventory value: $3.1M.
- DSO gap: 38 vs. 32 days = 6-day excess. Root cause: the company offers net-45 terms to its top 3 customers (representing 40% of revenue) while peers negotiate net-30 terms. Estimated receivables excess: $1.6M.
- DPO gap: 16 vs. 22 days = 6-day shortfall. Root cause: the company pays early to capture 2/10 net 30 discounts from key suppliers, but the annualized discount rate (18.4%) does not justify this when compared to cost of capital. Estimated cost of early payment: $1.1M in foregone float.

**Step 4 — Remediation Impact Modeling:**
If DIO is reduced to 35 days (achievable via dual-sourcing and demand forecasting improvements), DSO to 34 days (via revised customer payment terms), and DPO extended to 20 days (via payment term renegotiation), the revised CCC = 35 + 34 − 20 = 49 days. This represents an 18-day improvement from 67 days, releasing approximately $4.7M in cash at current revenue levels. Full peer parity (CCC = 38 days) would release approximately $7.5M.

**Step 5 — CCC Trend Analysis:**
A 3-year historical review shows CCC has deteriorated: Year 1: 54 days, Year 2: 61 days, Year 3 (current): 67 days. The deterioration correlates with (a) the shift to overseas suppliers in Year 2 (increased DIO) and (b) competitive pressure to extend customer payment terms in Year 2-3 (increased DSO). The trend signals a structural issue, not a seasonal one, requiring process and relationship changes rather than short-term fixes.

**Step 6 — Cash Flow Impact Assessment:**
Reducing CCC from 67 to 49 days by end of Year 1 would generate a one-time cash inflow of approximately $4.7M as working capital is released. Ongoing, a 49-day CCC at 10% revenue growth would require $712,000 less in working capital annually than the current 67-day CCC at the same growth rate, improving free cash flow conversion and reducing the credit facility size needed.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
