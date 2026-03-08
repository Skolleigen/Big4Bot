# Shared Standards

The `shared/` directory establishes the global governance and data interoperability layer for the entire Big4Bot library. While consulting frameworks are diverse, they must share a common language to be accurately chained and evaluated.

## 1. Evaluation Rubrics
Located in `shared/evaluation/rubric.md`, this document provides a universal standard for assessing LLM-generated consulting outputs.

The rubric evaluates four critical dimensions:
1. **Schema Conformance:** (Pass/Fail) Does the JSON match the `output_schema.json`?
2. **Methodological Adherence:** (1-5) Did the agent follow the step-by-step diagnostic in `SKILL.md`?
3. **Data Integration:** (1-5) Are the provided inputs deeply woven into the analysis?
4. **Analytical Depth:** (1-5) Does the output reach professional consulting-tier insights?

## 2. Base Schema Envelope
Located in `shared/schemas/base_envelope.json`, this schema defines the mandatory wrapper for all analytical outputs. It ensures that every framework execution provides consistent metadata, such as:
- `skill_id`
- `confidence_score` (1-100)
- `assumptions_made`
- `data_limitations`
- `suggested_next_steps`

## 3. Industry Taxonomies
Located in `shared/taxonomies/`, these are centralized JSON files that provide standardized classifications for data entries.
- **`industry_sectors.json`:** Provides a canonical list of industry categories (e.g., Financial Services, Healthcare, Technology).

By using shared taxonomies, analytical results from one skill (e.g., Market Segmentation) can be used as structured inputs for another (e.g., DCF Valuation) without manual data mapping.

## 4. Academic References
Located in `shared/references/`, this area contains global methodological anchors and citations that support the entire repository's commitment to professional consulting standards.
