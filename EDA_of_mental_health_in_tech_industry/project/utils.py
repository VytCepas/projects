from collections import Counter

import pandas as pd
from fuzzywuzzy import process


def order_combined_value(values: str) -> str:
    """
    Order combined values alphabetically and rejoin them with '|'.
    """
    if "|" not in values:
        pass

    return "|".join(sorted(values.split("|")))


def standardize_values(
    value: str, standards_dict: dict, matching_score: int | float = 90
) -> str:
    """
    Standardize values based on a given dictionary of standards using fuzzy matching.

    Args:
        value (str): The value to be standardized.
        standards_dict (dict): Dictionary where keys are standard values and values are lists of possible variations.
        matching_score (int | float, optional): The minimum score for a match to be considered valid.

    Returns:
        str: The standardized value.
    """
    reverse_lookup = {v: k for k, values in standards_dict.items() for v in values}
    values_list = value.split("|")
    standardized_values = []

    for val in values_list:
        val = val.strip()
        if not val:
            standardized_values.append("Other")
            continue

        best_match, score = process.extractOne(val, reverse_lookup.keys())
        if score >= matching_score:
            standardized_values.append(reverse_lookup[best_match])
        else:
            standardized_values.append("Other")

    return "|".join(standardized_values)


def assess_and_convert_combined_into_single_value(
    combined_value: str,
    unclear_value: str = "Unsure",
) -> str:
    """
    Convert a combined value string into a single value based on the most frequent occurrence.

    Args:
        combined_value (str): The combined value string.
        unclear_value (str, optional): The value to return if there is no clear single value.

    Returns:
        str: The single value or the unclear value if there is no clear single value.
    """
    combined_value_list = combined_value.split("|")
    standardized_value_count: dict[str, int] = Counter(combined_value_list)

    if combined_value == "":
        return unclear_value

    max_count = max(standardized_value_count.values())

    max_values = [
        value for value, count in standardized_value_count.items() if count == max_count
    ]

    return "".join(max_values) if len(max_values) == 1 else unclear_value


def get_unique_values_from_dict(series_dict: dict[int, str]) -> set:
    """
    Extract unique values from a dictionary where values are strings that may contain
    multiple items separated by '|'.
    """
    unique_values = set()

    for value in series_dict.values():
        if "|" in value:
            value_arr = value.split("|")
            for element in value_arr:
                unique_values.add(element.strip())
        else:
            unique_values.add(value)

    return unique_values


def get_matching_value_counts(
    series_of_interest: pd.Series, matching_values: list
) -> pd.Series:
    """
    Count occurrences of matching values in a pandas Series.

    Args:
        series_of_interest (pd.Series): The Series to search for matching values.
        matching_values (list): List of values to count in the Series.

    Returns:
        pd.Series: A Series with the counts of matching values.
    """
    count_of_matching_values = {
        value: sum(series_of_interest.str.contains(value)) for value in matching_values
    }

    return pd.Series(data=count_of_matching_values, dtype=int)
