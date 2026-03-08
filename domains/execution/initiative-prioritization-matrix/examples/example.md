# Initiative Prioritization Matrix — Example

## Scenario
A global logistics company has identified 14 candidate initiatives for its 2026 transformation program, spanning operational efficiency, customer experience, and technology modernization. The Chief Transformation Officer must present a sequenced execution roadmap to the board in six weeks. Available transformation budget is $28M and internal delivery capacity is capped at 120 FTE-months for the year.

## Inputs
- **Initiative candidates:** 14 initiatives across three categories — operational efficiency (5), customer experience (4), technology modernization (5)
- **Strategic objectives:** Reduce cost-per-shipment by 12%, increase on-time delivery to 97%, and achieve NPS uplift of +15 points by end of 2026
- **Scoring dimensions and weights:** Strategic fit (30%), customer impact (25%), implementation effort — inverse scored (20%), risk (15%), time to value (10%)
- **Constraints:** $28M total budget; 120 FTE-months capacity; no more than 3 major initiatives in parallel at any time

## Analysis

**Step 1 — Compile initiative candidates.**
Fourteen initiatives are collected through a structured intake form distributed to business unit sponsors. Each submission includes a one-paragraph description, named executive sponsor, preliminary cost estimate, and intended strategic objective linkage. Two submissions are returned for additional detail before scoring.

**Step 2 — Define dimensions and weights.**
The transformation steering committee agrees on five scoring dimensions. Strategic fit (30%) is weighted highest because board mandates are non-negotiable. Customer impact (25%) reflects the NPS uplift target. Implementation effort (20%) is inverse-scored so lower effort receives higher marks. Risk (15%) accounts for regulatory exposure and dependency chains. Time to value (10%) rewards initiatives that can demonstrate results within the fiscal year.

**Step 3 — Score each initiative.**
A cross-functional scoring panel of six (Finance, Operations, Technology, Customer, Risk, and PMO) independently scores each of the 14 initiatives on a 1–5 scale per dimension using pre-defined rubrics. Scores are averaged and outliers discussed in a 90-minute calibration session.

**Step 4 — Calculate weighted scores.**
Composite scores are calculated for all 14 initiatives. Top three: (1) Last-mile routing optimization — score 4.31; (2) Customer track-and-trace portal — score 4.18; (3) Warehouse management system upgrade — score 4.02. Bottom three average below 2.50 and are flagged for deferral.

**Step 5 — Plot on impact-effort matrix.**
The matrix reveals: 3 quick wins (high impact, low effort) including a carrier invoice reconciliation automation tool; 3 major bets (high impact, high effort) including the WMS upgrade; 5 fill-ins; and 3 time-wasters recommended for removal from the backlog.

**Step 6 — Apply constraints.**
The top 7 initiatives by composite score total $31M — exceeding the $28M envelope by $3M. The lowest-scoring initiative in the top 7 (a fleet telematics rollout at $4.2M) is descoped from Year 1 to bring the portfolio within budget. Dependency analysis confirms the WMS upgrade must precede two downstream data initiatives.

**Step 7 — Produce prioritized backlog.**
A sequenced backlog of 6 funded initiatives is finalized. Wave 1 (Q1–Q2): 3 quick wins. Wave 2 (Q2–Q4): 2 major bets. Wave 3 (Q3–Q4): 1 fill-in initiative. Three initiatives are deferred to 2027 planning; three are removed from the backlog with documented rationale.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
