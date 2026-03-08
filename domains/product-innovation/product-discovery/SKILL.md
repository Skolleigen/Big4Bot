# Product Discovery

## Domain
Product & Innovation

## Description
Structured research and validation process for understanding user problems, testing solution hypotheses, and defining product requirements before committing to full development cycles.

## Purpose
Product Discovery prevents teams from entering costly development with unvalidated assumptions about what users need and whether proposed solutions will work. It creates an evidence-based foundation for the product roadmap by systematically validating problem existence, solution desirability, and requirement specificity before engineering investment begins. The process reduces the rate of features built that fail to achieve adoption by ensuring each requirement traces to a confirmed user need.

## When to Use
- A new product, feature set, or significant redesign is being planned and user needs have not been recently validated through direct research
- Usage data indicates declining engagement or unexpected churn but the root cause is unclear
- The product team holds competing hypotheses about user problems and requires structured evidence to arbitrate between them
- Stakeholders are requesting new features without demonstrated user demand or a clear connection to business outcomes

## When NOT to Use
- The user problem is already validated through recent, high-quality research and the need is execution rather than further discovery
- The engagement timeline precludes meaningful user access before development must begin
- The product serves an internal audience where behavioral requirements are specified by organizational mandate rather than user preference
- Discovery would duplicate recently completed research without meaningful change in context or user segment

## Inputs Required
- Problem opportunity statement or initial product hypothesis to investigate
- Definition of the target user segment including criteria for participant recruitment
- Access to users for interviews, usability sessions, or prototype testing
- Existing behavioral data, analytics, or prior research available for secondary analysis

## Optional Inputs
- Support ticket or customer complaint logs to surface recurring pain points before primary research
- Competitor or analogous product examples to anchor solution hypothesis generation

## Diagnostic Process
1. Frame the problem opportunity by writing an explicit opportunity statement that defines the user segment, the job to be done, and the current gap or friction being investigated.
2. Conduct user interviews with a minimum of five to eight participants from the target segment, using open-ended questions to surface actual behavior, workarounds, and unmet needs without leading toward a predetermined solution.
3. Analyze existing behavioral data — including product analytics, funnel drop-off points, feature usage patterns, and support contact frequency — to identify evidence that corroborates or contradicts interview findings.
4. Generate solution hypotheses by translating validated problem findings into candidate solution approaches; document each hypothesis in the form "We believe [solution] will [outcome] for [segment] because [assumption]."
5. Prototype and test solution concepts with users using the lowest-fidelity representation that allows meaningful feedback: paper mockups, wireframes, or narrative storyboards; capture reactions to specific elements rather than general sentiment.
6. Synthesize insights from interviews, data analysis, and prototype testing into a set of validated requirements, distinguishing confirmed needs from assumptions still requiring evidence.
7. Prioritize validated requirements by value to the user and business against estimated development effort, producing a ranked backlog ready for roadmap planning.

## Output
The output is a discovery report containing validated user needs, a prioritized requirement set, and documentation of discarded hypotheses with the evidence that invalidated them. The report provides the product team and engineering organization with a traceable, evidence-based brief that connects each roadmap item to a specific confirmed user problem.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- product-market-fit-diagnostics
- value-proposition-canvas
- lean-startup-cycle
- design-thinking
- market-segmentation

## References
- Teresa Torres: *Continuous Discovery Habits* (2021)
- Marty Cagan: *Inspired: How to Create Tech Products Customers Love* (2017)
- SVPG (Silicon Valley Product Group): Product discovery and dual-track agile frameworks
