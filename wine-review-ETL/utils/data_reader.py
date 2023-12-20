import pandas as pd
import glob


def read_csv_files(directory_path):
    """Read CSV files from a directory and concatenate into a DataFrame."""
    csv_files = glob.glob(directory_path + "*.csv")
    dfs = []

    for file in csv_files:
        df = pd.read_csv(file, index_col="Unnamed: 0")
        df.reset_index(drop=True, inplace=True)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def read_json_files(directory_path):
    """Read JSON files from a directory and concatenate into a DataFrame."""
    json_files = glob.glob(directory_path + "*.json")
    dfs = []

    for file in json_files:
        df = pd.read_json(file)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def create_dataset(directory_path="data/"):
    """Create a dataset by reading CSV and JSON files from a directory."""
    df_csv = read_csv_files(directory_path)
    df_json = read_json_files(directory_path)

    return pd.concat([df_csv, df_json], ignore_index=True)
