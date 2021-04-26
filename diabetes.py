import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

# load model
diab_model = load_model('diabetes_pred.h5')

def app():
    st.markdown(f"<div id='Diabetes'></div>", unsafe_allow_html=True)
    st.header('You are making prediction for Diabetes')
    a = st.number_input('Your age in Years')
    alopecia = st.selectbox("Alopecia - Sudden loss of hair that starts with one or more circular ", ("Yes","No"))
    if alopecia == "Yes":
        alopecia =1
    else:
        alopecia = 0
    polyuria = st.selectbox("Polyuria - Excessive Urination", ("Yes","No"))
    if polyuria == "Yes":
        polyuria =1
    else:
        polyuria = 0
    polydipsia = st.selectbox("Polydipsia - Abnormal increase in thirst", ("Yes","No"))
    if polydipsia == "Yes":
        polydipsia =1
    else:
        polydipsia = 0
    sex = st.selectbox("Sex", ("Male","Female"))
    if sex == "Male":
        sex =1
    else:
        sex = 0
    itching = st.selectbox("Itching - Dry itchy skin", ("Yes","No"))
    if itching == "Yes":
        itching =1
    else:
        itching = 0

    delayed_healing = st.selectbox("Delayed healing", ("Yes","No"))
    if delayed_healing == "Yes":
        delayed_healing =1
    else:
        delayed_healing = 0
    irritability = st.selectbox("Irritability - Rapid changes in Mode", ("Yes","No"))
    if irritability == "Yes":
        irritability =1
    else:
        irritability = 0

    dfd = pd.DataFrame(np.array([[a, alopecia, polyuria, polydipsia, sex, itching,	delayed_healing, irritability]]),
    columns=['Age',	'Alopecia',	'Polyuria',	'Polydipsia',	'Gender',	'Itching',	'delayed healing',	'Irritability'])
    # st.write(dfd)
    if st.button('Predict Diabetes'): 
        predd = diab_model.predict(dfd)
        if predd > 0.5:
            st.info('This patient is at risk of Diabetes! With a probability of: {}'.format(predd[0][0]) )
        else:
            st.info('This patient is not at risk of Diabetes! With a probability of: {}'.format(predd[0][0]) )