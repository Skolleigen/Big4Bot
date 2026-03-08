# Process Mapping

## Domain
Execution

## Description
Analytical technique for visually documenting business processes to understand current-state workflows, identify inefficiencies and design improved future-state processes. Produces step-by-step process documentation with quantified waste and a redesigned target-state process.

## Purpose
Organizations frequently operate with undocumented or inconsistently executed processes that create quality variability, training inefficiency and barriers to automation. When no authoritative process baseline exists, improvement efforts rely on anecdotal accounts, training is dependent on individual knowledge holders, and technology implementations automate broken processes rather than optimized ones. Process mapping provides the structured baseline required for identifying waste, clarifying ownership, designing scalable improvements and enabling technology implementation on a sound operational foundation.

## When to Use
- Before implementing automation, RPA or enterprise technology on a process — to ensure the improved process is being automated rather than the broken one
- When onboarding high volumes of new staff into complex workflows that are currently transmitted through informal knowledge transfer
- When a process has measurably high error rates, rework frequency or cycle time variability relative to internal targets or external benchmarks
- When preparing a process for outsourcing, offshoring or centre-of-excellence consolidation

## When NOT to Use
- When the process is highly creative, expert-judgment-intensive or knowledge-work-dominated and cannot be decomposed into repeatable steps
- When the organization is too early-stage to have repeatable processes — investment in mapping is premature if the process design is still being discovered
- When the improvement scope is purely strategic or organizational rather than operational — a different diagnostic framework is appropriate

## Inputs Required
- Process scope definition: the start event, the end event, and the explicit boundaries of what is in and out of scope
- List of process participants and roles involved across all steps and handoffs
- Existing process documentation, standard operating procedures or system workflows (if any exist)
- Process performance metrics: cycle time, error rate, rework frequency and transaction volume

## Optional Inputs
- Technology systems and platforms involved at each process step
- Regulatory, compliance or contractual requirements governing the process
- Customer service level agreements or turnaround time commitments

## Diagnostic Process
1. Define the process scope precisely — confirm start event, end event, key stakeholders to interview and the performance improvement objective that motivates the mapping exercise
2. Conduct structured process walkthroughs with process participants across all roles involved, documenting each step, decision point and handoff in sequence as performed in practice rather than as prescribed in policy
3. Construct the current-state process map with swim lanes by role, showing steps, decision diamonds, handoffs between roles and system interactions at each step
4. Measure and annotate the map with cycle time, handoff wait time, error rates and rework loop frequencies at each step — identify where time and quality loss occur
5. Classify waste across the map using standard waste categories: delays and wait time, unnecessary approvals and controls, manual data re-entry and reconciliation, rework loops and correction cycles, overprocessing and redundant handoffs
6. Design the future-state process map eliminating identified waste — challenge each step's necessity, consolidate handoffs, automate manual data entry and eliminate approval layers that add control without adding value
7. Define an implementation plan for transitioning from current to future state: process owner, training requirements, technology changes, policy updates and a success metrics baseline to track the improvement

## Output
The output consists of a current-state process map annotated with performance metrics and waste identification, a future-state process map showing the redesigned workflow, a waste quantification summary translating identified inefficiencies into cycle time, cost or error-rate impacts, and an implementation plan with accountability assignments. Together these documents provide the evidence base for an improvement business case and the operational specification for implementing the redesigned process.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- service-blueprinting
- raci-daci-governance
- agile-operating-model
- capability-maturity-assessment

## References
- Michael Hammer & James Champy: *Reengineering the Corporation: A Manifesto for Business Revolution* (1993)
- Object Management Group: *Business Process Model and Notation (BPMN) 2.0 Standard* (2011)
- Lean Enterprise Institute: *Value Stream Mapping* methodology
- Geary Rummler & Alan Brache: *Improving Performance: How to Manage the White Space on the Organization Chart* (1995)
