#!/usr/bin/env python3
"""Score a readiness questionnaire and print a markdown report.

Usage:
    python readiness/score.py answers.json

Input JSON:
    {
      "organisation": "Name",            (required, non-empty string)
      "assessed_on": "YYYY-MM-DD",       (required, a real calendar date)
      "stage": "understand" | "operate", (required)
      "answers": {"SO1": 3, ...}         (required, every question, integer 1-4)
    }

Scoring rule (see readiness/rubric.md):
    dimension level = the median of its five answers, capped at the lowest
    answer plus one. One weak answer therefore stops a dimension from
    reading as strong.

Exit codes: 0 report written, 2 invalid input or unreadable file.
Standard library only; Python 3.9+.
"""
import argparse
import datetime
import json
import re
import sys
import unicodedata

DIMENSIONS = [
    ("SO", "Strategy & ownership"),
    ("PC", "Process clarity"),
    ("DA", "Data & systems access"),
    ("PS", "People & skills"),
    ("GR", "Governance & risk"),
    ("OC", "Operations & cost"),
]
QUESTIONS_PER_DIMENSION = 5
STAGES = ("understand", "operate")
LEVEL_NAMES = {1: "Ad hoc", 2: "Informal", 3: "Documented", 4: "Evidenced"}

# What moves a dimension from its current level to the next one.
NEXT_STEPS = {
    "SO": {
        1: ["Name one executive sponsor and one workflow owner in writing.",
            "Write the business outcome for the first workflow as a measurable statement with an owner."],
        2: ["Record the decision rights: who approves scope, go-live and stopping.",
            "Agree how the outcome will be measured before the pilot starts."],
        3: ["Put a review date on the outcome and decision record, and show one decision taken from it."],
    },
    "PC": {
        1: ["Walk the workflow end to end with the people who do it and write down each step.",
            "List the exceptions people handle today and who decides them."],
        2: ["Turn the walkthrough into a documented map with inputs, outputs and decision points.",
            "Collect a small set of real past cases, including difficult ones, as the reference set."],
        3: ["Time-stamp the main steps so a baseline can be measured from records, not memory."],
    },
    "DA": {
        1: ["Name the systems the workflow touches and the owner of each.",
            "Request read-only access for the engineers and record the approval."],
        2: ["Document where each data field comes from and who may see it.",
            "Test one real read from each system in a non-production setting."],
        3: ["Confirm write paths, rate limits and a recovery route for each integration."],
    },
    "PS": {
        1: ["Identify who will review AI output and who will own prompts and rules after handover.",
            "Schedule the role-based sessions in enablement/roles.md."],
        2: ["Give reviewers protected time and a written review standard.",
            "Nominate an internal builder or admin and a deputy."],
        3: ["Run a practice task per role and record the sign-off criterion met."],
    },
    "GR": {
        1: ["Adopt an acceptable-use policy (governance/acceptable-use.md) and name an incident contact.",
            "List the data classes the workflow handles and which may reach a model provider."],
        2: ["Define which actions need human approval and how the approval is recorded.",
            "Agree the change route for prompts, rules and models (governance/change-control.md)."],
        3: ["Rehearse the incident route once and keep the record."],
    },
    "OC": {
        1: ["Choose who watches usage and spend and where they look.",
            "Define the unit of work so cost per unit can be calculated."],
        2: ["Set up a regular review of the adoption metrics (adoption/metrics.md).",
            "Set a spend limit and an alert owner for model and hosting costs."],
        3: ["Review cost per unit against the agreed budget and record the decision taken."],
    },
}
MAINTAIN = "Keep the evidence current and re-assess at the next stage."


DATE_PATTERN = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


def clean_organisation(value):
    """Return a single-line organisation name or raise InputError.

    Whitespace (including newlines) collapses to single spaces; any other
    control or line-separator character is rejected; a leading '#' is escaped
    so the name can never read as a markdown heading.
    """
    if not isinstance(value, str):
        raise InputError("'organisation' must be a non-empty string")
    for char in value:
        if not char.isspace() and unicodedata.category(char) in ("Cc", "Cf", "Zl", "Zp"):
            raise InputError("'organisation' must not contain control characters")
    name = " ".join(value.split())
    if not name:
        raise InputError("'organisation' must be a non-empty string")
    return "\\" + name if name.startswith("#") else name


class InputError(ValueError):
    """Raised when the answers file is not valid input."""


def question_ids():
    """Question ids by dimension code, e.g. SO1..SO5, PC1..PC5, ..."""
    return {
        code: [f"{code}{n}" for n in range(1, QUESTIONS_PER_DIMENSION + 1)]
        for code, _ in DIMENSIONS
    }


def dimension_level(answers):
    """Median of the answers, capped at the lowest answer plus one."""
    if not answers:
        raise ValueError("no answers to score")
    ordered = sorted(answers)
    median = ordered[len(ordered) // 2]
    return min(median, ordered[0] + 1)


def validate(data):
    """Return (organisation, assessed_on, stage, answers) or raise InputError."""
    if not isinstance(data, dict):
        raise InputError("top level of the file must be a JSON object")
    for key in ("organisation", "assessed_on", "stage", "answers"):
        if key not in data:
            raise InputError(f"missing required field '{key}'")
    org = clean_organisation(data["organisation"])
    when = data["assessed_on"]
    try:
        if not isinstance(when, str) or not DATE_PATTERN.fullmatch(when):
            raise ValueError("not YYYY-MM-DD")
        datetime.date.fromisoformat(when)
    except ValueError:
        raise InputError("'assessed_on' must be a real date written YYYY-MM-DD")
    stage = data["stage"]
    if stage not in STAGES:
        raise InputError("'stage' must be one of: " + ", ".join(STAGES))
    answers = data["answers"]
    if not isinstance(answers, dict):
        raise InputError("'answers' must be an object of question id to 1-4")
    expected = [q for qs in question_ids().values() for q in qs]
    unknown = sorted(set(answers) - set(expected))
    if unknown:
        raise InputError("unknown question id(s): " + ", ".join(unknown))
    missing = [q for q in expected if q not in answers]
    if missing:
        raise InputError("missing answer(s) for: " + ", ".join(missing))
    for qid in expected:
        value = answers[qid]
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 4:
            raise InputError(f"answer for {qid} must be an integer from 1 to 4, got {value!r}")
    return org, when, stage, answers


def score(answers):
    """Return a list of per-dimension result dicts, in rubric order."""
    results = []
    for index, (code, name) in enumerate(DIMENSIONS):
        values = [answers[q] for q in question_ids()[code]]
        results.append({
            "code": code,
            "name": name,
            "index": index,
            "values": values,
            "level": dimension_level(values),
            "mean": sum(values) / len(values),
        })
    return results


def weakest(results, count=3):
    """Lowest level first, then lowest mean, then rubric order."""
    return sorted(results, key=lambda r: (r["level"], r["mean"], r["index"]))[:count]


def render(org, when, stage, results):
    """Build the markdown report. Output depends only on the input."""
    lowest = min(r["level"] for r in results)
    point = "01 Understand" if stage == "understand" else "05 Operate"
    lines = [
        "# Readiness report",
        "",
        f"Organisation: {org} · Assessed on: {when} · Assessment point: stage {point}",
        "",
        f"Overall: L{lowest} ({LEVEL_NAMES[lowest]}), set by the lowest dimension. "
        "Dimensions are not averaged: a strong area does not offset a weak one.",
        "",
        "## Levels by dimension",
        "",
        "| Dimension | Level | Answers | Mean |",
        "|---|---|---|---|",
    ]
    for r in results:
        answers = " ".join(str(v) for v in r["values"])
        lines.append(
            f"| {r['name']} | L{r['level']} {LEVEL_NAMES[r['level']]} | {answers} | {r['mean']:.1f} |"
        )
    lines += ["", "## Weakest dimensions", ""]
    for rank, r in enumerate(weakest(results), start=1):
        lines.append(f"{rank}. {r['name']} (L{r['level']}, mean {r['mean']:.1f})")
    lines += ["", "## Suggested next steps", ""]
    for r in weakest(results):
        target = f"L{r['level'] + 1}" if r["level"] < 4 else "maintain"
        lines.append(f"### {r['name']}: L{r['level']} to {target}")
        lines.append("")
        steps = NEXT_STEPS[r["code"]].get(r["level"], [MAINTAIN])
        lines += [f"- {s}" for s in steps]
        lines.append("")
    blockers = [r["name"] for r in results if r["level"] == 1]
    lines += ["## Before stage 03 Build starts", ""]
    if blockers:
        lines.append(
            "Dimensions at L1 are resolved, or knowingly accepted by the executive sponsor in writing, "
            "before build work begins: " + ", ".join(blockers) + "."
        )
    else:
        lines.append("No dimension is at L1. Record the sponsor's go-ahead and keep the lowest dimensions on the plan.")
    lines.append("")
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(
        prog="score.py",
        description="Score a readiness questionnaire (JSON) and print a markdown report.",
    )
    parser.add_argument("answers", help="path to the answers JSON file")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        with open(args.answers, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        org, when, stage, answers = validate(data)
    except OSError as exc:
        print(f"error: cannot read {args.answers}: {exc.strerror or exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"error: {args.answers} is not valid JSON ({exc.msg}, line {exc.lineno})", file=sys.stderr)
        return 2
    except RecursionError:
        print(f"error: {args.answers} is nested too deeply to read", file=sys.stderr)
        return 2
    except UnicodeDecodeError:
        print(f"error: {args.answers} is not UTF-8 text", file=sys.stderr)
        return 2
    except InputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    report = render(org, when, stage, score(answers))
    # Write bytes so output is UTF-8 with LF endings on every platform.
    sys.stdout.flush()
    sys.stdout.buffer.write(report.encode("utf-8"))
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
