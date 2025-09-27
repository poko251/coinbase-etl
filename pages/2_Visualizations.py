import streamlit as st
from src.analysis import monthly_fees, transaction_type_distribution, top_fees

st.title("📈 Visualizations")

if "df" not in st.session_state:
    st.warning("Please load data first on the main page.")
else:
    df = st.session_state["df"]

    # Monthly Fees
    st.subheader("Monthly Fees")
    fees_series = monthly_fees(df).reset_index()
    fees_series["Timestamp"] = fees_series["Timestamp"].astype(str)
    st.line_chart(fees_series.set_index("Timestamp"))

    # Transaction Type Distribution
    st.subheader("Transaction Type Distribution")

    tx_dist = transaction_type_distribution(df)          
    tx_dist_sorted = tx_dist.sort_values(ascending=False) 

    
    tx_dist_df = tx_dist_sorted.reset_index()
    tx_dist_df.columns = ["Transaction Type", "Count"]

    st.bar_chart(tx_dist_df.set_index("Transaction Type"))

    # Top Fees
    st.subheader("Top 5 Fees")
    top_fees_df = top_fees(df, n=5)[["Notes", "Fees and/or Spread_clean"]]
    top_fees_df_sorted = top_fees_df.sort_values(by="Fees and/or Spread_clean", ascending=True)
    st.bar_chart(top_fees_df_sorted.set_index("Notes"))
