from collections import defaultdict
import json
from typing import List, Dict
import pandas as pd

# import datasets.mock_user_preferences.mock_user_prefs
from datasets.mock_user_preferences import get_mock_user_prefs
import random


# Prevent trimming the output
pd.set_option("display.max_colwidth", None)

mock_user_prefs = get_mock_user_prefs()

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


# Enrich the dataset with artificial data
def _add_new_features(vibes):
    if pd.isna(vibes) or vibes == "null":
        rnd_feature = random.randint(0, len(FEATURES) - 1)
        vibes_dict = {FEATURES[rnd_feature]: 1}
    else:
        vibes_dict = json.loads(vibes)

    # Add new features with default values
    vibes_dict["safety"] = 1
    vibes_dict["weather"] = 1

    return json.dumps(vibes_dict)


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
    if isinstance(vibes, str):
        print("yes, it's a string")
        try:
            vibes = json.loads(vibes)
        except json.JSONDecodeError:
            vibes = {}
    # print(vibes_dict)
    print("vibes: ", type(vibes), vibes, len(vibes), len(FEATURES))
    DEFAULT_VALUE = 0.5  # Assume neutral if unknown
    if pd.isna(vibes) or vibes == "null":
        print("it's empty")
        return {feature: DEFAULT_VALUE for feature in FEATURES}
    elif len(vibes) < len(FEATURES):
        print("checking lengths")
        print(len(vibes))
        print(len(FEATURES))
        # Some features are missing
        for feature in FEATURES:
            if feature not in vibes:
                # Add them with neutral values
                vibes[feature] = DEFAULT_VALUE

    print("pass all")

    return vibes


def apply_parse_vibes(df: pd.DataFrame) -> pd.DataFrame:
    # vibes_df = load_csv_values("iata_airports_and_locations_with_vibes.csv")
    df["vibes"] = df["vibes"].apply(_parse_vibes)
    return df


##### Turn user preferences into a single group weight vector
def create_single_group_weight_vector(user_prefs):
    print("user_prefs: ", user_prefs)
    group_raw = defaultdict(int)
    print("group_raw:", group_raw)

    for user in user_prefs:
        # for k, v in user.items():
        # print("burek", k, v)
        # print(user)
        group_raw[user["feature"]] += user["score"]

    print("group_raw:", group_raw)
    # Compute average
    group_avg = {f: group_raw[f] / len(user_prefs) for f in FEATURES}
    print("group_avg:", group_avg)

    # Normalise the group vector
    # total = sum(group_avg.values())
    # group_weights = {k: (v - 1) / 4 for k, v in group_avg.items()}
    # print("group_weights:", group_weights)
    return group_raw
    # return group_weights


# Rate each destination based on group weights
def score_destination(vibes, group_weights, neutral_score=0.5):
    raw_score = sum(
        float(vibes.get(k, neutral_score)) * group_weights.get(k, 0)
        for k in group_weights
    )
    max_possible_score = sum(
        abs(weight) for weight in group_weights.values()
    )  # Denominator
    if max_possible_score == 0:
        return 0.0
    normalised_score = raw_score / max_possible_score
    return normalised_score


def get_top_destinations(user_prefs):
    print("user_prefs here")
    print(user_prefs)
    df = load_csv_values("datasets/modified_locations_with_vibes.csv")
    # print("before apply parse")
    # print(df)
    # print("features ", FEATURES)
    df = apply_parse_vibes(df)
    print("after parse vibes")
    print(df["vibes"].head(50))
    # print("type user_prefs", type(user_prefs))
    group_weights = create_single_group_weight_vector(
        user_prefs=user_prefs  # list of user prefs
    )
    print("finished group weights")
    df["score"] = df["vibes"].apply(score_destination, group_weights=group_weights)
    print("omlet", df["score"])

    # Get top 10 destinations for the group
    top_destinations = df.sort_values(by="score", ascending=False).head(10)
    print("top_destinations", top_destinations)
    return top_destinations  # [id, IATA, en-GB, latitude, longitude, vibes, score]


if __name__ == "__main__":
    # df = load_csv_values("iata_airports_and_locations_with_vibes.csv")
    df = load_csv_values("modified_locations_with_vibes.csv")

    # One time vibes enrichment
    # df["vibes"] = df["vibes"].apply(_add_new_features)
    # Export the modified DataFrame to a new CSV file
    # df.to_csv("modified_locations_with_vibes.csv", index=False)

    df = apply_parse_vibes(df)
    group_weights = create_single_group_weight_vector(
        mock_user_prefs  # list of user prefs
    )  # Mock user prefs
    df["score"] = df["vibes"].apply(score_destination, group_weights=group_weights)

    # Get top 10 destinations for the group
    top_destinations = df.sort_values(by="score", ascending=False).head(10)
    print(top_destinations)
    print(top_destinations.columns)


# unique_vibes = _extract_unique_vibes("iata_airports_and_locations_with_vibes.csv")
# print(unique_vibes)
