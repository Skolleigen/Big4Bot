# Scrum Framework

## Domain
Execution

## Description
Agile delivery framework organizing work into time-boxed sprints with defined ceremonies (planning, daily standup, review, retrospective) and roles (Product Owner, Scrum Master, Development Team) to deliver value incrementally. Creates a structured feedback cadence that enables teams to course-correct based on real evidence at the end of every sprint.

## Purpose
Traditional project management approaches defer value delivery to project completion, accumulating scope risk, misalignment risk and integration risk throughout the delivery cycle. By the time stakeholders see working output they have often waited months or years, and course-correction requires expensive rework. Scrum replaces this pattern with a cadence of short delivery cycles — the Scrum Guide (Schwaber & Sutherland, 2020) permits sprints of up to one month, though most teams adopt 1–2 week sprints as an industry best practice to enable faster feedback cycles — and structured feedback loops at each cycle boundary, enabling teams to confirm they are building the right thing while there is still time and budget to change direction. The framework also creates team rhythm, surfaces impediments rapidly through daily standups, and generates empirical velocity data that improves forecast accuracy over time.

## When to Use
- When building a product or service through iterative development where the full scope cannot or should not be fixed at the start
- When requirements are expected to evolve based on user feedback, market input or emerging technical constraints
- When a cross-functional delivery team needs a structured operating cadence with clear roles, ceremonies and accountability
- When the goal is frequent delivery of testable, working increments rather than a single large release at the end of a long delivery cycle

## When NOT to Use
- When the project has fully fixed scope, fixed timeline and zero tolerance for iteration — Scrum's value lies in adaptation, which requires flexibility in at least one of these dimensions
- When regulatory environments mandate exhaustive upfront design documentation and prohibit iterative development approaches
- When the team is distributed across time zones with fewer than 3 hours of daily overlap — the daily standup and sprint ceremonies require synchronous participation to function
- When the deliverable is a one-time document, analysis or advisory output rather than an iterated product or service

## Inputs Required
- Product vision statement and high-level goals defining what the team is building and the problem it solves
- Initial product backlog containing User Stories or equivalent feature descriptions sufficient to fill the first 2–3 sprints
- Team composition confirming the Product Owner, Scrum Master and development team members with their capacity
- Sprint cadence decision: the Scrum Guide allows sprints of up to one month (four weeks), but 1–2 week sprints are the most common industry practice; confirm sprint duration before Sprint 1 begins

## Optional Inputs
- Definition of Done criteria specifying the quality and completeness standards a backlog item must meet to be accepted
- Team working agreements covering communication norms, escalation expectations and core hours
- Historical velocity data from prior team Scrum experience to improve Sprint 1 capacity planning

## Diagnostic Process
1. Define the product vision and create the initial product backlog: the Product Owner writes User Stories with acceptance criteria and prioritizes the backlog by value and risk
2. Refine and estimate backlog items using story points or t-shirt sizing in a backlog refinement session — aim to have 2–3 sprints' worth of refined, estimated stories before Sprint 1 begins
3. Conduct Sprint Planning: the team selects backlog items they commit to completing in the sprint, defines the sprint goal as the unifying objective, and decomposes selected stories into development tasks on the sprint backlog
4. Execute the sprint: the development team self-organizes to complete sprint backlog tasks; the Scrum Master facilitates daily standups (15 minutes: what did I do yesterday, what will I do today, what is blocking me) and removes impediments raised; the Product Owner remains available to clarify requirements but does not add scope mid-sprint
5. Conduct the Sprint Review at sprint end: the development team demonstrates completed, working increments to stakeholders; the Product Owner accepts or rejects each item against acceptance criteria; stakeholder feedback updates the product backlog for future sprints
6. Conduct the Sprint Retrospective immediately after the review: the team reflects on what went well, what did not, and commits to one specific process improvement for the next sprint — the retrospective is the primary mechanism for continuous team improvement
7. Update the product backlog based on review feedback, re-prioritize as needed, and begin the next sprint planning cycle

## Output
The output of each sprint cycle is a potentially shippable product increment — tested, integrated working software or service that meets the Definition of Done — along with an updated product backlog reflecting new stakeholder feedback and a retrospective improvement commitment for the next sprint. Over multiple sprints, the team also produces an empirical velocity record that enables increasingly accurate sprint forecasting and release date projection.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- agile-operating-model
- raci-daci-governance
- portfolio-governance
- okr-design

## References
- Ken Schwaber & Jeff Sutherland: *The Scrum Guide* (2020 edition) — the authoritative definition of the Scrum framework
- Jeff Sutherland: *Scrum: The Art of Doing Twice the Work in Half the Time* (2014)
- Scaled Agile Framework (SAFe): *SAFe 6.0 Framework* — practitioner guidance on scaling Scrum across multiple teams and portfolios
- Mike Cohn (Mountain Goat Software): *Succeeding with Agile: Software Development Using Scrum* (2009)
