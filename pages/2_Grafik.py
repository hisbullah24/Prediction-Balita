import streamlit as st
import pandas as pd
import plotly.express as px

uploaded_file = st.file_uploader("./data_balita.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    fig = px.sunburst(
        df,
        path=['jenis_kelamin', 'status_gizi'],
        values=None,                          
        color_discrete_sequence=['#f66095', '#2bcdc1']
    )

    st.plotly_chart(fig)
