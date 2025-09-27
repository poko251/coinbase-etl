import streamlit as st
from src.analysis import (
    total_fees, total_invested, get_date_range,
    total_by_type, average_fee_of_transaction_type, top_fees
)

st.title("📊 Overview")

if "df" not in st.session_state:
    st.warning("Please load data first on the main page.")
else:
    df = st.session_state["df"]

    min_date, max_date = get_date_range(df)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Fees", f"{total_fees(df):.2f} PLN")
    with col2:
        st.metric("Total Invested (Buy)", f"{total_invested(df):.2f} PLN")
    with col3:
        st.metric("Total Sold (Sell)", f"{total_by_type(df, 'Sell'):.2f} PLN")

    col4, col5 = st.columns(2)
    with col4:
        st.metric("Average Fee (Buy)", f"{average_fee_of_transaction_type(df, 'Buy'):.2f} PLN")
    with col5:
        st.metric("Average Fee (Sell)", f"{average_fee_of_transaction_type(df, 'Sell'):.2f} PLN")

    # Biggest single fee
    biggest_fee = top_fees(df, n=1)[["Notes", "Fees and/or Spread_clean"]]
    st.write("💸 **Biggest Fee:**")
    st.dataframe(biggest_fee)

    # Date range
    st.write(f"**Date range:** {min_date.date()} → {max_date.date()}")
    st.subheader("Sample of Data")
    st.dataframe(df.head())
