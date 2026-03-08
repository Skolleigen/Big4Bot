# Control Mapping — Example

## Scenario
ClearPath Health Technologies is a 280-person healthcare technology company providing a cloud-based patient engagement platform to 340 hospital systems. The company is preparing for its first SOC 2 Type II audit, which covers the 12-month period from January through December. An internal readiness assessment identified concerns about three areas: access provisioning and deprovisioning, data encryption practices, and backup and recovery verification. The CISO has engaged a consulting team to map existing controls against the AICPA Trust Service Criteria and identify gaps requiring remediation before the Type II observation period begins.

## Inputs
- **Scope:** SOC 2 Type II covering Security (CC), Availability (A), and Confidentiality (C) trust service criteria — 47 applicable risks identified in scoping workshop
- **Existing control inventory:** 38 controls documented across IT security, infrastructure, HR/onboarding, vendor management, and incident response domains
- **Gap hypothesis:** Three high-priority gaps flagged by internal readiness review — access review process (manual and infrequent), encryption at rest enforcement (policy exists but not technically enforced on all storage tiers), backup verification (manual spot-check only, no automated testing)
- **Audit window:** Type II observation period starts in 90 days

## Analysis

**Step 1 — Trust service criteria risk universe compilation:**
Forty-seven risks mapped to the applicable trust service criteria. Security (CC series): 29 risks covering logical access, change management, risk assessment, monitoring, and incident response. Availability (A series): 10 risks covering capacity management, backup/recovery, and environmental controls. Confidentiality (C series): 8 risks covering data classification, encryption, and data retention/disposal. Risk universe validated against AICPA SOC 2 criteria and ClearPath's customer contract commitments (SLA, data processing agreements).

**Step 2 — Existing control inventory:**
Thirty-eight controls inventoried from policy documents, system configurations, and process documentation. Controls categorized: preventive (22), detective (12), corrective (4). Domains covered: identity and access management (8 controls), change management (5 controls), network security (6 controls), vulnerability management (3 controls), incident response (4 controls), HR security (4 controls), backup and recovery (4 controls), vendor management (4 controls).

**Step 3 — Control-to-risk mapping:**
Each of the 38 controls mapped to the 47 risks it addresses. Mapping approach: one control may address multiple risks; one risk should be covered by at least one control. Results: 44 of 47 risks have at least one mapped control (94% coverage at mapping stage). Three risks remain unmapped: (1) CC6.2 — no automated quarterly access review process (manual reviews occur annually, not quarterly as required by criteria); (2) C1.1 — encryption at rest not technically enforced on legacy PostgreSQL database tier (policy references encryption but enforcement is inconsistent); (3) A1.2 — backup recovery not tested via automated restore verification (manual spot-check occurred once in the prior 12 months, not sufficient for Type II evidence).

**Step 4 — Design adequacy assessment:**
Each of the 38 existing controls assessed for design adequacy: does the control, if operating as designed, address the risk it is mapped to? Result: 35 of 38 controls assessed as adequately designed (92%). Three controls assessed as inadequately designed: (1) IAM-07 (access review) — designed as an annual manual review; SOC 2 CC6.2 requires a process to periodically review access rights; annual cadence and manual execution create design gaps for a Type II period. (2) ENC-03 (encryption at rest) — policy states all data at rest must be encrypted; technical control exists for AWS S3 and RDS but not for the legacy PostgreSQL instance holding 22% of PHI records. (3) BCR-02 (backup verification) — control is designed as a manual spot-check; no automated restore testing cadence defined.

**Step 5 — Operating effectiveness assessment:**
Twenty-eight of the 35 adequately-designed controls assessed as operating effectively (80% operating effectiveness). Seven controls operating inconsistently: change management approval (CM-03): 4 of 47 changes in the past 6 months lacked documented approval; vendor security review (VM-01): 2 of 8 new vendors onboarded without completed security assessment questionnaire; vulnerability remediation SLA (VM-02): 3 critical vulnerabilities exceeded the 30-day remediation SLA. Operating effectiveness gaps documented with evidence (pull of change records, vendor onboarding log, vulnerability tracker).

**Step 6 — Gap remediation design:**
Three new controls designed for the unmapped risks, with owners and implementation timelines: (1) IAM-39 (Quarterly Access Review Automation): implement automated access certification in Okta Workflows; quarterly review triggers sent to resource owners with automated escalation after 5 days; Owner: IT Security; Target: 60 days. (2) ENC-12 (PostgreSQL Encryption Enforcement): enable Transparent Data Encryption on legacy PostgreSQL instance and document encryption coverage for all storage tiers; Owner: Infrastructure Engineering; Target: 30 days. (3) BCR-11 (Automated Backup Restore Testing): configure weekly automated restore test for critical databases with pass/fail alerting to the on-call team; document monthly restore test results in the evidence repository; Owner: SRE Team; Target: 45 days. Seven operating effectiveness gaps remediated through process corrections (change approval enforcement, vendor questionnaire gate in onboarding workflow, vulnerability SLA tracking dashboard).

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
