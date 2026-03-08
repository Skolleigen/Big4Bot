# OKR Design

## Domain
Strategy

## Description
Goal-setting framework that connects organizational objectives to quantitative, time-bound key results, enabling cascaded alignment from company level through teams to individuals. Objectives are qualitative and directional; key results are numerical and falsifiable.

## Purpose
Organizations routinely fail to translate strategy into operational action because goals are either too vague to be measurable or are set at a level of detail that does not cascade to team behavior. OKR Design addresses this by establishing a disciplined goal-setting architecture that makes strategic intent concrete at every organizational level, creates a shared accountability structure, and produces a cadenced review mechanism for real-time course correction. The framework also surfaces cross-team dependencies and resource conflicts before they become execution failures.

## When to Use
- When an organization has defined a strategy and needs to operationalize it through measurable team-level commitments
- When existing goal-setting processes produce goals that are not measurable, not time-bound, or not connected to strategic priorities
- When alignment between teams on shared outcomes is insufficient and cross-functional friction is impeding execution
- When leadership needs a lightweight mechanism to monitor strategic progress without creating a full balanced scorecard infrastructure

## When NOT to Use
- Before organizational strategy is sufficiently defined — OKRs operationalize strategy; they cannot substitute for it
- In organizations where performance management is tightly coupled to compensation, as this tends to cause OKRs to be set conservatively and defeats the stretch purpose of the framework
- When the organization lacks the management discipline to conduct regular OKR review cycles, which renders the system performative rather than functional

## Inputs Required
- Documented organizational mission and strategy (including strategic priorities for the planning period)
- Current performance data establishing the baseline for each key result candidate
- Resource and capacity constraints at company and team level
- List of strategic initiatives already committed or under consideration

## Optional Inputs
- Prior OKR cycle results and scoring data
- Employee or team-level goal inputs from bottom-up contribution process

## Diagnostic Process
1. Define organizational mission and confirm the strategic priorities for the OKR period; OKRs must be traceable to strategic choices already made, not invented independently.
2. Set three to five top-level company objectives — each must be qualitative, directional, and inspirational enough to motivate without being measurable itself; test each by asking whether achieving it would represent clear strategic progress.
3. Define two to five key results per company objective — each key result must be quantitative, time-bound, outcome-oriented (not task-based), and independently verifiable; reject key results that are binary (done/not done) unless the binary outcome is itself the strategic measure.
4. Cascade OKRs to team and individual level by having each team define its own objectives and key results that contribute to company-level key results; require each team OKR to have an explicit stated connection to at least one company OKR.
5. Identify dependencies between OKRs across teams — surface any key result that requires contribution from another team, and establish explicit shared ownership or service-level agreements for those dependencies.
6. Establish the scoring and review cycle — define the cadence for weekly check-ins, mid-cycle reviews, and end-of-cycle scoring; the standard Google scoring convention uses 0.0–1.0 with 0.7 as the expected target score for stretch OKRs.
7. Conduct end-of-cycle scoring and retrospective — score each key result, identify patterns in over- and under-performance, extract learnings for the next cycle, and adjust the ambition calibration or resource allocation accordingly.

## Output
The analysis produces a complete OKR set with company, team, and (where required) individual levels populated, including objectives, key results with baseline and target values, dependency maps, and a review cadence specification. The output serves as the operating plan complement to a strategic initiative roadmap or balanced scorecard.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- balanced-scorecard
- strategic-initiative-mapping
- agile-operating-model

## References
- Andy Grove: *High Output Management* (1983) — Introduced Management by Objectives (MBO) at Intel, the direct precursor to OKRs, establishing the principle that goals must be measurable and that output matters more than activity
- John Doerr: *Measure What Matters* (2018, Portfolio/Penguin) — Documented the OKR methodology as implemented at Google and across Doerr's investment portfolio; introduced the FAST criteria (Frequently discussed, Ambitious, Specific, Transparent)
- Google: *OKR Playbook* (re:Work, 2012) — Practitioner specification of OKR implementation at scale, including the 0.0–1.0 scoring convention, the 70% expected attainment norm, and the separation of committed OKRs from aspirational OKRs
