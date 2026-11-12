# Readiness rubric

Six dimensions, four levels each. A level is defined by what we can observe, not by how anyone describes themselves. If we cannot see the evidence, the level is not met.

The levels use the same names in every dimension.

| Level | Name | What we see, in general |
|---|---|---|
| L1 | Ad hoc | Practice lives in individuals' heads. Nothing is written down that we can inspect. |
| L2 | Informal | Practice exists and is described consistently, but it is undocumented or depends on one person. |
| L3 | Documented | It is written down, assigned to a named owner and in current use. |
| L4 | Evidenced | It is documented, and a dated record shows it was reviewed or used to make a decision. |

## 1. Strategy & ownership

| Level | Observable evidence |
|---|---|
| L1 | No named sponsor or workflow owner. The goal is stated as "use AI" with no measure. |
| L2 | Sponsor and owner are known by name to the team but not recorded. The goal is described verbally with a rough measure. |
| L3 | Sponsor and owner are named in writing. The outcome is written with a unit of measure. Decision rights for scope, go-live and stopping are written down. |
| L4 | As L3, and a decision record shows the sponsor or owner used the outcome measure to continue, narrow or stop work. |

## 2. Process clarity

| Level | Observable evidence |
|---|---|
| L1 | Different people describe different steps. No map. Exceptions are discovered when they happen. |
| L2 | People describe the same steps, but there is no map. Some exceptions are known; owners vary. |
| L3 | A process map exists with inputs, outputs and decision points. Exceptions are listed with owners. A set of real past cases is available. |
| L4 | As L3, and the main steps are time-stamped in a system, so a baseline can be taken from records. The map was corrected after a review with the team. |

## 3. Data & systems access

| Level | Observable evidence |
|---|---|
| L1 | The systems involved are not all listed. Access for outside engineers has no route. |
| L2 | Systems are listed from memory. Access has been granted before, case by case, by someone who knows the right person. |
| L3 | A system list with owners exists. Sensitive fields are identified. Read-only access is granted through a defined route. A non-production environment, or an agreed alternative, is available. |
| L4 | As L3, and a real read from each system has been tested end to end, with a recorded outcome. Write routes, limits and recovery for each integration are documented. |

## 4. People & skills

| Level | Observable evidence |
|---|---|
| L1 | Reviewers and future owners are not identified. No one has been asked to make time. |
| L2 | Likely reviewers and an owner are known informally. Time for review comes out of existing workload. |
| L3 | Reviewers are named, time is allocated, and a written standard defines correct output. An internal owner and a deputy are named and their managers agree. |
| L4 | As L3, and each named person has completed a practice task and met the sign-off criterion in [enablement/roles.md](../enablement/roles.md). |

## 5. Governance & risk

| Level | Observable evidence |
|---|---|
| L1 | No AI policy. It is not defined which data may reach a model provider. No incident contact. |
| L2 | Rules are communicated verbally or by email. Data handling is decided case by case. |
| L3 | A written policy has been issued. Data classes are mapped to model-provider rules. Actions needing approval are listed, and approvals are recorded. An incident contact is named. |
| L4 | As L3, and legal, security or compliance review is on file, the incident route has been rehearsed once, and the policy has a review date that has been met. |

## 6. Operations & cost

| Level | Observable evidence |
|---|---|
| L1 | No owner after handover. The unit of work is not defined. No one looks at spend. |
| L2 | An owner is assumed. Someone looks at the usage bill occasionally. No limit exists. |
| L3 | An owner is named. The unit of work is defined. A spend limit exists with an alert owner. A review meeting is scheduled. |
| L4 | As L3, and cost per unit of work has been reviewed against the agreed budget, with a recorded decision, at least once. |

## From answers to levels

The [questionnaire](questionnaire.md) asks five questions per dimension, each answered 1 to 4 using the evidence test on that page. `score.py` computes a dimension's level as follows.

1. Take the median of its five answers.
2. Cap the result at the lowest answer plus one.

The cap is deliberate. A dimension with one answer of 1 cannot read above L2, however strong the others. One unanswered gap, such as no named owner or no access route, is the usual reason a build stalls.

| Answers (sorted) | Median | Lowest + 1 | Level |
|---|---|---|---|
| 3 3 3 3 3 | 3 | 4 | L3 |
| 1 4 4 4 4 | 4 | 2 | L2 |
| 2 4 4 4 4 | 4 | 3 | L3 |
| 3 4 4 4 4 | 4 | 4 | L4 |
| 1 1 1 4 4 | 1 | 2 | L1 |

The overall level is the lowest dimension level. We do not average dimensions, because a strong policy does not make up for a missing owner.

Scores are a way to organise a conversation and decide what to fix first. They are not a certification and not a measure of the organisation's worth.
