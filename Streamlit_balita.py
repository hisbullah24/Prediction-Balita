import streamlit as st
import pickle

st.title('Prediction Stunting Toddler')

gender = st.radio(
    "Apa jenis kelamin anak kamu?",
    ["***Laki-laki***", "***Perempuan***"],
    index=None,
)

st.write("You selected:", gender)

umur = st.slider("Berapa bulan umur anak anda?", 0, 130, 25)
st.write("Anak anda berumur ", umur, "Bulan")
