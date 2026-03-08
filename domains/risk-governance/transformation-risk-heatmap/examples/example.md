# Transformation Risk Heatmap — Example

## Scenario
Apex Logistics Group is a 4,000-person third-party logistics provider embarking on a 3-year, $47M digital transformation program to replace its legacy Transportation Management System (TMS) and Warehouse Management System (WMS) and launch a new customer self-service portal. The program spans 12 warehouse facilities, 3,200 field operations staff, and integrations with 85 carrier APIs and the company's 15-year-old SAP ERP. The program office has identified 22 transformation risks through leadership interviews and is constructing a heatmap to guide steering committee governance.

## Inputs
- **Program scope:** New TMS (SaaS), custom WMS build (replacing two legacy systems), customer portal (greenfield), ERP integration layer; 36-month delivery horizon
- **Risk identification method:** 14 semi-structured interviews with C-suite, program sponsors, workstream leads, IT, and frontline operations managers; supplemented by lessons-learned review from two prior failed technology programs
- **Risk scoring:** 5x5 likelihood-impact matrix; Red zone ≥12, Amber 6–11, Green ≤5
- **Red-zone risks at identification:** Integration complexity between new TMS and legacy SAP ERP (L4, I5, score 20), change fatigue across 3,200 field workforce (L4, I4, score 16), vendor delivery risk on custom WMS build (L3, I5, score 15)

## Analysis

**Step 1 — Transformation scope and risk universe definition:**
Program scope decomposed into four delivery streams: TMS deployment (months 1–18), WMS build and deployment (months 6–30), customer portal (months 12–30), and ERP integration (months 1–36, continuous). Risk universe defined as the set of risks that could cause delivery delays exceeding 3 months, cost overruns exceeding 15% of stream budget, or significant operational disruption during transition. Twenty-two risks identified and documented.

**Step 2 — Risk identification and categorization:**
Twenty-two risks categorized across five dimensions: Technology (7 risks — integration, data migration, platform performance, cybersecurity), Vendor/Partner (4 risks — WMS custom build delivery, SaaS TMS vendor stability, system integrator capacity, carrier API compatibility), People and Change (5 risks — change fatigue, skills gap, key person dependency, union engagement, remote site adoption), Program Governance (3 risks — scope creep, budget overrun, steering committee alignment), and External/Market (3 risks — fuel cost volatility affecting ROI assumptions, regulatory change, customer volume forecasting). Each risk documented with trigger event, consequence description, and early warning indicators.

**Step 3 — Scoring and heatmap construction:**
All 22 risks scored on the 5x5 matrix by program director and two workstream leads independently; discrepancies reconciled. Heatmap zones: Red (score ≥12): 8 risks; Amber (score 6–11): 10 risks; Green (score ≤5): 4 risks. Top three red-zone risks: (1) TMS-ERP integration complexity (L4, I5 = 20) — 85+ carrier API touchpoints and real-time freight cost calculation require a custom middleware layer; similar integration work took a competitor 14 months vs. the 12-month program plan. (2) Change fatigue (L4, I4 = 16) — 3,200 field staff have experienced two prior failed system rollouts in 4 years; union stewards have signaled resistance; field manager interviews reveal low confidence in program success. (3) Custom WMS delivery risk (L3, I5 = 15) — the selected WMS vendor has not delivered a project of this complexity; 40% of WMS functionality is custom-built with no reference implementation; fixed-price contract creates vendor incentive to cut scope rather than absorb overruns.

**Step 4 — Owner assignment for red and amber risks:**
Owners assigned for all 18 Red and Amber risks. Red zone owners: TMS-ERP integration (CIO, with dedicated integration architect assigned), change fatigue (Chief People Officer, with external change management firm contracted), WMS delivery risk (Chief Operating Officer, with biweekly vendor delivery reviews and independent QA firm appointed). Amber zone owners distributed across program workstream leads with monthly status reporting obligation.

**Step 5 — Mitigation plans for top 5 risks:**
Detailed mitigation plans developed for the five highest-scoring risks. Risk 1 (TMS-ERP integration, score 20): appoint a dedicated integration architect as a single accountable owner; conduct a 4-week technical spike to validate the middleware architecture before month 3 program commitment; contract an independent technical reviewer to assess integration design at month 6. Risk 2 (change fatigue, score 16): deploy Prosci ADKAR change management model; hire 4 dedicated change management leads embedded in operations; conduct frontline listening sessions at all 12 sites in month 1; establish a "transformation ambassador" network of 48 field staff volunteers (4 per site). Risk 3 (WMS delivery, score 15): introduce monthly independent QA reviews of WMS build progress against contracted deliverables; define clear escalation rights in the vendor contract for delivery shortfalls; establish a contingency budget of $2.8M (10% of WMS build cost) reserved for scope rescue or alternate vendor engagement. Risk 4 (scope creep, score 12): implement change control board with CFO sign-off required for any scope change exceeding $200K or 2-week schedule impact. Risk 5 (data migration, score 12): mandate three data migration dry runs (months 6, 12, 20) with automated reconciliation; define data quality acceptance thresholds before first dry run.

**Step 6 — Governance integration and monthly review cadence:**
Heatmap reviewed at monthly Program Steering Committee (12-person committee including CEO, CFO, COO, CIO, CPO, and 7 workstream sponsors). Review format: (a) re-score any risk with a material status change, (b) update mitigation plan status for all Red risks, (c) confirm owner for any risk that has moved zones, (d) identify new risks not in the current register. Escalation protocol: any risk reaching score ≥18 triggers an extraordinary Steering Committee session within 5 business days. Heatmap version-controlled in the program SharePoint with monthly snapshots retained for program audit trail.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
