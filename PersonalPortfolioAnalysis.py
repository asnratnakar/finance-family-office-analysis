import streamlit as st


st.set_page_config(
    page_title="Personal Finance Analysis",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    "<style>.main {padding: 0rem 0rem !important;}</style>",
    unsafe_allow_html=True,
)

st.title("💰 Personal Finance Analysis")
st.markdown("# Welcome to Personal Financial Analysis Dashboard")

st.info("Tip: You can upload your own CSV files or use sample data to get started!")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Metal Investment Performance")
with col2:
    st.subheader("Sector-wise Investment Analysis")
with col3:
    st.subheader("Loan Repayment Calculator")

st.markdown(
    '<div style="text-align: center;"><small>Personal Finance Analysis Tool | Built with Streamlit | v1.0</small></div>',
    unsafe_allow_html=True,
)
