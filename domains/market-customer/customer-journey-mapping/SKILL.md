# Customer Journey Mapping

## Domain
Market & Customer

## Description
Visual diagnostic tool that maps the end-to-end experience of a customer across all touchpoints with a product or service, surfacing pain points, friction moments, and improvement opportunities at each stage of the relationship. Translates qualitative customer experience data into a structured artifact that drives prioritized operational and product investment.

## Purpose
Organizations frequently design and optimize internal processes without visibility into how those processes are experienced by customers. Customer journey mapping resolves this by documenting the actual sequence of customer actions, emotions, and decision points across all channels and interactions. The output identifies the highest-impact moments where experience improvements will produce measurable gains in conversion, retention, or satisfaction.

## When to Use
- Customer satisfaction scores or Net Promoter Score are declining and the root causes are not well understood
- A product or service redesign requires a baseline understanding of the current customer experience before defining the target state
- Acquisition funnel analysis shows drop-off at specific stages and the causal experience factors have not been diagnosed
- Cross-functional alignment is needed on which touchpoints are owned by which teams and where handoff failures occur

## When NOT to Use
- A valid, current customer persona does not exist; journey mapping without an anchoring persona produces generic outputs that are not actionable
- The organization is unwilling or unable to conduct primary customer research to validate journey assumptions
- The scope of the journey is undefined, risking a map so broad that no stage receives sufficient analytical depth

## Inputs Required
- Defined customer persona including demographics, goals, and primary jobs-to-be-done
- Enumeration of all known customer touchpoints across channels (digital, physical, human-assisted)
- Existing quantitative data on touchpoint performance (e.g., web analytics, call center volume, survey scores by interaction type)
- Qualitative customer feedback such as support tickets, interview transcripts, or usability study findings

## Optional Inputs
- Internal process documentation or service blueprints showing backstage operations that affect customer-facing touchpoints
- Competitor experience benchmarks or industry CX benchmark data

## Diagnostic Process
1. Define the customer persona and journey scope. Specify the persona (demographic profile, primary goal, context of use) and the journey boundaries (e.g., from first awareness of the product to completion of first successful use). A single journey map should cover one persona and one primary use case.
2. Identify all customer touchpoints within the defined scope. Enumerate every interaction point where the customer engages with the brand, product, or service — including digital (website, app, email), physical (retail, packaging, signage), and human-assisted (sales call, support chat, onboarding call) channels.
3. Map customer actions at each stage. For each touchpoint, document the specific actions the customer takes: what they click, say, request, or decide. Use behavioral data and direct customer observation where available rather than internal assumptions.
4. Document customer thoughts and emotions at each touchpoint. Capture what the customer is thinking (questions, concerns, expectations) and feeling (confidence, frustration, confusion, satisfaction) at each stage. Source this from interview transcripts, survey verbatims, or structured observation sessions.
5. Identify pain points and friction moments. Systematically flag touchpoints where customer emotions are negative, where actions require disproportionate effort, where handoffs between channels or teams are visible to the customer, and where quantitative data shows drop-off or complaint volume spikes.
6. Map internal process ownership at each touchpoint. For each touchpoint, identify the internal team, system, or process responsible. This step surfaces accountability gaps and handoff failures that are invisible from a purely customer-facing view.
7. Prioritize improvement opportunities by scoring each pain point on two dimensions: frequency (what proportion of customers experience it) and severity (how significantly it affects customer goal completion, satisfaction, or retention). Focus recommendations on high-frequency, high-severity pain points.

## Output
The analysis produces a structured journey map documenting customer actions, thoughts, and emotions at each touchpoint, a ranked list of pain points with supporting evidence, a map of internal ownership by touchpoint, and prioritized recommendations for experience improvement. Outputs are structured to support cross-functional prioritization workshops and product or service redesign initiatives.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- market-segmentation
- value-proposition-canvas
- service-blueprinting
- inbound-marketing-strategy

## References
- Adam Richardson: *Using Customer Journey Maps to Improve Customer Experience* (Harvard Business Review, 2010) — Practitioner framework establishing the structure and application of journey maps in a business context
- IDEO: *Design Thinking Methodology* — Provides the empathy-first research methods (observation, interview, shadowing) that generate the qualitative inputs required for valid journey mapping
- Mark S. Rosenbaum, Mauricio L. Otalora & German C. Ramirez: *How to Create a Realistic Customer Journey Map* (MIT Sloan Management Review / Journal of Retailing, 2017) — Academic synthesis of journey mapping best practices and common methodological failure modes
