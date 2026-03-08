# OKR Design — Example

## Scenario
A 200-person Series C fintech company providing embedded lending infrastructure has completed its annual strategy review and identified three priorities for the coming year: accelerate enterprise client acquisition, achieve operational scalability through platform automation, and build the regulatory compliance capability required to enter two new US state markets. The CPO and CEO have asked the strategy team to design the OKR architecture for the full company and the three most critical teams.

## Inputs
- **Organizational mission and strategy:** Enable any platform to offer embedded lending in days, not months; strategic priorities are enterprise growth, platform scalability, and regulatory expansion
- **Current performance baseline:** 14 enterprise clients (target: 30 by year-end); average API integration time 18 days (target: under 5 days); licensed in 12 states (target: 14 by Q3); platform uptime 99.2% (target: 99.9%); engineering deployment frequency 2x per week (target: daily)
- **Resource constraints:** Engineering headcount capped at 85 for the year; compliance team at 4 FTEs with budget to add 2; sales team has capacity for approximately 40 qualified enterprise opportunities per quarter
- **Committed initiatives:** API v2 rewrite (Q1–Q2), state licensing applications for Texas and Florida (Q1), enterprise sales team expansion by 3 account executives (Q1)

## Analysis

### Step 1 — Confirm Strategic Priorities
Three confirmed priorities for the OKR period: (1) enterprise client growth, (2) platform scalability and reliability, (3) regulatory market expansion. All OKRs must trace to one of these three.

### Step 2 — Set Company-Level Objectives
- **O1:** Become the enterprise embedded lending platform of choice for mid-market and enterprise fintech platforms
- **O2:** Deliver a platform experience that sets the industry standard for integration speed and reliability
- **O3:** Establish the regulatory foundation for national market coverage

### Step 3 — Define Company-Level Key Results

**O1 — Enterprise Growth:**
- KR1.1: Increase enterprise client count from 14 to 30 by December 31
- KR1.2: Achieve net revenue retention of 120% across existing enterprise accounts
- KR1.3: Reduce average sales cycle from 67 days to 40 days

**O2 — Platform Scalability:**
- KR2.1: Reduce median API integration time from 18 days to 5 days
- KR2.2: Achieve platform uptime of 99.9% measured over each quarter
- KR2.3: Increase engineering deployment frequency from 2x/week to daily

**O3 — Regulatory Expansion:**
- KR3.1: Obtain full lending licenses in Texas and Florida by September 30
- KR3.2: Establish compliance monitoring infrastructure covering all 14 target states by Q4

### Step 4 — Cascade to Teams

**Sales Team OKRs (contributes to O1):**
- Objective: Build and convert the highest-quality enterprise pipeline in company history
- KR: Generate 40 qualified enterprise opportunities per quarter (160 annual)
- KR: Convert 19% of qualified pipeline to closed-won (from current 14%)
- KR: Reduce average contract value discount from 18% to 10% through value-based selling

**Engineering Team OKRs (contributes to O2):**
- Objective: Eliminate integration friction and achieve carrier-grade platform reliability
- KR: Ship API v2 with full documentation and sandbox environment by March 31
- KR: Reduce mean time to resolution for P1 incidents from 4.2 hours to 1 hour
- KR: Achieve 80% test coverage across core lending workflow modules by June 30

**Compliance Team OKRs (contributes to O3):**
- Objective: Build the regulatory infrastructure that enables national expansion
- KR: Submit complete license applications for Texas and Florida by January 31
- KR: Complete examination readiness review for all 12 existing state licenses by June 30
- KR: Implement automated compliance monitoring covering BSA/AML, TILA, and state-specific requirements by Q3

### Step 5 — Identify Dependencies
- Sales KR (pipeline volume) depends on Engineering delivering API v2 sandbox by March 31 — without the sandbox, enterprise prospects cannot complete technical due diligence
- Compliance KR (Texas and Florida licenses) depends on Engineering providing platform architecture documentation for regulator review by January 15
- Engineering uptime KR requires Operations to provision additional redundancy infrastructure — a shared ownership item requiring explicit SLA

### Step 6 — Establish Review Cadence
- Weekly: Team-level key result check-ins (owners update progress scores)
- Monthly: Cross-functional dependency review with CPO and CTO
- Quarterly: Company-level OKR review with executive team and board observer
- Annual: Full cycle retrospective and next-cycle OKR design

### Step 7 — End-of-Cycle Scoring Convention
Key results scored 0.0–1.0; 0.7 is the expected attainment for stretch OKRs. Scores below 0.4 require written retrospective. Scores of 1.0 on all key results indicate targets were set too conservatively and require recalibration next cycle.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
