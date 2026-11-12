# Role-based paths

Each role has a short list of things the person must be able to do, the sessions they attend, a practice task on the client's own workflow, and a sign-off criterion. Sign-off is given by a named person who watched the task, not by the person who ran the session alone.

Session numbers refer to the [session plans](session-plans/). Each role maps to a playbook role in the [roles table](../README.md#roles). Fill in the `⟦...⟧` fields once per engagement.

| Role | Sessions | Signed off by |
|---|---|---|
| [Executive sponsor](#executive-sponsor) | 04 | Lead engineer |
| [Workflow owner](#workflow-owner) | 01, 02, 03, 04 | Executive sponsor |
| [Daily operator / reviewer](#daily-operator--reviewer) | 01, 02 | Workflow owner |
| [Internal builder / admin](#internal-builder--admin) | 02, 03, 04 | Lead engineer, then workflow owner |
| [IT & security](#it--security) | 02, 03 | Client security lead |

## Executive sponsor

**Must be able to**

- Read the operating metrics and say whether the workflow is healthy.
- Decide to continue, narrow, pause or stop, using the decision rules in the [90-day plan](../adoption/90-day-plan.md).
- Approve or refuse a change that alters what the workflow may do without approval.
- Name the workflow owner and the champion, and protect their time.

**Sessions:** 04 Cost and usage (about 60 minutes), plus a 30-minute briefing with the lead engineer at handover.

**Practice task:** with last month's metrics from [adoption/metrics.md](../adoption/metrics.md), decide whether to continue, narrow or pause, and write the reason in three sentences.

**Sign-off criterion:** the decision names which metric drove it and states what would change it. ⟦sponsor name⟧ · ⟦date⟧.

## Workflow owner

**Must be able to**

- Explain what the workflow does, what it never does without approval, and where a person decides.
- Judge whether a reviewer's correction is a one-off or a pattern that needs a rule change.
- Approve change requests against [change control](../governance/change-control.md).
- Run the monthly review using the adoption metrics.

**Sessions:** 01, 02, 03 (as approver), 04.

**Practice task:** take ten cases from the reference set, including two exceptions. Classify each correction as one-off or pattern. Raise one change request for a pattern and approve or reject a second one prepared by the engineers.

**Sign-off criterion:** the classification agrees with the engineers' on every exception case, or the difference is explained and recorded; the change request is complete enough to be applied without a conversation. ⟦sponsor name⟧ · ⟦date⟧.

## Daily operator / reviewer

**Must be able to**

- Run a unit of work through the workflow start to finish in the live system.
- Review AI output against the written standard and accept, correct or escalate it.
- Record a correction in the form the team uses, so it can be counted.
- Recognise when to stop and use the pause route.
- Handle an exception using the quick reference without asking an engineer.

**Sessions:** 01 Reviewing AI output, 02 Running the workflow.

**Practice task:** review a prepared batch of ⟦number⟧ cases drawn from the reference set. The batch includes cases that look right and are wrong, an out-of-scope case, and a case needing escalation. Run one live unit of work with the workflow owner watching.

**Sign-off criterion:** every planted error is caught or the miss is discussed; out-of-scope and escalation cases are routed correctly; corrections are recorded in the agreed form. ⟦workflow owner⟧ · ⟦date⟧.

## Internal builder / admin

**Must be able to**

- Read the workflow's current prompts, rules and settings and explain what each does.
- Make a change on a branch or copy, run the eval cases, compare against the last result and read the difference.
- Submit a change under [change control](../governance/change-control.md), including a rollback.
- Roll back a change.
- Read the usage and cost view and spot a spike.

**Sessions:** 02, 03 Changing prompts and rules safely, 04.

**Practice task:** three stages, each with an engineer. Shadow two of our changes. Make one change with the engineer watching. Make one alone and submit it through change control.

**Sign-off criterion:** the change was applied through the route, eval results were attached and read correctly, rollback was demonstrated in the test environment, and the record is complete. ⟦lead engineer⟧ · ⟦date⟧; then ⟦workflow owner⟧ · ⟦date⟧.

## IT & security

**Must be able to**

- List the accounts, keys and permissions the workflow uses, and rotate or revoke them.
- Confirm which data classes may reach a model provider and show where that is enforced.
- Locate the audit trail of actions the workflow took and who approved them.
- Run the incident route in [acceptable-use](../governance/acceptable-use.md).
- Pause the workflow without the engineers.

**Sessions:** 02, 03 (for the access and change-control parts).

**Practice task:** a tabletop incident. A reviewer reports that a draft contained data it should not have. Walk the route: pause, contain, trace, record, notify, restore.

**Sign-off criterion:** the pause was achieved without outside help, the trace found the record, and the incident record is complete. ⟦security lead⟧ · ⟦date⟧.

## Sign-off record

| Role | Person | Practice task date | Signed off by | Date | Open items |
|---|---|---|---|---|---|
| Executive sponsor | ⟦name⟧ | ⟦date⟧ | ⟦name⟧ | ⟦date⟧ | ⟦item or none⟧ |
| Workflow owner | ⟦name⟧ | ⟦date⟧ | ⟦name⟧ | ⟦date⟧ | ⟦item or none⟧ |
| Daily operator / reviewer | ⟦names⟧ | ⟦date⟧ | ⟦name⟧ | ⟦date⟧ | ⟦item or none⟧ |
| Internal builder / admin | ⟦name, deputy⟧ | ⟦date⟧ | ⟦name⟧ | ⟦date⟧ | ⟦item or none⟧ |
| IT & security | ⟦name⟧ | ⟦date⟧ | ⟦name⟧ | ⟦date⟧ | ⟦item or none⟧ |

A role with open items is not handed over. The item gets an owner and a date in the [90-day plan](../adoption/90-day-plan.md).
