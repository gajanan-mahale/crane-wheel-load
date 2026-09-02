import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wheel Load - M5", layout="wide")
st.title("Single Girder Crane - Wheel Load Calc for M5")

try:
    df = pd.read_excel("crane_data.xlsx", sheet_name="SG TABLE")
    df = df[['SWL_kg','Span_M','Girder_kg','Crane_kg']].dropna()
    df['SWL_kg'] = df['SWL_kg'].astype(int)
    df['Span_M'] = df['Span_M'].astype(int)

    st.write("Sheet loaded OK", df.head(3))
    st.markdown("---")
    st.subheader("Wheel Load Calculation")

    swl_options = [1000,2000,3000,5000,7500,10000]
    def format_swl(x):
        t = {1000:"1T",2000:"2T",3000:"3T",5000:"5T",7500:"7.5T",10000:"10T"}
        return f"{x} kg ({t.get(x,str(x/1000)+'T')})"

    c1, c2, c3 = st.columns(3)
    swl_input = c1.selectbox("SWL", swl_options, format_func=format_swl, index=0)
    span = c2.select_slider("Span m", options=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,30], value=20)
    approach = c3.number_input("Min Hook Approach m", 0.5, 3.0, 1.0, step=0.1)

    filt = df[(df['SWL_kg']==swl_input) & (df['Span_M']==span)]
    if filt.empty:
        st.warning(f"No exact data for {swl_input}kg - {span}M, using nearest span")
        temp = df[df['SWL_kg']==swl_input]
        filt = temp.iloc[(temp['Span_M']-span).abs().argsort()[:1]]

    girder_kg = float(filt.iloc[0]['Girder_kg'])
    crane_kg = float(filt.iloc[0]['Crane_kg'])
    crab_kg = swl_input * 0.1
    wheels = 4

    Live_Load = (swl_input + crab_kg)
    R_max_end = Live_Load * (span - approach) / span + crane_kg/2
    R_min_end = Live_Load * approach / span + crane_kg/2
    max_wheel = R_max_end / (wheels/2)
    min_wheel = R_min_end / (wheels/2)
    Horiz_load = 0.05 * Live_Load
    Longi_load = 0.05 * (crane_kg + swl_input)

    st.markdown("---")
    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Girder wt", f"{girder_kg:.0f} kg")
    k2.metric("Crane wt", f"{crane_kg:.0f} kg")
    k3.metric("Crab wt", f"{crab_kg:.0f} kg")
    k4.metric("Live_Load", f"{Live_Load:.0f} kg")

    st.success(f"MAX Static LT Wheel load without impact = {max_wheel:.0f} kg")
    st.info(f"MIN static LT Wheel load= {min_wheel:.0f} kg")
    st.success(f"Horizontal load = {Horiz_load:.0f} kg")
    st.info(f"Longitudinal load= {Longi_load:.0f} kg")

except Exception as e:
    st.error(f"Error: {e}")
