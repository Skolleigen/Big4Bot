# Agile Operating Model — Example

## Scenario
A regional insurance company with 2,400 employees has been running a digital transformation program for 18 months with limited results. Product delivery is organized by function — business analysis, development, QA, and operations are separate departments — resulting in average feature lead times of 14 weeks. The Chief Digital Officer has mandated a shift to an agile operating model to reduce lead time to under four weeks within 12 months.

## Inputs
- **Organizational structure:** 6 functional departments, 38 project managers, ~180 IT delivery staff
- **Initiative inventory:** 22 active projects under a traditional PMO with stage-gate governance
- **Value streams identified:** Personal lines digital sales, claims self-service, policy administration, and internal data platforms
- **Delivery methodology:** Waterfall with quarterly steering committee reviews; no existing sprint cadences

## Analysis

**Step 1 — Assess current structure and delivery model.**
Workshop interviews and time-motion analysis reveal that an average feature request passes through 7 handoff points across 4 departments before reaching production. Decision latency at the steering committee level averages 3.2 weeks per cycle. Two-thirds of defects are introduced at functional boundaries.

**Step 2 — Identify value streams.**
Four primary value streams are mapped: (1) Personal Lines Digital Sales, (2) Claims Self-Service, (3) Policy Administration, and (4) Internal Data & Analytics. Each stream has a distinct customer segment, a measurable outcome metric, and an identifiable owner.

**Step 3 — Define squad and tribe topology.**
Four tribes are defined, one per value stream. Each tribe contains 2–4 squads of 6–8 people, each with a Product Owner, engineers, QA, and a UX representative. A Platform Tribe is established to provide shared infrastructure services. Total headcount shifts from functional pools to 19 co-located or virtually aligned squads.

**Step 4 — Map current processes to agile equivalents.**
Stage-gate project initiation is replaced with product backlog creation and quarterly planning (PI Planning). Monthly steering committees are replaced with squad-level sprint reviews (bi-weekly) and a monthly Portfolio Sync. Change Advisory Board reviews are streamlined into automated deployment pipelines with lightweight change records.

**Step 5 — Identify governance changes.**
Budget authority for squad-level decisions (under $50K) is delegated to Product Owners. Quarterly funding reviews replace annual project budget approvals. Escalation paths are defined for architectural decisions and regulatory changes. HR grading structures are adapted to accommodate the Product Owner and Scrum Master career tracks.

**Step 6 — Define transition roadmap.**
Phase 1 (months 1–3): Stand up two pilot squads in the Claims Self-Service tribe with coaching support. Phase 2 (months 4–6): Expand to all four tribes, decommission PMO stage-gate for in-scope streams. Phase 3 (months 7–12): Full operating model adoption, including revised budgeting and performance management frameworks.

**Step 7 — Establish cadences.**
Sprint length set at two weeks across all squads. Quarterly PI Planning workshops (2 days) established for each tribe. A monthly Portfolio Sync with tribe leads and the CDO is institutionalized to review OKR progress and re-prioritize the portfolio.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
