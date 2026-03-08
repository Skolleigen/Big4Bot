# Transformation Risk Heatmap

## Domain
Risk & Governance

## Description
Visual risk prioritization tool that maps the risks associated with a specific transformation program, plotting them by likelihood and impact to guide mitigation planning. The heatmap gives program leadership and sponsors an at-a-glance view of where the most dangerous concentrations of risk sit within the transformation portfolio.

## Purpose
Transformation programs — whether technology implementations, operating model redesigns, or post-merger integrations — generate a distinctive and time-bounded risk profile that differs from steady-state operational risk. The Transformation Risk Heatmap makes this profile explicit and visually navigable for executive sponsors, enabling rapid identification of the risks most likely to derail delivery or destroy value. By combining likelihood and impact scoring with a structured mitigation ownership model, it converts risk awareness into risk accountability and drives action before issues materialize.

## When to Use
- A major transformation program (ERP implementation, digital platform launch, organizational restructuring, post-merger integration) is entering or mid-way through execution and program leadership requires a consolidated risk view
- A program steering committee or sponsor requires a structured risk briefing for board or investor reporting that goes beyond a simple issue log
- The program risk log has grown unwieldy and leadership needs a prioritization mechanism to focus mitigation resources on the risks with the highest potential to impact delivery, cost, or benefits realization
- A new phase of a multi-phase transformation is commencing and the risk profile needs to be refreshed to reflect changed conditions and emerging risks

## When NOT to Use
- The exercise covers steady-state operational risk rather than a bounded transformation or change initiative — a standard risk register is the appropriate tool in that case
- The transformation is in its earliest conceptual stage and insufficient detail exists about scope, approach, and execution timeline to score risks with reasonable accuracy
- The heatmap is intended to replace rather than complement narrative risk analysis — visual tools summarize but do not substitute for the analytical rigor required to understand root causes and design effective mitigations

## Inputs Required
- Defined transformation scope including the workstreams, systems, processes, and organizational units affected
- Program plan with milestone schedule to enable assessment of risks in the context of timeline and sequencing
- Stakeholder interviews with program workstream leads, sponsors, and subject matter experts across impacted functions
- Risk scoring scale with defined likelihood and impact descriptors calibrated to the specific program context

## Optional Inputs
- Lessons-learned logs from analogous prior transformations within the organization or from industry benchmarks
- Program risk log or issue register from an earlier phase of the same transformation to incorporate carry-forward risks

## Diagnostic Process
1. Define the transformation scope by confirming the full set of in-scope workstreams (technology, process, people, data, organizational design) and the program timeline with the program director or sponsor; document scope boundaries explicitly to prevent risk identification drift.
2. Identify transformation-specific risks across all risk categories — delivery risk, technology risk, change management and adoption risk, data migration risk, vendor and dependency risk, financial risk, and regulatory risk — through structured interviews with workstream leads and a facilitated risk workshop.
3. Score each identified risk on a 1–5 likelihood scale and a 1–5 impact scale using descriptors calibrated to the program; inherent scores should reflect the pre-mitigation position to reveal the true risk exposure before existing controls are credited.
4. Plot all scored risks on a 5x5 heatmap matrix using consistent coordinates; apply color coding — red for scores of 15 or above (high likelihood, high impact), amber for scores of 8–14, and green for scores of 7 or below — to create the visual risk concentration picture.
5. Identify the red-zone risks requiring immediate executive attention and deep-dive analysis; for each red-zone risk, document the root cause, early warning indicators, and the specific delivery outcomes or benefits at risk if the issue materializes.
6. Assign a named mitigation owner and a documented mitigation plan to every red-zone and amber-zone risk; confirm that each mitigation action is specific, time-bound, and within the assigned owner's authority to execute.
7. Establish a regular heatmap review cadence — weekly for red-zone risks, bi-weekly or monthly for amber-zone risks — and integrate the review into the program governance rhythm so that risk status is a standing agenda item at steering committee meetings.

## Output
The heatmap deliverable comprises a visually formatted 5x5 risk matrix with all program risks plotted, a risk register table providing the supporting detail for each plotted risk, and a narrative executive summary that articulates the top five to ten risks, their current mitigation status, and any residual exposures requiring sponsor-level decision or escalation.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- risk-register
- control-mapping
- capability-maturity-assessment
- change-management
- scenario-and-sensitivity-analysis

## References
- PMI: *Managing Change in Organizations: A Practice Guide* (2013)
- McKinsey & Company: *Transformation risk frameworks and transformation success factors research*
- KPMG: *Major Programme Management methodology*
