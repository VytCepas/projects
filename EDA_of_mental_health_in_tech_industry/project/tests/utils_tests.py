import unittest
import pandas as pd

from project.utils import (
    order_combined_value,
    standardize_values,
    assess_and_convert_combined_into_single_value,
    get_unique_values_from_dict,
    get_matching_value_counts,
)


class TestOrderCombinedValue(unittest.TestCase):
    def test_single_value_no_pipe(self):
        self.assertEqual(order_combined_value("apple"), "apple")

    def test_multiple_values(self):
        self.assertEqual(
            order_combined_value("banana|apple|cherry"), "apple|banana|cherry"
        )

    def test_already_sorted_values(self):
        self.assertEqual(
            order_combined_value("apple|banana|cherry"), "apple|banana|cherry"
        )

    def test_reverse_order_values(self):
        self.assertEqual(
            order_combined_value("cherry|banana|apple"), "apple|banana|cherry"
        )

    def test_duplicate_values(self):
        self.assertEqual(
            order_combined_value("apple|banana|apple"), "apple|apple|banana"
        )

    def test_empty_string(self):
        self.assertEqual(order_combined_value(""), "")


class TestStandardizeValues(unittest.TestCase):
    def setUp(self):
        self.standards_dict = {
            "StandardA": ["A", "a", "Alpha", "Alph"],
            "StandardB": ["B", "b", "Beta", "Bet"],
            "StandardC": ["C", "c", "Charlie", "Char"],
        }

    def test_exact_match(self):
        result = standardize_values("A", self.standards_dict)
        self.assertEqual(result, "StandardA")

    def test_fuzzy_match_high_score(self):
        result = standardize_values("Alph", self.standards_dict, matching_score=80)
        self.assertEqual(result, "StandardA")

    def test_no_match_below_threshold(self):
        result = standardize_values("Gamma", self.standards_dict, matching_score=95)
        self.assertEqual(result, "Other")

    def test_multiple_values_with_pipe(self):
        result = standardize_values("Alph|Bet", self.standards_dict, matching_score=95)
        self.assertEqual(result, "StandardA|StandardB")

    def test_mixed_matches_and_non_matches(self):
        result = standardize_values(
            "Alph|Gamma", self.standards_dict, matching_score=95
        )
        self.assertEqual(result, "StandardA|Other")

    def test_empty_input(self):
        result = standardize_values("", self.standards_dict)
        self.assertEqual(result, "Other")

    def test_lower_matching_score(self):
        result = standardize_values("Alp", self.standards_dict, matching_score=50)
        self.assertEqual(result, "StandardA")

    def test_high_matching_score_no_match(self):
        result = standardize_values("Alpl", self.standards_dict, matching_score=100)
        self.assertEqual(result, "Other")

    def test_partial_match_in_reverse_lookup(self):
        result = standardize_values("Char", self.standards_dict, matching_score=80)
        self.assertEqual(result, "StandardC")


class TestGetUniqueValuesFromDict(unittest.TestCase):
    def test_single_value_per_key(self):
        series_dict = {1: "A", 2: "B", 3: "C"}
        result = get_unique_values_from_dict(series_dict)
        self.assertEqual(result, {"A", "B", "C"})

    def test_multiple_values_per_key(self):
        series_dict = {1: "A|B", 2: "B|C", 3: "C|D"}
        result = get_unique_values_from_dict(series_dict)
        self.assertEqual(result, {"A", "B", "C", "D"})

    def test_mixed_single_and_multiple_values(self):
        series_dict = {1: "A", 2: "A|B", 3: "B|C"}
        result = get_unique_values_from_dict(series_dict)
        self.assertEqual(result, {"A", "B", "C"})

    def test_empty_dictionary(self):
        series_dict = {}
        result = get_unique_values_from_dict(series_dict)
        self.assertEqual(result, set())

    def test_duplicate_values(self):
        series_dict = {1: "A|B", 2: "A|B", 3: "C"}
        result = get_unique_values_from_dict(series_dict)
        self.assertEqual(result, {"A", "B", "C"})

    def test_values_with_whitespace(self):
        series_dict = {1: "A | B", 2: " B|C ", 3: "C | D "}
        result = get_unique_values_from_dict(series_dict)
        self.assertEqual(result, {"A", "B", "C", "D"})


class TestAssessAndConvertCombinedIntoSingleValue(unittest.TestCase):
    def test_single_value_no_pipe(self):
        self.assertEqual(assess_and_convert_combined_into_single_value("A"), "A")

    def test_multiple_same_values(self):
        self.assertEqual(assess_and_convert_combined_into_single_value("A|A|A"), "A")

    def test_multiple_different_values(self):
        self.assertEqual(
            assess_and_convert_combined_into_single_value("A|B|A|B"), "Unsure"
        )

    def test_tie_with_different_values(self):
        self.assertEqual(
            assess_and_convert_combined_into_single_value("A|B|C|A|B|C"), "Unsure"
        )

    def test_custom_unclear_value(self):
        self.assertEqual(
            assess_and_convert_combined_into_single_value(
                "A|B|A|B", unclear_value="Tie"
            ),
            "Tie",
        )

    def test_empty_string(self):
        self.assertEqual(assess_and_convert_combined_into_single_value(""), "Unsure")


class TestGetMatchingValueCounts(unittest.TestCase):
    def setUp(self):
        self.series_of_interest = pd.Series(
            [
                "apple banana",
                "banana apple",
                "cherry",
                "apple",
                "banana",
                "cherry apple",
                "banana cherry",
                "apple banana cherry",
            ]
        )
        self.matching_values = ["apple", "banana", "cherry", "date"]

    def test_matching_value_counts(self):
        expected_counts = pd.Series(
            {"apple": 5, "banana": 5, "cherry": 4, "date": 0}, dtype=int
        )

        result = get_matching_value_counts(
            self.series_of_interest, self.matching_values
        )

        pd.testing.assert_series_equal(result, expected_counts)

    def test_empty_series(self):
        empty_series = pd.Series([])
        expected_counts = pd.Series(
            {"apple": 0, "banana": 0, "cherry": 0, "date": 0}, dtype=int
        )

        result = get_matching_value_counts(empty_series, self.matching_values)

        pd.testing.assert_series_equal(result, expected_counts)

    def test_no_matching_values(self):
        no_match_values = ["date", "fig", "grape"]
        expected_counts = pd.Series({"date": 0, "fig": 0, "grape": 0}, dtype=int)

        result = get_matching_value_counts(self.series_of_interest, no_match_values)

        pd.testing.assert_series_equal(result, expected_counts)

    def test_partial_matching_values(self):
        partial_match_values = ["apple", "date"]
        expected_counts = pd.Series({"apple": 5, "date": 0}, dtype=int)

        result = get_matching_value_counts(
            self.series_of_interest, partial_match_values
        )

        pd.testing.assert_series_equal(result, expected_counts)


if __name__ == "__main__":
    unittest.main()
