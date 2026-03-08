# Risk Register

## Domain
Risk & Governance

## Description
Structured documentation and management tool that inventories identified risks, their likelihood and impact assessments, ownership, and mitigation actions. The register serves as the authoritative single source of truth for an organization's active risk profile across strategic, operational, financial, compliance, and reputational categories.

## Purpose
A Risk Register transforms an organization's understanding of its threat environment from informal and fragmented into a governed, prioritized, and actionable record that supports management decision-making. By capturing risk ownership and mitigation commitments alongside each risk entry, the register creates accountability and ensures that risk response actions are tracked to completion. It also provides the foundation upon which control mapping, heat map analysis, and board-level risk reporting are built.

## When to Use
- An organization, program, or project is initiating a formal risk management process and requires a comprehensive baseline inventory of identified risks
- A new strategic initiative, acquisition, or regulatory change has introduced risks that are not reflected in the current risk inventory and a structured update is required
- Governance or audit requirements mandate a documented, owned, and periodically reviewed risk register for reporting to a board, audit committee, or regulator
- A prior risk event or near-miss has prompted leadership to commission a thorough review of the risk landscape to confirm coverage and mitigation adequacy

## When NOT to Use
- The engagement requires real-time, quantitative risk modeling with probabilistic distributions — a scenario and sensitivity analysis is the more appropriate tool for that purpose
- The risk register is being used as a compliance checkbox exercise without genuine commitment to ongoing ownership and review, as an unmaintained register provides false assurance
- The scope is so narrowly defined (e.g., a single vendor contract) that a full categorical risk taxonomy is disproportionate — a targeted risk assessment memo is sufficient

## Inputs Required
- Defined risk assessment scope (organization-wide, business unit, program, or project level) with explicit inclusion and exclusion boundaries
- Stakeholder interviews, facilitated risk workshops, and historical incident and loss data to support risk identification
- A risk categorization taxonomy (strategic, operational, financial, compliance, reputational, or equivalent client-specific categories)
- A likelihood and impact scoring scale with defined descriptors for each level (1–5 recommended)

## Optional Inputs
- Industry risk benchmarking data or sector-specific risk library to supplement internal identification and ensure completeness
- Existing audit findings, board papers, and prior risk assessments to incorporate previously identified risks and their historical treatment

## Diagnostic Process
1. Define the risk assessment scope and objectives by confirming with the client sponsor the organizational boundary, time horizon, risk categories to be covered, and the intended audience and use of the completed register.
2. Conduct risk identification through structured stakeholder interviews, facilitated workshops using techniques such as SWOT analysis and risk prompt lists, and review of historical incident data, audit reports, and industry risk libraries.
3. Categorize each identified risk into the agreed taxonomy (strategic, operational, financial, compliance, reputational) and assign a unique risk identifier; consolidate duplicate or overlapping risk entries into single, clearly scoped risk statements.
4. Score each risk on a 1–5 likelihood scale and a 1–5 impact scale using the defined descriptors; record both the inherent risk score (before controls) and the residual risk score (after considering existing controls) for each entry.
5. Calculate the composite risk score (likelihood multiplied by impact) for each risk and plot all risks on a 5x5 risk matrix to produce a visual representation of the risk distribution and identify the population of high-priority risks.
6. Assign a named risk owner for each risk entry, with the owner being the individual accountable for monitoring the risk and ensuring mitigation actions are implemented; confirm ownership with each assigned individual.
7. Define and document mitigation actions for each risk, specifying the action, the responsible party, the target completion date, and the expected residual risk score post-mitigation; record the agreed risk response strategy (avoid, reduce, transfer, or accept) for each entry.

## Output
The completed risk register is a structured table containing all identified risks with their category, inherent score, residual score, owner, mitigation actions, and response strategy. An executive summary synthesizes the overall risk profile, highlights the top risks by residual score, and identifies any risks that exceed the organization's stated risk appetite threshold.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- control-mapping
- transformation-risk-heatmap
- capability-maturity-assessment
- scenario-and-sensitivity-analysis

## References
- ISO: *ISO 31000:2018 Risk Management — Guidelines*
- COSO: *Enterprise Risk Management — Integrating with Strategy and Performance* (2017)
- PMI: *Practice Standard for Project Risk Management* (2009)
