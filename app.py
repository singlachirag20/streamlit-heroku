import numpy as np
import streamlit as st
import pandas as pd

st.write("""
# Maximum Number Finder App

This app finds the maximum number from the given input
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    firstNumber = st.number_input("First No")
    secondNumber = st.number_input("Second No")
    thirdNumber = st.number_input("Third No")

    inputData = {'firstNumber': firstNumber,
            'secondNumber': secondNumber,
            'thirdNumber': thirdNumber
            }
    features = pd.DataFrame(inputData, index = [0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Processing
st.subheader('Result')

if ((df['firstNumber'] > df['secondNumber']) & (df['firstNumber'] > df['thirdNumber'])):
    st.write(df['firstNumber'] +' is the greatest number.')
elif ((df['secondNumber'] > df['firstNumber']) & (df['secondNumber'] > df['thirdNumber'])):
    st.write(df['secondNumber'] +' is the greatest number.')
else:
    st.write(df['thirdNumber'] +' is the greatest number.')
