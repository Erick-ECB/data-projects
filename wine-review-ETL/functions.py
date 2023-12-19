import pandas as pd
import glob


def read_csv_files(directory_path):
    csv_files = glob.glob(directory_path + "*.csv")
    dfs = []

    for file in csv_files:
        df = pd.read_csv(file, index_col="Unnamed: 0")
        df.reset_index(drop=True, inplace=True)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def read_json_files(directory_path):
    json_files = glob.glob(directory_path + "*.json")
    dfs = []

    for file in json_files:
        df = pd.read_json(file)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
