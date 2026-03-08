# Product-Market Fit Diagnostics — Example

## Scenario
A vertical SaaS company has been selling a field service management platform to independent HVAC contractors for 18 months. The product launched with strong initial press coverage and 300 paying accounts in the first 6 months, but growth has slowed materially. The founding team believes the product has strong fit but investors are questioning whether the growth slowdown reflects a market saturation issue or a fit problem. A systematic PMF diagnostic has been commissioned to generate an evidence-based assessment.

## Inputs
- **Target segment:** Independent HVAC contractors with 3–20 technicians in the United States; currently 440 paying accounts
- **Retention data:** Monthly cohort data for 18 cohorts available; subscription plan is month-to-month with annual option; 34% of accounts have elected annual billing
- **Sean Ellis survey:** Deployed to 440 active users 3 weeks ago; 187 responses received (42.5% response rate)
- **NPS data:** Most recent NPS survey conducted 2 months ago; n=210 responses; NPS score of +31; 180 verbatim comments available
- **Engagement data:** Product analytics available including daily active use, job scheduling activity, and invoicing module usage by account

## Analysis

1. **Define target segment precisely:** The platform serves HVAC contractors, but the account base contains three distinct sub-segments: (a) owner-operators with 1–2 technicians (38% of accounts), (b) independent shops with 3–12 technicians (49% of accounts), and (c) larger independents with 13–20 technicians (13% of accounts). The product roadmap was designed for segment (b). PMF analysis will be segmented across all three to determine whether fit is uniform or concentrated.

2. **Measure retention cohorts:** Month-6 retention by segment: owner-operators (segment a): 41%; independent shops (segment b): 67%; larger independents (segment c): 72%. Month-12 retention: segment (a): 28%; segment (b): 61%; segment (c): 68%. Cohort curves for segments (b) and (c) flatten between months 6 and 12 — a strong PMF signal. Segment (a) curves continue declining through month 12 with no flattening, indicating continuing churn rather than retained engagement.

3. **Sean Ellis survey results:** Overall: 44% "very disappointed" — above the 40% benchmark. Segmented: segment (a) owner-operators: 29% very disappointed (below benchmark); segment (b) 3–12 technician shops: 54% very disappointed (strong); segment (c) 13–20 technician shops: 61% very disappointed (very strong). The overall 44% figure is an artifact of mixing a weak-fit sub-segment (a) into the analysis; when restricted to the intended target segment (b+c), the PMF signal is strong.

4. **NPS and qualitative feedback analysis:** Overall NPS: +31. Promoter verbatims (coded): "saves time on scheduling" (n=47), "invoicing is much faster" (n=38), "customers love the text notifications" (n=29). Detractor verbatims: "too expensive for a one-person shop" (n=24), "the mobile app crashes on older Android phones" (n=18), "missing QuickBooks sync" (n=15). Detractor themes align directly with segment (a) pricing sensitivity and a specific technical defect rather than a core value proposition failure in segments (b) and (c).

5. **Engagement and usage patterns:** Segment (b) and (c) accounts average 4.2 login days per week per account with at least one technician active; 78% of segment (b) accounts used the invoicing module in the last 30 days. Segment (a) accounts average 1.8 login days per week; only 41% used invoicing in the last 30 days. Core habit formation is present in segments (b) and (c) and absent in segment (a).

6. **Organic growth indicators:** 23% of new paying accounts in the last 90 days came from referrals by existing customers. Referrals come disproportionately from segment (b): 87% of referrals originate from 3–12 technician shops. Branded search volume has grown 34% in the last 6 months without a corresponding increase in paid search spend. The product has been mentioned in 3 HVAC trade publications without paid placement.

7. **Fit level scoring:** Segments (b) and (c): strong fit. Retention curves flatten above 60% at month 12; Sean Ellis score of 54–61%; NPS promoter themes confirm the core value proposition is delivering; organic referral rate of 23%; habitual weekly engagement. Segment (a): weak to no fit. Retention declining at month 12; Sean Ellis score of 29%; pricing sensitivity is the primary detractor theme; low engagement frequency. Limiting factor for overall growth: segment (a) accounts (38% of base) are diluting aggregate metrics and generating disproportionate churn without contributing to organic referrals.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
