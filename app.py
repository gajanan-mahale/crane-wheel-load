import streamlit as st

st.set_page_config(page_title="Code Crane Tools", layout="wide")

# SIDEBAR MENU - THIS IS THE FIX
with st.sidebar:
    st.title("Code Crane Tools")
    st.markdown("---")
    if st.button("🏗️ Wheel Load Calc", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Wheel_Load.py")
    
    if st.button("🔧 Tool 2 (Soon)", use_container_width=True):
        st.toast("Coming soon")

# MAIN DASHBOARD
st.title("CranEdge - Crane Design Suite")
st.markdown("---")
st.write("Welcome! Select a tool from left sidebar.")

st.info("👈 Click 'Wheel Load Calc' in left sidebar to open")

# Also add center button for mobile users
if st.button("Open Wheel Load - Mobile", type="primary"):
    st.switch_page("pages/1_Wheel_Load.py")
