# RACI / DACI Governance

## Domain
Execution

## Description
Accountability framework that assigns explicit roles — Responsible, Accountable, Consulted, Informed (RACI) or Driver, Approver, Contributor, Informed (DACI) — to decisions and process activities to clarify ownership and decision rights across cross-functional teams. In the DACI model, the Driver is the person responsible for driving the decision process, the Approver has final decision authority, Contributors are subject matter experts who provide input, and Informed stakeholders must be kept aware of the decision outcome. Surfaces accountability gaps, ownership conflicts and consultation bottlenecks before they create operational failures.

## Purpose
Unclear accountability is a leading cause of decision delays, duplicated effort and organizational conflict. Without explicit role assignment, cross-functional decisions default to whoever asserts authority in the moment, creating inconsistent outcomes and resentment between functions. RACI and DACI frameworks create a structured mapping between decisions or activities and the roles responsible for driving, approving, contributing expertise and receiving information, converting implicit expectations into explicit agreements that can be validated with stakeholders and used to redesign governance structures that are actively creating bottlenecks.

## When to Use
- When launching a new cross-functional process, program or operating model that requires clear ownership across multiple departments
- When decision delays, escalation failures or recurring conflicts indicate unclear or contested ownership in an existing process
- When onboarding new team members, new leaders or new functions into complex governance structures where role expectations are not documented
- When preparing for organizational restructuring and new accountability structures must be designed and communicated before the change lands

## When NOT to Use
- When a single owner is clearly responsible with no meaningful cross-functional dependencies — formal role mapping adds process overhead without governance value
- When the process is fully automated with no human decision points requiring accountability assignment
- When the team is small (fewer than five people) and decision rights are established through direct communication rather than formal structure

## Inputs Required
- List of decisions or process activities requiring role assignment — the rows of the matrix
- Roster of stakeholder roles to appear on the matrix — the columns; individual names are included but roles are the primary unit of mapping
- Existing escalation paths and authority limits relevant to the decisions being mapped

## Optional Inputs
- Decision frequency and urgency classification to identify which decisions most need governance clarity
- Existing process documentation or swim lane maps to anchor the activity list
- RACI or DACI matrices from comparable functions or organizations as reference benchmarks

## Diagnostic Process
1. Define the scope of decisions or process activities to be mapped — establish boundaries and confirm with stakeholders that the list is complete and correctly scoped
2. Identify all stakeholder roles to appear on the matrix columns — include roles that participate even indirectly; err toward inclusion at this stage
3. List all decisions or process activities as rows in the matrix in the sequence in which they occur
4. Workshop the assignment of RACI or DACI roles for each role-activity intersection, either in a live session with stakeholders or through an asynchronous review with structured validation
5. Validate completed assignments with stakeholders to surface disagreements — disagreements are the diagnostic signal; they indicate where governance expectations are misaligned
6. Review the completed matrix for structural governance issues: multiple Accountable (A) owners for a single activity, activities with no Responsible (R), roles that are Consulted (C) on every activity regardless of relevance, and decision bottlenecks where Accountable roles are over-loaded
7. Finalize the revised matrix incorporating stakeholder validation, publish it as an authoritative governance document and communicate role expectations to all parties

## Output
The output is a completed RACI or DACI matrix covering all in-scope decisions and activities with role assignments validated by stakeholders, accompanied by a governance issues log documenting the structural problems identified (dual accountability, missing responsibility, over-consultation) and the design decisions made to resolve them. Implementation notes specify any escalation path changes, approval authority updates or communication requirements needed to activate the new accountability structure.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- process-mapping
- agile-operating-model
- portfolio-governance
- change-management

## References
- Smith, M. & Erwin, J.: *Role & Responsibility Charting (RACI)* (2005) — practitioner guide to RACI construction and validation
- Bain & Company: *RAPID Decision Framework* — decision rights framework using Recommend, Agree, Perform, Input, Decide as an alternative accountability model
- Project Management Institute: *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*, 7th Edition (2021)
- Intuit / Atlassian: *DACI Decision-Making Framework* — Driver, Approver, Contributor, Informed model for product and cross-functional team decision governance
