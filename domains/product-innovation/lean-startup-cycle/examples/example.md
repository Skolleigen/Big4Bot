# Lean Startup Cycle — Example

## Scenario
An enterprise SaaS company serving professional services firms has a hypothesis that its existing legal workflow clients would pay for an AI-assisted contract review module. The product team has allocated a 10-week discovery and validation sprint before the annual roadmap investment decision. Rather than building a full AI module, the team has been directed to apply the Lean Startup Cycle to generate validated evidence before committing to an 8-month development program.

## Inputs
- **Core hypothesis:** Mid-size law firms (20–200 attorneys) using the platform will pay at least $500/month additional for an AI-assisted contract review feature that flags non-standard clauses and generates redline suggestions
- **Target segment:** Existing platform customers in the legal vertical with active contract management use cases; focus on firms with 20–200 attorneys
- **Current data available:** 3,400 active platform users in the legal segment; contract management module used by 41% of legal customers; average contract volume per firm is 120 documents per month
- **Available resources:** 2 engineers, 1 product manager, 8 weeks, and $15,000 in operational budget for the experiment

## Analysis

1. **Identify business hypotheses:** Three core assumptions underpin the business case: (a) attorneys find manual clause review a significant time burden worth paying to reduce, (b) AI-generated redline suggestions will be trusted and acted upon by practicing attorneys, and (c) $500/month incremental pricing will not create meaningful churn risk among existing customers.

2. **Rank by risk:** Assumption (b) — attorney trust in AI-generated suggestions — is the riskiest. If attorneys review every AI suggestion with the same effort as manual review, there is no time saving and willingness to pay collapses. Assumptions (a) and (c) are secondary: (a) is likely true based on attorney time-study benchmarks, and (c) can only be fully tested with a real pricing page. Assumption (b) is the first test target.

3. **Design MVP:** Rather than building AI infrastructure, the team designs a "Wizard of Oz" MVP: attorneys upload contracts via a dedicated intake form; a junior associate and a paralegal manually review each contract within 2 hours and return a formatted clause-flag report mimicking the intended AI output; the UI presents it as "AI Analysis." The MVP tests whether attorneys act on the suggestions and how frequently they override or dismiss them — direct evidence for assumption (b) — without any model training cost.

4. **Define success metrics:** Pass threshold: at least 60% of flagged clauses in test contracts are acted upon by the reviewing attorney (accepted, modified, or negotiated) without requiring independent manual verification by the attorney. Fail threshold: less than 40% action rate, or attorneys report re-verifying every flag independently. Secondary metric: time-to-complete review reduced by at least 25% versus attorney self-report baseline.

5. **Build and release:** Recruited 12 volunteer customers from the legal segment for a 3-week "Early Access" cohort. Each firm submitted 3–5 contracts. The operations team processed 47 total contracts using the manual fulfillment model. Attorneys were not informed the analysis was human-assisted; the interface presented results identically to the planned AI output. Instrumented the UI to capture which flags were clicked, dismissed, or triggered edits.

6. **Measure:** 47 contracts processed. Clause action rate: 71% of flagged items were acted upon without attorney noting a need to re-verify. Time-to-complete: attorneys self-reported 32% average reduction in review time versus their usual process. 9 of 12 firms submitted additional contracts beyond the initial batch without prompting. 3 attorneys sent unsolicited feedback indicating intent to discuss pricing with their account manager.

7. **Pivot or persevere:** Results exceed both pass thresholds. Assumption (b) is validated: attorneys act on AI-style suggestions at a rate consistent with trusting the output rather than re-verifying it. The unsolicited additional submissions and pricing inquiries are secondary positive signals. Decision: persevere. Advance to testing assumption (c) — willingness to pay at $500/month — by adding a pricing page to the Early Access experience in the next cycle and presenting it to the 12 cohort firms as a paid continuation.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
