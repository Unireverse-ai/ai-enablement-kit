# Session 01 · Reviewing AI output

**Length:** 90 minutes · **Format:** in person or video, in the client's workspace · **Led by:** forward-deployed engineer, with the workflow owner co-presenting
**For:** daily operators and reviewers, workflow owner · **FDE stage:** 04 Evaluate (reviewers also label eval cases)

## Objective

By the end, each reviewer can review AI output against the written standard, catch the kinds of error this workflow produces, and record a correction in a form that can be counted.

## Prerequisites

- The review standard for this workflow is written: what a correct output looks like, in a page or less.
- A reference set of real past cases is available, including at least a few where the workflow was wrong or unsure. Details are removed or approved for use according to the data rules.
- Reviewers have access to the review screen or queue in a test environment.
- The workflow owner has chosen which of the cases are used in the exercise and has not shown them to the reviewers.

## Agenda

| Min | Item | Who | Notes |
|---|---|---|---|
| 0–10 | What the workflow does and where a person decides | Workflow owner | Show the real queue. State what happens if a reviewer does nothing. |
| 10–25 | The review standard, read through | Engineer | One example each of accept, correct, escalate. |
| 25–40 | How this workflow gets things wrong | Engineer | Walk through the failure patterns seen in the eval cases: missing context, confident wrong values, wrong category, an input outside scope. Use cases from the reference set. |
| 40–70 | Exercise: review a batch | Reviewers | See below. |
| 70–80 | Debrief on the batch | Engineer, workflow owner | Reveal the planted errors. Discuss every miss without blame. |
| 80–90 | Recording corrections; check for understanding | Engineer | See below. |

## Exercise

Each reviewer reviews the same batch of ⟦number⟧ cases from the reference set, working alone, using the real screen. The batch is prepared by the workflow owner and contains:

- cases that are correct and should be accepted;
- cases that look plausible but contain one wrong value;
- a case outside the workflow's scope, which should be routed rather than fixed;
- a case where a person must decide, which should be escalated;
- one case where the output is acceptable but the input was unusual.

For each case the reviewer records: accept, correct or escalate; the field or reason; one sentence of evidence. Reviewers then compare results in pairs before the debrief.

## Check for understanding

Ask each reviewer, without notes:

1. Which three kinds of error does this workflow most often produce, and where would you look for each?
2. A case is outside scope. What do you do, and what do you not do?
3. You correct the same field for the third time in a morning. What do you record, and who do you tell?
4. You are unsure and the queue is long. What is the safe action?

A reviewer is ready for the practice task in [roles.md](../roles.md#daily-operator--reviewer) when they answer all four correctly, or the gap is addressed in the debrief and re-asked.

## Materials

The review standard · the batch with answers · [operator quick reference](../operator-quick-reference.md) · a blank corrections log.
