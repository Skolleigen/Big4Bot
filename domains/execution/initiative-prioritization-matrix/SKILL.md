# Initiative Prioritization Matrix

## Domain
Execution

## Description
Decision framework for ranking strategic initiatives or projects using weighted scoring across dimensions such as impact, effort, strategic fit, and risk. It converts subjective executive judgment into a structured, comparable, and defensible sequencing of investment decisions.

## Purpose
Organizations routinely face more candidate initiatives than they have capacity, capital, or management bandwidth to execute simultaneously. The initiative prioritization matrix provides a repeatable mechanism to evaluate options against consistent criteria, surface hidden trade-offs, and align leadership on a sequenced backlog. It reduces political bias in resource allocation by grounding decisions in quantified scoring.

## When to Use
- The organization has more proposed initiatives than current capacity allows and needs a structured method to sequence or deprioritize
- Strategic planning or annual budgeting cycles require a defensible rationale for initiative funding decisions
- A transformation program must triage a large backlog of ideas across multiple business units with competing priorities
- Leadership alignment on initiative sequencing is absent and a neutral scoring mechanism is needed to build consensus

## When NOT to Use
- There is only a single initiative under consideration with no competing alternatives
- The decision is already constrained to a mandated regulatory or compliance program where prioritization is not discretionary
- Insufficient information exists to score initiatives on key dimensions, rendering scores unreliable

## Inputs Required
- Candidate initiative list with brief descriptions and sponsoring business unit
- Strategic objectives or OKRs against which initiatives will be scored for fit
- Estimated effort or cost for each initiative (ranges are acceptable if point estimates are unavailable)
- Risk assessment or dependency flags for each initiative

## Optional Inputs
- Capacity data (FTE availability, budget envelopes) to apply as a constraint filter after scoring
- Historical data on initiative delivery performance to calibrate effort estimates

## Diagnostic Process
1. Compile the full list of initiative candidates from all business units and sponsors, ensuring descriptions are sufficiently detailed to permit consistent scoring.
2. Define scoring dimensions and assign weights reflecting organizational priorities; typical dimensions include strategic impact, customer value, implementation effort, risk, and time to value.
3. Score each initiative on each dimension using a consistent scale (e.g., 1–5), with scoring criteria defined in advance for each level to reduce evaluator subjectivity.
4. Calculate weighted composite scores for each initiative by multiplying raw scores by dimension weights and summing across dimensions.
5. Plot initiatives on a two-dimensional impact-effort matrix to provide an intuitive visual layer on top of numerical scores, identifying quick wins, major bets, fill-ins, and time-wasters.
6. Apply constraints including available budget, headcount capacity, and initiative dependencies to test whether the top-scored initiatives are executable within realistic limits.
7. Produce the prioritized initiative backlog, documenting scores, rationale, and any constraint-driven adjustments, and present to leadership for validation and sign-off.

## Output
The skill produces a scored and ranked initiative backlog with supporting rationale, a visual impact-effort matrix, and a recommended sequencing plan calibrated to organizational capacity and strategic objectives. The output is suitable for executive decision-making and PMO planning intake.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- portfolio-governance
- strategic-initiative-mapping
- balanced-scorecard
- okr-design

## References
- Dwight D. Eisenhower: *Eisenhower Matrix* — Urgency/importance decision framework foundational to prioritization methodology
- Boston Consulting Group: *Prioritization Frameworks for Strategic Planning* — BCG advisory perspectives on portfolio prioritization and resource allocation
- Intercom: *RICE Scoring Model* (2016) — Reach, Impact, Confidence, Effort scoring framework developed for product prioritization
