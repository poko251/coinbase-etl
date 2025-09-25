import pandas as pd

def total_fees(df: pd.DataFrame) -> float:

    return df["Fees and/or Spread_clean"].sum()

def total_by_type(df: pd.DataFrame, transaction_type: str, column: str = "Total (inclusive of fees and/or spread)_clean") -> float:

    return df[df["Transaction Type"] == transaction_type][column].sum()



def monthly_fees(df: pd.DataFrame) -> pd.DataFrame:

    return df.groupby(df["Timestamp"].dt.to_period("M"))["Fees and/or Spread_clean"].sum()


def get_date_range(df: pd.DataFrame, column="Timestamp") -> tuple[pd.Timestamp, pd.Timestamp]:

    min_date = df[column].min()
    max_date = df[column].max()

    return (min_date, max_date)

def transaction_type_distribution(df: pd.DataFrame) -> pd.DataFrame:

    return df.groupby("Transaction Type")["ID"].count()


def top_fees(df: pd.DataFrame, n=5, column="Fees and/or Spread_clean") -> pd.DataFrame:

    return df.nlargest(n=n, columns=column)


def average_fee_of_transaction_type(df: pd.DataFrame, column="Buy") -> float :

    avg = df[df["Transaction Type"] == column]["Fees and/or Spread_clean"].mean()
    return float(avg)

def total_invested(df: pd.DataFrame) -> float:

    return df[df["Transaction Type"] == "Buy"]["Total (inclusive of fees and/or spread)_clean"].sum()


def average_fee_percent(df: pd.DataFrame) -> float:

    fee_percent = df["Fees and/or Spread_clean"] / df["Total (inclusive of fees and/or spread)_clean"]
    return float(fee_percent.mean())



    

    