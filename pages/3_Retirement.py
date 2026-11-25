import streamlit as st


st.set_page_config(page_title="Retirement", page_icon="🎯", layout="wide")
st.title("🎯 Retirement Planning")
st.info("Retirement planning uses planning assumptions until the retirement ledger is implemented.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Planning Horizon", "30 years")
col2.metric("Target Income", "TBD", help="Set after account balances and spending goals are loaded")
col3.metric("Account Coverage", "Not yet consolidated")
col4.metric("Currency", "USD / INR")

st.markdown("### Retirement Accounts")
st.info("Connect 401(k), IRA, pension, PPF, EPF, and NPS balances through future ledger imports.")

st.markdown("### Planning Checklist")
for item in (
    "Estimated annual retirement spending",
    "Retirement age and location",
    "Social Security / pension income",
    "Healthcare costs",
    "Asset allocation and withdrawal rate",
):
    st.checkbox(item)

st.markdown('<div style="text-align: center;"><small>Planning estimates are not financial advice.</small></div>', unsafe_allow_html=True)
