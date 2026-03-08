# The Reasoning Graph

The Big4Bot Reasoning Graph (`registry/dependencies.yaml`) encodes the conceptual relationships between the 46 individual consulting skills. It establishes explicit pathways that allow agents to transition logically between domains—for instance, navigating from an analysis of product viability (`unit-economics`) into an actionable operational response (`product-discovery`).

## A Map, Not a Prison

The most critical operational principle to remember when building agents with Big4Bot is that **the graph is a map, not a prison.**

Traditional software workflow engines are brittle because they strictly mandate step A, then step B, then step C. However, consulting reasoning is rarely a clean, deterministic line. It regularly requires pivoting, backtracking, or jumping to conclusions based on incomplete data.

The dependency graph dictates what steps *should* logically follow, it never forces an underlying AI agent to block user execution.

## Defining Triggers

The Reasoning Layer is powered by **Triggers**. A Trigger represents an explicit, directed edge mapping an upstream capability to a downstream need.

```yaml
  dcf-valuation:
    triggers:
      - skill: ma-due-diligence
        relevance: high
      - skill: comparable-company-valuation
        relevance: high
```

## Relevance Levels

To aid an LLM in narrowing down its suggestions to a user during a Guided Analysis, each Trigger is annotated with a contextual `relevance` rating:

- **`high`:** A standard, natural continuation of the engagement (e.g., A completed DCF Valuation strongly suggests proceeding into Due Diligence).
- **`medium`:** A situational continuation, ideal for exploring newly uncovered organizational vulnerabilities.
- **`low`:** An optional edge, commonly used to represent a long-tail feedback path (e.g., a failing operational metric recommending an investigation all the way back up to core product viability mapping).
