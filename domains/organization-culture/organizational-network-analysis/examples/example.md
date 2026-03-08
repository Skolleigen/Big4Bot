# Organizational Network Analysis — Example

## Scenario
A 350-person management consulting firm has grown rapidly through lateral hiring over 5 years, resulting in two practice areas — Strategy and Technology — that operate largely as separate businesses despite sharing clients and office space. The Managing Partner suspects that knowledge silos are creating sub-optimal client proposals and missed cross-selling opportunities but lacks data to confirm the diagnosis. An ONA is commissioned covering all 350 employees to map the informal collaboration and advice networks across the firm.

## Inputs
- **Organization:** 350-person management consulting firm; two primary practice areas (Strategy: 210 people, Technology: 140 people)
- **Survey questions:** (1) Who do you go to for professional advice or expertise? (2) Who do you go to for project information or updates? (3) Who gives you energy or motivation when facing challenges?
- **Response rate:** 83% (291 of 350 employees responded)
- **Time reference:** Relationships in the past 3 months
- **Segmentation:** Practice area, level (partner, manager, consultant, analyst), office location, tenure

## Analysis

**Step 1 — ONA scope and survey design:**
The ONA scope covers all 350 employees across both practice areas and three office locations. Three relationship types are surveyed — advice, information, and energy — to capture different network functions. The roster-based survey design presents each respondent with a complete list of all 350 employees and asks them to select up to 15 people per relationship type. The data use protocol commits to reporting only aggregated, anonymized outputs at the cluster level, with individual-level data accessed only by the ONA analyst team for centrality calculations. A 10-day survey window with two reminders achieves 83% response.

**Step 2 — Network graph construction:**
A directed network graph is built from 291 responses. Total edges in the advice network: 2,847 directed ties. Network density: 0.023 (2.3% of all possible ties are present), which is typical for a 350-person organization. Reciprocity rate: 31% of advice relationships are mutual, suggesting the network has significant hierarchical directionality (advice flows upward and to senior experts). Response completeness check: 59 non-respondents are distributed across both practices with slight over-representation in the Technology practice (19 non-respondents, 13.6% of Technology population), noted as a limitation in the analysis.

**Step 3 — Centrality calculation:**
Betweenness centrality is calculated for all 291 responding nodes. Three individuals are flagged with betweenness centrality exceeding 0.35 — the critical broker threshold for a network of this size: (1) Node A: a Strategy Partner with betweenness = 0.41, receiving 67 inbound advice ties and serving as the primary bridge between the Strategy leadership cluster and the Technology practice. (2) Node B: a Technology Manager with betweenness = 0.38, the primary conduit between the junior Technology team and both senior Technology and Strategy partners. (3) Node C: a Strategy Manager with betweenness = 0.36, bridging the Strategy practice's two sub-clusters (Operations strategy and Digital strategy). Degree centrality: the top 5% of nodes by in-degree receive 31% of all advice requests, indicating a highly concentrated advice-seeking pattern.

**Step 4 — Current culture radar chart equivalent — Key structural findings:**
Silo analysis: Strategy and Technology practices share only 4% of cross-practice communication ties in the advice network (116 cross-practice edges out of 2,847 total). Within-practice density: Strategy internal density = 0.041 (significantly higher than firm average), Technology internal density = 0.038. Cross-practice density: 0.007 — confirming severe silo conditions. The energy network shows slightly higher cross-practice connectivity (7% cross-practice ties) suggesting that informal social connections exist but are not translating into professional collaboration or knowledge sharing.

**Step 5 — Peripheral node identification:**
27 nodes (9.3% of the total population) have 3 or fewer inbound advice ties, placing them in the peripheral category. Of these 27, 19 are in the Technology practice and 14 have been with the firm for fewer than 18 months. 8 peripheral nodes have zero cross-practice ties in any network type, representing individuals who are fully isolated within their practice. Peripheral status correlates with higher 12-month voluntary attrition in the prior year's data (38% attrition for peripheral nodes versus 14% firm average), confirming that network peripherality is an attrition risk signal.

**Step 6 — Formal versus informal structure alignment:**
The formal organizational chart shows two practice area heads with equal authority and a firm-level partnership committee as the governance mechanism for cross-practice decisions. The informal network shows Node A (a Strategy Partner) has significantly greater cross-practice informal influence than any Technology partner, with 67 inbound advice requests versus the Technology Practice Head's 31. This misalignment means that critical cross-practice knowledge flows are depending on a single non-designated individual rather than being distributed through the formal governance structure. Node A is also a flight risk: the partner is 18 months from eligibility for an external equity opportunity and has been approached by a competitor according to HR data.

**Step 7 — Structural intervention recommendations:**
Four interventions are prioritized: (1) Node A knowledge transfer program: immediately initiate a structured knowledge transfer program documenting Node A's cross-practice relationships, client knowledge, and broker networks; designate two managers from each practice to shadow Node A in cross-practice client engagements over the next 6 months. (2) Cross-practice collaboration mechanism: establish 6 cross-practice client pursuit teams with paired Strategy and Technology co-leads, shared revenue attribution, and joint quarterly reviews — the structural mechanism required to generate the cross-practice ties that do not currently exist. (3) Peripheral node integration: pair all 27 peripheral nodes with a network buddy from a different practice area and seniority level; include peripheral node status as a visible indicator in the HR dashboard reviewed at the annual talent review. (4) Reduced inbound load for Node A: assign a Chief of Staff to Node A to absorb 30% of inbound requests and redistribute routine information-sharing responsibilities to reduce the concentration risk before Node A's departure becomes a crisis.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
