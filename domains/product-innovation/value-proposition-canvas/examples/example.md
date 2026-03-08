# Value Proposition Canvas — Example

## Scenario
A legal technology company is preparing to launch a document automation product targeting in-house legal teams at mid-size companies ($100M–$1B revenue). Internal product development has been underway for 8 months and the team believes the product is nearly ready for market. However, early pilot feedback has been lukewarm and conversion from trial to paid has been 12%, well below the 30% target. A value proposition canvas analysis has been commissioned to diagnose the alignment gap before a broader go-to-market launch.

## Inputs
- **Target customer segment:** In-house legal counsel and legal operations managers at companies with $100M–$1B revenue, managing 50–500 contracts per year with teams of 2–8 legal staff
- **Customer research available:** 9 user interviews conducted during pilot; NPS survey from 34 pilot users (NPS: +8); 47 support tickets from the pilot period; conversion funnel data showing 88% trial abandonment
- **Product inventory:** Contract template library (400+ templates), guided interview-based document assembly, e-signature integration, basic clause library, and a contract repository with search

## Analysis

1. **Define target customer segment:** In-house legal generalists and legal operations managers at mid-market companies; 2–8 person legal teams; responsible for commercial contracts, NDAs, employment agreements, and vendor agreements; operating without outside counsel support for routine matters; budget authority for tools under $50,000 annually.

2. **Map customer jobs:**
   - Functional jobs: Draft and review standard commercial contracts quickly; ensure contract language is legally defensible without outside counsel review; track contract status and renewal dates; onboard new contract templates when business needs change; maintain a searchable repository of executed agreements.
   - Social jobs: Demonstrate to business stakeholders that legal is an enabler, not a bottleneck; show that the legal team is managing risk proactively without requiring expensive outside counsel for routine work.
   - Emotional jobs: Feel confident that routine contracts are handled correctly without personal legal liability exposure; reduce the anxiety of managing a high volume of routine agreements with a small team.

3. **Document customer pains (ranked by severity):**
   - Critical: Standard contracts drafted from scratch or from uncontrolled Word file versions produce inconsistent language; errors reach execution stage and are discovered post-signature.
   - Critical: No visibility into contract renewal and expiration dates; teams miss renewal windows and auto-renewal clauses trigger unintended commitments.
   - High: Routing contracts for internal business approvals is managed through email chains, with no status visibility or audit trail.
   - High: Onboarding the tool requires IT involvement for SSO and integration with existing systems, creating a deployment delay that causes pilot abandonment.
   - Medium: The template library does not cover industry-specific clause variations (e.g., SaaS-specific data processing terms, geographic-specific data protection language).

4. **Document customer gains (ranked by relevance):**
   - Essential: Any standard NDA or commercial agreement can be generated in under 10 minutes without requiring legal staff to start from scratch.
   - Essential: Executed contracts are searchable and renewal dates are surfaced proactively, eliminating missed deadlines.
   - Expected: Business stakeholders can see the status of their contract requests without emailing legal for updates.
   - Desired: Clause-level fallback options allow legal to offer business teams acceptable alternatives during negotiation without escalating every redline.
   - Surprise: The tool learns from the team's past agreements to suggest clause preferences aligned with how the company has historically negotiated.

5. **Map product features and services:** Contract template library (400+ templates); guided document assembly interview; e-signature integration (DocuSign, Adobe Sign); basic clause library with no fallback logic; contract repository with keyword search; no renewal alerting; no approval routing; SSO requires IT configuration; no industry-specific template variants.

6. **Identify pain relievers:**
   - The template library addresses the version control and consistency pain for teams that use templates as their starting point — but only if the templates match the team's jurisdiction and industry (currently unverified).
   - Guided document assembly reduces drafting time for standard agreements.
   - The repository with keyword search partially addresses discoverability of executed agreements.
   - Pain NOT relieved: Renewal and expiration tracking (no alerting feature); approval routing (no workflow); IT-dependent SSO deployment (the deployment friction that is driving pilot abandonment per support tickets).

7. **Identify gain creators:**
   - Template-based assembly creates the essential gain of sub-10-minute standard agreement generation for the covered template types.
   - E-signature integration creates the expected gain of a tracked execution process.
   - Gain NOT created: Proactive renewal date surfacing (no alerting); business-visible contract status (no approval routing); clause-level fallback options during negotiation (clause library has no fallback logic); learned clause preferences (not built).

8. **Assess fit:** Strong fit areas: standard contract generation speed and repository search. Fit gaps: renewal alerting (essential gain, not addressed); approval routing (expected gain and high-severity pain, not addressed); IT-dependent deployment (the highest-frequency pain in pilot support tickets, directly causing trial abandonment); industry-specific clause variants (medium pain, partially limiting template utility). The 12% trial-to-paid conversion rate is explained primarily by the deployment friction and missing renewal alerting — the two gaps most frequently cited in pilot interviews.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
