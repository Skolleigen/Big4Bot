# Cash Conversion Cycle

## Domain
Finance & Valuation

## Description
Operational efficiency metric measuring the number of days a business takes to convert inventory investments into cash received from customers. It captures the net time a company's cash is tied up in the operating cycle before it is recovered from sales.

## Purpose
The Cash Conversion Cycle (CCC) reveals how efficiently a company manages its working capital by combining the three levers of inventory, receivables, and payables into a single, comparable metric. A shorter CCC indicates faster cash generation from operations and reduced reliance on external financing, while a lengthening CCC is an early warning of liquidity pressure or operational inefficiency. The framework enables targeted interventions by isolating which component — DIO, DSO, or DPO — is the primary drag on working capital performance.

## When to Use
- Diagnosing working capital inefficiency when a company has adequate profits but insufficient operating cash flow
- Benchmarking operational liquidity management against industry peers or historical trends
- Evaluating the working capital impact of a proposed acquisition, product line change, or customer/supplier contract renegotiation
- Identifying the root cause of a cash flow shortfall during rapid revenue growth

## When NOT to Use
- For businesses with no physical inventory (e.g., pure software or professional services firms) where DIO is not meaningful
- When financial statements are prepared on a cash basis and accrual-based receivables and payables data are unavailable
- When seasonality causes extreme fluctuations in the component metrics such that a single-period CCC is not representative

## Inputs Required
- Average inventory balance for the period
- Cost of goods sold (COGS) for the period
- Average accounts receivable balance for the period
- Average accounts payable balance for the period

## Optional Inputs
- Total revenue for the period (used to cross-check DSO against revenue rather than COGS)
- Peer company CCC data for benchmarking

## Diagnostic Process
1. Calculate Days Inventory Outstanding (DIO): (Average Inventory / Cost of Goods Sold) x 365. This represents the average number of days inventory is held before sale.
2. Calculate Days Sales Outstanding (DSO): (Average Accounts Receivable / Revenue) x 365. This represents the average number of days to collect payment after a sale.
3. Calculate Days Payable Outstanding (DPO): (Average Accounts Payable / Cost of Goods Sold) x 365. This represents the average number of days the company takes to pay its suppliers.
4. Compute the Cash Conversion Cycle: CCC = DIO + DSO - DPO. A positive CCC means cash is deployed before it is recovered; a negative CCC (common in retail) means the company collects cash before paying suppliers.
5. Benchmark the CCC and each component against direct industry peers using public data (S&P Capital IQ, Bloomberg) or industry medians from Damodaran's dataset.
6. Identify the largest driver of CCC by comparing each component's absolute contribution and year-over-year change; flag components that have deteriorated by more than 5 days.
7. Recommend targeted improvement actions specific to the leading driver: inventory reduction programs (DIO), credit policy or collections process improvements (DSO), or supplier payment term extension negotiations (DPO).

## Output
The analysis produces a CCC summary table showing DIO, DSO, DPO, and net CCC for the current period and at least two prior periods, a peer benchmarking comparison, and a root-cause attribution identifying the primary working capital drag. Quantified improvement targets are provided for each lever.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- financial-ratio-analysis
- unit-economics
- dupont-analysis
- scenario-and-sensitivity-analysis

## References
- Verlyn Richards, Eugene Laughlin: *A Cash Conversion Cycle Approach to Liquidity Analysis* (Financial Management, 1980)
- Aswath Damodaran: *Investment Valuation* (3rd ed., 2012) — working capital analysis chapters
