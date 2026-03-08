# Unit Economics

## Domain
Finance & Valuation

## Description
Financial analysis framework that measures the direct revenue and costs associated with a single unit of business — a customer, transaction, or product — to determine per-unit profitability and the long-term viability of the business model. It is the foundational lens for evaluating whether growth creates or destroys value at the margin.

## Purpose
Unit economics answers the most fundamental question in business model evaluation: does acquiring and serving one additional customer (or completing one additional transaction) generate more value than it costs? By isolating the economics of the repeatable unit, the framework exposes structural profitability or loss before aggregate revenue growth obscures the underlying dynamics. It is the primary tool for determining whether a growth-stage business is building toward a sustainable model or scaling an inherently unprofitable engine.

## When to Use
- Evaluating the business model viability of a startup or growth-stage company seeking investment or acquisition
- Diagnosing why an unprofitable business is not reaching profitability despite revenue growth
- Assessing the impact of a pricing change, new customer segment, or distribution channel on per-unit profitability
- Setting fundraising guidance, growth targets, or capital efficiency benchmarks for investor presentations

## When NOT to Use
- For businesses with highly heterogeneous customer or transaction types where a single representative unit cannot be meaningfully defined
- When data to separate customer-level acquisition costs, revenues, and direct costs is unavailable or unreliable
- As a sole basis for business model approval without also assessing fixed cost structure and break-even dynamics

## Inputs Required
- Customer Acquisition Cost (CAC): total sales and marketing spend divided by new customers acquired in the period
- Average Revenue Per User or Unit (ARPU): total revenue divided by average active customers or units
- Direct variable cost per unit (COGS, customer support, hosting, delivery costs attributable to serving one unit)
- Customer churn rate or average contract duration (for subscription businesses)

## Optional Inputs
- Expansion revenue rate (net revenue retention or upsell rate) for subscription businesses
- Payback period target set by management or investors

## Diagnostic Process
1. Define the unit of analysis precisely: for SaaS businesses, the unit is typically a paying customer; for marketplaces, it may be a transaction or a buyer-seller pair; for consumer products, it may be a unit sold or a household.
2. Calculate Customer Acquisition Cost (CAC): total fully-loaded sales and marketing expense for the period (including salaries, commissions, advertising, and tooling) divided by the number of new customers or units acquired in the same period; separately calculate blended CAC and paid CAC where both organic and paid channels exist.
3. Calculate Average Revenue Per Unit (ARPU) or per-transaction revenue: total net revenue attributed to the unit cohort divided by the number of active units in the period; for subscription businesses, use monthly recurring revenue per customer (MRR/customer).
4. Calculate direct variable costs per unit: sum all costs that scale directly with serving one additional unit — cost of goods sold, hosting, payment processing, customer support (per ticket multiplied by average tickets per customer), and delivery costs.
5. Calculate gross margin per unit: ARPU minus direct variable cost per unit; express as a percentage and compare to industry benchmarks; gross margins below 40% for software or 20% for transactional businesses typically signal structural cost problems.
6. Calculate Customer Lifetime Value (LTV): for subscription businesses, LTV = (ARPU x Gross Margin %) / Monthly Churn Rate; for transactional businesses, LTV = Average Order Value x Gross Margin % x Purchase Frequency x Average Customer Lifespan.
7. Compute the LTV:CAC ratio (healthy benchmark: above 3x) and CAC payback period (LTV:CAC / monthly gross profit per customer, measured in months; healthy benchmark: under 18 months for SaaS); interpret both metrics together, as a high LTV:CAC ratio with a long payback period still creates cash flow risk.

## Output
The analysis produces a unit economics summary table showing CAC, ARPU, gross margin per unit, LTV, LTV:CAC ratio, and CAC payback period alongside industry benchmarks and year-over-year trends. A cohort-level breakdown is included where customer data permits, and specific levers for improving the LTV:CAC ratio are quantified.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- break-even-analysis
- scenario-and-sensitivity-analysis
- financial-ratio-analysis
- business-model-canvas
- pricing-and-packaging-strategy
- product-discovery

## References
- Andreessen Horowitz (a16z): *SaaS Metrics Framework* — practitioner standard for LTV, CAC, and payback period benchmarks
- David Skok: *SaaS Metrics 2.0* (ForEntrepreneurs blog, 2012) — definitive practitioner guide to unit economics for subscription businesses
- Bill Gurley: *All Revenue is Not Created Equal* (Above the Crowd blog, 2011) — analysis of revenue quality and LTV assumptions
