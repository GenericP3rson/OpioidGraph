import streamlit as st
import pandas as pd

st.title('Opioid Visulisations')

df = pd.read_csv("NPI_Location.csv")
# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
st.map(df)
