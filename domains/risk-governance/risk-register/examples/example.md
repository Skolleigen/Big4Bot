# Risk Register — Example

## Scenario
Cascade Retail Group is a 180-store regional retail chain undertaking a $22M ERP implementation (SAP S/4HANA) to replace three legacy systems — a 20-year-old point-of-sale system, a disconnected inventory management platform, and a manual accounts payable process. The program director has commissioned a structured risk register before go-live, which is scheduled in 6 months. A series of risk workshops with 12 stakeholders surfaces 34 risks across operational, technology, compliance, and financial categories.

## Inputs
- **Program:** SAP S/4HANA ERP implementation, go-live in 6 months, $22M total budget
- **Stakeholders:** 12 workshop participants including CFO, CIO, Head of Store Operations, Head of Supply Chain, External SAP Implementation Partner (lead), 3 functional workstream leads, Internal Audit, HR, Finance Controller, IT Security
- **Risk scoring:** 5x5 likelihood-impact matrix; scores 1–25; Red zone ≥15, Amber 8–14, Green ≤7
- **Top risks identified:** Data migration failure (L4, I5, score 20), staff adoption failure (L4, I4, score 16), vendor dependency / SAP partner delivery risk (L3, I4, score 12), legacy system integration failure (L3, I4, score 12), go-live cutover failure (L3, I4, score 12)

## Analysis

**Step 1 — Scope and workshop design:**
Risk register scope defined as ERP go-live program over 6-month period, with post-go-live stabilization (months 7–12) flagged for a separate register refresh. Three workshops conducted: Workshop 1 — technology risks (CIO, IT Security, SAP partner, functional leads); Workshop 2 — operational and people risks (Head of Store Operations, Head of Supply Chain, HR, Finance Controller); Workshop 3 — compliance and financial risks (CFO, Internal Audit, Finance Controller). Each workshop used a pre-seeded risk prompt list based on SAP implementation risk taxonomies.

**Step 2 — Risk identification:**
Thirty-four risks identified across three workshops. Category breakdown: Operational (18 risks — store readiness, staff training, process change, supplier communication), Technology (9 risks — data migration, integration, performance testing, cybersecurity during cutover), Compliance (4 risks — SOX control continuity during ERP transition, PCI DSS for new payment processing module, state tax configuration), Financial (3 risks — budget overrun, parallel run cost, write-off of legacy system assets). Each risk documented with a description, trigger event, and potential consequence.

**Step 3 — Likelihood and impact scoring:**
Each risk scored independently by two workshop facilitators using the 5x5 matrix definitions. Likelihood scale: 1 = Rare (<10% probability), 2 = Unlikely (10–30%), 3 = Possible (30–60%), 4 = Likely (60–80%), 5 = Almost certain (>80%). Impact scale: 1 = Negligible, 2 = Minor, 3 = Moderate (reportable to leadership), 4 = Major (material financial impact or program delay >1 month), 5 = Critical (go-live failure, regulatory action, or >$2M financial impact). Discrepancies >1 level resolved in facilitated discussion. Final top-5 scores: data migration failure (L4, I5 = 20), staff adoption failure (L4, I4 = 16), vendor delivery risk (L3, I4 = 12), legacy integration failure (L3, I4 = 12), cutover failure (L3, I4 = 12).

**Step 4 — Risk matrix plotting:**
Thirty-four risks plotted on 5x5 matrix. Red zone (score ≥15): 3 risks — data migration failure (20), staff adoption failure (16). Amber zone (score 8–14): 11 risks — vendor delivery risk, integration failure, cutover failure, SOX control continuity, performance under peak load, cybersecurity during cutover, and 5 operational readiness risks. Green zone (score ≤7): 20 risks — mostly low-likelihood or low-impact operational and financial risks.

**Step 5 — Owner assignment and mitigation planning:**
Risk owners assigned for all Red and Amber risks (14 risks). Red zone mitigations: Data migration failure — Owner: CIO; Mitigation: conduct three parallel mock migration runs (months 1, 3, 5) with automated reconciliation against legacy system; establish a data quality dashboard with daily monitoring; define go/no-go criteria for go-live migration sign-off. Staff adoption failure — Owner: Head of Store Operations; Mitigation: deploy 120-hour role-based training program for all 1,800 store staff using a train-the-trainer model; conduct 4 regional readiness pilots in months 4–5; engage frontline staff champions (15 identified) as adoption advocates.

**Step 6 — Monthly review cadence and escalation:**
Risk register approved by Steering Committee. Monthly review scheduled for the first Tuesday of each month. Review agenda: status update on all Red/Amber mitigations, re-scoring of risks with material status changes, escalation of any risk that moves to Red zone, and review of new risks. Two escalation triggers defined: any risk reaching score ≥18 triggers a mandatory executive briefing within 48 hours; any go-live delay risk triggers an immediate Steering Committee extraordinary session. Register maintained in Archer GRC system with owner-reported monthly updates.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
