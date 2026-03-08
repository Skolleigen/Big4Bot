# RACI / DACI Governance — Example

## Scenario
A global retail company's pricing decision process involves 6 departments and has an average cycle time of 18 days from pricing request to approved price list publication. Business units report frequent delays, contradictory decisions from different price approvers, and frustration with the number of stakeholders required to sign off before a price can be published. A RACI design exercise is commissioned to map the current accountability structure and redesign it to resolve the identified governance failures.

## Inputs
- **Decisions and activities in scope:** 12 activities from pricing request initiation to price list publication
- **Stakeholder roles:** Commercial Director, Pricing Manager, Finance Business Partner, Category Manager, Legal/Compliance, Marketing Manager, Regional Sales Director, IT/Data team
- **Existing escalation paths:** Any price change above 15% requires Commercial Director sign-off; all price changes require Finance sign-off; Legal/Compliance review required on promotional pricing only
- **Decision frequency:** Approximately 40 pricing decisions per month across 8 product categories

## Analysis

**Step 1 — Scope definition:**
The 12 in-scope activities are confirmed: (1) Pricing request submission; (2) Market data analysis; (3) Competitor price benchmarking; (4) Cost-to-serve calculation; (5) Proposed price calculation; (6) Category Manager review; (7) Finance impact assessment; (8) Legal/Compliance promotional check (promotional prices only); (9) Regional Sales alignment check; (10) Commercial Director approval (>15% change); (11) Final price approval; (12) Price list publication and system update. The post-publication price dispute resolution process is explicitly out of scope.

**Step 2 — Stakeholder role identification:**
Eight roles are confirmed for the matrix columns. The IT/Data team is added during scoping when it emerges that they own the price publication system and price list data quality validation — a role that was previously invisible in the governance discussion.

**Step 3 — Activity list construction:**
All 12 activities are sequenced and confirmed as the matrix rows. In the workshop, participants identify that activities 6 and 9 (Category Manager review and Regional Sales alignment check) are currently treated as sequential but have no dependency on each other — they are blocking in sequence due to historical convention rather than design.

**Step 4 — Role assignment workshop:**
A 3-hour RACI workshop is conducted with representatives from all 8 roles. Immediate disagreements emerge at 3 activities: Activity 11 (Final price approval) has both the Commercial Director and Finance Business Partner claiming Accountable status; Activity 5 (Proposed price calculation) is claimed as Responsible by both the Pricing Manager and the Category Manager; Activity 12 (Price list publication) is claimed as Responsible by both the IT/Data team and the Pricing Manager. These disagreements are documented and flagged for structural analysis.

**Step 5 — Stakeholder validation:**
The draft matrix is circulated to all 8 roles for asynchronous validation. Additional feedback surfaces: the Regional Sales Director reports being Consulted on all 12 activities regardless of materiality — in practice they only need involvement when regional pricing variation exceeds 5%. Marketing Manager reports being Consulted on promotional pricing activities only but is currently included in all standard pricing cycles.

**Step 6 — Structural issue identification:**
Six structural governance issues are identified: (1) Dual Accountable on Activity 11 — both Commercial Director and Finance Business Partner are listed as A; resolved by assigning Commercial Director as A and Finance as C with right of escalation veto; (2) Dual Responsible on Activity 5 — Pricing Manager designated R, Category Manager moved to C with mandatory 48-hour turnaround SLA; (3) Dual Responsible on Activity 12 — IT/Data team designated R for system update, Pricing Manager designated R for data quality validation and sequencing (split responsibility acknowledged); (4) Regional Sales Director over-consulted — Consulted only when regional price variation exceeds 5%, reducing their involvement from 40 to approximately 8 decisions per month; (5) Marketing Manager scope reduced — Consulted on promotional pricing activities 8 and 11 only, removed from standard pricing cycle; (6) Activities 6 and 9 redesigned to run in parallel rather than sequentially — eliminating an average of 3.5 days from the cycle.

**Step 7 — Matrix finalization and publication:**
The revised RACI is finalized with all six structural issues resolved. The matrix is published to all 8 roles with a cover note from the Commercial Director confirming the new accountability structure. An updated escalation path is documented: Finance right of escalation veto on Activity 11 replaces the previous dual-approval requirement. A 30-day review is scheduled to assess whether the parallel execution of Activities 6 and 9 is functioning as designed.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
