import pandas as pd
import streamlit as st

df = pd.read_csv("./data_balita.csv")

st.title("Dataset Stunting Toddlers")

st.write("Kumpulan data Deteksi Bayi/Balita Stunting ini didasarkan pada rumus z-score untuk menentukan stunting menurut WHO (Organisasi Kesehatan Dunia), yang berfokus pada deteksi stunting pada anak di bawah usia lima tahun. Kumpulan data ini terdiri dari 121.000 baris data, yang merinci informasi tentang usia, jenis kelamin, tinggi badan, dan status gizi balita. Kumpulan data ini bertujuan untuk membantu para peneliti, ahli gizi, dan pembuat kebijakan memahami dan mengatasi masalah stunting pada anak di bawah usia lima tahun.")

st.write(df)
