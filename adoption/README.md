# Adoption

Adoption is what happens after handover: whether the team keeps using the workflow, whether it stays healthy, and whether it earns the next one. A workflow that is delivered and then ignored has not been adopted. A workflow that is used but quietly overridden has not been adopted either.

Three documents:

| Document | Use |
|---|---|
| [metrics.md](metrics.md) | The adoption and health metrics: exact definitions, denominators, sources and review cadence |
| [90-day-plan.md](90-day-plan.md) | Template for the first 90 days after handover, with checkpoints at day 0, 30, 60 and 90, owners and decisions |
| [champions.md](champions.md) | The internal champion model: how the champion is chosen, what they do, and how ownership moves from us to them |

## How they fit together

1. The metrics are agreed in stage 02 and measured from stage 04 onwards, so the baseline and the evaluation period use the same definitions the team will keep using.
2. The 90-day plan starts at handover, the first activity of stage 05. It sets who reviews which metric, when, and what decision follows from each reading.
3. The champion runs the plan. Our engineers hand it over at day 0 and step back in stages, as the plan sets out.
4. At day 90 the team has the operating metrics, the re-assessed [readiness](../readiness/README.md) and a recommendation for the next workflow. Results scope the next workflow in the same way the first one was scoped.

## Principles

- **Counts come from systems, not memory.** Every metric names its data source. If a metric cannot be measured from a record, we say so and use a stated sampling method.
- **Separate use from quality.** High use of a poor workflow is a problem; low use of a good one is also a problem. We read the metrics in pairs.
- **A metric has an owner and a decision.** If no one will act on a reading, we do not collect it.
- **Thresholds come from the client.** We set the definitions and the review cadence. The client's workflow owner sets the thresholds before the first reading, with the sponsor's agreement.
