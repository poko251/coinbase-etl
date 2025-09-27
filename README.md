Coinbase Stats Dashboard

Interactive dashboard for analyzing personal **Coinbase transactions**.  
The project combines a simple **ETL pipeline** (load → clean → transform) with **analytical functions** and a **Streamlit dashboard** for visualization.  
Additionally, all functions can be reused in **Jupyter Notebook** for custom analysis.

---

## Features

- **ETL (Extract, Transform, Load)**
  - Load transactions from `data/raw/` or upload CSV directly in the app
  - Clean currency columns (remove "zł", convert to float)
  - Convert timestamps to proper datetime (UTC)

- **Analytics**
  - Total fees, invested and sold amounts
  - Monthly fees aggregation
  - Transaction type distribution
  - Top N biggest fees
  - Average fee per transaction type

- **Streamlit Dashboard**
  - **Overview page**  
    - Key metrics (total fees, total invested, total sold)  
    - Average fees per type (Buy/Sell)  
    - Biggest single fee  
    - Date range of dataset  
  - **Visualizations page**  
    - Monthly fees (line chart)  
    - Transaction type distribution (bar chart)  
    - Top fees (bar chart)  
  - **Download clean dataset as CSV**

- **Jupyter Notebook**
  - Direct use of `src/etl.py`, `src/analysis.py`, and `src/viz.py` functions  
  - Custom plots and analyses outside of Streamlit

---