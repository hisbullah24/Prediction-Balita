import streamlit as st
import pandas as pd
import plotly.express as px

uploaded_file = pd.read_csv("./data_balita.csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("Data CSV:", df.head())

    fig = px.sunburst(
        df,
        path=['jenis_kelamin', 'status_gizi'],  
        values=df.value_counts().values,        
        color_discrete_sequence=['#f66095', '#2bcdc1']
    )

    st.plotly_chart(fig)
