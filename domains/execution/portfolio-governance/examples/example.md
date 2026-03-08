# Portfolio Governance — Example

## Scenario
A $450M financial services firm has 18 active transformation initiatives consuming 340 FTE and $28M annually across technology modernization, regulatory compliance, digital distribution and operational efficiency. The PMO has been tracking each initiative independently with no consolidated portfolio view. The quarterly portfolio review is the first time leadership has seen integrated status across all 18 initiatives simultaneously.

## Inputs
- **Active initiative inventory:** 18 initiatives; 6 classified as strategic transformation, 7 as regulatory/compliance-mandated, 5 as operational efficiency
- **Resource capacity:** 340 FTE demand against 310 FTE available supply; $28M annual spend against $26M approved envelope
- **Current health status:** 9 green, 6 amber, 3 red across the 18 initiatives
- **Risk and issue logs:** 47 open issues across the portfolio; 8 classified as high severity
- **Interdependency map:** Pre-read document identifying 14 dependency relationships between the 18 initiatives

## Analysis

**Step 1 — Initiative inventory and classification:**
All 18 initiatives are logged in a consolidated register. Classification reveals that 7 of the 18 are compliance-mandated with non-negotiable regulatory deadlines — these are immediately ring-fenced from prioritization trade-offs. The remaining 11 strategic and efficiency initiatives enter the portfolio review decision process. Health status is confirmed: 3 red initiatives include one regulatory initiative (critical), one technology modernization program and one digital distribution initiative.

**Step 2 — Resource demand vs. capacity assessment:**
Consolidated resource demand totals 340 FTE against 310 FTE available — a 30 FTE shortfall consuming shadow capacity from business-as-usual functions. The data engineering team (12 FTE) is the most critical bottleneck: 3 initiatives each require 100% of this team simultaneously. The PMO confirms the team has been context-switching across all three, reducing effective output to approximately 55% per initiative. Annual spend at $28M against a $26M envelope indicates two initiatives are drawing on unapproved contingency.

**Step 3 — Interdependency review:**
The 14 dependency relationships are mapped and two critical blocking chains are identified. First: Initiative 7 (data platform modernization) is a dependency for Initiatives 11, 14 and 16 — but Initiative 7 is currently amber with a 3-month schedule slip, which will cascade to the three dependent initiatives if unresolved. Second: Initiatives 4 and 9 have conflicting data model requirements — both initiatives are attempting to establish the master customer record standard and the conflict has not been escalated to architecture governance.

**Step 4 — Performance evaluation:**
Six initiatives are behind schedule by more than 4 weeks. Three of these are also over budget. The one red regulatory initiative is 11 weeks behind a statutory deadline with no approved recovery plan — this is the highest-severity item in the portfolio. The two initiatives drawing on unapproved contingency are the digital distribution platform ($1.4M over) and a branch automation initiative ($0.6M over).

**Step 5 — Portfolio-level risk assessment:**
The data engineering bottleneck creates systemic delivery risk across 3 initiatives with combined budget of $9.2M. The regulatory initiative delay creates legal and financial risk estimated at $4–8M in potential regulatory fines. The conflicting data model standards between Initiatives 4 and 9 create a technical debt risk estimated at $2–4M in rework if both proceed without resolution.

**Step 6 — Stop/start/continue/accelerate decisions:**
Portfolio review produces the following decisions: STOP — Initiative 12 (branch automation, low strategic alignment, $2.1M budget recovered); STOP — Initiative 17 (a duplicative reporting enhancement addressed by Initiative 8 scope extension, $0.9M recovered). MERGE — Initiatives 4 and 9 merged with a single data architecture owner to resolve the conflicting standards conflict. ACCELERATE — Data engineering team is increased by 6 FTE (contractors) funded from the $3M recovered from the two stopped initiatives, resolving the bottleneck for the three blocked initiatives. CONTINUE with recovery plan — the red regulatory initiative receives dedicated executive sponsorship and a 6-week recovery sprint.

**Step 7 — Portfolio roadmap update:**
Portfolio is updated from 18 to 16 active initiatives (2 stopped, 1 merge reducing count by 1). Resource demand falls from 340 to 304 FTE — within the 310 FTE envelope. The updated roadmap is communicated to all initiative teams within 48 hours. The next portfolio review is scheduled for 6 weeks (shortened from quarterly given the number of active recovery actions).

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
