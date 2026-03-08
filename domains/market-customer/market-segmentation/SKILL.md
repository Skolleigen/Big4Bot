# Market Segmentation

## Domain
Market & Customer

## Description
Analytical framework for dividing a heterogeneous market into distinct, homogeneous customer groups based on demographic, psychographic, behavioral, or geographic criteria. Enables targeted strategy development by identifying which customer groups represent the greatest commercial opportunity.

## Purpose
Organizations operating in broad or undifferentiated markets waste resources by treating all customers identically. Market segmentation resolves this by revealing structural differences in customer needs, willingness to pay, and buying behavior. The output informs go-to-market prioritization, product development sequencing, and resource allocation across sales and marketing functions.

## When to Use
- A company is entering a new market or geographic region and must determine which customer groups to target first
- Revenue growth has stalled and leadership needs to identify underserved or high-value segments being missed
- A product portfolio is being rationalized and the business needs to determine which segments each product should serve
- Pricing strategy work requires differentiation of customer willingness to pay across distinct groups

## When NOT to Use
- The total addressable market is too small to warrant sub-segmentation (fewer than a few hundred potential customers)
- Customer data is insufficient or unreliable, making segmentation outputs speculative rather than evidence-based
- The organization lacks the operational capacity to execute differentiated strategies across multiple segments simultaneously

## Inputs Required
- Definition of the total addressable market (industry, geography, product category boundaries)
- Existing customer data including firmographic or demographic attributes, purchase history, and behavioral signals
- Revenue and margin data by customer or customer cohort
- Sales and marketing funnel data indicating where different customer types convert or drop off

## Optional Inputs
- Third-party market research or industry reports on market size and segment structure
- Customer survey data including stated needs, preferences, and pain points

## Diagnostic Process
1. Define the total addressable market boundary by specifying the industry vertical, geographic scope, product category, and customer type (B2B vs. B2C) that bound the analysis.
2. Collect and clean customer data across segmentation variables: demographic or firmographic attributes (company size, industry, geography), psychographic attributes (values, risk tolerance), behavioral attributes (purchase frequency, channel preference, feature usage), and geographic attributes.
3. Apply segmentation criteria by grouping customers using one or more of the four variable classes. For B2B contexts, firmographic and behavioral variables typically yield the most actionable segments. For B2C, demographic and psychographic variables are commonly primary.
4. Evaluate each candidate segment against four attractiveness criteria: size (revenue potential), growth rate (trajectory over 3-5 years), profitability (margin achievable), and accessibility (cost and feasibility of reaching the segment through existing or buildable channels).
5. Select target segments by ranking segments on attractiveness criteria and filtering based on organizational capability to serve each segment competitively. Document the rationale for inclusion or exclusion of each segment.
6. Profile each selected target segment in detail: quantify size, describe representative customer characteristics, articulate primary needs and pain points, identify key buying criteria, and map current purchasing behavior.
7. Validate segment distinctiveness by confirming that selected segments are internally homogeneous (customers within a segment behave similarly) and externally heterogeneous (segments respond differently to marketing or product stimuli). Apply statistical clustering techniques where data volume permits.

## Output
The analysis produces a structured set of target segment profiles with quantified size and attractiveness rankings, a rationale for segment selection and de-selection, and segment-specific implications for product, pricing, channel, and messaging strategy. Each profile is sufficiently detailed to drive go-to-market planning without additional primary research.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- competitive-positioning
- value-proposition-canvas
- customer-journey-mapping
- swot-analysis

## References
- Philip Kotler & Gary Armstrong: *Principles of Marketing* (16th ed.) — Comprehensive treatment of STP (Segmentation, Targeting, Positioning) methodology
- Wendell R. Smith: *Product Differentiation and Market Segmentation as Alternative Marketing Strategies* (Journal of Marketing, 1956) — Foundational academic paper establishing segmentation as a strategic concept
- McKinsey & Company: *The art of customer segmentation* — Practitioner framework emphasizing behavioral and needs-based segmentation over demographic proxies
