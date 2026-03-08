# Scrum Framework — Example

## Scenario
A 400-person logistics company's IT team is transitioning a 9-person delivery team from a waterfall project model to Scrum for the rebuild of a customer-facing shipment tracking portal. The existing portal was built 6 years ago and has a 34% customer satisfaction score. The project has a 9-month total budget window. The team has no prior Scrum experience; a Scrum Master has been designated (an internal agile coach) and a Product Owner has been assigned from the commercial team.

## Inputs
- **Product vision:** A real-time shipment tracking portal that gives business customers full visibility of their consignment status, reducing inbound tracking calls to the customer service team by 60%
- **Initial product backlog:** 67 User Stories created during a product discovery workshop, estimated total effort approximately 580 story points
- **Team composition:** Product Owner (Commercial team lead), Scrum Master (internal agile coach), 7 development team members (4 developers, 2 QA engineers, 1 UX designer)
- **Sprint cadence:** 2-week sprints confirmed; first sprint start date set 10 days after Scrum adoption decision

## Analysis

**Step 1 — Product backlog creation:**
The Product Owner prioritizes the 67 User Stories from the product discovery workshop. The top-priority items are the core tracking status view, real-time ETA calculation, push notification for delivery events and the customer authentication flow — these four epics are estimated to represent 60% of end-user value. The backlog is organized into five priority tiers. Twenty-two stories in the bottom two tiers are marked as candidates for de-scoping if velocity requires trade-offs.

**Step 2 — Backlog refinement and estimation:**
A 3-hour refinement session is held before Sprint 1. The top 25 stories are refined to the level of clear acceptance criteria. Story points are assigned using planning poker. The team estimates average sprint velocity at 30–35 points for Sprint 1 given the team's Scrum inexperience and onboarding overhead; experienced Scrum practitioners benchmark first-sprint velocity as typically 60–70% of stabilized velocity.

**Step 3 — Sprint 1 Planning:**
Sprint 1 goal: "Deliver a working authentication flow and a basic shipment status view for internal testing." Eight stories totaling 32 story points are selected for Sprint 1. Each story is decomposed into development tasks on the sprint backlog. The team confirms the Definition of Done: code reviewed, unit tests passing, QA sign-off, deployed to staging environment.

**Step 4 — Sprint 1 execution:**
Daily standups surface two impediments in Week 1: the development environment provisioning is incomplete (resolved by Scrum Master in Day 3 by escalating to IT infrastructure), and the UX designer is unclear on brand guidelines for the new portal (resolved by Product Owner connecting the designer with the brand team on Day 4). Six of eight stories are completed by sprint end. Two stories are returned to the backlog: the real-time ETA calculation story was found to require an API integration with the logistics engine that needs a separate technical discovery spike.

**Step 5 — Sprint 1 Review:**
Sprint Review is attended by 7 stakeholders including the Head of Customer Experience and the Customer Service Manager. The working authentication flow and status view are demonstrated. Stakeholder feedback generates 4 new User Stories: a bulk tracking view for customers managing multiple shipments (high priority, added to top of backlog), a CSV export feature (medium priority), an accessibility compliance requirement (added as non-functional requirement affecting all subsequent stories), and a mobile-responsive breakpoint requirement (added as Definition of Done criterion). Sprint 1 velocity: 28 story points (6 of 8 stories accepted).

**Step 6 — Sprint 1 Retrospective:**
What went well: daily standups caught blockers early; the sprint goal provided clear focus; the staging deployment process worked. What did not: the API dependency in the ETA calculation story was not identified during planning (a discovery spike protocol is needed for stories with external system dependencies); the UX designer was not involved in the initial story estimation, causing an underestimate of design effort. One improvement committed for Sprint 2: any story involving a new external system integration must be preceded by a 1-point discovery spike on the sprint before it is committed.

**Step 7 — Subsequent sprint progression:**
By Sprint 3, the discovery spike protocol and improved UX estimation are in place. Sprint velocity increases: Sprint 2: 36 points, Sprint 3: 42 points, Sprint 4: 48 points. By Sprint 6, velocity stabilizes at 54 story points with 85% sprint goal achievement. At Sprint 6, 387 of the 580 estimated story points are complete, placing the project on track for an 11-sprint delivery of the full scope within the 9-month budget window. Stakeholder satisfaction with delivery transparency, measured in a Sprint 6 survey, improves from a 3.1 pre-Scrum baseline to 4.4 out of 5.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
