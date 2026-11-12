# Change control · Template

**Use:** this describes how prompts, rules, models and integrations are changed after handover. The client adopts it at day 0 of the [90-day plan](../adoption/90-day-plan.md). Replace every `⟦...⟧` field.

Workflow: ⟦name⟧ · Approver (workflow owner): ⟦name⟧ · Deputy approver: ⟦name⟧ · IT & security reviewer: ⟦name⟧ · Change log location: ⟦location⟧ · Revision: ⟦record⟧.

## Why

An AI workflow can change behaviour from a small edit to a prompt, a change in the model provider's model, or an update to a connected system. Without a record, a drop in quality cannot be traced to its cause and cannot be undone. The route below keeps every change tested, approved, reversible and logged.

## What counts as a change

| Class | Examples | Approver | Evals required | Notice |
|---|---|---|---|---|
| A. Wording | Fixing typos in a prompt; clarifying a rule's text with no change in meaning | Workflow owner | Yes, regression run | Operators told after |
| B. Behaviour | Changing a prompt's instructions; adding or changing a rule, threshold, routing or a field mapping | Workflow owner | Yes, regression run plus new cases for the change | Operators told before |
| C. Model | Changing the model, its version or its settings; adding a model provider | Workflow owner and IT & security | Yes, full run on the whole case set | Sponsor and operators told before |
| D. Integration and permissions | Adding or changing a connected system, a write path, an account, a key or access rights; changing what the workflow may do without approval | Workflow owner, IT & security and sponsor | Yes, plus a test in the non-production environment | Sponsor and operators told before |
| E. Emergency | A fix needed to stop harm now | Any approver, after pausing | Run afterwards, within ⟦agreed time⟧ | Everyone told at once; reviewed at the next monthly review |

When in doubt about the class, use the higher one.

Changes made by someone else do not escape control. A model provider retiring a model version, an update to the ERP or CRM, or a change to an input format arrives as a change request raised by the internal builder as soon as it is known.

## The route

```
request -> prepare in a copy -> run evals -> record -> approve -> apply -> watch -> close
                                    |                     |
                                    +-- fail: adjust or abandon      +-- problem: roll back
```

1. **Request.** Anyone may ask: operators, the champion, the builder, IT. The request states the problem seen, with examples from the corrections log or the metrics, and the outcome wanted.
2. **Prepare.** The internal builder makes the change in a copy or a branch, not in the live configuration. It is the smallest change that could meet the request.
3. **Run evals.** Run the eval cases and compare with the last accepted result. Control cases, those that must never fail, are listed in the record. Any control case failing blocks the change.
4. **Record.** Complete the change record below.
5. **Approve.** The approver for the class reads the record and the eval comparison and approves, asks for changes or rejects. Builder and approver are different people for classes B to E.
6. **Apply.** The builder applies the exact version that was tested. The time is recorded. The new version identifier goes on the [quick reference](../enablement/operator-quick-reference.md).
7. **Watch.** For ⟦period⟧ after applying, the champion watches the override rate, exception rate and failed run rate. A reading outside the thresholds in [metrics](../adoption/metrics.md) triggers a rollback decision.
8. **Close.** Record the observed effect against the stated outcome. Update the reference documents.

## Rollback

Every change record includes how to roll back. The route is rehearsed in the test environment before approval for classes B to D. Rolling back does not need new approval: the builder, the champion, or the workflow owner may do it and tell the others. After a rollback, record why.

## Change record

Change ID: ⟦number⟧ · Class: ⟦A–E⟧ · Raised by: ⟦name, date⟧ · Builder: ⟦name⟧ · Approver: ⟦name⟧.

| Field | Entry |
|---|---|
| Problem seen, with examples | ⟦description and links⟧ |
| Outcome wanted | ⟦measurable statement⟧ |
| What changes | ⟦old and new text, or a diff reference⟧ |
| What should not change | ⟦behaviours that must remain, including control cases⟧ |
| Version tested | ⟦identifier of the copy⟧ |
| Eval result: previous accepted vs this version | ⟦summary; link to the full report⟧ |
| Cases that changed, in either direction, and why | ⟦list⟧ |
| Control cases | ⟦all passed / failed: list⟧ |
| Data or provider impact | ⟦none, or details; IT & security view⟧ |
| Rollback | ⟦exact steps and how to confirm it worked⟧ |
| Approval | ⟦name, role, date, conditions⟧ |
| Applied | ⟦time, applied by, version identifier⟧ |
| Observation period and readings | ⟦metrics watched and results⟧ |
| Outcome | ⟦met / not met / rolled back; reason⟧ |

## Eval cases

The eval cases are part of the workflow and are maintained like any other. When reviewers meet a new kind of failure, it is added to the case set, with the correct answer agreed by the workflow owner. Removing a case needs the same approval as the change class it protects. The set is reviewed at the monthly review.

## Audit

At each monthly review, the workflow owner compares the live configuration with the change log. A difference, meaning a change with no record, is treated as an incident under [acceptable-use](acceptable-use.md) until explained. The number of such differences is reported in the [metrics](../adoption/metrics.md).

## Changes to this document

Changes to this route are class D changes.
