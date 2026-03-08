# Service Blueprinting — Example

## Scenario
A UK telecommunications provider's residential broadband installation service has a 31% first-visit failure rate — an engineer arrives at the customer premises but cannot complete the installation and must reschedule. Industry benchmark for broadband installation first-visit completion is below 8%. Each failed visit costs approximately £185 in engineer time and rescheduling overhead, and generates a net promoter score of −42 among affected customers. A service blueprinting exercise is commissioned to identify the backstage root causes of the first-visit failure pattern.

## Inputs
- **Service scope:** Residential broadband installation — from order confirmation to successful broadband activation at the customer premises
- **Customer segment:** New residential broadband customers ordering standard FTTC (fibre to the cabinet) installation
- **Service stages:** 8 stages from order processing to post-installation support handoff
- **Internal roles:** Order management team, network provisioning team, scheduling team, field engineer, customer service representative
- **Supporting systems:** CRM (order management), network infrastructure database, field workforce management system, engineer mobile app
- **Failure data:** 31% first-visit failure rate from the past 12 months; failure reason codes available from engineer job completion logs

## Analysis

**Step 1 — Service scope definition:**
Service scope confirmed: residential FTTC broadband installation from order confirmation email to broadband speed test completion and successful handoff to post-installation support. Eight stages are defined: (1) Order confirmation and processing; (2) Network infrastructure validation; (3) Appointment scheduling; (4) Pre-appointment preparation; (5) Engineer dispatch and travel; (6) On-site installation; (7) Speed test and quality confirmation; (8) Handoff to customer service and welcome call. The scope boundary excludes the pre-sale and ordering process (handled separately) and post-installation fault resolution.

**Step 2 — Customer actions mapped:**
Customer actions are mapped across all 8 stages: receiving order confirmation, selecting an installation appointment slot, receiving appointment reminder communications, being present at the premises during the appointment window, granting engineer access to the property, observing the installation process, confirming broadband connectivity at the end, and receiving the welcome call from customer service. Customer actions are relatively simple and not identified as a source of failure in the engineer job logs.

**Step 3 — Frontstage employee actions mapped:**
The customer service representative's frontstage actions include sending the order confirmation, communicating the appointment window and sending the 48-hour reminder. The field engineer's frontstage actions include arriving at the premises, introducing themselves to the customer, conducting the installation, running the speed test and handing off. No structural fail points are identified in the frontstage layer itself — the frontstage interactions are generally well-executed according to customer satisfaction data on the completed installations.

**Step 4 — Backstage employee actions mapped:**
Backstage actions are mapped across the 8 stages for the order management team, network provisioning team and scheduling team. Critical backstage finding at Stage 2: network infrastructure validation is performed by the provisioning team at the time of order, but the validation checks only current infrastructure availability, not scheduled infrastructure works that may affect cabinet capacity between order date and installation date. Critical backstage finding at Stage 3: appointment scheduling assigns engineer skill categories based on the order type (standard FTTC), but does not check whether the specific engineer assigned has completed the certification update required for installations using the new ONT hardware model (deployed in 34% of installations since March). Critical backstage finding at Stage 4: the pre-appointment preparation step does not include an equipment check confirming that the engineer's van kit includes the correct cable type for the specific property connection distance — this check relies entirely on engineer judgment from a job note field that is frequently incomplete.

**Step 5 — Support processes and systems mapped:**
The supporting systems layer reveals three structural gaps. First: the CRM and the network infrastructure database are not integrated — the provisioning team performs infrastructure validation by running a manual query in the network database after receiving the CRM order notification, creating a 24–48 hour lag and no automated re-check if infrastructure status changes between order and installation date. Second: the field workforce management system assigns engineers by skill category but does not hold the ONT certification status field — this data exists in the HR system but is not accessible in the scheduling workflow, making it impossible to route ONT installations to certified engineers automatically. Third: the engineer mobile app displays job notes but does not generate an equipment checklist based on the specific job parameters (property distance, connection type, hardware model) — the checklist is a static template that does not vary by job.

**Step 6 — Fail point identification:**
Three primary fail points are identified: (a) Infrastructure readiness fail point at Stage 2/3 boundary — infrastructure validation is not re-checked before appointment confirmation, and scheduled infrastructure works after order creation are not visible to the scheduling team, resulting in engineers arriving at premises where the cabinet infrastructure is not ready (engineer job log reason code "infrastructure not ready": 14% of all failed visits); (b) Engineer skill-job mismatch fail point at Stage 3 — ONT installations are being assigned to engineers without ONT certification because certification status is not accessible in the scheduling system (engineer job log reason code "incorrect engineer skill": 9% of all failed visits); (c) Equipment kit fail point at Stage 4/5 — engineers arrive without the correct cable length or hardware variant for the specific installation because the pre-appointment equipment check is not job-specific (engineer job log reason code "missing or incorrect equipment": 8% of all failed visits). Together these three root causes account for 31% of first-visit failures — covering the entire observed failure rate.

**Step 7 — Prioritization and improvement design:**
Improvements are prioritized by combined customer impact and implementation feasibility. Highest priority (implement within 60 days): integrate network infrastructure database status feed into the CRM scheduling workflow to enable automated infrastructure re-check 48 hours before each appointment — addresses 14% first-visit failure rate, estimated implementation cost £85K. Medium priority (implement within 90 days): expose ONT certification field from HR system in the field workforce management scheduling view and add a routing rule that flags ONT jobs for certified engineers only — addresses 9% first-visit failure rate, estimated implementation cost £22K. Medium priority (implement within 90 days): redesign the engineer mobile app job note to generate a dynamic equipment checklist based on job parameters (distance, hardware model, connection type) — addresses 8% first-visit failure rate, estimated implementation cost £38K. Combined target: reduce first-visit failure rate from 31% to below 8%, saving approximately £2.1M annually in failed-visit costs at current installation volumes.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
