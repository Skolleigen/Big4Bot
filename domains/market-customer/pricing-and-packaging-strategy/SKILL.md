# Pricing & Packaging Strategy

## Domain
Market & Customer

## Description
Analytical framework for determining optimal price levels, pricing models, and product packaging configurations to maximize revenue, margin, and market penetration. Integrates cost structure analysis, customer willingness-to-pay research, and competitive benchmarking to produce a defensible monetization architecture.

## Purpose
Mispriced products leave revenue on the table when prices are set below willingness to pay, or suppress adoption when prices exceed perceived value. This framework resolves pricing uncertainty by grounding decisions in cost economics, customer value perception, and market context rather than cost-plus defaults or competitive mimicry. The output provides leadership with a structured, evidence-based pricing model and packaging configuration that aligns monetization with customer segmentation.

## When to Use
- A new product or feature set is being launched and requires an initial pricing model and price point
- Revenue per customer is declining and the organization needs to identify whether pricing architecture or packaging is the primary driver
- A competitor pricing action has disrupted the market and a strategic pricing response is required
- The business is shifting commercial model (e.g., from perpetual license to subscription) and needs to design the transition pricing structure

## When NOT to Use
- Customer willingness-to-pay data is entirely absent and primary research cannot be conducted, making pricing outputs speculative
- The product is in pre-product-market-fit stage where the value proposition itself remains unvalidated; pricing analysis before PMF validation produces low-reliability outputs
- Regulatory pricing constraints (e.g., government rate setting, price controls) eliminate strategic discretion over price levels

## Inputs Required
- Full cost structure including variable cost per unit, fixed cost base, and current gross margin by product line
- Competitor pricing data including price levels, pricing model type, and packaging tiers
- Existing customer data on average revenue per user or account, churn rates by price tier, and upgrade/downgrade patterns
- Customer willingness-to-pay data from surveys, conjoint analysis, or sales conversation intelligence

## Optional Inputs
- Price elasticity estimates from historical pricing experiments or econometric modeling
- Sales team win/loss data with price-related attribution

## Diagnostic Process
1. Analyze cost structure and margin floors. Calculate variable cost per unit or per customer, fully loaded unit economics, and minimum acceptable gross margin. Establish the price floor below which the business cannot sustain the model at scale.
2. Assess customer willingness to pay through primary or secondary research. Use Van Westendorp Price Sensitivity Meter, conjoint analysis, or Gabor-Granger studies to establish the acceptable price range and optimal price point for each target segment. Where primary research is not available, triangulate from sales call transcripts and churn analysis at current price points.
3. Benchmark competitor pricing across direct and indirect competitors. Document price levels, pricing model type (subscription, usage-based, perpetual, freemium), and packaging tier structure. Identify whether the market has established price anchors and whether those anchors reflect genuine customer value or historical convention.
4. Identify pricing model options applicable to the business context. Evaluate subscription (recurring flat fee), usage-based (metered on consumption), tiered (feature or capacity-based tiers), freemium (free base tier with paid upgrades), and hybrid models. Assess each model's fit with the customer's buying behavior, budget cycle, and value realization pattern.
5. Design packaging configurations by bundling features, capacity limits, or service levels into discrete tiers. Ensure that each tier is differentiated by value-driving attributes meaningful to distinct customer segments, and that the step-up value between tiers is sufficient to drive upgrade behavior. Define the metric that scales pricing (seats, usage, revenue, outcomes).
6. Model the revenue impact of pricing scenarios. Build a financial model projecting revenue, gross margin, and customer volume under at least three pricing scenarios (current, proposed lower, proposed higher) across a 24-month horizon. Incorporate estimated elasticity, churn sensitivity, and upgrade/downgrade flow between tiers.
7. Select a pricing strategy and rollout approach. Recommend the pricing model, price points, and packaging configuration with the strongest combination of revenue potential and market penetration. Define the rollout approach for existing customers (grandfather, migrate, sunset legacy pricing) and the timeline and communication plan.

## Output
The analysis produces a recommended pricing model and tier structure with supporting financial projections, a summary of willingness-to-pay and competitive benchmarking findings, packaging configuration rationale by segment, and a prioritized rollout plan. Outputs are structured to enable executive pricing decisions and commercial team implementation.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- competitive-positioning
- value-proposition-canvas
- unit-economics
- business-model-canvas
- market-segmentation

## References
- Thomas T. Nagle & Reed K. Holden: *The Strategy and Tactics of Pricing* (4th ed.) — The definitive practitioner reference for value-based pricing methodology and price sensitivity analysis tools
- Madhavan Ramanujam & Georg Tacke: *Monetizing Innovation* (2016) — Empirical study of why product launches fail commercially and how willingness-to-pay research should precede product development
- Simon-Kucher & Partners: *Global Pricing Study* — Annual practitioner benchmark on pricing model adoption, monetization maturity, and pricing power by industry
