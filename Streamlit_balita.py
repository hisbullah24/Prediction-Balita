import streamlit as st
import pickle

st.title('Prediction Stunting Toddler')

gender = st.radio(
    "Apa jenis kelamin anak kamu?",
    ["***Laki-laki***", "***Perempuan***"],
    index=None,
)

st.write("Gender anakmu:", gender)

umur = st.slider("Berapa bulan umur anak anda?", 0, 60, 30)
st.write("Anak anda berumur ", umur, "Bulan")

tinggi = st.slider("Berapa tinggi anak anda?", 0, 150, 0)
st.write("Tinggi anak anda ", tinggi, "cm")
