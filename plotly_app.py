import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.header("Data Visulization using Streamlit and Plotly👏")
st.write("Display Sport Car")

data = pd.read_csv("Sport_car_price.csv")

# change data type of columns
data['Car Make'] = data['Car Make'].astype(str)
data['Car Model'] = data['Car Model'].astype(str)
data['Year'] = data['Year'].astype(str)
data['Engine Size (L)'] = data['Engine Size (L)'].astype(str)
data['Horsepower'] = data['Horsepower'].astype(str)
data['Torque (lb-ft)'] = data['Torque (lb-ft)'].astype(str)
data['0-60 MPH Time (seconds)'] = data['0-60 MPH Time (seconds)'].astype(str)

data['Price (in USD)'] = data['Price (in USD)'].str.replace(',','').astype(int)# converting to int


# Plotting the bar chart for Car Make
car_make_counts = data['Car Make'].value_counts().reset_index()
car_make_counts.columns = ['Car Make', 'Count']

# Plotting the bar chart
fig = px.bar(car_make_counts,
             x='Car Make',
             y='Count',
             title='Count of Cars by Car Make',
             text='Count',  # Display count on top of each bar
             color='Car Make',  # Automatically assign colors based on 'Car Make'
             color_discrete_sequence=px.colors.qualitative.Dark24  # Choose a color palette
            )

# Plot!
st.plotly_chart(fig, width='stretch')