from decimal import Decimal

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from utils.loan import build_amortization_schedule, calculate_monthly_payment


st.set_page_config(page_title="Loan Repayment Calculator", page_icon="💳", layout="wide")
st.title("💳 Loan Repayment Calculator")

tab1, tab2, tab3 = st.tabs(["Single Loan Calculator", "Amortization Schedule", "Loan Comparison"])

with tab1:
    principal = st.number_input("Loan Amount ($)", value=200000.0, min_value=0.0, step=1000.0, key="single_principal")
    rate = st.number_input("Annual Interest Rate (%)", value=5.5, min_value=0.0, max_value=100.0, step=0.01, key="single_rate")
    years = st.number_input("Loan Duration (Years)", value=30.0, min_value=0.0, step=1.0, key="single_years")
    if years:
        payment = calculate_monthly_payment(Decimal(str(principal)), Decimal(str(rate)), int(years))
        schedule = build_amortization_schedule(Decimal(str(principal)), Decimal(str(rate)), int(years))
        total_paid = sum(row["payment"] for row in schedule)
        total_interest = total_paid - Decimal(str(principal))
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Monthly Payment", f"${payment:,.2f}")
        m2.metric("Total Interest", f"${total_interest:,.2f}")
        m3.metric("Total Amount Paid", f"${total_paid:,.2f}")
        m4.metric("Interest as % of Principal", f"{total_interest / Decimal(str(principal)) * 100:.2f}%" if principal else "0.00%")
        st.info("Loan Summary")

with tab2:
    principal = st.number_input("Loan Amount ($)", value=200000.0, min_value=0.0, step=1000.0, key="amort_principal")
    rate = st.number_input("Annual Interest Rate (%)", value=5.5, min_value=0.0, max_value=100.0, step=0.01, key="amort_rate")
    years = st.number_input("Loan Duration (Years)", value=30.0, min_value=0.0, step=1.0, key="amort_years")
    show_all = st.checkbox("Show all months", value=False)
    rows = st.number_input("Show first N rows", value=12, min_value=1, step=12, key="amort_rows")
    if years:
        schedule = build_amortization_schedule(Decimal(str(principal)), Decimal(str(rate)), int(years))
        display = schedule if show_all else schedule[:int(rows)]
        frame = pd.DataFrame(display)
        st.dataframe(frame, hide_index=True, use_container_width=True)
        donut = go.Figure(go.Pie(labels=["Principal", "Interest"], values=[float(principal), float(sum(row["interest"] for row in schedule))], hole=0.3))
        st.plotly_chart(donut, use_container_width=True)
        balance = go.Figure(go.Scatter(x=[row["month"] for row in schedule], y=[float(row["balance"] ) for row in schedule], mode="lines", name="Remaining Balance", fill="tozeroy"))
        st.plotly_chart(balance, use_container_width=True)

with tab3:
    principal = st.number_input("Loan Amount ($)", value=200000.0, min_value=0.0, step=1000.0, key="compare_principal")
    rate = st.number_input("Annual Interest Rate (%)", value=5.5, min_value=0.0, max_value=100.0, step=0.01, key="compare_rate")
    selections = {}
    first, second, third = st.columns(3)
    selections[5] = first.checkbox("5", value=True)
    selections[10] = first.checkbox("10", value=True)
    selections[15] = second.checkbox("15", value=True)
    selections[20] = second.checkbox("20", value=False)
    selections[30] = third.checkbox("30", value=True)
    custom = third.checkbox("Custom Years", value=False)
    custom_years = st.number_input("Custom Years", value=25, min_value=1, step=1) if custom else None
    if custom_years:
        selections[custom_years] = True

    table = []
    for term, selected in selections.items():
        if selected:
            payment = calculate_monthly_payment(Decimal(str(principal)), Decimal(str(rate)), term)
            schedule = build_amortization_schedule(Decimal(str(principal)), Decimal(str(rate)), term)
            total_paid = sum(row["payment"] for row in schedule)
            total_interest = total_paid - Decimal(str(principal))
            table.append({"Loan Term (Years)": term, "Monthly Payment ($)": float(payment), "Total Interest ($)": float(total_interest), "Total Paid ($)": float(total_paid)})
    if table:
        frame = pd.DataFrame(table)
        st.dataframe(frame, hide_index=True, use_container_width=True)
        payment_chart = go.Figure(go.Scatter(x=frame["Loan Term (Years)"], y=frame["Monthly Payment ($)"], mode="lines", line={"color": "#1f77b4", "width": 3}))
        payment_chart.update_layout(title="Monthly Payment vs Loan Duration")
        st.plotly_chart(payment_chart, use_container_width=True)
        interest_chart = go.Figure(go.Scatter(x=frame["Loan Term (Years)"], y=frame["Total Interest ($)"], mode="lines", fill="tozeroy", line={"color": "#ff7f0e", "width": 3}))
        interest_chart.update_layout(title="Total Interest vs Loan Duration")
        st.plotly_chart(interest_chart, use_container_width=True)

st.markdown('<div style="text-align: center;"><small>All calculations are estimates. Actual results may vary based on lender terms and market conditions.</small></div>', unsafe_allow_html=True)
