from decimal import Decimal

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.local_data import find_latest_vanguard_summary, read_latest_vanguard_summary


st.set_page_config(page_title="Market Investments", page_icon="📈", layout="wide")
st.title("📈 Market Investments - Portfolio Analysis")

summary = read_latest_vanguard_summary()
normalize = {
    "Symbol/CUSIP": "Symbol",
    "Total cost": "Total Cost",
    "Market Value": "Market Value",
    "Total Gain Loss": "Total Gains/Loss",
}
summary = summary.rename(columns=normalize)

total_cost = Decimal(str(summary["Total Cost"].sum()))
market_value = Decimal(str(summary["Market Value"].sum()))
total_gain = market_value - total_cost
return_pct = total_gain / total_cost * Decimal("100") if total_cost else Decimal("0")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Cost", f"${total_cost:,.2f}")
c2.metric("Market Value", f"${market_value:,.2f}")
c3.metric("Total Gains/Loss", f"${total_gain:,.2f}")
c4.metric("Return %", f"{return_pct:.2f}%")

sector = summary.groupby("Sector", dropna=False)["Market Value"].sum().sort_values(ascending=False)
fig_sector = go.Figure(data=[
    go.Pie(labels=sector.index, values=sector.values, hole=.3)
])
fig_sector.update_layout(title_text="Combined Portfolio Allocation")
st.plotly_chart(fig_sector, use_container_width=True)

stocks = summary[summary["Type"] == "Stock"]
etfs = summary[summary["Type"] == "ETF"]
stock_col, etf_col = st.columns(2)

for title, frame, column in (("Stocks", stocks, stock_col), ("ETFs", etfs, etf_col)):
    with column:
        st.markdown(f"### {title}")
        cost = Decimal(str(frame["Total Cost"].sum()))
        gains = Decimal(str(frame["Total Gains/Loss"].sum()))
        value = Decimal(str(frame["Market Value"].sum()))
        a, b = st.columns(2)
        a.metric("Total Cost", f"${cost:,.2f}")
        a.metric("Total Gains", f"${gains:,.2f}")
        b.metric("Market Value", f"${value:,.2f}")
        b.metric("Holdings", len(frame))
        sector_counts = frame.groupby("Sector", dropna=False)["Market Value"].sum()
        pie = go.Figure(data=[
            go.Pie(labels=sector_counts.index, values=sector_counts.values, hole=.3)
        ])
        pie.update_layout(title_text=f"{title} by Sector")
        st.plotly_chart(pie, use_container_width=True)

st.markdown("### Market Value Trend Charts")
trend_files = sorted(find_latest_vanguard_summary().parent.glob("VAN_costbasis_summary_*.csv"))
for title, frame_type in (("Stock Market Value Trends", "Stock"), ("ETF Market Value Trends", "ETF")):
    rows = []
    for path in trend_files:
        dated = pd.read_csv(path)
        dated = dated[dated["Type"] == frame_type]
        report_date = str(dated["Report Date"].iloc[0]) if not dated.empty else path.stem.rsplit("_", 1)[-1]
        for _, row in dated.iterrows():
            rows.append({"Date": report_date, "Symbol/CUSIP": row["Symbol/CUSIP"], "Market Value": row["Market Value"]})
    if rows:
        trend = pd.DataFrame(rows)
        fig = px.line(trend, x="Date", y="Market Value", color="Symbol/CUSIP", title=title)
        st.plotly_chart(fig, use_container_width=True)

st.markdown("### Top Holdings")
left, right = st.columns(2)
with left:
    st.markdown("#### Top Stocks by Market Value")
    st.dataframe(stocks.nlargest(10, "Market Value")[["Symbol", "Company", "Market Value"]], hide_index=True, use_container_width=True)
with right:
    st.markdown("#### Top ETFs by Market Value")
    st.dataframe(etfs.nlargest(10, "Market Value")[["Symbol", "Company", "Market Value"]], hide_index=True, use_container_width=True)

with st.expander("📋 View Full Portfolio Data"):
    st.dataframe(summary, hide_index=True, use_container_width=True)
