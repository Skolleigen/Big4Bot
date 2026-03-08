# M&A Due Diligence

## Domain
Finance & Valuation

## Description
Structured due diligence framework for Mergers and Acquisitions (M&A). This skill evaluates the strategic, commercial, operational, and financial rationale for a transaction. It translates theoretical valuation models (like DCF or comparables) into practical diligence priorities to confirm synergy assumptions, uncover deal-breakers, and inform negotiation strategy.

## Purpose
Valuation models indicate what a target might be worth under specific assumptions, but due diligence determines whether those assumptions are valid and achievable. This framework bridges the gap between financial modeling and deal execution by systematically testing the target's standalone commercial viability, operational health, and the acquirer's ability to integrate and realize projected synergies.

## When to Use
- An acquirer has identified a target and signed a Letter of Intent (LOI) to proceed with formal diligence.
- A private equity firm is evaluating the commercial and operational thesis of a platform acquisition.
- Strategic finance teams need to stress-test the revenue and cost synergy assumptions built into a preliminary DCF model.
- Preparing for sell-side diligence to pre-emptively identify weaknesses a buyer might use to negotiate down the purchase price.

## When NOT to Use
- For purely legal or regulatory compliance checks (this is a strategic/financial consulting diagnostic, not legal counsel).
- Very early-stage target screening where basic strategic fit hasn't yet been established.
- Post-merger integration (PMI) execution (this framework assesses the *deal thesis*, not the post-close operational project plan).

## Inputs Required
- Articulation of the core strategic deal thesis (why the acquirer wants to buy this target).
- Key valuation assumptions driving the initial offer (e.g., revenue growth rates, expected cost synergies, multiple expansion).
- Preliminary financial and commercial information provided by the target (confidential information memorandum, initial data room extracts).

## Optional Inputs
- Findings from upstream valuation frameworks (`dcf-valuation`, `comparable-company-valuation`).
- Target's management presentations and business plan forecasts.
- Known red flags or initial concerns raised by the deal team.

## Diagnostic Process
1. **Commercial & Strategic Diligence:** Evaluate the target's market position, competitive advantage, customer concentration, and top-line growth sustainability. Validate the core strategic rationale for the deal (e.g., geographic expansion, product adjacency, technological acquisition).
2. **Financial Diligence (Quality of Earnings):** Beyond statutory audits, assess the underlying normalized EBITDA. Identify one-off adjustments, run-rate anomalies, working capital requirements, and off-balance-sheet liabilities.
3. **Operational Diligence:** Assess the target's operating model, supply chain resilience, IT infrastructure scalability, and capital expenditure needs to maintain current growth.
4. **Synergy Validation:** Rigorously test the acquirer's revenue synergy assumptions (cross-selling, pricing power) and cost synergy assumptions (headcount rationalization, procurement scale, facility consolidation). Assign probability weightings to each synergy pool.
5. **Integration Risk Assessment:** Identify cultural mismatches, key personnel retention risks, and operational complexities that could delay or destroy value during post-merger integration.
6. **Deal-Breaker & Valuation Impact Synthesis:** Aggregate red flags and synergy shortfalls to recommend specific adjustments to the purchase price, deal structure (e.g., earn-outs), or advise walking away from the transaction.

## Output
The analysis produces a prioritized diligence readout highlighting validated value drivers, quantified risks to the valuation model, synergy achievability scores, and concrete recommendations for deal negotiation and integration planning.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.

## Related Skills
- dcf-valuation
- comparable-company-valuation
- scenario-and-sensitivity-analysis
- strategic-initiative-mapping

## References
- McKinsey & Company / Various Authors: *Valuation: Measuring and Managing the Value of Companies* — Connects valuation theory directly to M&A due diligence and synergy realization.
- Harding, D., & Rovit, S. (2004). *Mastering the Merger: Four Critical Decisions That Make or Break the Deal*. Harvard Business Review Press — Canonical text on focusing diligence on the deal thesis and integration realities rather than just basic financial audits.
