# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 05:16:23 2023

@author: USER
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

kidney_model = pickle.load(open('kidney_model.sav','rb'))


# sidebar for navigate

with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           
                           ['Chronic Kidney Prediction'],
                           default_index = 0)
    
    
    
# Predicting Chronic Kidney page

if (selected == 'Chronic Kidney Prediction'):
    
    # page title
    st.title('Chronic Kidney Prediction using ML')
    
    
   # getting the input data from user
    
  
    Age = st.text_input('Age')
    
   
    Blood_Pressure = st.text_input('Blood Pressure')
    
    
    Specific_Gravity = st.text_input('Specific Gravity')
    
   
    Albumin = st.text_input('Albumin')
    
    
    Sugar = st.text_input('Sugar')
    
    
    Red_Blood_Cells = st.text_input('Red Blood Cells')
    
    
    Pus_Cell = st.text_input('Pus Cell')
    
    
    Pus_Cell_Clumps = st.text_input('Pus Cell Clumps')
    
    
    Bacteria = st.text_input('Bacteria')
    
    
    Blood_Glucose_Random = st.text_input('Blood Glucose Random')
    
   
    Blood_Urea = st.text_input('Blood Urea')
    
   
    Serum_Creatinine = st.text_input('Serum Creatinine')
    
    
    Sodium = st.text_input('Sodium')
    
   
    Potassium = st.text_input('Potassium')
    
    
    Hemoglobin = st.text_input('Hemoglobin')
    
   
    Packed_Cell_Volume = st.text_input('Packed Cell Volume')
    
   
    White_Blood_Cell_Count = st.text_input('White Blood Cell Count')
    
   
    Red_Blood_Cell_Count = st.text_input('Red Blood Cell Count')
    
   
    Hypertension = st.text_input('Hypertension')
    
    
    Diabetes_Mellitus = st.text_input('Diabetes Mellitus')
    
   
    Coronary_Artery_Disease = st.text_input('Coronary Artery Disease')
    
  
    Appetite = st.text_input('Appetite')
    
   
    Pedal_Edema = st.text_input('Pedal Edema')
    
   
    Anemia = st.text_input('Anemia')
    
    
    
    # code for Prediction
    kidney_diagnosis = ''
    kidney_prediction = ''
    
    
    
    # creating a button for Prediction
    
    if st.button('Diagnosis Result'):
       kidney_prediction = kidney_model.predict([[Age, Blood_Pressure, Specific_Gravity, Albumin, Sugar, Red_Blood_Cells, Pus_Cell, Pus_Cell_Clumps, Bacteria, Blood_Glucose_Random, Blood_Urea, Serum_Creatinine, Sodium, Potassium, Hemoglobin, Packed_Cell_Volume, White_Blood_Cell_Count, Red_Blood_Cell_Count, Hypertension, Diabetes_Mellitus, Coronary_Artery_Disease, Appetite, Pedal_Edema, Anemia]])
        
    if (kidney_prediction[0] == 1):
      kidney_diagnosis = 'Positive'
        
    else:
        kidney_diagnosis = 'Negative'
        
    st.success(kidney_diagnosis)
        
        
        
        
    
    
    
    
    
    
    
    