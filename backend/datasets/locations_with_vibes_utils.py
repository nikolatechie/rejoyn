import json
from typing import List
import pandas as pd

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


def _parse_vibes(vibes):
    if pd.isna(vibes) or vibes == "null":
        pass

    return json.loads(vibes)


unique_vibes = _extract_unique_vibes("iata_airports_and_locations_with_vibes.csv")
print(unique_vibes)
