# Operator quick reference · Template

**Use:** fill this in during [session 02](session-plans/02-running-the-workflow.md), print it or pin it where the team works, and keep it to one page. The workflow owner updates it whenever a change under [change control](../governance/change-control.md) alters anything on it.

Workflow: ⟦name⟧ · Version of prompts and rules: ⟦identifier⟧ · Last updated: ⟦date⟧ by ⟦name⟧.

## What it does

⟦One sentence: what triggers it, what it produces, where the result goes.⟧

It never does the following without a person's approval: ⟦list⟧.

## Each unit of work

| Step | What you do | Where |
|---|---|---|
| 1 | ⟦open the item in the queue⟧ | ⟦system and view⟧ |
| 2 | ⟦check the output against the review standard⟧ | ⟦link to the standard⟧ |
| 3 | Accept, correct or escalate | ⟦control⟧ |
| 4 | Record any correction | ⟦form or field⟧ |

## Accept, correct, escalate

| Do this | When |
|---|---|
| Accept | ⟦the output meets every item in the standard⟧ |
| Correct | ⟦a field is wrong but the case is in scope; record it⟧ |
| Escalate | ⟦out of scope, a person must decide, or you are unsure⟧; route to ⟦name or queue⟧ |

## Exceptions

| Exception | Handle it by | Decided by |
|---|---|---|
| ⟦case⟧ | ⟦action⟧ | ⟦role⟧ |
| ⟦case⟧ | ⟦action⟧ | ⟦role⟧ |

## When something is wrong

| Symptom | Check first | Then |
|---|---|---|
| Run has not finished after ⟦time⟧ | ⟦where to see run status⟧ | ⟦escalate to name⟧ |
| Two similar records | Do not retry. Look at ⟦log or record⟧ | ⟦escalate to name⟧ |
| Output you did not expect, repeatedly | Record three examples | Tell ⟦workflow owner⟧ |
| Data in an output that should not be there | Pause the workflow | Follow the incident route below |

## Pause and restore

Pause: ⟦exact control and location⟧ · May pause: ⟦roles⟧ · Restore: ⟦who and how⟧.

## Who to call

| For | Name | Contact |
|---|---|---|
| Questions about the workflow | ⟦workflow owner⟧ | ⟦contact⟧ |
| Changing a prompt or rule | ⟦internal builder⟧ | ⟦contact⟧ |
| Access, accounts, data problems | ⟦IT & security⟧ | ⟦contact⟧ |
| Incident | ⟦incident contact⟧ | ⟦contact, out of hours too⟧ |
| Anything else | ⟦champion⟧ | ⟦contact⟧ |

Review turnaround we aim for: ⟦agreed target⟧. Backup reviewer when you are away: ⟦name⟧.
