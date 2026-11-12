# Session 03 · Changing prompts and rules safely

**Length:** 120 minutes, then a supervised change in the following weeks · **Format:** hands on, in the test environment · **Led by:** forward-deployed engineer
**For:** internal builder / admin and deputy, workflow owner, IT & security · **FDE stage:** 05 Operate

## Objective

By the end, the internal builder can change a prompt, a rule or a setting without breaking the workflow: make the change in a copy, run the eval cases, read the difference, submit it through [change control](../../governance/change-control.md), apply it and roll it back.

## Prerequisites

- [Sessions 01 and 02](01-reviewing-ai-output.md) completed by the workflow owner; session 02 by the builder.
- The eval cases and the harness that runs them are handed over, with the last accepted result stored.
- A test environment exists where changes can be applied without affecting live work.
- The change-control route is agreed and the workflow owner has approval authority.
- The builder has shadowed at least two of our changes. These are done during stage 03 and 04, and the shadowing record is kept.

## Agenda

| Min | Item | Who | Notes |
|---|---|---|---|
| 0–15 | What can be changed and what cannot | Engineer | Prompts, rules, thresholds, routing, model, integration. The classes in change control decide who approves. |
| 15–35 | Reading the current prompt and rules line by line | Engineer, builder | The builder explains each line back. Unclear lines are noted and fixed in the documentation. |
| 35–50 | The eval cases and what a difference means | Engineer | Run the cases, read a report, tell a real regression from noise, understand which cases are the controls. |
| 50–95 | Exercise: make a change | Builder, with engineer | See below. |
| 95–110 | Submitting, applying, rolling back | Builder, workflow owner | Complete a change record. Apply in the test environment. Roll it back. |
| 110–120 | Check for understanding; plan the supervised change | Engineer | See below. |

## Exercise

The engineer gives a realistic request, such as: reviewers keep correcting one field the same way; make that the default. The builder:

1. States in one sentence what outcome would show the change worked.
2. Copies the current prompt or rules and makes the smallest change that could achieve it.
3. Runs the eval cases and compares with the stored result.
4. Finds the cases that changed, in either direction, and says why.
5. Decides whether to submit, adjust or abandon.
6. Completes the change record, including rollback.

A second request is prepared that looks small but breaks a control case. The builder is not told this in advance. The aim is for the evals to catch it.

## Check for understanding

1. The eval result improves overall but one control case fails. Do you submit? Why?
2. A reviewer asks you to change the model to a cheaper one. Which class of change is that and who approves it?
3. You made a change on Friday and Monday's metrics look worse. What do you do first?
4. Show me the rollback. How long does it take, and how do you confirm it worked?

## After the session

The builder makes one change with an engineer watching, then one alone through change control. Each is logged. This is the practice task in [roles.md](../roles.md#internal-builder--admin).

## Materials

Current prompts and rules, with comments · eval cases and harness · last accepted result · blank change record from [change control](../../governance/change-control.md) · shadowing record.
