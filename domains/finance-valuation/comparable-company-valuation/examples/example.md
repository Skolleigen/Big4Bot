# Comparable Company Valuation — Example

## Scenario
A private equity firm is conducting buy-side due diligence on a mid-market cloud security company that provides identity and access management (IAM) software to enterprise clients. The target has $18M in trailing twelve-month (TTM) revenue growing at 32% year-over-year and $4.5M in TTM EBITDA (25% margin). The PE firm's investment committee requires a public comparable company valuation to anchor the acquisition offer range ahead of a management presentation.

## Inputs
- **Target revenue (TTM):** $18M
- **Target EBITDA (TTM):** $4.5M
- **Target revenue growth rate:** 32% YoY
- **Target EBITDA margin:** 25%
- **Comparable universe:** 6 publicly traded cloud security companies (IAM and endpoint security focus)
- **Peer median EV/Revenue (NTM):** 6.0x
- **Peer median EV/EBITDA (NTM):** 22.0x
- **Peer EV/Revenue range:** 4.2x to 9.1x
- **Peer EV/EBITDA range:** 16.0x to 31.0x

## Analysis

**Step 1 — Comparable Universe Selection:**
Six publicly traded cloud security peers were selected based on three criteria: (1) primary business in cloud-delivered security software (IAM, endpoint, or SASE), (2) revenue between $15M and $200M TTM (size-comparable), and (3) SaaS-dominant revenue model (>70% recurring). Selected peers include companies in the IAM and zero-trust security subsegments. Two initially considered names were excluded: one due to hardware-heavy revenue mix (not comparable business model) and one due to pending acquisition (distorted trading multiples).

**Step 2 — Peer Multiple Benchmarking:**
The 6-company peer set shows the following NTM multiples (sorted by EV/Revenue):
- Peer A: EV/Revenue 9.1x, EV/EBITDA 31.0x (fastest grower, 45% revenue growth)
- Peer B: EV/Revenue 7.8x, EV/EBITDA 27.0x (38% growth)
- Peer C: EV/Revenue 6.2x, EV/EBITDA 23.0x (30% growth, best margin profile)
- Peer D: EV/Revenue 5.9x, EV/EBITDA 21.0x (28% growth)
- Peer E: EV/Revenue 5.1x, EV/EBITDA 18.0x (22% growth)
- Peer F: EV/Revenue 4.2x, EV/EBITDA 16.0x (15% growth, lower margin)

Peer median: EV/Revenue 6.0x, EV/EBITDA 22.0x. Mean: EV/Revenue 6.4x, EV/EBITDA 22.7x.

**Step 3 — Positioning the Target Within the Peer Set:**
The target's 32% revenue growth places it between Peer B and Peer C by growth rate, suggesting a fair multiple positioning near the median to slightly above. However, two adjustments are warranted: (a) the target is private, warranting a 15–20% illiquidity discount versus public peers; (b) the target's smaller scale ($18M vs. $50M+ for most peers) may compress multiples slightly. A 15% private company discount applied to median multiples yields adjusted multiples of approximately 5.1x EV/Revenue and 18.7x EV/EBITDA.

**Step 4 — Implied Valuation Range:**
Using unadjusted peer medians (pre-discount):
- EV/Revenue: $18M × 6.0x = $108M implied EV
- EV/EBITDA: $4.5M × 22.0x = $99M implied EV
- Unadjusted range midpoint: $103.5M

Applying the 15% private company discount:
- EV/Revenue adjusted: $108M × 0.85 = $91.8M
- EV/EBITDA adjusted: $99M × 0.85 = $84.2M
- Adjusted range midpoint: $88M

The valuation range for offer anchoring is $84M to $108M, with the midpoint at approximately $96M. The upper end assumes the target commands peer-level public market multiples without illiquidity discount (strategic acquirer logic); the lower end applies the full discount (financial buyer logic).

**Step 5 — Sensitivity to Multiple Selection:**
If the relevant peer set is narrowed to only IAM-focused companies (Peers A, B, C), the median EV/EBITDA rises to 27.0x, implying an unadjusted EBITDA-based valuation of $121.5M. This represents the bull case for sellers positioning the target as a pure-play IAM asset. Conversely, applying 25th percentile multiples (EV/Revenue 4.6x, EV/EBITDA 17.0x) yields a bear case of $74M–$83M, applicable if growth decelerates or the deal is structured as an asset purchase.

**Step 6 — Valuation Cross-Check:**
As a cross-check, the Rule of 40 score (revenue growth + EBITDA margin = 32% + 25% = 57%) places the target above the 40-point threshold that institutional SaaS investors use as a quality benchmark. High Rule of 40 scores correlate with premium multiples in the peer set (Peers A and B both score above 55%), supporting the case for applying above-median multiples absent the private company discount.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
