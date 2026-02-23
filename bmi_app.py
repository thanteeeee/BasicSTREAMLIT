import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.markdown("""
<style>
body {
    background-color: #f8f9fa;
    font-family: "Prompt", sans-serif;
}
</style>
""", unsafe_allow_html=True)


# Give a title to the app
st.title('Welcome to BMI Calculator')

# Take weight input in kgs
weight = st.number_input("Enter your weight (in kgs)")

# Radio button to choose height format
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

# Initialize bmi variable
bmi = None

# Compare status value to take the appropriate height input
if status == 'cms':
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height / 100) ** 2)
    except ZeroDivisionError:
        st.text("Enter a valid value for height")
elif status == 'meters':
    height = st.number_input('Meters')
    try:
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        st.text("Enter a valid value for height")
else:
    height = st.number_input('Feet')
    try:
        bmi = weight / ((height / 3.28) ** 2)
    except ZeroDivisionError:
        st.text("Enter a valid value for height")

# Check if the 'Calculate BMI' button is pressed
if st.button('Calculate BMI'):
    if bmi is not None:
        st.text("Your BMI Index is {:.2f}.".format(bmi))
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        elif bmi >= 30:
            st.error("Extremely Overweight")
    else:
        st.error("Please enter valid weight and height to calculate BMI.")