import pandas as pd


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from a DataFrame."""
    return df.drop_duplicates().reset_index(drop=True)


def drop_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Drop specified columns from a DataFrame."""
    return df.drop(cols, axis=1)


def add_year(df: pd.DataFrame) -> pd.DataFrame:
    """Extract and add the year from the 'title' column."""
    df["year"] = df["title"].str.extract(r"\b(20(?:0[0-9]|1[0-9]|2[0-3]))\b")
    df["year"] = df["year"].fillna(0).astype(int)

    return df


def obtain_region(df: pd.DataFrame) -> pd.DataFrame:
    """Extract and update 'region_1' based on 'title'."""
    return df.apply(
        lambda row: row["title"].split("(")[-1].rstrip(")")
        if pd.notna(row["title"]) and pd.isna(row["region_1"])
        else row["region_1"],
        axis=1,
    )


def deal_with_price(df: pd.DataFrame) -> pd.Series:
    """Fill missing values in 'price' with the median."""
    print(df.columns)
    return df["price"].fillna(df["price"].median())


def handle_missed_data(df: pd.DataFrame) -> pd.DataFrame:
    df["region_1"] = obtain_region(df)
    df["price"] = deal_with_price(df)

    return df

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Process data by applying various transformations."""
    cols = ['taster_twitter_handle']
    df = drop_duplicates(df)
    df = drop_columns(df, cols)
    df = add_year(df)
    df = handle_missed_data(df)

    return df