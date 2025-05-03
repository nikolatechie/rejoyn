import pandas as pd


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


def extract_unique_vibes(file_path: str) -> None | list[str]:
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
        return list(
            unique_vibes
        )  # ['art_and_culture', 'great_food', 'nightlife_and_entertainment', 'outdoor_adventures', 'beach', 'underrated_destinations']
    else:
        print("Column 'vibes' not found in the DataFrame or DataFrame is None.")
        return None


unique_vibes = extract_unique_vibes("iata_airports_and_locations_with_vibes.csv")
print(unique_vibes)
