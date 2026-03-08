# Product Discovery — Example

## Scenario
A B2B fintech company offers an accounts payable automation platform for mid-market manufacturing firms. Despite adding three new features in the past two quarters, the monthly active user rate for the core approval workflow module has declined 18% over six months. Engineering is ready to build a mobile approvals interface based on an internal assumption that approvers want to take action from their phones. The product team has been asked to conduct discovery before committing the 6-week development sprint.

## Inputs
- **Problem opportunity statement:** Investigate why approval workflow engagement has declined 18% among the target segment of accounts payable managers and financial controllers at manufacturing firms with 100–500 employees, and determine whether a mobile interface addresses the root cause
- **Target user segment:** Accounts payable managers (primary users) and financial controllers (approvers) at manufacturing clients; firms with 100–500 employees; 3+ months on the platform
- **Available data:** Product analytics from 340 active manufacturing clients; 6 months of session logs; 112 support tickets tagged to the approval workflow; churn records for 23 clients who did not renew in Q3
- **User access:** 14 user interviews scheduled across 8 clients; 2 on-site observation sessions arranged with clients in the Midwest manufacturing corridor

## Analysis

1. **Frame the problem opportunity:** The opportunity statement is "Understand why accounts payable managers and financial controllers at mid-market manufacturing firms are reducing their use of the approval workflow module, and determine whether the proposed mobile interface addresses the actual barrier or a secondary symptom." The framing explicitly holds the mobile interface hypothesis open rather than treating it as confirmed.

2. **Conduct user interviews:** Interviewed 14 users across 8 client companies: 9 AP managers and 5 financial controllers. Key behavioral finding: approvers are not failing to approve due to device constraints. 11 of 14 interviewees reported that the primary friction is invoice exception handling — when an invoice requires a coding correction or a PO mismatch resolution, the approval workflow drops the approver into a separate legacy module that requires re-entry of data already visible in the main interface. Controllers described abandoning the digital workflow and returning to email approval for any invoice flagged as an exception, which takes more total time but feels more controllable.

3. **Analyze existing behavioral data:** Queried session logs for approval workflow drop-off points. 67% of incomplete approval sessions end at the point where the system surfaces an exception flag, consistent with the interview finding. Mobile session data shows only 8% of approvals are initiated on mobile devices, directly contradicting the internal hypothesis that mobile friction is a primary driver of engagement decline. Support tickets tagged to "approval workflow" contain the phrase "exception" or "coding" in 74 of 112 cases (66%).

4. **Generate solution hypotheses:** Based on interview synthesis and data analysis, three solution hypotheses were formulated: (a) "Embedding exception resolution directly in the approval workflow — without redirecting to a separate module — will reduce workflow abandonment by eliminating the context switch that drives approvers back to email." (b) "Providing approvers with a 'Request Correction' action that notifies the AP manager without exiting the approval interface will reduce exception-related abandonment." (c) "A mobile interface will not materially improve engagement because the primary barrier is workflow interruption, not device availability."

5. **Prototype and test solution concepts:** Built a clickable wireframe prototype embedding exception coding directly in the approval view (hypothesis a) and a second prototype adding a "Request Correction" notification button without context switching (hypothesis b). Tested with 8 users across 3 client sessions. In 7 of 8 cases, users completed the approval workflow on the embedded exception prototype without exiting to email. The "Request Correction" button was understood immediately and rated as "how it should have always worked" by 4 of 5 AP managers who tested it.

6. **Synthesize insights into validated requirements:** Validated requirements: (1) Exception coding must be completable within the approval view without navigating to a separate module. (2) Approvers must be able to flag an invoice for AP manager correction from within the approval interface without exiting the workflow. (3) The system must display the original PO and vendor details alongside the exception flag to support in-context decision-making. Mobile interface: not validated as a priority requirement; defer to future discovery cycle with usage evidence.

7. **Prioritize requirements:** Requirement 1 (in-context exception coding) is the highest priority: it addresses 67% of abandonment events and directly reverses the engagement decline. Requirement 2 (Request Correction button) is high priority: low development complexity and addresses the remaining exception-related abandonments where the AP manager must make the correction. Requirement 3 (contextual PO display) is a dependency of requirement 1 rather than a standalone item. Mobile interface is deprioritized pending evidence that it addresses a real usage pattern.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
