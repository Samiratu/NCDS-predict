import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

# load model
heart_model = load_model('heart_pred.h5')

def app():
    st.markdown(f"<div id='Heart Diseases'></div>", unsafe_allow_html=True)
    # st.title('Heart Diseases')
    st.header('You Detecting for Risk of Heart Disease')
    age = st.number_input('Age in years')
    thalach = st.number_input('Maximum heart rate achieved - e.g 71, 202, 152')
    oldpeak = st.number_input('ST depression induced by exercise relative to rest looks at stress of heart during excercise unhealthy heart will stress more - e.g 2.3', min_value=0.0, step= 1.0)
    ca = st.number_input('number of major vessels colored by flourosopy - e.g 0 - 3')
    chol = st.number_input('Serum cholestoral in mg/dl- e.g 100')
    trestpbs = st.number_input('resting blood pressure in mm Hg on admission to the hospital- e.g 115')
    st.header('Chest Pain Types')
    st.write('0: Typical angina: chest pain related decrease blood supply to the heart')
    st.write('1: Atypical angina: chest pain not related to heart')
    st.write('2: Non-anginal pain: typically esophageal spasms (non heart related)')
    st.write('3: Asymptomatic: chest pain not showing signs of disease')
    cp = st.number_input('Chest Pain Type', 0,3,0)
    gender = st.selectbox("Gender", ("Male","Female"))
    if gender == "Male":
        gender =1
    else:
        gender = 0
    st.write(gender)
    dfh = pd.DataFrame(np.array([[age, thalach, oldpeak, ca, chol, trestpbs, cp, gender]]),
    columns=['age', 'thalach', 'oldpeak','ca','chol', 'trestbps','cp','sex'])
    # st.write(dfh)
    # dfh = scaler.fit_transform(dfh)
    # st.write(dfh)
    if st.button('Predict Heart Disease'):
        predh = heart_model.predict(dfh)
        if predh > 0.5:
            st.info('This patient is at risk of Heart disease! With a probability of: {}'.format(predh[0][0]) )
        else:
            st.info('This patient is not at risk of Heart disease! With a probability of: {}'.format(predh[0][0]))