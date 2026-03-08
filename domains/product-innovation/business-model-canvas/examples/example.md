# Business Model Canvas — Example

## Scenario
A mid-market logistics software company is considering launching a new freight visibility product targeting small and medium-sized freight brokers. Leadership has allocated preliminary budget but has not yet confirmed that the model is internally coherent or financially viable. A structured canvas analysis has been commissioned before the investment decision is finalized.

## Inputs
- **Target segment:** Independent freight brokers with annual revenues between $5M and $50M operating in North American truckload markets
- **Proposed value proposition:** Real-time shipment tracking, automated carrier status updates, and exception alerting to reduce broker dispatcher workload and improve shipper satisfaction scores
- **Revenue model hypothesis:** SaaS subscription at $299–$599 per month per broker, tiered by shipment volume
- **Existing capabilities:** Proprietary carrier API integration layer, EDI processing infrastructure, and a 12-person engineering team with logistics domain expertise

## Analysis

1. **Customer Segments:** Independent freight brokers, $5M–$50M revenue band, operating approximately 500–5,000 shipments per month. Excluded from initial scope: enterprise 3PLs (different procurement cycle and integration requirements) and asset-based carriers (different job-to-be-done).

2. **Value Proposition per Segment:** Reduces dispatcher time spent on manual status calls by automating carrier check-calls; provides shippers with self-serve tracking links that reduce inbound status inquiries; surfaces exceptions before delivery failures occur. The primary metric promised: 30–40% reduction in dispatcher time on status management.

3. **Channels:** Direct inside sales for initial 50 accounts; integration partnerships with broker TMS vendors (McLeod, Aljex, Rose Rocket) as distribution channels once product-market fit is established; inbound digital marketing targeting broker operations forums and industry events.

4. **Customer Relationships:** Self-serve onboarding with documentation and video tutorials; shared Slack community for peer support and product feedback; dedicated account management reserved for accounts above 2,000 shipments per month.

5. **Revenue Streams:** Primary: monthly SaaS subscription ($299 Starter / $499 Growth / $599 Pro), billed annually with 15% discount. Secondary (Year 2): per-shipment overage fees above tier limits. No professional services revenue in initial model.

6. **Key Resources:** Carrier API integration library (covering 85% of top 500 carriers); cloud infrastructure on AWS; product and engineering team; broker customer success team (2 FTE at launch).

7. **Key Activities:** Maintaining and expanding carrier API coverage; product development and iteration based on broker feedback; inside sales and broker onboarding; data reliability monitoring to sustain tracking accuracy SLA.

8. **Key Partnerships:** TMS vendors for embedded distribution; major carrier EDI networks for data sourcing; AWS for infrastructure. No dependency on any single partner that would create unacceptable concentration risk at launch.

9. **Cost Structure:** Engineering and product salaries (58% of total cost); AWS infrastructure scaled to shipment volume (12%); sales and marketing (20%); customer success (10%). Fixed cost base is high; unit economics improve materially above 200 paying accounts.

10. **Coherence Assessment:** The model is internally coherent at target scale. Critical risk identified: the inside sales channel is cost-prohibitive below $400 average contract value (ACV). At the $299 entry tier, customer acquisition cost (CAC) through direct sales will likely exceed 12-month payback period. Recommendation: prioritize TMS partnership channel from launch to reduce CAC, or adjust minimum tier to $499 to support direct sales economics.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
