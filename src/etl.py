import pandas as pd
import os

def get_file_path() -> str: 
    """Return path to the single CSV file in data/raw."""
    folder_path = "data/raw"
    files = [f for f in os.listdir(folder_path) if f != ".gitkeep"]

    if not files:
        raise FileNotFoundError("No files found in data/raw")
    elif len(files) == 1:
        file_path = os.path.join(folder_path, files[0])
    else:
        raise ValueError("Folder contains more than one file")
    
    return file_path


def load_transactions(filepath: str) -> pd.DataFrame:
    """Load Coinbase CSV file into a pandas DataFrame."""
    # Coinbase exports have 3 header rows -> skip them
    return pd.read_csv(filepath, skiprows=3, encoding="utf-8")


def clean_currency_columns(
    df: pd.DataFrame, 
    col_names: list[str] = [
        'Price at Transaction',
        'Subtotal',
        'Total (inclusive of fees and/or spread)',
        'Fees and/or Spread'
    ]
) -> pd.DataFrame:
    """Clean currency columns: remove 'zł', replace ',' with '.', cast to float."""
    for col in col_names:
        df[f"{col}_clean"] = (
            df[col]
            .astype(str)
            .str.replace("zł", "", regex=False)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )
    return df


def convert_dates(df: pd.DataFrame, column="Timestamp") -> pd.DataFrame:
    """Convert string column to pandas datetime (UTC)."""
    df[column] = pd.to_datetime(df[column], utc=True)
    return df


def filter_transactions(df: pd.DataFrame, transaction_type: str) -> pd.DataFrame:
    """Filter transactions by type (e.g. Buy, Sell, Reward)."""
    return df[df["Transaction Type"] == transaction_type]


def save_clean_data(df: pd.DataFrame, filename: str = "processed_data.csv") -> str:
    """Save DataFrame to data/processed as CSV and return the path."""
    folder = "data/processed"
    os.makedirs(folder, exist_ok=True)   # create folder if missing
    path = os.path.join(folder, filename)
    df.to_csv(path, index=False)
    return path
