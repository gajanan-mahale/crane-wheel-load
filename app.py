import streamlit as st

st.set_page_config(page_title="CranEdge Tools", layout="wide")
st.title("CranEdge - Crane Design Suite")
st.markdown("---")

st.write("Welcome! All your crane calculators at one place.")

col1, col2 = st.columns(2)
with col1:
    st.info("**1. Wheel Load Calc**\n\nSingle Girder M5 Wheel load with SG Table")
    st.page_link("pages/1_Wheel_Load.py", label="Open Wheel Load", icon="🏗️")
with col2:
    st.info("**2. More Tools Coming...**\n\nGirder Design, Cost, etc")
    
st.markdown("---")
st.caption("Nagpur | Works on Mobile")
