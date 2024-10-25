import streamlit as st
import pickle

st.title('Prediction Stunting Toddler')

gender = st.radio(
    "What's your kids gender",
    ["Laki-laki :male:", "Perempuan :female:"],
    index=None,
)

st.write("You selected:", gender)
