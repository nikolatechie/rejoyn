from collections import defaultdict
import json
from typing import List, Dict
import pandas as pd
from mock_user_preferences import mock_user_prefs


# Prevent trimming the output
pd.set_option("display.max_colwidth", None)


# List of features related to trip preferences
FEATURES: None | List[str] = [
    "art_and_culture",
    "beach",
    "outdoor_adventures",
    "nightlife_and_entertainment",
    "great_food",
    "underrated_destinations",
    "safety",  # Added
    "weather",  # Added
]


def load_csv_values(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file and retrieves all values as a pandas DataFrame.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing all the values from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        # print(df)
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


def _extract_unique_vibes(file_path: str) -> None | list[str]:
    if FEATURES is not None:
        return FEATURES

    df = load_csv_values(file_path)
    if df is not None and "vibes" in df.columns:
        unique_vibes = set()
        for value in df["vibes"].dropna():
            try:
                json_dict = eval(value)  # Assuming the JSON is stored as a string
                unique_vibes.update(json_dict.keys())
            except Exception as e:
                print(f"Error processing row value: {e}")
        # unique_vibes = list(unique_vibes)
        return list(unique_vibes)
    else:
        print("Column 'vibes' not found in the DataFrame or DataFrame is None.")
        return None


def _parse_vibes(vibes) -> Dict[str, int]:
    DEFAULT_VALUE = 0.5  # Assume neutral if unknown
    if pd.isna(vibes) or vibes == "null":
        return {feature: DEFAULT_VALUE for feature in FEATURES}
    elif len(vibes) < len(FEATURES):
        # Some features are missing
        for feature in FEATURES:
            if feature not in vibes:
                # Add them with neutral values
                vibes[feature] = DEFAULT_VALUE

    return json.loads(vibes)


def apply_parse_vibes(df: pd.DataFrame) -> pd.DataFrame:
    # vibes_df = load_csv_values("iata_airports_and_locations_with_vibes.csv")
    df["vibes"] = df["vibes"].apply(_parse_vibes)
    return df


##### Turn user preferences into a single group weight vector
def create_single_group_weight_vector(user_prefs):
    group_raw = defaultdict(int)

    for user in user_prefs:
        for k, v in user.items():
            group_raw[k] += v

    # Compute average
    group_avg = {f: group_raw[f] / len(user_prefs) for f in FEATURES}
    return group_avg


print(create_single_group_weight_vector(mock_user_prefs))

# unique_vibes = _extract_unique_vibes("iata_airports_and_locations_with_vibes.csv")
# print(unique_vibes)
