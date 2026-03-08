# Capability Maturity Assessment — Example

## Scenario
Pinnacle Financial Group is a regional bank with $8.4B in assets preparing for a scheduled examination by its primary federal regulator. Internal audit flagged concerns about data governance and change management practices during a prior review cycle. The Chief Risk Officer has engaged a consulting team to conduct a structured capability maturity assessment across five domains before the regulatory inspection, with a mandate to identify gaps and produce a remediation roadmap demonstrating proactive action to the examiner.

## Inputs
- **Organization:** Pinnacle Financial Group ($8.4B AUM, 1,200 employees, regulated by OCC)
- **Assessment domains:** Data Governance, Risk Reporting, Change Management, IT Security Controls, Regulatory Compliance Operations
- **Maturity model:** CMMI-based 5-level scale adapted for financial services: Level 1 (Initial/Ad Hoc), Level 2 (Repeatable), Level 3 (Defined), Level 4 (Managed/Quantitatively controlled), Level 5 (Optimizing)
- **Evidence base:** 15 stakeholder interviews (CRO, CIO, CDO, 6 department heads, 5 process owners), review of 40 policy/procedure documents, observation of 3 live process walkthroughs

## Analysis

**Step 1 — Assessment scope and model selection:**
Five capability domains defined in alignment with OCC examination pillars. CMMI-based model selected over P3M3 due to regulatory familiarity; model adapted to add financial services-specific indicators at each level (e.g., Level 4 data governance requires automated data lineage tracking and board-level data quality reporting). Target maturity levels established: Data Governance L4 (regulatory requirement), Risk Reporting L4, Change Management L3, IT Security Controls L4, Regulatory Compliance Operations L3.

**Step 2 — Evidence collection:**
Fifteen interviews conducted over two weeks using structured interview guides with 8–12 questions per domain. Document review covered: data governance policy (last updated 2021), data dictionary (partial, covering 62% of critical data elements), risk reporting procedures (exists, not version-controlled), change management process documentation (informal, varies by team), IT security controls inventory (current, linked to NIST CSF). Three process walkthroughs: monthly risk reporting cycle, software change deployment, and data quality exception handling.

**Step 3 — Domain scoring:**
Each domain scored against 12–15 maturity indicators per level. Scoring completed independently by two assessors; discrepancies >1 level reconciled through additional evidence gathering. Final scores: Data Governance L2 (Repeatable) — policies exist but inconsistently applied; data dictionary covers 62% of critical elements vs. L4 requirement of 95%; no automated data lineage. Risk Reporting L3 (Defined) — standardized templates in use; manual aggregation introducing errors; no statistical quality controls (required for L4). Change Management L2 (Repeatable) — change log maintained; no formal impact assessment for 34% of changes; post-implementation review completed for only 18% of changes. IT Security Controls L3.5 (approaching Managed) — strong controls inventory; penetration testing current; privileged access review manual. Regulatory Compliance Operations L3 (Defined) — compliance calendar maintained; regulatory change management process documented but exam management workflow informal.

**Step 4 — Heatmap construction:**
Five-domain heatmap produced with color coding: Red (L1–L2, gap >2 levels from target), Amber (L2–L3, gap 1–2 levels), Green (at or above target). Red: Data Governance (current L2, target L4, gap 2 levels). Amber: Risk Reporting (L3, target L4, gap 1 level), Change Management (L2, target L3, gap 1 level). Green: IT Security Controls (L3.5, target L4, approaching target). Amber: Regulatory Compliance Operations (L3, target L3, at target but exam management workflow needs documentation).

**Step 5 — Critical gap identification:**
Two critical gaps flagged for regulatory risk: (1) Data Governance L2 — the 38% gap in critical data element coverage and absence of automated data lineage are likely to be cited as examination findings; estimated remediation: 6–9 months, $340K investment. (2) Change Management L2 — 82% post-implementation review gap means the bank cannot demonstrate controlled change execution; a failed change causing a regulatory reportable event during this gap period would constitute a significant examination finding.

**Step 6 — Remediation roadmap:**
Six-month roadmap structured across three horizons. Horizon 1 (0–60 days, pre-examination): document existing data governance processes more formally to demonstrate L2+ intent; complete data dictionary for remaining 38% of critical data elements using existing staff; formalize post-implementation review template and enforce for all changes. Horizon 2 (60–120 days): implement data lineage tooling (vendor shortlist: Collibra, Alation); automate risk report aggregation to eliminate manual errors; implement change management workflow in ServiceNow. Horizon 3 (120–180 days): achieve L3 data governance with automated quality controls in place; conduct internal pre-examination simulation using OCC examination procedures.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
