import streamlit as st

Emission_Factors= :{
  "India": {
    #kgC02 is the unit for carbon emission
    "Transportation": 0.14, #kgCO2/km
    "Electricity":0.82, # kgCO2/KwH
    "Diet": 1.25, #kgCO2 per meal
    "Waste": 0.1 #kgCO2/kg
  }
}

st.title("Carbon Emission Footprint Calculator")
