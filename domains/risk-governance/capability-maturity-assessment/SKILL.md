# Capability Maturity Assessment

## Domain
Risk & Governance

## Description
Structured evaluation framework that rates organizational or process capabilities on a maturity scale (1=Initial to 5=Optimizing) to identify improvement priorities. The assessment produces a capability heat map that reveals gaps between current and target maturity states.

## Purpose
Capability Maturity Assessment gives leadership a calibrated, evidence-based view of where organizational processes and functions stand relative to recognized best-practice levels. By quantifying maturity gaps, it directs limited improvement investment toward the capabilities that carry the greatest strategic importance. The output also establishes a defensible baseline against which future progress can be measured.

## When to Use
- A business unit or function is undergoing strategic review and leadership needs an objective benchmark of current operational effectiveness
- A transformation program is being planned and sponsors require a starting-point assessment to scope improvement initiatives and set realistic timelines
- An audit or regulatory review has flagged process inconsistency and management needs a structured remediation plan
- An organization is evaluating whether to insource, outsource, or restructure a capability and requires comparative maturity data to inform the decision

## When NOT to Use
- The assessment scope is a single, isolated process step rather than an end-to-end capability domain — a process mapping exercise is more appropriate in that case
- Maturity is already well-documented from a recent assessment conducted within the past 12 months and operating conditions have not materially changed
- The organization lacks the stakeholder access or documentary evidence needed to score capabilities reliably, as the output will be misleading without sufficient evidence

## Inputs Required
- List of capability domains to be assessed (e.g., data management, procurement, risk management, IT service delivery)
- Chosen maturity model and its level descriptors (CMMI v2.0, P3M3, or a client-specific framework)
- Access to key stakeholders across assessed domains for structured interviews
- Existing process documentation, policies, standard operating procedures, and prior audit or assessment reports

## Optional Inputs
- Benchmarking data from peer organizations or industry surveys to enable comparative scoring
- Strategic objectives or transformation roadmap to weight capability importance during prioritization

## Diagnostic Process
1. Define the capability domains to assess by reviewing the organization's operating model, strategic plan, and any existing process inventories; confirm scope, boundaries, and exclusions with the client sponsor before proceeding.
2. Select the appropriate maturity model — CMMI v2.0 for development and service capabilities, P3M3 for portfolio and programme management, or a custom model — and calibrate level descriptors to the client's industry context and terminology.
3. Administer the assessment through structured stakeholder interviews, facilitated focus groups, and systematic documentation review; collect and record evidence for each capability domain against each maturity level descriptor.
4. Score each capability on the 1–5 scale by reconciling stakeholder self-assessment responses with documentary evidence; apply an evidence-weighting rule so that undocumented verbal claims do not inflate scores beyond the level supportable by written evidence.
5. Produce a capability heat map that plots current maturity scores across all domains, using red (levels 1–2), amber (level 3), and green (levels 4–5) shading for rapid executive communication of the overall picture.
6. Identify priority capabilities for improvement by cross-referencing maturity gaps with strategic importance ratings; capabilities that are simultaneously low-maturity and high-importance form the critical improvement set requiring immediate attention.
7. Define an improvement roadmap that sequences capability uplift initiatives, estimates effort and resource requirements for each maturity level transition, and sets measurable milestones with defined accountability.

## Output
The assessment produces a scored capability heat map accompanied by a narrative summary that explains the evidence base for each rating and the business implications of identified gaps. Priority improvement initiatives are ranked by strategic impact, with indicative effort estimates and sequencing logic to guide program planning.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- risk-register
- transformation-risk-heatmap
- control-mapping
- process-mapping

## References
- CMMI Institute: *CMMI for Development, Version 2.0* (2018)
- SEI (Software Engineering Institute): *CMMI Model and Supporting Materials*
- OGC: *P3M3 Portfolio, Programme and Project Management Maturity Model*
