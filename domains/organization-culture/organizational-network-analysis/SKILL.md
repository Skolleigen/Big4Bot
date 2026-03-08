# Organizational Network Analysis

## Domain
Organization & Culture

## Description
Data-driven method for mapping informal communication and collaboration networks within organizations to identify key influencers, silos, bottlenecks, and at-risk knowledge nodes. It makes the invisible informal organization visible by translating relationship and communication patterns into a directed network graph with quantified centrality metrics.

## Purpose
Formal organization charts describe who reports to whom but reveal nothing about how work actually gets done, where information flows, or who the true organizational connectors are. ONA addresses this gap by mapping the informal networks through which knowledge, decisions, and energy actually travel. Leaders use ONA findings to redesign collaboration structures, identify and protect critical knowledge nodes before they depart, break down organizational silos, and target change management interventions at the individuals with the highest informal influence.

## When to Use
- The organization suspects knowledge silos between teams, functions, or geographies but lacks data to confirm their location or severity
- A critical employee departure has raised concern about knowledge concentration and the organization wants to identify other at-risk nodes before they become crises
- A post-merger integration requires understanding how well the two legacy organizations are developing informal connections beyond the formal integration structure
- A change management initiative needs to identify informal influencers who can serve as change champions with genuine peer credibility

## When NOT to Use
- The organization cannot guarantee respondent anonymity and data confidentiality — without trust, survey responses will be distorted and the network map will be inaccurate
- The target population is fewer than 30 people, where network density is naturally high and ONA adds limited insight beyond direct observation
- The primary question is about formal authority or accountability rather than informal influence — use RACI/DACI frameworks for role clarity questions
- Leadership intends to use ONA data punitively to identify underperformers based on low network centrality — this misuse damages trust and is methodologically invalid

## Inputs Required
- Network survey responses: structured questions asking each respondent who they go to for (a) advice or expertise, (b) information or project updates, and (c) energy or motivation when facing challenges
- Complete roster of the target population so that non-respondents can be identified and follow-up conducted to maximize coverage
- Organizational segmentation data: function, team, level, location, and tenure for each node in the network
- Minimum response rate of 70% to produce a sufficiently complete network map for reliable centrality calculations

## Optional Inputs
- Communication metadata from collaboration platforms (email volume, Slack message patterns, meeting attendance) to triangulate with survey-based network data
- Prior ONA results for the same population to track network changes over time following an intervention
- Formal organizational chart for comparison between the official reporting structure and the informal network map

## Diagnostic Process
1. Define the ONA scope and target population by specifying which organizational unit or cross-functional population will be mapped, the specific network questions to be asked (advice, information, energy), and the time reference frame for relationship reporting (typically "in the past 3 months").
2. Administer the network survey using a roster-based design where each respondent selects their relationships from a complete list of all population members; avoid open-text name entry which produces incomplete and inconsistent responses; guarantee anonymity for all non-directional aggregated outputs and explain the specific data use protocol to respondents.
3. Build a directed network graph from the survey responses, representing each person as a node and each reported relationship as a directed edge; weight edges by relationship type (advice, information, energy) and calculate network density, reciprocity rates, and response completeness before proceeding to analysis.
4. Calculate centrality metrics for each node: degree centrality (number of direct connections, distinguishing in-degree from out-degree), betweenness centrality (frequency with which a node lies on the shortest path between other pairs of nodes, identifying brokers), and closeness centrality (average distance to all other nodes, identifying well-connected hubs); flag nodes in the top decile of betweenness centrality as critical brokers.
5. Identify key structural findings: (a) critical brokers — high betweenness centrality nodes who are the primary connectors between clusters; (b) peripheral nodes — individuals isolated from the core network who may be at flight risk or who lack access to information and relationships needed for effectiveness; (c) isolated clusters — subsets of the network with few connections to the broader organization, representing knowledge silos or collaboration barriers.
6. Assess the alignment between the formal organizational chart and the informal network structure, identifying cases where formal authority is not matched by informal influence, where critical knowledge flows bypass formal reporting lines, and where the formal structure creates unintended bottlenecks in the informal network.
7. Recommend structural interventions targeting the identified network pathologies: for overloaded brokers, design role redistributions or deputy structures to reduce concentration risk; for silos, create cross-cluster collaboration mechanisms (cross-functional teams, shared OKRs, communities of practice); for peripheral nodes, design onboarding or mentoring interventions to increase network integration; and for at-risk departures, initiate knowledge transfer programs and succession planning for critical nodes.

## Output
The skill produces a network visualization report showing the directed network graph with nodes colored by organizational unit and sized by betweenness centrality, a centrality metrics table identifying the top 10 brokers and the 10 most peripheral nodes, a silo analysis quantifying the density of ties within versus between organizational clusters, and a prioritized set of structural recommendations targeting network pathologies. When delivered alongside formal ONA platform data, it includes a longitudinal change analysis.

## Output Schema

See `output_schema.json` in this directory for the full structured schema.

The schema defines the framework-specific analytical output produced by this skill.


## Related Skills
- change-management
- raci-daci-governance
- culture-workshops
- 360-feedback

## References
- Rob Cross & Andrew Parker: *The Hidden Power of Social Networks* (2004)
- IBM: Social Business and Organizational Network Analysis Methodology
- Rob Cross, Stephen Borgatti & Andrew Parker: *Making Invisible Work Visible*, MIT Sloan Management Review (2002)
