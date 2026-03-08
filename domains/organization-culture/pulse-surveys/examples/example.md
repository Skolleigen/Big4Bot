# Pulse Surveys — Example

## Scenario
A 1,200-person retail chain operating 48 stores and 3 distribution centers has been running biweekly pulse surveys for 8 months. In Q3, the company announces a restructuring that eliminates one management layer across all distribution centers, affecting 12 distribution center team leaders who are redeployed rather than made redundant. The following two pulse cycles show the most significant engagement score drops in the program's history. The People Analytics team is asked to diagnose the drop and recommend a targeted intervention.

## Inputs
- **Organization:** 1,200-person retail chain; 48 stores, 3 distribution centers, corporate HQ
- **Pulse survey cadence:** Biweekly, rotating 50% sample; full population cycle monthly
- **Survey dimensions:** Overall engagement (1 question), manager support (2 questions), role clarity (2 questions), belonging (1 question), well-being (2 questions), recognition (1 question), voice (1 question)
- **Pre-restructuring engagement score (distribution centers):** 72 / 100
- **Post-restructuring engagement score (distribution centers, cycle 1):** 63 / 100 (-9 points)
- **Post-restructuring engagement score (distribution centers, cycle 2):** 58 / 100 (-14 points from baseline)
- **Comparison:** Retail store engagement over same period: 71 to 69 (-2 points, within normal variation range)
- **Sharpest dimension declines:** Manager support (-18 points), role clarity (-16 points)

## Analysis

**Step 1 — Measurement dimension review:**
The existing 10-question instrument covers all 6 dimensions required for the diagnostic. No changes are made to the instrument to preserve trend comparability. The open-text question for the two post-restructuring cycles asks: "Is there anything specific that has changed about your experience at work recently?" This produces 147 open-text responses from distribution center employees across the two cycles — a 61% open-text response rate, significantly above the 30% baseline, indicating high motivation to share views.

**Step 2 — Instrument design confirmation:**
The 10-question instrument with a consistent 5-point Likert scale (1 = strongly disagree to 5 = strongly agree) has been in use for 8 months and produces reliable trend data. The biweekly rotating sample produces 85–90 distribution center respondents per cycle (from a total DC population of 178), meeting the threshold for analysis. All 12 distribution center team locations have at least 9 respondents in each cycle, exceeding the 5-response anonymity threshold for manager-level reporting.

**Step 3 — Frequency and sampling confirmation:**
The biweekly rotating 50% sample is appropriate for detecting rapid engagement changes post-restructuring. The full monthly cycle (100% population) in cycle 2 provides the comprehensive data needed for the investigation. Response rate in distribution centers: 91% in cycle 1 post-restructuring and 88% in cycle 2 — elevated above the 74% baseline, consistent with high engagement motivation during a period of uncertainty.

**Step 4 — Survey administration and anonymity:**
All cycles adhere to the 5-response manager reporting threshold. Manager-level reports are available for all 12 distribution center team leaders and all 3 distribution center general managers. The anonymity protocol communication was repeated at the start of cycle 1 post-restructuring given the sensitivity of the restructuring context.

**Step 5 — Trend analysis and flagging:**
Overall distribution center engagement drops from 72 to 63 (-9 points) in cycle 1 — flagged automatically by the platform as exceeding the 5-point threshold for management attention. In cycle 2, the score drops to 58 (-14 points from baseline, -5 points from cycle 1) — triggering the escalation protocol to the CPO. Dimension-level analysis: manager support drops from 74 to 56 (-18 points), the largest single-dimension decline in the program's 8-month history. Role clarity drops from 71 to 55 (-16 points). Belonging drops from 69 to 63 (-6 points). Well-being drops from 70 to 66 (-4 points). Recognition and voice show minimal change (-2 points each). The concentration of the decline in manager support and role clarity is the key diagnostic signal — it points specifically to leadership behavior and role confusion post-restructuring rather than a general sentiment collapse.

**Step 6 — Manager-level and leadership-level reporting:**
Manager-level reports reveal the decline is not uniform across all 12 distribution center locations. Three locations (Distribution Centers A, B, and C) account for 68% of the total score decline despite representing 52% of the distribution center workforce. Within these three locations, the manager support score averages 47/100 — 22 points below the DC average and 27 points below the pre-restructuring baseline. The three general managers at these locations are identified for targeted coaching and support. Open-text theme analysis from 147 responses produces 5 themes: "I don't know who my manager is now" (38% of responses), "My new manager doesn't know my role" (29%), "No one has explained the new structure to us" (24%), "I'm worried about what's next" (19%), "The workload has increased but no one has acknowledged it" (14%). The manager support and role clarity drivers are confirmed qualitatively.

**Step 7 — Closed-loop communication:**
Within 10 days of cycle 2 results, the VP of Operations records a 5-minute video message for all distribution center employees acknowledging the specific findings ("We heard that role clarity and manager support have declined significantly since the restructuring"), describing the three actions being taken, and thanking employees for their honesty. The three actions communicated: (1) All 12 distribution center team leaders will have 1:1 conversations with each team member within 2 weeks to clarify the new reporting structure and role expectations. (2) The 3 general managers at the most-affected locations will receive coaching support from the HR business partners over the next 60 days. (3) A dedicated Q&A session will be held at each distribution center within 2 weeks where employees can ask any questions about the restructuring.

## Output

### Structured Output

The expected structured output format for this framework is defined in `output_schema.json` in this directory.

The example below focuses on the analytical reasoning process. Agents should generate outputs that conform to the formal schema specification.
