# Process Mapping — Example

## Scenario
A UK motor insurer's claims settlement process takes an average of 23 calendar days from first notification of loss to settlement payment. The industry benchmark for equivalent claim complexity is 12 days. A process improvement initiative has been commissioned to identify root causes of the 11-day performance gap and design a future-state process targeting a cycle time competitive with the benchmark.

## Inputs
- **Process scope:** First notification of loss (FNOL) call received to settlement payment issued — 14 steps across 5 roles
- **Process participants:** Claims handler, loss adjuster, supervisor, finance settlement team, third-party repair network coordinator
- **Existing documentation:** A 2018 standard operating procedure document covering 8 of the 14 steps; the remaining 6 steps are undocumented
- **Performance metrics:** Average cycle time 23 days; error rate (claims requiring rework) 28%; monthly volume 1,400 claims; settlement team SLA breach rate 34%

## Analysis

**Step 1 — Scope definition:**
Process scope is confirmed from FNOL receipt to payment issuance. The claims re-opening process (post-settlement disputes) is explicitly out of scope for this exercise. Key stakeholders confirmed: claims handlers (22 FTE), loss adjusters (8 FTE), supervisors (4 FTE), finance settlement (6 FTE), repair network coordinator (3 FTE). The improvement objective is to reach a 12-day average cycle time and reduce rework rate from 28% to below 10%.

**Step 2 — Process walkthrough:**
Six walkthroughs are conducted across all five roles over 3 days. Participants are asked to describe what they actually do, not what the SOP prescribes. Material divergences between the 2018 SOP and actual practice are discovered in 5 of the 14 steps. The walkthrough also surfaces a 15th step (informal supervisor sign-off on third-party repair estimates over £2,000) not documented anywhere.

**Step 3 — Current-state process map construction:**
A swim lane map is constructed across 5 role lanes with 15 steps, 4 decision diamonds and 12 handoffs. System interactions are noted: 3 different systems are used across the process (claims management system, repair network portal and a standalone finance settlement tool) with no direct integration between them. Data is manually re-keyed between all three systems at three separate points.

**Step 4 — Cycle time and waste measurement:**
Average time per step measured from system timestamps and supervisor log data. Results: Steps 1–4 (FNOL intake to loss adjuster assignment): 1.2 days. Step 5 (loss adjuster inspection booking and attendance): 6.1 days — the single largest contributor. Steps 6–8 (inspection report, estimate review, supervisor approval): 4.5 days. Steps 9–11 (manual data re-entry into settlement tool, finance queue, payment): 4.8 days. Steps 12–15 (repair network coordination, completion confirmation, closure): 6.4 days. Total: 23 days. Manual data re-entry contributes 4.5 days; supervisor approval queues contribute 3.2 days; repair network coordination laps contribute 2.8 days.

**Step 5 — Waste classification:**
Waste identified across five categories: (1) Manual data re-entry: 4.5 days lost re-keying claim data between 3 unintegrated systems — affects every claim; (2) Unnecessary approvals: supervisor approval required for all third-party repair estimates above £2,000 but 71% of claims exceed this threshold, making this a universal bottleneck rather than an exception control; (3) Rework loops: 28% of claims require re-inspection because the initial inspection report is incomplete — driven by a loss adjuster checklist with 6 optional fields that adjusters routinely skip; (4) Repair network delays: coordination of repair slot confirmation is manual and untracked, creating 2–5 day variance in Steps 12–15; (5) Overprocessing: claims handlers complete a full liability assessment for all claims before triage — for clear-liability claims (estimated at 58% of volume), this assessment adds 0.8 days with no decision value.

**Step 6 — Future-state design:**
Future-state map redesigned to 11 steps eliminating identified waste. Key changes: API integration between the 3 systems eliminating manual data re-entry (−4.5 days); supervisor approval threshold raised from £2,000 to £8,000 reducing approval queue cases from 71% to 12% of claims (−2.1 days saved for 59% of claims); loss adjuster inspection checklist revised to make the 6 critical fields mandatory with system enforcement (expected to reduce rework rate from 28% to 9%, saving 1.4 days per rework case amortized across all claims); automated repair slot booking via repair network portal integration (−1.2 days average); early triage step added to route clear-liability claims to an accelerated pathway (0.8 days saved for 58% of claims). Projected future-state average cycle time: 11 days.

**Step 7 — Implementation plan:**
Three workstreams defined. Technology (lead: IT Director, 4-month timeline): API integration between the 3 systems; repair network portal automation. Process and policy (lead: Claims Operations Manager, 6-week timeline): revised supervisor approval thresholds; mandatory inspection checklist enforcement; triage routing logic. Training (lead: L&D, 8-week timeline): all 22 claims handlers and 8 loss adjusters trained on revised process before go-live. Process owner designated as Head of Claims Operations with monthly cycle time and rework rate reporting to the Claims Director.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
