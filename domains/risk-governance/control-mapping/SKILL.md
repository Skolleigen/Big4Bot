# Control Mapping

## Domain
Risk & Governance

## Description
Governance analysis technique that maps internal controls to the risks they mitigate, assessing control design adequacy and operating effectiveness. The output identifies control gaps, redundancies, and enhancement priorities across the organization's risk and compliance landscape.

## Purpose
Control Mapping provides a structured, auditable linkage between an organization's identified risk universe and the controls in place to address those risks, making invisible coverage gaps visible to management. It enables the organization to confirm that every material risk is addressed by at least one adequately designed and consistently operating control. The analysis also surfaces over-controlled areas where control rationalization can reduce cost and operational friction without increasing net exposure.

## When to Use
- An internal audit, external audit, or regulatory review requires evidence that controls are designed and operating effectively against the full risk population
- A risk management refresh has produced an updated risk register and controls need to be re-mapped to confirm alignment with the new risk profile
- A business unit is implementing a new process, system, or operating model and management needs to confirm the updated control environment remains complete
- The organization is preparing for a compliance certification (e.g., SOX, ISO 27001, SOC 2) that requires documented control-to-risk traceability

## When NOT to Use
- The risk register is immature or incomplete — control mapping against an insufficient risk universe will produce a false sense of assurance and should be deferred until risks are properly catalogued
- The exercise is intended to design net-new controls from scratch without an existing baseline — a risk-based control design workshop is more appropriate
- The scope is limited to a single regulatory requirement without reference to the broader risk environment, as point-in-time compliance mapping does not constitute a full control adequacy assessment

## Inputs Required
- Documented risk universe or risk register covering the scope of the assessment
- Inventory of existing controls, including control descriptions, control type (preventive, detective, corrective), and control owner
- Process documentation and system descriptions for the in-scope operational areas
- Relevant regulatory, legal, and internal policy requirements that controls must satisfy

## Optional Inputs
- Prior internal audit findings or external audit management letters identifying known control weaknesses
- Industry control frameworks (COSO, COBIT, NIST) to use as a reference overlay for gap identification

## Diagnostic Process
1. Compile the risk universe for the scope in question by extracting risks from the existing risk register or, where none exists, by conducting a facilitated risk identification session with process owners and risk managers.
2. Inventory existing controls by gathering control descriptions from policy documents, system configurations, audit workpapers, and interviews with control owners; classify each control as preventive, detective, or corrective.
3. Map each control to the specific risks it is designed to address, using a structured control-to-risk matrix; a single control may address multiple risks, and a single risk should ideally be addressed by multiple complementary controls.
4. Assess control design adequacy by asking whether each control, if operating exactly as described and intended, is sufficient to reduce the related risk to an acceptable residual level; flag any controls whose design does not fully address the stated risk.
5. Assess operating effectiveness by reviewing evidence of consistent control execution — transaction samples, system logs, exception reports, and sign-off records — and flag controls where execution is inconsistent, infrequent, or undocumented.
6. Identify control gaps (risks with no adequate control or with a control that fails design or effectiveness assessment) and over-controlled areas (risks with disproportionate layers of controls relative to their materiality).
7. Recommend control enhancements, additions, or rationalizations, assigning each recommendation to the responsible control owner and indicating implementation priority based on risk severity and gap materiality.

## Output
The primary deliverable is a control-to-risk matrix that provides full traceability from each identified risk to its associated controls, with design adequacy and operating effectiveness ratings for each control. An executive summary highlights material control gaps, redundancies, and the recommended remediation plan with ownership and timeline.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- risk-register
- capability-maturity-assessment
- raci-daci-governance
- transformation-risk-heatmap

## References
- COSO: *Internal Control — Integrated Framework* (2013)
- IIA (Institute of Internal Auditors): *International Standards for the Professional Practice of Internal Auditing*
- ISACA: *COBIT 2019 Framework: Governance and Management Objectives*
