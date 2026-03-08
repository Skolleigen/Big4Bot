# Portfolio Governance

## Domain
Execution

## Description
Management framework for overseeing a collection of projects and initiatives to ensure alignment with strategy, optimal resource allocation, and effective risk management at portfolio level. Establishes the decision-making structures and reporting cadences to manage a portfolio as an integrated whole rather than as isolated projects.

## Purpose
Organizations running multiple concurrent initiatives frequently suffer from resource conflicts, misaligned priorities and insufficient leadership visibility into collective delivery risk. Individual project managers focus on their own initiatives without authority or visibility to resolve cross-initiative conflicts, creating bottlenecks and duplicated effort that are invisible until they cause delivery failures. Portfolio governance establishes the oversight structures, decision rights and reporting processes that give senior leadership the information and authority to make stop/start/continue/accelerate decisions across the portfolio as conditions change.

## When to Use
- When managing five or more concurrent strategic initiatives that share resources, dependencies or strategic objectives
- When resource contention between initiatives is creating delivery bottlenecks that individual project managers cannot resolve
- When senior leadership lacks consolidated visibility into collective initiative status, budget consumption and risk exposure
- When investment decisions across the portfolio need to be rationalized against strategic priorities and available capacity

## When NOT to Use
- When managing a single project or program with no portfolio-level resource conflicts or dependencies
- When the organization is in early start-up phase with limited initiative scope and direct executive oversight is sufficient
- When all initiatives are wholly independent with no shared resources, dependencies or strategic trade-offs requiring portfolio-level adjudication

## Inputs Required
- Active initiative inventory with current status, budget consumption, schedule variance and strategic objective alignment
- Resource capacity plan showing supply and demand for shared resources (technology, data, program staff, executive sponsorship)
- Risk and issue logs for each active initiative
- Strategic objectives and the alignment mapping between each initiative and those objectives

## Optional Inputs
- Benefit realization tracking data showing actual versus forecast benefits for completed or in-flight initiatives
- Stage-gate criteria defining the governance decision points for each initiative lifecycle stage
- Benefit dependency networks showing how initiative outputs combine to produce strategic outcomes

## Diagnostic Process
1. Inventory all active and proposed initiatives, classify each by strategic objective, phase and current health status (green/amber/red)
2. Assess resource demand versus available capacity across shared resources — identify over-allocated functions, teams or individuals
3. Review interdependencies and sequencing constraints between initiatives — identify blocking relationships and critical path impacts
4. Evaluate performance of active initiatives against schedule, budget and benefit targets; flag initiatives that are amber or red on two or more dimensions
5. Apply portfolio-level risk assessment aggregating risks across all initiatives to identify systemic exposures not visible at individual project level
6. Facilitate a portfolio review with senior leadership to apply stop/start/continue/accelerate decisions to each initiative based on the evidence gathered
7. Update the portfolio roadmap to reflect decisions, reallocate resources, communicate changes to initiative teams and schedule the next portfolio review cycle

## Output
The output is a portfolio status report showing each initiative's health, resource consumption, benefit trajectory and strategic alignment, accompanied by a decision log recording the stop/start/continue/accelerate outcomes and rationale from the latest portfolio review. The updated portfolio roadmap reflects revised sequencing, resource allocations and risk mitigations, providing a single source of truth for leadership and initiative teams on portfolio priorities and constraints.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- initiative-prioritization-matrix
- strategic-initiative-mapping
- agile-operating-model
- raci-daci-governance
- balanced-scorecard

## References
- Project Management Institute: *The Standard for Portfolio Management*, 4th Edition (2017)
- Axelos: *Managing Successful Programmes (MSP)*, 5th Edition (2020)
- Axelos: *Portfolio, Programme and Project Offices (P3O)* (2013)
- Gartner: *IT Portfolio Management* — practitioner research on portfolio governance structures and reporting cadences
