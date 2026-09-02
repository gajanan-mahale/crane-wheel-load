import streamlit as st

st.set_page_config(page_title="Code Crane Tools", layout="wide")
st.title("Code Crane - Crane Design Suite")
st.markdown("---")

st.write("All your crane calculators at one place.")

st.subheader("🏗️ 1. Wheel Load Calc")
st.write("Single Girder M5 Wheel load")

if st.button("Open Wheel Load Calculator", type="primary"):
    st.switch_page("pages/1_Wheel_Load.py")

st.markdown("---")
st.caption("Gajanan Mahale Pune - Use sidebar menu also")
