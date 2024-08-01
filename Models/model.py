import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

dataset =  pd.read_csv("cleaned_dataset.csv")
st.dataframe(dataset, width=1000,height=500)
# st.table(dataset)
# st.write(dataset)
st.line_chart(dataset)