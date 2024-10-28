import gdown
import pickle
import numpy as np
import streamlit as st

# Google Drive file ID
file_id = "1RNd9oQZhzQWRFVqQhXO0ggAOAMSaKKao"

# Download model file
url = f"https://drive.google.com/file/d/1RNd9oQZhzQWRFVqQhXO0ggAOAMSaKKao"
output = "model_stunting.pkl"
gdown.download(url, output, quiet=False)

# Load the model
with open(output, "rb") as file:
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
