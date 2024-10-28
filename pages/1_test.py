import pandas as pd
import streamlit as st

df = pd.read_csv("./pages/data_balita.csv")

st.write(df)
