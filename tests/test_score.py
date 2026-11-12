"""Tests for readiness/score.py. Standard library only."""
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
READINESS = os.path.join(ROOT, "readiness")
sys.path.insert(0, READINESS)

import score  # noqa: E402

SCRIPT = os.path.join(READINESS, "score.py")
EXAMPLE = os.path.join(READINESS, "example-answers.json")
REPORT = os.path.join(READINESS, "example-report.md")


def all_ids():
    return [q for qs in score.question_ids().values() for q in qs]


def make_data(value=3, **overrides):
    data = {
        "organisation": "Test Organisation",
        "assessed_on": "2026-02-01",
        "stage": "operate",
        "answers": {q: value for q in all_ids()},
    }
    data.update(overrides)
    return data


def run_cli(*args):
    return subprocess.run(
        [sys.executable, SCRIPT, *args], capture_output=True, text=True, encoding="utf-8"
    )


class DimensionLevelTests(unittest.TestCase):
    def test_uniform_answers_give_that_level(self):
        for level in (1, 2, 3, 4):
            self.assertEqual(score.dimension_level([level] * 5), level)

    def test_one_weak_answer_caps_the_level(self):
        # median 4, lowest 1 -> capped at 2
        self.assertEqual(score.dimension_level([1, 4, 4, 4, 4]), 2)

    def test_cap_boundary_lowest_plus_one(self):
        self.assertEqual(score.dimension_level([2, 4, 4, 4, 4]), 3)
        self.assertEqual(score.dimension_level([3, 4, 4, 4, 4]), 4)

    def test_median_limits_the_level(self):
        # lowest 1 allows 2, but median is 1
        self.assertEqual(score.dimension_level([1, 1, 1, 4, 4]), 1)
        self.assertEqual(score.dimension_level([1, 1, 2, 4, 4]), 2)

    def test_order_of_answers_does_not_matter(self):
        self.assertEqual(score.dimension_level([4, 1, 3, 2, 3]), score.dimension_level([1, 2, 3, 3, 4]))

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            score.dimension_level([])


class ScoreAndWeakestTests(unittest.TestCase):
    def test_six_dimensions_in_rubric_order(self):
        results = score.score(make_data()["answers"])
        self.assertEqual([r["code"] for r in results], ["SO", "PC", "DA", "PS", "GR", "OC"])
        self.assertEqual(len(all_ids()), 30)

    def test_weakest_orders_by_level_then_mean_then_rubric_order(self):
        data = make_data(4)
        for q in ("PC1", "PC2", "PC3", "PC4", "PC5"):
            data["answers"][q] = 2
        for q in ("OC1", "OC2", "OC3", "OC4", "OC5"):
            data["answers"][q] = 2
        data["answers"]["OC1"] = 1  # same level 2, lower mean than PC
        results = score.score(data["answers"])
        names = [r["code"] for r in score.weakest(results)]
        self.assertEqual(names[:2], ["OC", "PC"])
        self.assertEqual(len(names), 3)

    def test_tie_falls_back_to_rubric_order(self):
        results = score.score(make_data(3)["answers"])
        self.assertEqual([r["code"] for r in score.weakest(results)], ["SO", "PC", "DA"])

    def test_render_lists_l1_blocker(self):
        data = make_data(3)
        for q in score.question_ids()["DA"]:
            data["answers"][q] = 1
        org, when, stage, answers = score.validate(data)
        text = score.render(org, when, stage, score.score(answers))
        self.assertIn("Overall: L1", text)
        self.assertIn("before build work begins: Data & systems access.", text)

    def test_render_without_l1_has_no_blockers(self):
        org, when, stage, answers = score.validate(make_data(3))
        text = score.render(org, when, stage, score.score(answers))
        self.assertIn("No dimension is at L1", text)
        self.assertIn("stage 05 Operate", text)

    def test_all_l4_says_maintain(self):
        org, when, stage, answers = score.validate(make_data(4))
        text = score.render(org, when, stage, score.score(answers))
        self.assertIn("L4 to maintain", text)
        self.assertIn(score.MAINTAIN, text)

    def test_every_step_table_entry_exists_for_levels_1_to_3(self):
        for code, _ in score.DIMENSIONS:
            for level in (1, 2, 3):
                self.assertTrue(score.NEXT_STEPS[code][level])


class ValidationTests(unittest.TestCase):
    def assert_invalid(self, data, fragment):
        with self.assertRaises(score.InputError) as ctx:
            score.validate(data)
        self.assertIn(fragment, str(ctx.exception))

    def test_valid_input_passes(self):
        org, when, stage, answers = score.validate(make_data())
        self.assertEqual((org, when, stage), ("Test Organisation", "2026-02-01", "operate"))
        self.assertEqual(len(answers), 30)

    def test_not_an_object(self):
        self.assert_invalid([1, 2], "JSON object")

    def test_missing_field(self):
        data = make_data()
        del data["stage"]
        self.assert_invalid(data, "missing required field 'stage'")

    def test_blank_organisation(self):
        self.assert_invalid(make_data(organisation="  "), "organisation")

    def test_bad_date(self):
        self.assert_invalid(make_data(assessed_on="2026-02-30"), "assessed_on")
        self.assert_invalid(make_data(assessed_on=20260201), "assessed_on")

    def test_assessed_on_must_be_strict_iso_shape(self):
        for value in ("2026-W05-1", "20260201", "2026-2-1", "2026-02-01\n", "\u0662\u0660\u0662\u0666-02-01"):
            with self.subTest(value=value):
                self.assert_invalid(make_data(assessed_on=value), "assessed_on")

    def test_organisation_whitespace_and_controls(self):
        self.assertEqual(score.validate(make_data(organisation="  Acme \t  Ltd\n"))[0], "Acme Ltd")
        self.assertEqual(score.validate(make_data(organisation="Acme\n# Pwned"))[0], "Acme # Pwned")
        self.assertEqual(score.validate(make_data(organisation="# Big"))[0], "\\# Big")
        for bad in ("Ac\x00me", "Ac\x1bme", "Acme\u202ex", "", "\n \t", 5):
            with self.subTest(value=bad):
                self.assert_invalid(make_data(organisation=bad), "organisation")

    def test_bad_stage(self):
        self.assert_invalid(make_data(stage="build"), "stage")

    def test_answers_wrong_type(self):
        self.assert_invalid(make_data(answers=[3] * 30), "'answers' must be an object")

    def test_missing_answer(self):
        data = make_data()
        del data["answers"]["GR3"]
        self.assert_invalid(data, "missing answer(s) for: GR3")

    def test_unknown_question(self):
        data = make_data()
        data["answers"]["ZZ9"] = 3
        self.assert_invalid(data, "unknown question id(s): ZZ9")

    def test_out_of_range_boundaries(self):
        for bad in (0, 5, -1, 100):
            data = make_data()
            data["answers"]["SO1"] = bad
            self.assert_invalid(data, "SO1")

    def test_in_range_boundaries_accepted(self):
        for good in (1, 4):
            data = make_data()
            data["answers"]["SO1"] = good
            score.validate(data)

    def test_non_integer_answers_rejected(self):
        for bad in (2.5, "3", None, True, [3]):
            data = make_data()
            data["answers"]["PC2"] = bad
            self.assert_invalid(data, "PC2")


class QuestionnaireConsistencyTests(unittest.TestCase):
    def test_questionnaire_ids_match_scorer(self):
        path = os.path.join(READINESS, "questionnaire.md")
        with open(path, encoding="utf-8") as handle:
            found = re.findall(r"^\| ([A-Z]{2}\d) \|", handle.read(), flags=re.M)
        self.assertEqual(sorted(found), sorted(all_ids()))

    def test_example_answers_are_valid(self):
        with open(EXAMPLE, encoding="utf-8") as handle:
            score.validate(json.load(handle))


class CliTests(unittest.TestCase):
    def write_temp(self, text):
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        self.addCleanup(os.unlink, handle.name)
        handle.write(text)
        handle.close()
        return handle.name

    def test_example_output_matches_committed_report(self):
        result = run_cli(EXAMPLE)
        self.assertEqual(result.returncode, 0, result.stderr)
        with open(REPORT, encoding="utf-8", newline="") as handle:
            expected = handle.read().replace("\r\n", "\n")
        self.assertEqual(result.stdout.replace("\r\n", "\n"), expected)

    def test_bad_json_exits_2_with_message(self):
        path = self.write_temp("{not json")
        result = run_cli(path)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("error:", result.stderr)
        self.assertIn("not valid JSON", result.stderr)

    def test_out_of_range_answer_exits_2_with_message(self):
        data = make_data()
        data["answers"]["OC5"] = 9
        path = self.write_temp(json.dumps(data))
        result = run_cli(path)
        self.assertEqual(result.returncode, 2)
        self.assertIn("answer for OC5 must be an integer from 1 to 4, got 9", result.stderr)

    def test_bad_date_shapes_exit_2(self):
        for value in ("2026-W05-1", "20260201"):
            with self.subTest(value=value):
                result = run_cli(self.write_temp(json.dumps(make_data(assessed_on=value))))
                self.assertEqual(result.returncode, 2)
                self.assertIn("assessed_on", result.stderr)

    def test_newline_injection_in_organisation_cannot_add_markdown_blocks(self):
        data = make_data(organisation="Acme\n\n# Injected\n- item")
        result = run_cli(self.write_temp(json.dumps(data)))
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertIn("Organisation: Acme # Injected - item", lines[2])
        self.assertNotIn("# Injected", [line for line in lines if line.startswith("#")])

    def test_deeply_nested_json_exits_2(self):
        depth = 200000
        path = self.write_temp("[" * depth + "]" * depth)
        result = run_cli(path)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("error:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_missing_file_exits_2(self):
        result = run_cli(os.path.join(ROOT, "no-such-file.json"))
        self.assertEqual(result.returncode, 2)
        self.assertIn("cannot read", result.stderr)

    def test_no_arguments_exits_2(self):
        result = run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("usage", result.stderr.lower())

    def test_non_utf8_file_exits_2(self):
        handle = tempfile.NamedTemporaryFile("wb", suffix=".json", delete=False)
        self.addCleanup(os.unlink, handle.name)
        handle.write(b"\xff\xfe\x00")
        handle.close()
        result = run_cli(handle.name)
        self.assertEqual(result.returncode, 2)
        self.assertIn("error:", result.stderr)


if __name__ == "__main__":
    unittest.main()
