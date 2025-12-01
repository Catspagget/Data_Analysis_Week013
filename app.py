import streamlit as st
import pandas as pd 
import numpy as np 
from Prediction import predict

st.title('Classifying Iris Flowers')
st.markdown('Toy model to play classify iris flowers into \
            (setosa,versicolor,virginica) based on their sepal/petal \
            and length/width')

st.header("Plant Features")
col1,col2 = st.columns(2)

with col1:
    st.text("Sepal Characteristics")
    sepal_l = st.slider("sepal lenght (cm)",1.2,8.0,0.5)
    sepal_w = st.slider('sepal width (cm)',2.0,4.4,0.5)

with col2:
    st.text("Pepal Characteristics")
    petal_l = st.slider("petal lenght (cm)",1.0,7.0,0.5)
    petal_w = st.slider("petal width (cm)",0.1,2.5,0.5)

st.text('')
if st.button("Predict type of Iris"):
            result = predict(
                        np.array([[sepal_l,sepal_w,petal_l,petal_w]]))
            st.text(result[0])

st.text('')
st.text('')
st.markdown()
