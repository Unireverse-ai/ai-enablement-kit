# Session 04 · Cost and usage

**Length:** 60 minutes · **Format:** around the real usage and billing views · **Led by:** forward-deployed engineer
**For:** executive sponsor, workflow owner, internal builder / admin · **FDE stage:** 05 Operate

## Objective

By the end, the sponsor and owner can read what the workflow costs per unit of work, tell a healthy trend from a problem, and know which levers reduce cost without lowering quality. The builder can find the cause of a spike.

## Prerequisites

- The unit of work is defined in [adoption/metrics.md](../../adoption/metrics.md) and counted.
- Usage data is visible to the team: model usage, workflow runs, hosting and any per-seat charges, each with an owner.
- At least some weeks of operating data exist, or the data from the evaluation period is used and labelled as such.
- A spend limit and an alert owner have been proposed.

## Agenda

| Min | Item | Who | Notes |
|---|---|---|---|
| 0–10 | What costs money in this workflow | Engineer | Model calls, runs, hosting, integration fees, and the people time for review. Show each line on the client's own account. |
| 10–25 | Cost per unit of work, calculated | Engineer, workflow owner | Use the definition in the metrics document. Say what is and is not included. |
| 25–40 | Exercise: find the cause of a spike | Builder, owner | See below. |
| 40–50 | Levers and their trade-offs | Engineer | Shorter inputs, caching, routing simple cases to a smaller model, batching, stopping runs that cannot succeed. Each lever has a quality risk, which is checked with evals under change control. |
| 50–60 | Limits, alerts, and the monthly review; check for understanding | Sponsor | Agree the limit and who is alerted. |

## Exercise

The engineer provides a usage export in which cost per unit rose in one week. Working from the export, the group finds the cause. It may be a change in input length, a rise in retries, a new case type or a change made without a record. They write down: what changed, how it was found, what to do, and what would prevent it.

## Check for understanding

1. Cost per unit rose and the number of units did not. Name three places to look.
2. Someone proposes a cheaper model to cut cost. What must be shown before the change is made?
3. What does the spend alert do, and who answers it?
4. When would the sponsor decide to pause the workflow on cost grounds, in terms of the metrics?

## Materials

Usage and billing views · metrics definitions · spike export for the exercise · limits and alert template.
