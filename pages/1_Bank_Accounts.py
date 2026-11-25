import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from utils.banking import (
    calculate_cd_maturity,
    calculate_future_value,
    calculate_present_value,
    latest_checking_balances,
    normalize_savings_accounts,
)
from utils.local_data import (
    read_checking_accounts,
    read_savings_accounts,
    read_cd_accounts,
    read_local_csv,
)


st.set_page_config(page_title="Bank Accounts", page_icon="🏦", layout="wide")
st.title("🏦 Bank Accounts")

checking = read_checking_accounts()
latest = latest_checking_balances(checking)

st.markdown("### 💰 Checking Accounts")
left, right = st.columns([2, 1])
with left:
    st.dataframe(latest, use_container_width=True, hide_index=True)
with right:
    st.metric("Total Ending Balance", f"${latest['Ending Balance'].sum():,.2f}")

st.markdown("### Checking Account Ending Balance Trend")
trend = checking.copy()
month_order = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
               "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
trend["__month"] = trend["Month"].map(month_order)
trend["__date"] = pd.to_datetime(trend["Year"].astype(str) + "-" + trend["__month"].astype(str) + "-01")
trend = trend.sort_values(["Account Name", "__date"])
fig = go.Figure()
for account, rows in trend.groupby("Account Name"):
    fig.add_trace(go.Scatter(x=rows["__date"], y=rows["Ending Balance"], mode="lines+markers", name=account))
fig.update_layout(title="Checking Account Ending Balance Trends", template="plotly_white", xaxis_title="Month", yaxis_title="Ending Balance")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 🏪 Savings Accounts")
savings = normalize_savings_accounts(read_savings_accounts())
left, right = st.columns([2, 1])
with left:
    st.dataframe(savings, use_container_width=True, hide_index=True)
with right:
    st.metric("Total Savings Balance", f"${savings['Balance'].sum():,.2f}")

st.markdown("### 💳 Certificate of Deposit (CD) Accounts")
cds = read_cd_accounts()
cd_rows = []
for row in cds.itertuples(index=False):
    from decimal import Decimal
    principal = Decimal(str(row.Principal))
    apy = Decimal(str(row.APY))
    term_months = int(row[3])
    maturity = calculate_cd_maturity(principal, apy, term_months)
    interest = maturity - principal
    cd_rows.append({
        "Bank": row.Bank,
        "Principal": f"${principal:,.2f}",
        "APY": f"{apy:.2f}%",
        "Term": f"{term_months} months",
        "Interest Earned": f"${interest:,.2f}",
        "Maturity Value": f"${maturity:,.2f}",
        "Annual Yield": f"{apy:.2f}%",
        "Maturity Date": str(row[4]),
    })
st.dataframe(pd.DataFrame(cd_rows), use_container_width=True, hide_index=True)

if cd_rows:
    principals = cds["Principal"].astype(float)
    apys = cds["APY"].astype(float)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total CD Principal", f"${principals.sum():,.2f}")
    c2.metric("Total Interest to Earn", f"${sum(Decimal(r['Interest Earned'].replace('$', '').replace(',', '')) for r in cd_rows):,.2f}")
    c3.metric("Total Maturity Value", f"${sum(Decimal(r['Maturity Value'].replace('$', '').replace(',', '')) for r in cd_rows):,.2f}")
    c4.metric("Average Rate", f"{apys.mean():.2f}%")

st.markdown("### 📊 Fed Funds vs Inflation vs Savings Rate")
fed = read_local_csv("banking", "fedRate.csv")
inflation = read_local_csv("banking", "inflationRate.csv")
savings_rates = read_local_csv("banking", "savingsIntrestRate.csv")
for frame in (fed, inflation, savings_rates):
    frame["Date"] = pd.to_datetime(frame["Date"])
comparison = go.Figure()
comparison.add_trace(go.Scatter(x=fed["Date"], y=fed["Federal Funds Rate"], mode="lines", name="Fed Funds Rate"))
comparison.add_trace(go.Scatter(x=inflation["Date"], y=inflation["Inflation Rate"], mode="lines", name="Inflation Rate"))
comparison.add_trace(go.Scatter(x=savings_rates["Date"], y=savings_rates["Savings Interest Rate"], mode="lines", name="Savings Account Interest Rates"))
comparison.update_layout(template="plotly_white")
st.plotly_chart(comparison, use_container_width=True)

calculation = st.radio("What would you like to calculate?", ["Future Value (PV → FV)", "Present Value (FV → PV)"], horizontal=True, key="converter_type")
compound_options = ["Annually", "Semi-Annually", "Quarterly", "Monthly", "Daily"]
frequency = {"Annually": 1, "Semi-Annually": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365}

if calculation == "Future Value (PV → FV)":
    pv = st.number_input("Present Value ($)", value=10000.0, min_value=0.0, step=100.0)
    rate = st.number_input("Annual Rate (%)", value=4.5, min_value=0.0, max_value=20.0, step=0.01)
    years = st.number_input("Years", value=5.0, min_value=0.0, max_value=50.0, step=0.5)
    compound = st.selectbox("Compound", compound_options, index=0)
    from decimal import Decimal
    future = calculate_future_value(Decimal(str(pv)), Decimal(str(rate)), Decimal(str(years)), frequency[compound])
    interest = future - Decimal(str(pv))
    m1, m2, m3 = st.columns(3)
    m1.metric("Future Value", f"${future:,.2f}")
    m2.metric("Interest Earned", f"${interest:,.2f}")
    m3.metric("Total Return", f"{(interest / Decimal(str(pv)) * 100):,.2f}%" if pv else "0.00%")
else:
    fv = st.number_input("Future Value ($)", value=15000.0, min_value=0.0, step=100.0)
    rate = st.number_input("Annual Rate (%)", value=4.5, min_value=0.0, max_value=20.0, step=0.01)
    years = st.number_input("Years", value=5.0, min_value=0.0, max_value=50.0, step=0.5)
    compound = st.selectbox("Compound", compound_options, index=0)
    from decimal import Decimal
    present = calculate_present_value(Decimal(str(fv)), Decimal(str(rate)), Decimal(str(years)), frequency[compound])
    needed = Decimal(str(fv)) - present
    m1, m2, m3 = st.columns(3)
    m1.metric("Present Value", f"${present:,.2f}")
    m2.metric("Interest Needed", f"${needed:,.2f}")
    m3.metric("Interest Percentage", f"{(needed / Decimal(str(fv)) * 100):,.2f}%" if fv else "0.00%")

st.markdown('<div style="text-align: center;"><small>All calculations are estimates. Actual results may vary based on bank policies and market conditions.</small></div>', unsafe_allow_html=True)
