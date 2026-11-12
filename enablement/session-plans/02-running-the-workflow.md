# Session 02 · Running the workflow

**Length:** 90 minutes · **Format:** in the live or staging environment, hands on · **Led by:** forward-deployed engineer, IT lead present for the last block
**For:** operators and reviewers, workflow owner, internal builder, IT & security · **FDE stage:** 04 Evaluate into 05 Operate

## Objective

By the end, the team can start the workflow, follow a unit of work through it, recognise a stuck or failed run, use the pause route, and know who to call. The team fills in their [operator quick reference](../operator-quick-reference.md) during the session.

## Prerequisites

- [Session 01](01-reviewing-ai-output.md) completed by the operators, or taking place the same day.
- The runbook draft from stage 03 exists. It is expected to be incomplete; the session completes it.
- Accounts exist for each attendee with the permissions their role needs, and nothing more.
- A safe way to run test units of work exists: a staging copy, or a flag that marks test items.
- IT & security has confirmed where the pause control is and who may use it.

## Agenda

| Min | Item | Who | Notes |
|---|---|---|---|
| 0–10 | The map: what triggers a run, what it touches, where a person decides | Engineer | Draw it on a whiteboard from memory, then compare with the real map. |
| 10–30 | Follow one unit of work from trigger to completion | Engineer, then operators | Show each system it passes through and what is written back. |
| 30–50 | Exercise: run three units of work | Operators | See below. |
| 50–65 | When it goes wrong: stuck, duplicated, partly completed | Engineer | Show the controls that prevent a duplicate and how to see what actually happened. Never retry blindly. |
| 65–80 | Pause, restore, escalate | IT lead, engineer | Everyone practises the pause route once. |
| 80–90 | Fill in the quick reference; check for understanding | Operators | See below. |

## Exercise

Each operator runs three units of work in staging, using cases from the reference set:

1. A normal unit, start to finish, including review.
2. An exception case, handled with the quick reference only.
3. A case where the engineer has injected a failure, such as a connected system being unavailable. The operator must find what state the unit is in and decide whether it is safe to retry.

The IT lead then asks one operator to pause the workflow, confirm that it has paused, and restore it.

## Check for understanding

1. A run has not completed after the usual time. What do you check, in what order, before asking for help?
2. You see two records that look the same. What could have caused that, and what do you do?
3. Show me how you pause the workflow. Who may restore it?
4. Which things on the quick reference do you expect to change, and who updates it?

Operators who cannot do the pause without help repeat that block before sign-off.

## Materials

Runbook draft · [operator quick reference](../operator-quick-reference.md), blank · reference set cases · failure-injection notes for the engineer · account list.
