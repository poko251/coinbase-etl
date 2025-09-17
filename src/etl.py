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


