import pickle
import numpy as np
import streamlit as st

with open('model_stunting.pkl', 'rb') as file:
    models = pickle.load(file)
    
clf1 = models['clf1']
clf2 = models['clf2']

st.title('Prediction Stunting Toddler')

#input
gender = st.radio(
    "Apa jenis kelamin anak kamu?",
    ["***Laki-laki***", "***Perempuan***"],
    index=None,
)

st.write("Gender anakmu:", gender)

umur = st.slider("Berapa bulan umur anak anda?", 0, 60, 30)
st.write("Anak anda berumur ", umur, "Bulan")

tinggi = st.slider("Berapa tinggi anak anda?", 0, 150, 75                                                           )
st.write("Tinggi anak anda ", tinggi, "cm")

gender_binary = 0 if gender == "Laki-laki" else 1

model_choice = st.selectbox("Pilih Model untuk Prediksi", ["LightGBM", "XGBoost"])

if st.button ("Prediksi"):
    input_data = np.array([[gender, umur, tinggi]])
    prediction = model.predict(input_data)
    
    if model_choice == "LightGBM":
        prediction = clf1.predict(input_data)
    elif model_choice == "XGBoost":
        prediction = clf2.predict(input_data)
    
    status_mapping = {
        0: "Tinggi",
        1: "Normal",
        2: "Stunted",
        3: "Severely Stunted"
    }
    
    status = status_mapping.get(prediction[0], "Unknown")
    st.write(f"Hasil Prediksi : Balita termasuk dalam kategori **{status}**.")

