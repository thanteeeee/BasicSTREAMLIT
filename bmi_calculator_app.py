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

st.title('Welcome to Datafame BMI Calculator')

weight = st.number_input("Enter your weight (in kgs)")

status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

bmi = None

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
    if bmi is not None and weight > 0:
        st.text("Your BMI Index is {:.2f}.".format(bmi))
        category = ""
        if bmi < 16:
            st.error("You are Extremely Underweight")
            category = "Extremely Underweight"
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
            category = "Healthy"
        elif 25 <= bmi < 30:
            st.warning("Overweight")
            category = "Overweight"
        elif bmi >= 30:
            st.error("Extremely Overweight")
            category = "Extremely Overweight"
        

        new_row = pd.DataFrame({
            "Weight": [weight],
            "Height": [height],
            "Unit": [status],
            "BMI": [round(bmi, 2)],
            "Category": [category]
        })
        st.session_state.bmi_data = pd.concat(
            [st.session_state.bmi_data, new_row], ignore_index=True
        )
    else:
        st.error("Please enter valid weight and height to calculate BMI.")


if "bmi_data" not in st.session_state:
    st.session_state.bmi_data = pd.DataFrame(
        columns=["Weight", "Height", "Unit", "BMI", "Category"]
)


st.dataframe(st.session_state.bmi_data, width=700, height=400,hide_index=True)