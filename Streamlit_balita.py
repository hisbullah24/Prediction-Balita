import streamlit as st
import pickle

st.title('Prediction Stunting Toddler')

gender = st.radio(
    "Apa jenis kelamin anak kamu?",
    ["***Laki-laki***", "***Perempuan***"],
    index=None,
)

st.write("You selected:", gender)

umur = st.slider("Berapa bulan umur anak anda?", 0, 60, 30)
st.write("Anak anda berumur ", umur, "Bulan")

col1, col2 = st.columns(2)
col1.write('Column 1 Content')
col2.write('Column 2 Content')
