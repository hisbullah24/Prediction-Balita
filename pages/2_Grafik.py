import streamlit as st
import pandas as pd
import plotly.express as px

# File uploader untuk Streamlit
uploaded_file = st.file_uploader("./data_balita.csv", type="csv")

if uploaded_file is not None:
    # Membaca dataset dari CSV yang diunggah
    df = pd.read_csv(uploaded_file)

    # Menampilkan data CSV untuk konfirmasi
    st.write("Data CSV:", df.head())

    # Membuat grafik sunburst
    fig = px.sunburst(
        df,
        path=['jenis_kelamin', 'status_gizi'],  # Kolom hierarki
        values=None,                            # Optional: Anda bisa menggunakan 'size' atau 'count'
        color_discrete_sequence=['#f66095', '#2bcdc1']
    )

    # Tampilkan grafik di Streamlit
    st.plotly_chart(fig)
