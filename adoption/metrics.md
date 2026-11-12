# Adoption and health metrics · Template

**Use:** agree definitions, sources and thresholds before the first reading. Replace every `⟦...⟧` field. The definitions are ours; the thresholds are the client's, set by the workflow owner with the sponsor's agreement and recorded in the table.

Workflow: ⟦name⟧ · Unit of work: ⟦for example: one eligible incoming enquiry⟧ · Eligible: ⟦inclusion rule⟧ · Excluded: ⟦exclusion rule and why⟧ · Plan revision/date: ⟦record⟧.

Metrics owner: ⟦role/name⟧ · Workflow owner: ⟦role/name⟧ · Sponsor: ⟦role/name⟧.

## Definitions

Count in one period, for example a calendar week. Use the same period for numerator and denominator. State any rounding. Report absolute counts next to every percentage.

### Use

| Metric | Definition | Denominator | Data source | Cadence | Reviewed by |
|---|---|---|---|---|---|
| Active use | Operators and reviewers who completed at least one unit of work through the workflow in the period | Operators and reviewers with access in the period | ⟦workflow log or system audit trail⟧ | Weekly | Champion |
| Coverage | Eligible units that entered the workflow | All eligible units in the period | ⟦system of record, filtered by the eligibility rule⟧ | Weekly | Workflow owner |
| Bypass | Eligible units handled outside the workflow, found by a manual route when a workflow route existed | All eligible units in the period | ⟦system of record, tagged by route⟧ | Monthly | Workflow owner |

### Quality and trust

| Metric | Definition | Denominator | Data source | Cadence | Reviewed by |
|---|---|---|---|---|---|
| Override rate | Reviewed outputs where the reviewer changed the AI output before accepting, or rejected it | Reviewed outputs in the period | ⟦review record: accept/correct/reject⟧ | Weekly | Workflow owner |
| Exception rate | Units routed to a person as outside what the workflow handles, including escalations | Units entering the workflow in the period | ⟦exception queue or route flag⟧ | Weekly | Workflow owner |
| Consequential error | Outputs found wrong after acceptance, and that caused rework, a wrong action or a client-visible problem | Accepted outputs in the period | ⟦incident records, downstream corrections, sampled audit⟧ | Monthly | Workflow owner and sponsor |
| Audit sample result | Correct outputs in a random sample of accepted outputs, as judged by someone who did not review them | Sample size in the period | ⟦audit sheet⟧ | Monthly | Workflow owner |

Read override rate and audit sample result together. A falling override rate with a falling audit result suggests reviewers are accepting without checking.

### Speed

| Metric | Definition | Denominator | Data source | Cadence | Reviewed by |
|---|---|---|---|---|---|
| Review turnaround | Elapsed time from output ready for review to review completed. Report the median and the slowest decile; state whether business hours or calendar time | Reviewed outputs in the period | ⟦timestamps in the review queue⟧ | Weekly | Champion |
| Time to completion | Elapsed time from unit entering the workflow to done | Completed units in the period | ⟦timestamps⟧ | Monthly | Workflow owner |
| Backlog | Outputs waiting for review at the end of the period | Not a rate; report the count and the age of the oldest | ⟦review queue⟧ | Weekly | Champion |

### Reliability

| Metric | Definition | Denominator | Data source | Cadence | Reviewed by |
|---|---|---|---|---|---|
| Failed run rate | Runs that ended in an error or unknown state | Runs started in the period | ⟦run log⟧ | Weekly | Internal builder |
| Unresolved failures | Failed runs not reconciled within ⟦agreed time⟧ | Failed runs in the period | ⟦run log and reconciliation record⟧ | Weekly | Internal builder |
| Pauses | Times the workflow was paused, with reason | Not a rate; list each | ⟦pause record⟧ | Monthly | Workflow owner |

### Cost

| Metric | Definition | Denominator | Data source | Cadence | Reviewed by |
|---|---|---|---|---|---|
| Cost per unit of work | Model, automation, hosting and integration charges for the period divided by units completed. State whether paid review time is included, and keep that choice fixed | Completed units in the period | ⟦billing and usage exports; unit count from the system of record⟧ | Monthly | Sponsor and workflow owner |
| Retry share | Model calls repeated after a failure or a rejected output | All model calls in the period | ⟦usage export⟧ | Monthly | Internal builder |
| Spend against limit | Spend to date in the period | The spend limit for the period | ⟦billing view⟧ | Weekly, with an automatic alert | Alert owner |

### Capability

| Metric | Definition | Denominator | Data source | Cadence | Reviewed by |
|---|---|---|---|---|---|
| Changes through change control | Changes to prompts, rules, models or integrations with a complete record | All changes found in the period, by comparing the live configuration with the change records | ⟦change log, configuration history⟧ | Monthly | Workflow owner |
| Signed-off roles | Roles with a current [sign-off](../enablement/roles.md) | Roles in the plan | ⟦sign-off record⟧ | Quarterly | Champion |

## Thresholds and decisions

Set before the first reading. A threshold needs an owner and a decision.

| Metric | Reading that triggers a review | Decision it leads to | Decision owner |
|---|---|---|---|
| Override rate | ⟦level or movement⟧ | ⟦investigate pattern, change rule, pause⟧ | ⟦role⟧ |
| Audit sample result | ⟦level⟧ | ⟦retrain reviewers, tighten review, pause⟧ | ⟦role⟧ |
| Review turnaround | ⟦level⟧ | ⟦add reviewer time, change routing⟧ | ⟦role⟧ |
| Failed run rate | ⟦level⟧ | ⟦fix, pause⟧ | ⟦role⟧ |
| Cost per unit of work | ⟦level or budget⟧ | ⟦apply a cost lever, escalate⟧ | ⟦role⟧ |
| Active use | ⟦level⟧ | ⟦find the reason: tool, trust, time⟧ | ⟦role⟧ |

## Rules we follow

- Report a number with its denominator and period. A rate without a count is not reported.
- Distinguish a reading from a trend. A single period moving is a prompt to look, not a conclusion.
- Keep definitions stable. A definition change is recorded, and the earlier periods are restated or marked as not comparable.
- When data are missing, say so. Do not fill gaps with estimates presented as readings.
- Do not read cost per unit alone. A cheaper unit with a higher consequential error rate is not an improvement.
