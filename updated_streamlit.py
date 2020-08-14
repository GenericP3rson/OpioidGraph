import streamlit as st
import pandas as pd
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir("streamlit_csv")
             if isfile(join("streamlit_csv", f))]


# st.title('Opioid Visulisations')

for i in onlyfiles[:3]:
    st.title(" ".join(i[:-3].split(".")))
    df = pd.read_csv("streamlit_csv/" + i)
    # df = pd.DataFrame(
    #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #     columns=['lat', 'lon'])
    # print(df)
    st.map(df)
