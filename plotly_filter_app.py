import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


# Header for the app
st.header("Data Visualization using Streamlit and Plotly")
st.write("Display Sport Car")

# Read data from the CSV file
data = pd.read_csv("Sport_car_price.csv")

# Change data type of columns
data['Car Make'] = data['Car Make'].astype(str)
data['Car Model'] = data['Car Model'].astype(str)
data['Year'] = data['Year'].astype(str)  # Keep 'Year' as string for filtering purposes
data['Engine Size (L)'] = data['Engine Size (L)'].astype(str)
data['Horsepower'] = data['Horsepower'].astype(str)
data['Torque (lb-ft)'] = data['Torque (lb-ft)'].astype(str)
data['0-60 MPH Time (seconds)'] = data['0-60 MPH Time (seconds)'].astype(str)

data['Price (in USD)'] = data['Price (in USD)'].str.replace(',','').astype(int)  # Convert to int

# Add a year filter
selected_years = st.multiselect(
    'Select Year(s) to Filter',  # Label for the filter
    options=data['Year'].unique(),  # Unique year options from the data
    default=data['Year'].unique()  # Default is all years selected
)

# Filter the data by the selected years
filtered_data = data[data['Year'].isin(selected_years)]

# Count the number of cars by 'Car Make' for the filtered data
car_make_counts = filtered_data['Car Make'].value_counts().reset_index()
car_make_counts.columns = ['Car Make', 'Count']

# Plotting the bar chart
fig = px.bar(car_make_counts,
             x='Car Make',
             y='Count',
             title=f'Count of Cars by Car Make for Year(s): {", ".join(selected_years)}',
             text='Count',  # Display count on top of each bar
             color='Car Make',  # Automatically assign colors based on 'Car Make'
             color_discrete_sequence=px.colors.qualitative.Dark24  # Choose a color palette
            )

# Display the plot
st.plotly_chart(fig, width='stretch')
