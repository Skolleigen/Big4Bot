# Break-Even Analysis

## Domain
Finance & Valuation

## Description
Financial calculation that determines the sales volume at which total revenues equal total costs, producing neither profit nor loss. It establishes the minimum output required for a business or product line to become self-sustaining.

## Purpose
Break-even analysis provides management with a clear threshold for operational viability, informing pricing decisions, cost structure trade-offs, and go/no-go investment choices. It quantifies the margin of safety between current or projected sales and the break-even point, making downside risk explicit. The framework also underpins target profit modeling, showing exactly what volume is required to achieve a specified return.

## When to Use
- Evaluating the viability of a new product, service line, or market entry before capital commitment
- Assessing the impact of a proposed price change, discount policy, or cost reduction initiative
- Determining minimum sales targets for budgeting, incentive-setting, or lender covenant compliance
- Stress-testing a business plan or financial model prior to board approval or fundraising

## When NOT to Use
- When cost structure is highly dynamic and cannot be reliably separated into fixed and variable components
- When the product mix is complex and multiple products share joint fixed costs without a defensible allocation method
- When the business operates under non-linear pricing or volume-tiered cost contracts that violate constant contribution margin assumptions

## Inputs Required
- Total fixed costs per period (rent, salaries, depreciation, SG&A overheads)
- Variable cost per unit (materials, direct labor, commissions, shipping)
- Selling price per unit or average revenue per unit
- Projection period (monthly, quarterly, or annual basis)

## Optional Inputs
- Target profit or EBITDA for target-profit break-even extension
- Current or projected sales volume (to calculate margin of safety)

## Diagnostic Process
1. Identify and categorize all costs as fixed or variable for the period; flag any semi-variable costs and split them using the high-low method or regression analysis if sufficient historical data is available.
2. Confirm the selling price per unit and ensure it reflects realized revenue net of returns, allowances, and volume rebates that reduce average selling price.
3. Calculate the contribution margin per unit: Selling Price per Unit minus Variable Cost per Unit.
4. Calculate the contribution margin ratio: Contribution Margin per Unit divided by Selling Price per Unit, expressed as a percentage.
5. Calculate the break-even volume: Total Fixed Costs divided by Contribution Margin per Unit (round up to the nearest whole unit).
6. Calculate the break-even revenue: Total Fixed Costs divided by the Contribution Margin Ratio, or equivalently Break-Even Volume multiplied by Selling Price per Unit.
7. Calculate margin of safety as projected volume minus break-even volume, and model target profit volume as (Fixed Costs plus Target Profit) divided by Contribution Margin per Unit.

## Output
The analysis delivers a break-even unit volume, break-even revenue figure, margin of safety, and target profit volume, supported by a cost-volume-profit table and, where appropriate, a chart showing the intersection of total cost and total revenue lines. Each output is accompanied by the key assumptions and flagged sensitivities.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- unit-economics
- scenario-and-sensitivity-analysis
- financial-ratio-analysis
- pricing-and-packaging-strategy

## References
- Charles T. Horngren, Srikant Datar, Madhav Rajan: *Cost Accounting: A Managerial Emphasis* (16th ed.)
- Ray Garrison, Eric Noreen, Peter Brewer: *Managerial Accounting* (16th ed.)
