# Break-Even Analysis — Example

## Scenario
A SaaS company is evaluating whether to launch a new $49/month subscription tier targeting small business customers. The product team estimates monthly fixed costs of $120,000 (engineering, customer support, and infrastructure overhead) and a variable cost of $8 per customer per month (hosting, payment processing, and third-party API fees). With 1,800 current subscribers on a legacy tier, management wants to determine how many new-tier subscribers are needed before the product line becomes profitable.

## Inputs
- **Price per unit:** $49/month per subscriber
- **Variable cost per unit:** $8/month per subscriber
- **Total fixed costs:** $120,000/month (engineering, support, infrastructure)
- **Current subscriber base:** 1,800 subscribers
- **Target analysis horizon:** 12 months

## Analysis

**Step 1 — Contribution Margin Calculation:**
The contribution margin per subscriber is $49 − $8 = $41/month. Each additional subscriber contributes $41 toward covering fixed costs before the tier generates profit. The contribution margin ratio is $41 / $49 = 83.7%, indicating a highly scalable cost structure typical of SaaS businesses where marginal delivery costs are low relative to the subscription price.

**Step 2 — Break-Even Volume:**
Break-even subscribers = $120,000 / $41 = 2,927 subscribers (rounded up). The tier must reach 2,927 paying subscribers to cover its fixed cost base. At the current base of 1,800 subscribers, the tier is operating at a $46,300/month deficit ($120,000 − 1,800 × $41). The gap to break-even is 1,127 additional subscribers.

**Step 3 — Break-Even Revenue:**
Break-even monthly revenue = 2,927 × $49 = $143,423/month, or approximately $1.72M annualized. Equivalently, fixed costs / contribution margin ratio = $120,000 / 0.837 = $143,369/month (minor rounding difference). This revenue target anchors the commercial plan.

**Step 4 — Time-to-Break-Even Sensitivity:**
Assuming a net new subscriber rate of 150/month (conservative) to 400/month (aggressive), time to break-even from the current 1,800-subscriber base ranges from approximately 2.8 months (1,127 / 400) to 7.5 months (1,127 / 150). A moderate scenario of 220 net new subscribers/month implies break-even in approximately 5.1 months.

**Step 5 — Margin of Safety Assessment:**
At 1,800 subscribers, the tier is 61.5% of the way to break-even (1,800 / 2,927). Once break-even is achieved, each additional subscriber adds $41 directly to operating profit. At 3,500 subscribers, monthly operating profit would be (3,500 − 2,927) × $41 = $23,493/month ($281,916 annualized). Management should treat 3,000 subscribers as the minimum viable scale threshold before committing additional fixed-cost investments.

**Step 6 — Sensitivity to Key Variables:**
If variable costs increase to $12/month (e.g., due to API repricing), the contribution margin falls to $37 and break-even rises to 3,244 subscribers (+317 from baseline). If price is discounted to $39/month for a promotional period, the contribution margin falls to $31 and break-even rises to 3,871 subscribers, a 32% increase in required volume. Price changes have the most significant impact on break-even volume given the current cost structure, making price discipline critical.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
