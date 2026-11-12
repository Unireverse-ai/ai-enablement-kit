# Readiness

Readiness is whether a client's organisation can take on, run and extend one specific AI workflow. It is about the workflow and the people around it, not about how advanced the company is.

We assess it against six dimensions, each with four levels described by evidence:

1. Strategy & ownership
2. Process clarity
3. Data & systems access
4. People & skills
5. Governance & risk
6. Operations & cost

## When we assess

| Point | FDE stage | Purpose | Who answers |
|---|---|---|---|
| First assessment | [01 Understand](https://github.com/Unireverse-ai/fde-playbook) | Find what must be fixed before build starts; shape the opportunity list and the pilot brief | The business owner, with the workflow owner |
| Re-assessment | [05 Operate](https://github.com/Unireverse-ai/fde-playbook) | Show what changed, confirm the team can run the workflow, and decide what the next workflow needs | Same people, same questions |

The questions do not change between the two points. That is what makes the second result comparable with the first. A dimension that has not moved is a finding, not a failure; it goes into the handover pack with an owner.

## How it works

1. The business owner, with the workflow owner, answers the [questionnaire](questionnaire.md) in one sitting. Each answer needs something they can point to. Role names are mapped in the [kit roles table](../README.md#roles).
2. An engineer checks a sample of the claimed evidence during the stage 01 interviews. An answer we cannot see is lowered by one.
3. `score.py` turns the answers into levels, the weakest dimensions and suggested next steps.
4. We review the report with the sponsor and agree owners for the next steps. Dimensions at L1 are resolved, or accepted in writing by the sponsor, before stage 03 starts.

```
python readiness/score.py readiness/example-answers.json
```

The output of that command is committed as [example-report.md](example-report.md).

## What readiness is not

- A pass or fail gate for the client. A low level tells us what to prepare first.
- A maturity ranking of the company. The assessment is per workflow.
- A replacement for the stage 04 acceptance decision, which tests the workflow itself.

## Files

| File | Use |
|---|---|
| [rubric.md](rubric.md) | The six dimensions and the evidence for each level |
| [questionnaire.md](questionnaire.md) | The 30 questions |
| [score.py](score.py) | Scores an answers file; standard library only |
| [example-answers.json](example-answers.json) | The input format |
| [example-report.md](example-report.md) | The report for the sample answers |

## Input format

```json
{
  "organisation": "Example Organisation",
  "assessed_on": "2026-01-15",
  "stage": "understand",
  "answers": { "SO1": 3, "SO2": 3, "...": 0 }
}
```

`stage` is `understand` or `operate`. Every question id from the questionnaire must be present, each answered with an integer from 1 to 4. The script exits with code 2 and a one-line message to stderr if the file cannot be read, is not valid JSON, has an unknown or missing question, or has an answer out of range.
