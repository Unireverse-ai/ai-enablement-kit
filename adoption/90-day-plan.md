# 90-day plan · Template

**Use:** agree this plan at the end of stage 04, before go-live. Day 0 is the day ownership of the workflow's operating routine passes to the client's champion. Replace every `⟦...⟧` field. Dates are set by the workflow owner and sponsor; checkpoints do not slip without a recorded reason.

Workflow: ⟦name⟧ · Day 0: ⟦date⟧ · Sponsor: ⟦name⟧ · Workflow owner: ⟦name⟧ · Champion: ⟦name⟧ and deputy ⟦name⟧ · Lead engineer: ⟦name⟧ · Revision: ⟦record⟧.

## Roles through the 90 days

| Period | Who runs the routine | What our engineers do |
|---|---|---|
| Days 0–30 | Champion, with engineers alongside | Join the weekly review, answer questions, make changes with the internal builder watching |
| Days 31–60 | Champion; internal builder makes changes | Review change records, attend the monthly review, available for incidents |
| Days 61–90 | Champion and workflow owner | Join the day 90 review; no routine involvement unless called |

The scope of continued support after day 90 is a separate decision at the day 90 checkpoint.

## Checkpoint: day 0, handover

| Item | Owner | Evidence | Done |
|---|---|---|---|
| Handover pack received: runbook, quick reference, eval cases and last accepted result, access list, change log | Lead engineer | Pack index | ⟦date⟧ |
| Five roles signed off, or open items listed with owners | Workflow owner | [Sign-off record](../enablement/roles.md#sign-off-record) | ⟦date⟧ |
| [Metrics](metrics.md): definitions, thresholds and baseline recorded | Champion | Filled-in metrics document | ⟦date⟧ |
| [Acceptable-use](../governance/acceptable-use.md) policy issued to the team | IT & security | Issue record | ⟦date⟧ |
| [Change-control](../governance/change-control.md) route live; first approvers named | Workflow owner | Route in use | ⟦date⟧ |
| Spend limit and alert owner set | Sponsor | Billing setting | ⟦date⟧ |
| Review meetings in calendars: weekly, monthly, day 30/60/90 | Champion | Calendar entries | ⟦date⟧ |

**Decision at day 0 (sponsor):** accept handover, or accept with listed open items and dates. ⟦decision and date⟧.

## Checkpoint: day 30

Question: is the workflow being used as intended, and does the team trust it?

| Review | Owner | Input |
|---|---|---|
| Active use, coverage, bypass | Champion | Weekly readings for four weeks |
| Override rate and audit sample result, read together | Workflow owner | Weekly and first monthly readings |
| Review turnaround and backlog | Champion | Weekly readings |
| Failed run rate and unresolved failures | Internal builder | Run log |
| Incidents and pauses | IT & security | Incident and pause records |
| Corrections that look like a pattern | Workflow owner | Corrections log; candidates for a rule change |

**Decision at day 30 (workflow owner, sponsor informed):** continue as is, change something (raise a change request), or pause. Record the reading that drove it. ⟦decision and date⟧.

## Checkpoint: day 60

Question: can the team change the workflow safely, and is cost where we expected?

| Review | Owner | Input |
|---|---|---|
| Changes made: how many, through change control, with evals attached | Workflow owner | Change log compared with live configuration |
| Internal builder practice task completed | Lead engineer | [Sign-off](../enablement/roles.md#internal-builder--admin) |
| Cost per unit of work against the limit | Sponsor, workflow owner | Monthly cost reading; [session 04](../enablement/session-plans/04-cost-and-usage.md) method |
| Trend in override and exception rates after any changes | Workflow owner | Weekly readings before and after each change |
| Training needs: new joiners, leavers, gaps | Champion | Role list vs current staff |

**Decision at day 60 (sponsor):** confirm the internal builder owns changes alone, or extend supervised changes by ⟦period⟧. Record the reading that drove it. ⟦decision and date⟧.

## Checkpoint: day 90

Question: is the workflow part of how the team works, and what comes next?

| Review | Owner | Input |
|---|---|---|
| Full metrics review against thresholds | Sponsor, workflow owner | Three months of readings |
| [Readiness](../readiness/README.md) re-assessed, using the same questionnaire | Workflow owner, lead engineer | Report compared with the stage 01 report |
| Open items from day 0 sign-off | Workflow owner | Sign-off record |
| Risks and recurring incidents | IT & security | Incident record |
| Next workflow: what the results suggest, and what the lowest readiness dimensions require first | Sponsor | Roadmap from stage 02, updated |

**Decision at day 90 (sponsor):** one of
- continue to operate as is, with ⟦support arrangement⟧;
- narrow or change the workflow's scope;
- retire it, recording why;
- start the next workflow, with its scope drawn from these results.

⟦decision, owner and date⟧.

## Weekly and monthly routine between checkpoints

| Meeting | Who | Length | Agenda |
|---|---|---|---|
| Weekly check | Champion, operators | ⟦short⟧ | Use, backlog, turnaround, override, anything odd |
| Monthly review | Workflow owner, champion, internal builder, IT & security; sponsor as needed | ⟦agreed⟧ | Full metrics, audit sample, cost, change log, incidents |

## Escalation

Any of these brings the sponsor in at once, outside the schedule: a consequential error that reached a client or a record of external effect; a data problem; spend at the limit; the champion or internal builder leaving without a deputy in place.
