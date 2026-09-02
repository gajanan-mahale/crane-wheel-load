import streamlit as st

st.set_page_config(page_title="CranEdge Tools", layout="wide")
st.title("CranEdge - Crane Design Suite")
st.markdown("---")

st.write("Welcome! All your crane calculators at one place.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🏗️ 1. Wheel Load Calc")
    st.write("Single Girder M5 Wheel load with SG Table")
    st.info("👉 Go to left sidebar and click on '1_Wheel_Load'")
    
with col2:
    st.subheader("🔧 More Tools")
    st.write("Girder Design, Cost, etc - Coming soon")

st.markdown("---")
st.caption("Nagpur | Works on Mobile")

st.sidebar.success("Select a tool above")
