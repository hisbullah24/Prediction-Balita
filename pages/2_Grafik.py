import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = "./data_balita.csv"

st.title("Grafik Stunting")
st.write("Dibawah ini adalah diagram anak laki-laki dan perempuan yang telah di kluster dalam 4 kondisi stunting")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    fig = px.sunburst(
        df,
        path=['jenis_kelamin', 'status_gizi'],
        values=None,                          
        color_discrete_sequence=['#f66095', '#2bcdc1']
    )

    st.plotly_chart(fig)
else:
    st.error("File tidak ditemukan di folder yang ditentukan.")

st.caption("Keterangan :")
st.caption("Tinggi : Anak yang tinggi badannya sangat tinggi (diatas rata-rata)")
st.caption("Normal : Anak yang tinggi badannya normal")
st.caption("Stunted : Anak yang tinggi badannya pendek")
st.caption("Severely Stunted : Anak yang tinggi badannya sangat pendek")

st.write("Dibawah ini adalah grafik jumlah anak dari setiap umur bulannya")

# Membuat grafik garis distribusi umur
plt.figure(figsize=(6, 4))

# Menghitung distribusi umur untuk plot garis
age_counts = df['umur'].value_counts().sort_index()
sns.lineplot(x=age_counts.index, y=age_counts.values, color='#91008a')

# Menambahkan judul dan label
plt.title('Distribusi Umur Balita')
plt.xlabel('Umur (Bulan)')
plt.ylabel('Frekuensi')

# Menampilkan plot di Streamlit
st.pyplot(plt)