from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.local_data import read_metal_spot_prices, read_metal_transactions


st.set_page_config(page_title="Metals", page_icon="🧈", layout="wide")
st.title("🧈 Metals Investment Performance Analysis")

st.sidebar.header("Data Source")
data_source = st.sidebar.radio("Data Source", ["Local Data (metals_transactionHistory.csv)", "Upload CSV"])

if data_source == "Upload CSV":
    uploaded = st.sidebar.file_uploader("Upload CSV", type="csv", help="CSV should have columns: Date, Metal, Cost, Quantity_oz")
    transactions = pd.read_csv(uploaded) if uploaded is not None else pd.DataFrame(columns=["Date", "Metal", "Cost", "Quantity_oz"])
else:
    transactions = read_metal_transactions()

allocation = transactions.groupby("Metal", as_index=False).agg(Cost=("Cost", "sum"), Quantity_oz=("Quantity_oz", "sum"))
spots = read_metal_spot_prices().set_index("Metal")["PricePerOz"]
allocation["Market Value"] = allocation.apply(lambda row: float(row["Quantity_oz"]) * float(spots.get(row["Metal"], 0)), axis=1)
allocation["% Growth"] = allocation.apply(lambda row: (row["Market Value"] - row["Cost"]) / row["Cost"] * 100 if row["Cost"] else 0, axis=1)
allocation["Unrealized Gains/Loss"] = allocation["Market Value"] - allocation["Cost"]

left, right = st.columns(2)
colors = {"Gold": "rgb(255, 215, 0)", "Silver": "rgb(192, 192, 192)"}
for column, field, title in ((left, "Market Value", "Market Value Allocation"), (right, "Cost", "Cost Allocation")):
    with column:
        fig = px.pie(allocation, values=field, names="Metal", hole=0.3, title=title)
        fig.update_traces(marker={"colors": [colors.get(metal, "lightgray") for metal in allocation["Metal"]]})
        st.plotly_chart(fig, use_container_width=True)

st.dataframe(allocation, hide_index=True, use_container_width=True)

st.markdown("### 💲Current Live Metal Prices")
gold = spots.get("Gold")
silver = spots.get("Silver")
g1, g2 = st.columns(2)
g1.metric("Gold (XAU)", f"${gold:,.2f}" if gold is not None else "Unavailable")
g1.expander("ℹ️ More Details").json({"metal": "Gold", "currency": "USD", "source": "data/metals/metals_spotPrice.csv"})
g2.metric("Silver (XAG)", f"${silver:,.2f}" if silver is not None else "Unavailable")
g2.expander("ℹ️ More Details").json({"metal": "Silver", "currency": "USD", "source": "data/metals/metals_spotPrice.csv"})
st.caption(f"Last update time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.markdown("### 🛒 Metals Procurement Analysis")
for metal in ("Gold", "Silver"):
    frame = transactions[transactions["Metal"] == metal]
    st.markdown(f"#### {metal} Procurement")
    st.dataframe(frame, hide_index=True, use_container_width=True)

st.markdown("### Investment Return")
initial_cost = allocation["Cost"].sum()
market_value = allocation["Market Value"].sum()
c1, c2, c3 = st.columns(3)
c1.metric("Total Cost", f"${initial_cost:,.2f}")
c2.metric("Market Value", f"${market_value:,.2f}")
c3.metric("Unrealized Gain", f"${market_value - initial_cost:,.2f}")

with st.expander("💰 Selling Bullion - Dealer Discount Information"):
    st.write("Dealer discounts and sales tax vary; confirm rates with the bullion dealer before selling.")
with st.expander("📊 View detailed Transaction History"):
    st.dataframe(transactions, hide_index=True, use_container_width=True)
