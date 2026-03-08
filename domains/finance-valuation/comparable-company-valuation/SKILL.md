# Comparable Company Valuation

## Domain
Finance & Valuation

## Description
Relative valuation method that estimates a company's value by benchmarking it against publicly traded peers using market multiples such as EV/EBITDA, P/E, and EV/Revenue. It derives an implied valuation range by applying peer median or selected multiples to the subject company's financial metrics.

## Purpose
Comparable company analysis (also called "trading comps") provides a market-grounded valuation anchor that reflects the price rational investors are currently paying for similar businesses in the same sector. It is the primary sanity check against intrinsic valuation methods such as DCF and serves as the standard valuation reference in M&A, IPO, and fairness opinion contexts. The framework also reveals how a company's operating profile compares to its peers on key financial dimensions, informing strategic positioning and investor communication.

## When to Use
- Valuing a private company for M&A, capital raise, or fairness opinion purposes where a market-based reference is required
- Providing a market sanity check on a DCF or LBO valuation output
- Benchmarking an existing public company's trading multiples against its peer set to assess relative value
- Supporting an IPO pricing process by establishing the market-implied valuation range

## When NOT to Use
- When no meaningful set of publicly traded comparable companies exists (highly unique business models or markets)
- When the subject company is in financial distress and market multiples are distorted or negative
- When public market conditions are severely dislocated (e.g., broad market crash) and multiples do not reflect normalized valuations

## Inputs Required
- Identified peer set of publicly traded comparable companies (minimum 5 peers)
- Current market capitalization, net debt, and enterprise value for each peer
- LTM (last twelve months) and forward financial metrics for each peer: revenue, EBITDA, EBIT, net income
- Subject company's corresponding LTM and forward financial metrics

## Optional Inputs
- Growth rates and margins for each peer (to support multiple regression or quartile selection)
- Transaction comps data for cross-reference against trading comps

## Diagnostic Process
1. Define the peer universe by selecting publicly traded companies that share the subject company's industry, business model, end markets, size range, and geographic exposure; document inclusion and exclusion criteria.
2. Collect financial data for each peer from public filings or financial databases: market cap, net debt, minority interest, cash, revenue, EBITDA, EBIT, and net income on both LTM and forward-year bases.
3. Calculate key trading multiples for each peer: EV/LTM Revenue, EV/Forward Revenue, EV/LTM EBITDA, EV/Forward EBITDA, P/LTM Earnings, P/Forward Earnings.
4. Screen for outliers by removing companies with negative EBITDA, recent M&A distortions, or non-recurring items that make multiples non-representative; adjust for stock-based compensation and lease capitalization where material.
5. Calculate median, mean, 25th percentile, and 75th percentile for each multiple across the cleaned peer set; use the interquartile range as the primary selection band.
6. Apply the selected multiple range to the subject company's corresponding financial metric to derive an implied enterprise value range; convert to equity value by subtracting net debt and adding cash.
7. Triangulate the implied valuation range from multiple metrics (EV/EBITDA and EV/Revenue at minimum) to produce a football field chart showing the consolidated range and central estimate.

## Output
The analysis produces a peer benchmarking table showing all multiples for each comparable company, summary statistics, the implied valuation range under each multiple, and a consolidated football field chart. Key assumptions and peer selection rationale are documented alongside the output.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- dcf-valuation
- financial-ratio-analysis
- dupont-analysis
- scenario-and-sensitivity-analysis

## References
- Aswath Damodaran: *Investment Valuation* (3rd ed., 2012)
- Tim Koller, Marc Goedhart, David Wessels (McKinsey & Company): *Valuation: Measuring and Managing the Value of Companies* (7th ed., 2020)
