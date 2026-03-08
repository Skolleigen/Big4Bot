# DCF Valuation

## Domain
Finance & Valuation

## Description
Intrinsic valuation methodology that estimates a company's value by discounting projected future free cash flows back to their present value using a risk-adjusted discount rate. It is the foundational framework for determining what a business is worth based on its underlying earnings power rather than market sentiment.

## Purpose
DCF valuation forces a disciplined, explicit articulation of every assumption driving business value — revenue growth, margins, capital intensity, and cost of capital — making the key value drivers transparent and auditable. It provides an intrinsic value estimate independent of current market pricing, which is essential in M&A negotiations, capital allocation decisions, and investment analysis. The sensitivity of DCF outputs to WACC and terminal growth rate assumptions also structures the risk dialogue with stakeholders by making valuation uncertainty quantifiable.

## When to Use
- Valuing a company for acquisition, divestiture, or strategic investment where intrinsic value must be established
- Supplementing a comparable company analysis with an intrinsic perspective when market multiples may be distorted
- Evaluating capital allocation decisions such as major capex programs, share buybacks, or strategic investments
- Supporting fairness opinion or impairment testing analyses requiring present value calculations

## When NOT to Use
- For early-stage companies with no meaningful operating history and highly speculative cash flow projections where forecast reliability is very low
- When the business has highly irregular or non-recurring cash flows that cannot be normalized into a projection period
- When real options embedded in the business (e.g., exploration rights, patents) account for a dominant share of value and require option pricing methods

## Inputs Required
- Historical income statements, balance sheets, and cash flow statements (minimum 3 years)
- Revenue growth assumptions for the explicit projection period (typically 5-10 years)
- Operating margin and tax rate assumptions for the projection period
- Capital expenditure and depreciation/amortization forecasts
- Working capital change assumptions
- Weighted Average Cost of Capital (WACC) or discount rate
- Terminal growth rate or exit multiple for terminal value calculation
- Current net debt position (debt minus cash) to bridge from enterprise value to equity value

## Optional Inputs
- Segment-level revenue and margin projections (for multi-segment businesses)
- Management guidance or analyst consensus forecasts as cross-checks on projection assumptions

## Diagnostic Process
1. Build a revenue forecast for the explicit projection period (5-10 years) grounded in historical growth rates, market sizing, competitive positioning, and any available management guidance or analyst consensus.
2. Project operating margins (EBIT margin or NOPAT margin) based on historical trend, operating leverage, and identified cost improvement or headwind drivers; apply the effective tax rate to derive NOPAT.
3. Calculate unlevered free cash flow to the firm (FCFF) each year: NOPAT plus Depreciation and Amortization minus Capital Expenditures minus Change in Net Working Capital.
4. Estimate the terminal value using the Gordon Growth Model (FCFF in terminal year / (WACC - terminal growth rate)) or an exit multiple (terminal year EBITDA multiplied by selected EV/EBITDA multiple); terminal value typically represents 60-80% of total enterprise value and must be stress-tested.
5. Calculate WACC: weighted average of after-tax cost of debt (using current market rate and the subject's effective tax rate) and cost of equity (using CAPM: risk-free rate plus beta-adjusted equity risk premium), weighted by target capital structure.
6. Discount all projected FCFFs and the terminal value to present value using WACC; sum to derive enterprise value.
7. Perform a two-variable sensitivity analysis on WACC (plus/minus 100 bps) and terminal growth rate (plus/minus 50 bps) to produce a sensitivity table showing the implied equity value range, and reconcile the central estimate against comparable company valuation output.

## Output
The analysis produces a 10-column projection model, terminal value calculation, WACC build-up, enterprise and equity value summary, and a sensitivity matrix. The output is typically presented as a football field chart alongside the comparable company valuation range.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- comparable-company-valuation
- scenario-and-sensitivity-analysis
- financial-ratio-analysis
- dupont-analysis
- ma-due-diligence

## References
- Aswath Damodaran: *Investment Valuation* (3rd ed., 2012)
- Tim Koller, Marc Goedhart, David Wessels (McKinsey & Company): *Valuation: Measuring and Managing the Value of Companies* (7th ed., 2020)
- Richard Brealey, Stewart Myers, Franklin Allen: *Principles of Corporate Finance* (13th ed.)
