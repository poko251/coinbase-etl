import pandas as pd
import os


def get_file_path() -> str: 
    folder_path = "data/raw"
    files = os.listdir(folder_path)

    #checks if only one file inside

    if not files:
        raise FileNotFoundError("No files found in data/raw")
    elif len(files) == 1:
        file_path = os.path.join(folder_path, files[0])
    else:
        raise ValueError("Folder contains more than one file")
    
    return file_path



def load_transactions(filepath: str) -> pd.DataFrame:

    df = pd.read_csv(filepath, skiprows=3, encoding="utf-8")
    
    return df


def clean_currency_columns(df: pd.DataFrame, col_names:list[str]) -> pd.DataFrame:

    for col in col_names:
        df[f"{col}_clean"] = (
            df[col]
            .astype(str)
            .str.replace("zł", "", regex=False)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )
    return df


def filter_transactions(df: pd.DataFrame, transaction_type:str) -> pd.DataFrame:

    df = df[df["Transaction Type"] == transaction_type]

    return df

def save_clean_data(df: pd.DataFrame, filename: str = "processed_data.csv") -> str:
    folder = "data/processed"
    os.makedirs(folder, exist_ok=True)   # upewniamy się, że folder istnieje
    path = os.path.join(folder, filename)
    df.to_csv(path, index=False)         # zapisujemy dane
    return path