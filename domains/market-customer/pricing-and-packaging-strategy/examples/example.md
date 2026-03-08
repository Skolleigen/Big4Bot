# Pricing & Packaging Strategy — Example

## Scenario
Taskflow is a project management SaaS platform with 14,200 paying accounts and $12.4M ARR, currently operating on a flat $29/user/month pricing model. Net Revenue Retention (NRR) is 98%, well below the SaaS benchmark of 110–120% for a B2B tool. Churn analysis shows sub-10-seat accounts churning at 34% annually (vs. 9% for accounts above 50 seats). Power users — accounts with 20+ seats using automation and integration features heavily — are paying the same per-seat rate as light users. The team wants to redesign packaging to drive expansion revenue from power users and reduce SMB churn.

## Inputs
- **Current pricing:** Flat $29/user/month, no tiers, annual or monthly billing, 14-day free trial
- **COGS:** $4.20/user/month (infrastructure, support, customer success allocation)
- **Competitive set:** Asana (Starter $10.99, Advanced $24.99, Enterprise custom), Monday.com (Basic $9, Standard $12, Pro $19, Enterprise custom), Notion (Plus $10, Business $18, Enterprise custom), ClickUp (Unlimited $7, Business $12, Business+ $19, Enterprise custom), Linear ($8 member/month flat to $16 enterprise)
- **Usage data signals:** Top 20% of accounts by usage: avg 31 seats, 847 automation runs/month, 6.2 integrations active; Bottom 20%: avg 4 seats, 12 automation runs/month, 0.8 integrations active

## Analysis

**Step 1 — Cost floor establishment:**
COGS of $4.20/user/month confirmed through finance review. At current $29/user/month, gross margin is 85.5% — healthy but not optimized by segment. Sub-10-seat accounts at $29/user average 4.1 seats = $119/month revenue; support cost analysis shows these accounts consume disproportionate support resources (avg 2.3 tickets/month vs. 0.8 for mid-market accounts). Contribution margin for sub-10 accounts estimated at 61% vs. 89% for accounts above 25 seats.

**Step 2 — Willingness-to-pay survey:**
Van Westendorp Price Sensitivity Meter administered to 214 customers segmented by usage tier. Results: SMB segment (1–10 seats) — optimal price range $8–$14/user/month; professional segment (11–50 seats) — optimal price range $18–$28/user/month; power users (50+ seats or heavy automation) — willing to pay $32–$48/user/month for advanced automation and integrations. Current $29/user/month pricing is above the optimal range for SMBs and below optimal for power users — simultaneously over-pricing and under-pricing.

**Step 3 — Competitive benchmarking:**
All five competitors use tiered pricing with 3–4 tiers. Entry-level tiers range $7–$11/user/month with limited automation and integrations. Mid-tier ranges $12–$25/user/month with expanded features. Enterprise is custom-priced. Differentiation levers used by competitors: automation runs (Asana, Monday), storage limits (Notion), member count limits (Linear), admin controls and SSO (universal at enterprise tier). Market has converged on automation runs and integrations as the primary usage-based differentiation metric.

**Step 4 — Usage-based differentiation design:**
Three differentiation axes selected based on usage data and willingness-to-pay research: (1) Automation runs/month — clearest proxy for power user value; (2) Active integrations — strong predictor of account stickiness and expansion; (3) Admin and governance features (SSO, audit logs, role-based permissions) — primary enterprise buying requirement. Seat count retained as primary billing metric (familiar to buyers) with automation runs as the secondary limit triggering upgrades.

**Step 5 — Three-tier packaging design:**
Starter ($9/user/month, billed annually): up to 10 seats, 100 automation runs/month, 2 integrations, standard support. Professional ($22/user/month, billed annually): unlimited seats, 2,000 automation runs/month, unlimited integrations, priority support, advanced reporting. Enterprise (custom): unlimited everything, SSO, audit logs, SAML, dedicated CSM, SLA guarantee, custom contract. Free tier retained (up to 3 seats, 10 automation runs/month) to maintain top-of-funnel. Monthly billing available at 20% premium.

**Step 6 — Revenue impact modeling:**
Migration model applied to 14,200 current accounts. Sub-10-seat accounts (8,400 accounts) migrate to Starter at $9/user/month — revenue decreases from $29 to $9/user but churn rate expected to fall from 34% to 14% based on competitive benchmarks; net ARR impact: +$1.1M from churn reduction. Mid-market accounts (4,800 accounts) migrate to Professional at $22/user/month — marginal price decrease from $29 but expansion from automation upsell expected; flat net impact. Power users (1,000 accounts) repriced from $29 to $22 base + automation overage fees averaging $11/user/month additional; net ARR increase $2.8M. NRR model: target 118% within 18 months.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
