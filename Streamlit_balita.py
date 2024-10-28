import streamlit as st
import pickle

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title('Prediction Stunting Toddler')

st.sidebar.success("Select a demo above.")

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
