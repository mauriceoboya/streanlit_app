import  streamlit as st
import pandas as pd
import numpy as np
st.write('Diabetes dynamics visualization')

dataset=pd.read_csv('diabetes.csv')

chart_data=pd.DataFrame(dataset,columns=['Pregnancies','BMI'])
st.bar_chart(chart_data)
st.dataframe(dataset)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)