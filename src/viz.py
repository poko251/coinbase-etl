import pandas as pd
import matplotlib.pyplot as plt    
from src.analysis import monthly_fees, transaction_type_distribution, top_fees
from matplotlib.figure import Figure

def plot_monthly_fees(df: pd.DataFrame) -> Figure:

    fees_series = monthly_fees(df)
    fees_series.index = fees_series.index.astype(str)
    
    fig, ax = plt.subplots(figsize=(16,6))
    ax.plot(
        fees_series.index,
        fees_series.values, 
        color="skyblue")

    ax.set_title("Monthly Fees (Sum)", fontsize=14)
    ax.set_xlabel("Month")
    ax.set_ylabel("Fees [PLN]")
    ax.grid(ax.grid(axis="y", linestyle="--", alpha=0.7))

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return fig
    

def plot_transaction_type_distribution(df: pd.DataFrame) -> Figure:

    transactions_series = transaction_type_distribution(df)
    transactions_series_sorted = transactions_series.sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(16,6))
    ax.bar(
        transactions_series_sorted.index,
        transactions_series_sorted.values,
        color="skyblue"
           )
    
    ax.set_title("Distribution of transactions by type", fontsize=14)
    ax.set_xlabel("Type")
    ax.set_ylabel("Ammount")
    ax.grid(ax.grid(axis="x", linestyle="--", alpha=0.7))

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return fig


def plot_top_fees(df: pd.DataFrame, n=5) -> Figure:

    top_fees_df = top_fees(df, n=n)
    plot_df = top_fees_df[["Fees and/or Spread_clean", "Notes"]]
    plot_df_sorted = plot_df.sort_values(by="Fees and/or Spread_clean", ascending=True)

    fig, ax = plt.subplots(figsize=(12,4))
    ax.barh(plot_df_sorted["Notes"],
            plot_df_sorted["Fees and/or Spread_clean"],
            color="skyblue")

    ax.set_title(f"Top {n} fees")
    ax.set_xlabel("Fees and/or Spread")
    ax.set_ylabel("Notes")
    ax.grid(ax.grid(axis="y", linestyle="--", alpha=0.7))
    plt.tight_layout()

    return fig





