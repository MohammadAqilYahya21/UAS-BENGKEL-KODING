# -*- coding: utf-8 -*-
"""stream-heart-disease

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13QgvT39QMfkXTbUT0JlGwPipzm66SRXs
"""

!pip install -q streamlit

import pickle
import streamlit as st

#membaca load model
heartdisease_model = pickle.load(open('heart_disease_model.pkl', 'rb'))

#judul web
st.title('Heart Disease Prediction')