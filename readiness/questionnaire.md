# Readiness questionnaire

Thirty questions, five per dimension. The business owner, with the workflow owner, answers them in one sitting, without preparation, by checking each against something they can point to. The [rubric](rubric.md) explains how answers become levels.

## How to answer

Give each question one answer from this scale. Answer for the workflow being assessed, not for the company in general.

| Answer | Meaning | Evidence test |
|---|---|---|
| 1 | No, or only in people's heads | Nothing exists that you could show us |
| 2 | Partly: informal, undocumented, or one person knows | You can describe it but not show it, or it depends on a single person |
| 3 | Yes, written down and in use | You can show us the document, system setting or record today |
| 4 | Yes, and it has been checked or used to make a decision | You can show us the document and a dated record of it being reviewed or acted on |

When unsure between two answers, give the lower one. The answer is for the team to discuss, not to defend. Record each answer in an [answers file](example-answers.json) and run `python readiness/score.py <file>`.

## Strategy & ownership

| ID | Question | Look for |
|---|---|---|
| SO1 | Is there a named executive sponsor for this workflow's AI work? | A name and a role in writing |
| SO2 | Is there a named workflow owner who runs the process day to day and can change it? | A name, and their authority over the process |
| SO3 | Is the business outcome written as something measurable (time, cost, quality, volume)? | A written outcome with a unit of measure |
| SO4 | Is it clear who may approve scope changes, go-live and stopping the work? | Written decision rights |
| SO5 | Has leadership agreed what the workflow may and may not do without a person's approval? | A written boundary on actions |

## Process clarity

| ID | Question | Look for |
|---|---|---|
| PC1 | Can the people who do the workflow describe the same sequence of steps? | A process map or checklist that matches practice |
| PC2 | Are the inputs and outputs of each step defined (what arrives, what leaves, in what format)? | Sample inputs and outputs on file |
| PC3 | Are the exceptions known, with a named person who decides each? | An exceptions list with owners |
| PC4 | Do you hold real past cases, including difficult ones, that could be used to test a workflow? | A case set or an agreed way to collect one |
| PC5 | Are the start and end of a unit of work time-stamped in a system? | Timestamps in the CRM, ERP, ticketing or inbox records |

## Data & systems access

| ID | Question | Look for |
|---|---|---|
| DA1 | Can you list the systems the workflow reads from and writes to, and who owns each? | A system list with owners |
| DA2 | Can engineers be given read-only access to those systems within an agreed time? | An access route and an approver |
| DA3 | Is it documented which data fields are sensitive and who may see them? | A data classification or field list |
| DA4 | Can a test or sandbox copy of each system be used, so build work does not touch live records? | A non-production environment, or a stated alternative |
| DA5 | Do the systems offer an API, export or integration route that can be used without screen scraping? | Documentation or a named admin who can confirm |

## People & skills

| ID | Question | Look for |
|---|---|---|
| PS1 | Have the people who will review AI output been identified by name? | A reviewer list |
| PS2 | Do those people have time in their week for review, not only in addition to a full workload? | Time allocated in plans or rotas |
| PS3 | Is there a written standard for what a correct output looks like? | A review checklist or style guide |
| PS4 | Is there someone internal who could own prompts, rules and settings after handover, plus a deputy? | Two names, and agreement from their managers |
| PS5 | Has the team used an AI tool at work before, with any rules about it? | Use cases the team can describe, and any guidance issued |

## Governance & risk

| ID | Question | Look for |
|---|---|---|
| GR1 | Is there a written policy for AI use covering data, approvals and prohibited uses? | A policy document, issued to staff |
| GR2 | Is it decided which data may be sent to a model provider and which may not? | A data-handling rule per data class |
| GR3 | Is it defined which AI actions need a person's approval, and how the approval is recorded? | An approval rule and a record location |
| GR4 | Is there a named person to call, and a route to follow, when an AI output causes harm or a data problem? | An incident route with a contact |
| GR5 | Have legal, security or compliance reviewed the intended use, and is their decision on file? | A dated review record |

## Operations & cost

| ID | Question | Look for |
|---|---|---|
| OC1 | Is there a named owner who will watch the workflow after handover? | A name and a role |
| OC2 | Is the unit of work defined, so volume and cost per unit could be counted? | A written unit definition |
| OC3 | Does anyone currently see how much is spent on model and automation usage? | A usage or billing view someone checks |
| OC4 | Is there a budget or spend limit for the workflow, with a person who is alerted? | A figure agreed in writing and an alert owner |
| OC5 | Is there a regular meeting or review where the workflow's results would be looked at? | A calendar entry or standing agenda item |
