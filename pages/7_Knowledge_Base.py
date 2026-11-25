import streamlit as st


st.set_page_config(page_title="Knowledge Base", page_icon="📚", layout="wide")
st.title("📚 Knowledge Base Hub - Step-by-Step Learning Path")
st.markdown("This six-stage learning journey progresses from economic foundations through banking, investing, alternative assets, and retirement strategies.")

st.markdown("### Macroeconomics - Understanding the Economy")
tabs = st.tabs(["Macroeconomics - Understanding the Economy"])
with tabs[0]:
    st.write("Understand GDP, inflation, interest rates, fiscal policy, monetary policy, and the business cycle.")

st.markdown("### Banking Basics + Credit Markets")
tabs = st.tabs(["Banking Basics - Savings & Accounts", "Credit Markets - How Money Flows"])
with tabs[0]:
    st.write("Review checking, savings, CDs, liquidity, deposit insurance, and account planning.")
with tabs[1]:
    st.write("Explore bonds, credit spreads, central-bank policy, and borrowing costs.")

st.markdown("### Securities Overview + Market Investing")
tabs = st.tabs(["Securities Overview - Stocks, Bonds, ETFs, Mutual Funds", "Market Investing - Investment Vehicles"])
with tabs[0]:
    stock_tabs = st.tabs(["Stocks Guide - Equity Investing", "Bonds Guide - Fixed Income", "Mutual Funds Guide - Pooled Investment", "ETFs Guide - Exchange-Traded Funds"])
    stock_tabs[0].write("Stocks represent ownership in companies.")
    stock_tabs[1].write("Bonds are fixed-income obligations with principal, coupon, maturity, and credit risk.")
    stock_tabs[2].write("Mutual funds pool investor assets under a manager or index strategy.")
    stock_tabs[3].write("ETFs provide exchange-traded, diversified exposure and require tax and liquidity review.")
with tabs[1]:
    st.write("Compare active and passive investing, diversification, costs, and long-term asset allocation.")

st.markdown("### Alternative Investments")
tabs = st.tabs(["Precious Metals - Alternative Asset Class", "Real Estate - Property Investing"])
with tabs[0]:
    st.write("Gold and silver can serve as diversifiers, but premiums, storage, bid-ask spreads, and tax treatment matter.")
with tabs[1]:
    st.write("Real estate analysis includes net operating income, net yield, ownership share, maintenance, and liquidity.")

st.markdown("### Retirement + S&P 500 + All Weather Portfolio")
tabs = st.tabs(["Retirement Planning - 401(k), IRA, Pensions", "S&P 500 Guide - Index Investing", "All Weather Portfolio - Dalio's Strategy"])
with tabs[0]:
    st.write("Compare employer plans, IRAs, pensions, withdrawal rules, and tax location.")
with tabs[1]:
    st.write("The S&P 500 is a large-cap U.S. equity benchmark, not a complete global portfolio.")
with tabs[2]:
    st.write("The All Weather framework emphasizes diversification across economic growth and inflation regimes.")

st.markdown('<div style="text-align: center;"><small>Last updated: March 2026 | Total Modules: 10</small></div>', unsafe_allow_html=True)
