import pickle
import numpy as np
import streamlit as st

with open('model_stunting(1).pkl', 'rb') as file:
    models = pickle.load(file)
    
clf1 = models['LightGBM']['model']
clf2 = models['XGBoost']['model']
akurasi_clf1 = models['LightGBM']['accuracy']
akurasi_clf2 = models['XGBoost']['accuracy']

st.title('Prediction Stunting Toddler')

#input
jenis_kelamin = st.radio(
    "Apa jenis kelamin anak kamu?",
    ["***Laki-laki***", "***Perempuan***"],
    index=None,
)

st.write("Gender anakmu:", jenis_kelamin)

umur_bulan = st.slider("Berapa bulan umur anak anda?", 0, 60, 30)
st.write("Anak anda berumur ", umur_bulan, "Bulan")

tinggi_badan = st.slider("Berapa tinggi anak anda?", 0, 150, 75                                                           )
st.write("Tinggi anak anda ", tinggi_badan, "cm")

gender_binary = 0 if jenis_kelamin == "Laki-laki" else 1

model_choice = st.selectbox("Pilih Model untuk Prediksi", ["LightGBM", "XGBoost"])

if st.button ("Prediksi"):
    input_data = np.array([[gender_binary, umur_bulan, tinggi_badan]])
    
    if model_choice == "LightGBM":
        prediction = clf1.predict(input_data)
        accuracy = akurasi_clf1
    elif model_choice == "XGBoost":
        prediction = clf2.predict(input_data)
        accuracy = akurasi_clf2
    
    status_mapping = {
        0: "Tinggi badan anak diatas rata - rata",
        1: "Tinggi badan anak normal",
        2: "Tinggi badan anak kurang (terkena gejala stunting)",
        3: "TInggi badan anak sangat kurang (terkena gejala stunting parah)"
    }
    
    status = status_mapping.get(prediction[0], "Unknown")
    st.write(f"Hasil Prediksi : Balita termasuk dalam kategori **{status}**.")
    st.write(f"Akurasi dari model **{model_choice}**: {accuracy*100:.2f}%")
