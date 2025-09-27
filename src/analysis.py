import pandas as pd

def total_fees(df: pd.DataFrame) -> float:
    """Return the sum of all fees."""
    return df["Fees and/or Spread_clean"].sum()


def total_by_type(
    df: pd.DataFrame,
    transaction_type: str,
    column: str = "Total (inclusive of fees and/or spread)_clean"
) -> float:
    """Return the total value of transactions of a given type."""
    return df[df["Transaction Type"] == transaction_type][column].sum()


def monthly_fees(df: pd.DataFrame) -> pd.Series:
    """Return monthly sum of fees (Series with Period index)."""
    return df.groupby(df["Timestamp"].dt.to_period("M"))["Fees and/or Spread_clean"].sum()


def get_date_range(df: pd.DataFrame, column="Timestamp") -> tuple[pd.Timestamp, pd.Timestamp]:
    """Return the minimum and maximum date in the DataFrame."""
    return df[column].min(), df[column].max()


def transaction_type_distribution(df: pd.DataFrame) -> pd.Series:
    """Return count of transactions grouped by type."""
    return df.groupby("Transaction Type")["ID"].count()


def top_fees(df: pd.DataFrame, n=5, column="Fees and/or Spread_clean") -> pd.DataFrame:
    """Return DataFrame with top n transactions with the highest fees."""
    return df.nlargest(n=n, columns=column)


def average_fee_of_transaction_type(df: pd.DataFrame, column="Buy") -> float:
    """Return average fee for a given transaction type."""
    avg = df[df["Transaction Type"] == column]["Fees and/or Spread_clean"].mean()
    return float(avg)


def total_invested(df: pd.DataFrame) -> float:
    """Return total invested amount (Buy transactions)."""
    return df[df["Transaction Type"] == "Buy"]["Total (inclusive of fees and/or spread)_clean"].sum()


