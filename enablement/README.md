# Enablement

Enablement is how a client's team becomes able to run and extend an AI workflow after our engineers leave. It is part of every build, not an add-on after it. The goal is stated in operational terms: named people can do named tasks, and we have watched them do it.

## Who is trained

Five roles, each with a different job to do. Not everyone sits through everything. See [roles.md](roles.md).

| Role | Why they are trained |
|---|---|
| Executive sponsor | Decides scope, go-live and stopping; reads the operating metrics |
| Workflow owner | Owns the process and the outcome; accepts changes |
| Daily operator / reviewer | Runs the workflow and reviews AI output every day |
| Internal builder / admin | Changes prompts, rules and settings safely after handover |
| IT & security | Owns access, data handling and incident response |

## When, by whom

Enablement runs alongside the build. The engineers who build the workflow teach it, because they know where it fails.

| FDE stage | Enablement activity | Led by | Output |
|---|---|---|---|
| 01 Understand | Readiness assessment; name the five roles and the internal champion | Lead engineer with the workflow owner | [Readiness report](../readiness/example-report.md) |
| 02 Assess | Agree who will be trained and how success of training is signed off | Lead engineer with the sponsor | Role list and the sign-off criteria in the pilot brief |
| 03 Build | Operators join build reviews; the internal builder shadows changes; runbook drafted with the team | Forward-deployed engineers | Runbook draft, shadowing record |
| 04 Evaluate | Reviewers label eval cases, so they learn the failure modes first-hand; sessions 01 and 02 | Forward-deployed engineers | Labelled cases; sign-offs for reviewers |
| 05 Operate | Sessions 03 and 04; practice tasks per role; 90-day plan; handover of ownership to the champion | Forward-deployed engineers, then the champion | Handover pack, [sign-offs](roles.md), re-assessment |

## The four sessions

| Session | For | Plan |
|---|---|---|
| 01 Reviewing AI output | Operators and reviewers, workflow owner | [01-reviewing-ai-output.md](session-plans/01-reviewing-ai-output.md) |
| 02 Running the workflow | Operators and reviewers, workflow owner, IT | [02-running-the-workflow.md](session-plans/02-running-the-workflow.md) |
| 03 Changing prompts and rules safely | Internal builder, workflow owner, IT | [03-changing-prompts-and-rules-safely.md](session-plans/03-changing-prompts-and-rules-safely.md) |
| 04 Cost and usage | Sponsor, workflow owner, internal builder | [04-cost-and-usage.md](session-plans/04-cost-and-usage.md) |

Sessions use the client's own workflow, in the client's own systems, with real cases from the reference set. We do not train on slides about AI in general.

## Principles

1. **Practice, then sign-off.** Attendance is not competence. Each role has a practice task and a sign-off criterion that a named person checks.
2. **Operate before change.** Operators run the workflow for a period before anyone changes its prompts or rules. The internal builder shadows several of our changes first, then makes one with us watching, then makes one alone.
3. **Written down while building.** Runbooks and the quick reference are drafted during stage 03 from what operators ask, not written afterwards from memory.
4. **One owner.** After handover, one champion owns the workflow's operating routine. See [adoption/champions.md](../adoption/champions.md).
5. **Same rules after we leave.** Changes follow [governance/change-control.md](../governance/change-control.md), and use of the workflow follows [governance/acceptable-use.md](../governance/acceptable-use.md).

## What the team keeps

- The [operator quick reference](operator-quick-reference.md), filled in for their workflow.
- The session plans, so new joiners can be trained internally.
- The sign-off record for each role.
- The [90-day plan](../adoption/90-day-plan.md) and [metrics](../adoption/metrics.md) used to review the workflow after handover.
