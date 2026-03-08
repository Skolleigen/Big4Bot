# Product-Market Fit Diagnostics

## Domain
Product & Innovation

## Description
Diagnostic framework for evaluating the degree to which a product satisfies a strong market demand, using quantitative signals and qualitative evidence to assess fit and identify the primary factors limiting or enabling it.

## Purpose
Product-Market Fit Diagnostics provides a structured method for answering the foundational investment question: does this product deserve continued or increased resource commitment? It combines retention metrics, user sentiment surveys, engagement analysis, and organic growth signals into a composite assessment that classifies fit level and isolates the specific dimensions — segment definition, value proposition, pricing, or distribution — most limiting current fit. The framework prevents both premature scaling (before fit is established) and continued investment in a fundamentally misaligned product.

## When to Use
- Leadership is deciding whether to scale marketing and sales investment in an early-stage product
- A product has been live for at least three months and sufficient behavioral data exists to assess retention cohorts
- Organic growth has stalled or reversed and the team needs to determine whether the issue is market fit or execution
- A portfolio review requires a standardized fit assessment across multiple products or business lines

## When NOT to Use
- The product has fewer than 100 active users and retention cohort analysis would be statistically unreliable
- The product has been live for less than six weeks and users have not had sufficient time to demonstrate repeat behavior
- The engagement is scoped to marketing strategy rather than product-market alignment
- The product serves a captive internal user base where voluntary adoption signals are not meaningful indicators of fit

## Inputs Required
- User retention cohort data segmented by acquisition period (minimum 8 weeks of data)
- Results from a Sean Ellis survey or equivalent willingness-to-pay and disappointment measurement
- Net Promoter Score data and verbatim qualitative feedback from users
- Product engagement metrics: active usage frequency, session depth, and core feature adoption rates

## Optional Inputs
- Organic referral and word-of-mouth acquisition data to assess virality signals
- Churn interview transcripts to understand exit reasons from former users

## Diagnostic Process
1. Define the target customer segment precisely, ensuring the analysis is conducted on the segment the product is actually designed to serve rather than the full user base, which may dilute signal with mismatched users.
2. Measure retention cohorts by plotting week-over-week or month-over-month retention for each acquisition cohort; determine whether retention curves flatten to a sustainable baseline or continue declining toward zero.
3. Administer the Sean Ellis survey to active users, measuring the percentage who would be "very disappointed" if the product no longer existed; score the result against the 40% threshold associated with strong fit, and segment responses by user type to identify which sub-segments show the strongest signal.
4. Analyze Net Promoter Score alongside verbatim qualitative feedback, coding open-text responses to identify the most frequently cited value drivers and detractors; compare promoter rationale against detractor rationale to surface fit-limiting factors.
5. Evaluate engagement and usage patterns by measuring frequency of core feature use, time-to-value for new users, and breadth of feature adoption; identify whether a meaningful segment demonstrates habitual, high-frequency use consistent with the intended use case.
6. Assess organic growth indicators including referral rate, direct or branded search traffic growth, and unsolicited press or community mentions as signals of word-of-mouth driven by genuine product satisfaction.
7. Score overall fit level as no fit, weak fit, or strong fit based on the composite signal from steps 2 through 6; document the primary limiting factor (segment mismatch, value proposition gap, pricing barrier, or awareness deficit) and recommend the most targeted intervention.

## Output
The output is a fit level classification (no fit, weak fit, or strong fit) with a quantitative and qualitative evidence summary supporting the assessment. The deliverable identifies the single highest-leverage intervention point — whether in product, segment, pricing, or go-to-market — and provides prioritized recommendations sequenced by expected impact on fit indicators.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- product-discovery
- value-proposition-canvas
- unit-economics
- pricing-and-packaging-strategy
- lean-startup-cycle

## References
- Sean Ellis: Product-Market Fit survey methodology and the 40% threshold benchmark
- Marc Andreessen: *The Only Thing That Matters* (2007) — foundational articulation of product-market fit as the primary startup success factor
- Andrew Chen: retention curve analysis and the flat retention curve as a PMF signal
