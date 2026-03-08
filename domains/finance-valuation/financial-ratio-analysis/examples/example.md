# Financial Ratio Analysis — Example

## Scenario
A private equity firm is conducting financial due diligence on a $200M revenue industrial services company that provides equipment maintenance and facility management services to oil and gas operators in the Gulf Coast region. The target has been flagged for elevated leverage and below-peer profitability during preliminary screening. The deal team has been asked to produce a comprehensive ratio analysis across liquidity, solvency, profitability, and efficiency dimensions before proceeding to a management presentation.

## Inputs
- **Revenue (TTM):** $200M
- **EBITDA (TTM):** $28M (14% margin)
- **Net income (TTM):** $6.2M
- **Total assets:** $185M
- **Total equity:** $41M
- **Total debt:** $127M
- **Current assets:** $52M
- **Current liabilities:** $43M
- **Cash and equivalents:** $8M
- **Accounts receivable:** $38M
- **Inventory:** $6M
- **Annual interest expense:** $10M
- **Industry peer median EBITDA margin:** 19%
- **Industry peer median D/E ratio:** 1.8x
- **Industry peer median current ratio:** 1.5x

## Analysis

**Step 1 — Liquidity Ratios:**
- Current ratio: $52M / $43M = 1.21x. The industry median for industrial services companies is 1.5x, placing the target below the threshold PE firms typically use as a minimum for acceptable short-term liquidity. A ratio below 1.5x indicates limited buffer if revenue collections slow or a large payable obligation comes due.
- Quick ratio (acid test): ($52M − $6M inventory) / $43M = $46M / $43M = 1.07x. Excluding inventory, the buffer narrows further. The quick ratio suggests the business depends on timely receivables collection to meet near-term obligations, which is a risk given the oil and gas customer concentration.
- Cash ratio: $8M / $43M = 0.19x. The company holds only $0.19 in cash for every $1.00 of current liabilities. This is a potential covenant risk in a cyclical downturn; however, an undrawn revolver would need to be evaluated as supplemental liquidity.

**Step 2 — Solvency and Leverage Ratios:**
- Debt-to-equity (D/E): $127M / $41M = 3.10x. The peer median is 1.8x. The target's leverage is 72% above the peer median, indicating a significantly more aggressive capital structure. This level of leverage is characteristic of a prior leveraged buyout or aggressive acquisition strategy.
- Net debt-to-EBITDA: ($127M − $8M cash) / $28M = $119M / $28M = 4.25x. Standard PE lending covenants typically require net leverage below 4.0x to 5.0x; the target is within the covenant range but close to the upper limit, leaving limited capacity for additional debt financing or a cyclical EBITDA decline.
- Interest coverage ratio (EBITDA/Interest): $28M / $10M = 2.8x. Most PE-backed covenants require a minimum of 2.5x–3.0x; the target is marginally within range but warrants close monitoring. A 10% revenue decline would reduce EBITDA to approximately $25M and push coverage toward 2.5x, the covenant floor.
- Debt-to-total-assets: $127M / $185M = 68.6%. Nearly 70 cents of every asset dollar is financed with debt, underscoring the capital structure risk.

**Step 3 — Profitability Ratios:**
- Gross margin: Not explicitly provided, but based on industry norms for industrial services, estimated at 28–32%. EBITDA margin of 14% is 500 basis points below the peer median of 19%, which is a significant gap requiring explanation.
- EBITDA margin: 14% vs. peer median 19%. This gap suggests either structural cost disadvantages (higher labor costs, suboptimal route density), pricing pressure from customer concentration (top 3 customers likely represent 50%+), or underinvestment in operational efficiency.
- Net profit margin: $6.2M / $200M = 3.1%. After interest expense of $10M on $127M debt, the company earns only 3 cents of net income per dollar of revenue.
- Return on assets (ROA): $6.2M / $185M = 3.4%. Below the risk-free rate, indicating the asset base is not generating sufficient returns relative to its cost.
- Return on equity (ROE): $6.2M / $41M = 15.1%. This appears relatively attractive but is mechanically elevated by the high leverage (equity multiplier 4.5x); without the debt, ROE would be significantly lower.

**Step 4 — Efficiency Ratios:**
- Days Sales Outstanding (DSO): ($38M / $200M) × 365 = 69.4 days. For industrial services with oil and gas clients, this is somewhat elevated (peer median approximately 55 days). Slow-paying E&P customers and disputed invoices are common contributors.
- Asset turnover: $200M / $185M = 1.08x. Moderate; suggests equipment and vehicle fleet are being deployed reasonably but with room for improvement through fleet utilization optimization.
- Accounts receivable turnover: $200M / $38M = 5.26x. The company collects its receivables approximately 5.3 times per year. At industry norms of 6–7 turns, there is a working capital gap of $5M–$8M in receivables.

**Step 5 — Integrated Assessment and Red Flags:**
Four ratios fall outside acceptable thresholds for a PE acquisition at this price:
1. Current ratio (1.21x, below 1.5x minimum): short-term liquidity risk
2. D/E ratio (3.10x, vs. 1.8x peer median): capital structure too aggressive for industrial cyclical
3. EBITDA margin (14%, vs. 19% peer median): structural profitability gap requires 500 bps of margin recovery to justify peer-level valuation
4. Interest coverage (2.8x): dangerously close to typical covenant floors, making the business vulnerable to any revenue softening

**Step 6 — Ratio Trend Analysis:**
Year-over-year trends (Year 2 vs. Year 3, if available) should be examined. Based on available data, EBITDA margin has been compressing (consistent with the current reading vs. prior management commentary suggesting 16–17% "normalized" margins), suggesting organic performance deterioration rather than a one-time event. This elevates the risk profile relative to a stable-margin business at the same current levels.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
