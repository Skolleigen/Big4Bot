# Market Segmentation — Example

## Scenario
A B2B SaaS company offering project management software has grown to $12M ARR primarily through self-serve acquisition but is experiencing slowing growth. Leadership wants to launch a direct sales motion and needs to identify which customer segments to target first. The company has 1,400 paying accounts ranging from individual freelancers to 200-person professional services firms, but has never formally segmented its customer base.

## Inputs
- **Total Addressable Market:** B2B project management software, North American market, companies with 10-500 employees
- **Customer Data:** 1,400 accounts with firmographic attributes (company size, industry, geography), ARR per account, product usage data (features used, seats, login frequency), and support ticket history
- **Revenue Data:** ARR by account; top 100 accounts represent 62% of total ARR
- **Funnel Data:** Trial-to-paid conversion rate by acquisition source and company size band

## Analysis

**Step 1 — Define TAM Boundary.**
The analysis scope is set to North American companies with 10-500 employees that manage project-based work. Individual freelancers (fewer than 3 seats) and enterprise accounts (500+ employees) are excluded: the former have insufficient contract value to support a direct sales motion, and the latter require enterprise features not yet available in the product. This bounds the addressable population to approximately 280 accounts in the current base and a broader market of an estimated 180,000 companies in North America.

**Step 2 — Collect Segmentation Variables.**
Customer data is assembled across four variable classes. Firmographic: industry vertical (extracted from LinkedIn company data), employee count, and geography. Behavioral: monthly active users per account, number of features used (breadth of adoption), average session length, and support ticket frequency. Financial: ARR, ARR growth rate over 12 months, and gross margin (estimated from infrastructure cost per seat). Psychographic proxies are derived from onboarding survey responses collected at signup.

**Step 3 — Apply Segmentation Criteria.**
An initial segmentation is run using two primary variables: industry vertical and company size band (10-49, 50-149, 150-500 employees). This produces 15 candidate segments. A secondary behavioral pass collapses segments with statistically similar product usage patterns. The resulting five candidate segments are: (A) Small creative agencies (10-49 employees), (B) Mid-size marketing agencies (50-149 employees), (C) Small professional services firms (10-49), (D) Mid-size professional services firms (50-149), (E) Technology product companies (50-500 employees).

**Step 4 — Evaluate Segment Attractiveness.**
Each segment is scored on size, growth, profitability, and accessibility.

| Segment | Accounts in Base | Avg ARR | Gross Margin | 12M Growth | Accessibility |
|---|---|---|---|---|---|
| A: Small creative agencies | 310 | $4,200 | 74% | +8% | High (self-serve) |
| B: Mid-size marketing agencies | 180 | $11,400 | 76% | +22% | Medium |
| C: Small professional services | 390 | $3,800 | 71% | +4% | High (self-serve) |
| D: Mid-size professional services | 210 | $14,600 | 78% | +31% | Medium |
| E: Technology product companies | 110 | $22,800 | 81% | +38% | Low (long sales cycle) |

**Step 5 — Select Target Segments.**
Segments D and B are selected as the primary targets for the direct sales motion. Segment D (mid-size professional services) has the highest ARR per account, highest gross margin, and strongest growth rate among existing customers. Segment B (mid-size marketing agencies) is selected as the secondary target given its growth trajectory and medium accessibility. Segment E (technology companies) is designated as a future motion once enterprise features are available. Segments A and C are assigned to a self-serve optimization track rather than a direct sales investment.

**Step 6 — Profile Target Segments.**
Segment D (Mid-size Professional Services, 50-149 employees): Typical buyer is a VP of Operations or Chief of Staff. Primary pain point is project profitability tracking across multiple concurrent client engagements. Key buying criteria are resource utilization reporting, time tracking integration, and client-facing project status views. Average evaluation cycle is 45-60 days with three to five stakeholders involved. Current NPS in this segment is 54.

Segment B (Mid-size Marketing Agencies, 50-149 employees): Typical buyer is a Director of Operations or Agency Principal. Primary pain point is campaign workflow management across multiple clients and freelancers. Key buying criteria are creative asset management, client approval workflows, and integration with design tools. Average evaluation cycle is 30-45 days. Current NPS is 48.

**Step 7 — Validate Segment Distinctiveness.**
A chi-squared test on feature usage patterns confirms that segments D and B have significantly different adoption profiles (p < 0.01): professional services accounts use time tracking and resource planning features at 3.4x the rate of marketing agency accounts, while marketing agencies use the asset library and approval workflow features at 2.8x the rate of professional services accounts. The segments are internally homogeneous and externally heterogeneous, confirming validity.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
