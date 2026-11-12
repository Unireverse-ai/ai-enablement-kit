# Acceptable use of AI workflows · Template policy

**Use:** a client adapts this policy to its own rules and issues it to the people who use or administer the workflow. It is a starting point, not legal advice; the client's legal, security and data-protection leads review it before issue. Replace every `⟦...⟧` field.

Organisation: ⟦name⟧ · Workflow(s) covered: ⟦names⟧ · Policy owner: ⟦role⟧ · Approved by: ⟦role, name, date⟧ · Revision: ⟦record⟧ · Next review: ⟦date⟧.

## 1. Purpose and scope

This policy sets out how ⟦organisation⟧ staff and contractors may use the AI workflow(s) named above, and the AI models and tools they rely on. It applies to everyone with access to a workflow, whether they operate it, review its output or administer it.

It covers the workflow's inputs, outputs, prompts, rules, logs and connected systems.

## 2. Data

| Data class | Examples in this workflow | May be sent to a model provider? | Conditions |
|---|---|---|---|
| ⟦Public⟧ | ⟦published product information⟧ | ⟦Yes⟧ | ⟦none⟧ |
| ⟦Internal⟧ | ⟦internal procedures, non-personal operational data⟧ | ⟦Yes, approved providers only⟧ | ⟦provider list, retention setting⟧ |
| ⟦Personal⟧ | ⟦names, contact details, order history⟧ | ⟦Only where the provider terms and settings listed in the data record are in place⟧ | ⟦minimise fields; no retention for training⟧ |
| ⟦Restricted⟧ | ⟦special-category data, credentials, financial identifiers, trade secrets⟧ | ⟦No⟧ | ⟦blocked at input, with a route to a person⟧ |

Rules:

1. Users send to the workflow only the data classes it is configured for.
2. Approved model providers are listed in ⟦data record location⟧. Adding a provider is a change under [change control](change-control.md), reviewed by IT & security.
3. Credentials, keys and tokens are never typed into a prompt, a note field or a message to the workflow.
4. Outputs inherit the highest data class of their inputs.
5. Data in prompts, outputs and logs is retained for ⟦period⟧ and then deleted, as the data record states.

## 3. Approvals

A person approves an AI output before the following happens. The approval is recorded with the person's name, the time, and the exact output approved.

| Action | Approver | Record |
|---|---|---|
| ⟦Sending text to a customer or external party⟧ | ⟦role⟧ | ⟦where⟧ |
| ⟦Changing a financial, contract, or master-data record⟧ | ⟦role⟧ | ⟦where⟧ |
| ⟦Any action that cannot be undone⟧ | ⟦role⟧ | ⟦where⟧ |
| ⟦Actions the workflow may take without approval, listed here and nowhere else⟧ | ⟦none required⟧ | ⟦log⟧ |

The reviewer's approval is their own. Approving on behalf of someone else, or approving without reading the output, is a breach of this policy.

## 4. Responsibilities

| Role | Responsibility |
|---|---|
| Executive sponsor | Owns this policy; accepts residual risk; receives incident reports |
| Workflow owner | Decides what the workflow does; approves changes; reviews corrections for patterns |
| Operators and reviewers | Review output against the standard; use the escalate and pause routes; report concerns |
| Internal builder / admin | Applies approved changes only; keeps change records |
| IT & security | Manages access, keys and provider settings; runs the incident route |

## 5. Prohibited uses

Users must not:

1. Use the workflow for purposes outside its stated scope, or for any decision about a person's employment, credit, health, legal status or access to a service, unless this policy lists that use explicitly.
2. Send restricted data to the workflow or any model provider.
3. Bypass the approval step, share accounts, or use another person's credentials.
4. Alter prompts, rules, thresholds, models or integrations outside [change control](change-control.md).
5. Present AI output as human-written where the recipient has a right to know, or where ⟦organisation's policy or law⟧ requires disclosure.
6. Use outputs without checking factual claims, figures and names against the source record.
7. Copy outputs or logs to personal tools or accounts.
8. Try to remove, disguise or circumvent logging.
9. ⟦Additional prohibited uses specific to the organisation⟧.

## 6. Quality and review

Reviewers follow the written review standard. Corrections are recorded in the agreed form. Recurring corrections are reported to the workflow owner as candidate changes. A reviewer who is unsure escalates rather than approves.

## 7. Incident route

An incident is any of the following: restricted or personal data reached a place it should not; an output caused or nearly caused harm; the workflow took an action outside its scope; credentials were exposed; the workflow behaved unexpectedly in a way that cannot be explained.

| Step | Who | What |
|---|---|---|
| 1. Pause | Anyone with pause rights | Use the pause control. Do not wait for permission if data may be leaving. |
| 2. Report | The person who noticed | Tell ⟦incident contact⟧ at ⟦contact⟧ at once, out of hours too. Say what, when, and what you did. |
| 3. Contain | IT & security | Revoke affected keys or access. Preserve logs. Do not delete anything. |
| 4. Trace | IT & security with the internal builder | Establish which records and outputs were affected and who approved them. |
| 5. Notify | Sponsor with legal or data-protection lead | Decide whether a regulator, client or data subject must be told, and by when under ⟦law or contract⟧. |
| 6. Fix | Workflow owner | Correct affected records; raise a change under change control if the workflow must change. |
| 7. Record | IT & security | Complete the incident record. Review at the next monthly review. |
| 8. Restore | Sponsor | Restore the workflow when the cause is understood and the fix is in place. |

If the workflow is supported by UniReverse under a managed-operations arrangement, ⟦incident contact at UniReverse⟧ is added to step 2 and attends step 4.

## 8. Breaches and review

Breaches are handled under ⟦organisation's disciplinary or contract process⟧. This policy is reviewed at least every ⟦period⟧ and after any incident that involved the workflow. Policy changes are issued to all users, and each user acknowledges receipt: ⟦method⟧.
