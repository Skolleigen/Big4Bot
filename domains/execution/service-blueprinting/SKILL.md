# Service Blueprinting

## Domain
Execution

## Description
Service design tool that maps end-to-end service delivery across four horizontal layers — customer actions, frontstage employee actions, backstage employee actions, and support processes and systems — separated by three lines of demarcation: interaction, visibility and internal interaction. Produces a complete cross-layer service map that makes invisible failure causes visible.

## Purpose
Service failures frequently originate not at the customer-facing touchpoint but in the backstage processes and supporting systems that customers never see. Tools that analyze only the customer-facing layer — such as customer journey mapping — cannot locate these root causes because they lie below the line of visibility. Service blueprinting extends the analytical scope to all four delivery layers simultaneously, exposing the fail points, handoff breakdowns and system failures that generate customer-visible quality problems but are structurally invisible to purely customer-facing analysis. This cross-layer visibility is essential for diagnosing service quality issues accurately and designing improvements that address root causes rather than symptoms.

## When to Use
- When redesigning a service to improve quality, reliability or consistency and the root causes of failure are not fully understood from customer feedback alone
- When service failures have been identified at the customer touchpoint but their backstage origins are unknown
- When designing a new service that requires coordination across multiple departments, employee roles and supporting systems
- When preparing a service for automation, outsourcing or centre-of-excellence consolidation and the full process scope must be documented end-to-end

## When NOT to Use
- When designing a purely digital self-service product with no human employee involvement — the frontstage and backstage employee layers are absent, making a full service blueprint unnecessary
- When only the customer-facing experience layer requires analysis — customer journey mapping is the more targeted tool for purely front-of-house diagnostics
- When the organization lacks the implementation capacity to act on backstage process improvements — blueprinting without improvement action produces documentation without value

## Inputs Required
- Service scope definition: the specific service, the target customer segment and the start and end points of the service being mapped
- Existing customer journey map or a documented inventory of customer touchpoints and stages across the service
- List of internal roles involved in service delivery at frontstage and backstage levels
- Inventory of supporting systems and technology platforms used at each stage of the service

## Optional Inputs
- Service level agreement requirements specifying the quality and turnaround standards the service is expected to meet
- Failure frequency data by touchpoint or stage, including customer complaint data and failure mode logs
- Cost-per-interaction data to enable prioritization of improvement opportunities by financial impact

## Diagnostic Process
1. Define the service scope: confirm the target customer segment, the service stages (typically 4–8 stages), and the start and end boundaries of what is being mapped
2. Map customer actions at each service stage — what the customer does, chooses, submits, receives or experiences at each stage, drawing directly from the customer journey map or touchpoint inventory
3. Map frontstage employee actions aligned to each customer action, separated from customer actions by the line of interaction — these are the visible, customer-facing service delivery activities performed by employees
4. Map backstage employee actions that support each frontstage activity, separated from frontstage by the line of visibility — these are the operational activities employees perform that the customer never sees but that determine whether the frontstage interaction succeeds or fails
5. Document the support processes, information systems and technology platforms that enable each backstage action, separated from backstage by the line of internal interaction — these are the processes and systems that backstage employees depend on
6. Identify fail points across all four layers at each stage — mark where the service design is structurally likely to break down, annotating with failure frequency and customer impact severity where data is available
7. Prioritize improvement opportunities by cross-referencing customer impact severity with implementation feasibility, and design targeted interventions at the layer where each fail point originates

## Output
The output is a completed service blueprint diagram showing all four layers across all service stages, with fail points marked and annotated with failure frequency and customer impact data. A prioritized improvement opportunity list identifies which fail points to address first based on customer impact and implementation feasibility, and specifies at which layer (frontstage, backstage or support systems) each intervention must be made. This cross-layer analysis enables improvement investments to be directed at root causes rather than symptoms.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- process-mapping
- customer-journey-mapping
- raci-daci-governance
- agile-operating-model

## References
- G. Lynn Shostack: *Designing Services That Deliver*, Harvard Business Review (1984)
- Mary Jo Bitner, Amy L. Ostrom & Felicia N. Morgan: *Service Blueprinting: A Practical Technique for Service Innovation*, California Management Review (2008)
- IDEO: *The Field Guide to Human-Centered Design* (2015) — service design methodology
- Stefan Moritz: *Service Design: Practical Access to an Evolving Field* (2005)
