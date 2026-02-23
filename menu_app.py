

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Header for the app
st.header("Data Visualization using Streamlit and Plotly👏")
st.subheader("Display Sport Car Data", divider="gray")

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

# Convert 'Price (in USD)' to int after removing commas
data['Price (in USD)'] = data['Price (in USD)'].str.replace(',','').astype(int)


# ----------- Dynamic Navigation Menu -----------
menu = st.sidebar.selectbox(
    'Navigation to Preview Data',
    ['View All Sport Car Price Data', 'Display Cars Price in Years']
)

# ----------- Page 1: Show All Data (DataFrame) -----------
if menu == 'View All Sport Car Price Data':
    st.header("View All Sport Car Price Data")
    st.dataframe(data, width = 800,height = 600)

elif menu == 'Display Cars Price in Years':
# Add a year filter using st.multiselect
    selected_years = st.multiselect(
        'Select Year(s) to Filter',
        options=data['Year'].unique(),
        default=data['Year'].unique()  # Default is all years selected
    )

    # Filter the data by the selected years
    filtered_data = data[data['Year'].isin(selected_years)]

    # ----------------- First Plot: Bar Chart for Car Make -----------------------
    # Count the number of cars by 'Car Make' for the filtered data
    car_make_counts = filtered_data['Car Make'].value_counts().reset_index()
    car_make_counts.columns = ['Car Make', 'Count']

    # Plotting the bar chart for car makes
    fig_bar = px.bar(car_make_counts,
                    x='Car Make',
                    y='Count',
                    title=f'Count of Cars by Car Make for Year(s): {", ".join(selected_years)}',
                    text='Count',
                    color='Car Make',
                    color_discrete_sequence=px.colors.qualitative.Vivid_r
                    )

    # Display the bar chart
    st.plotly_chart(fig_bar, use_container_width=True)

    # ----------------- Second Plot: Line Chart for Most Expensive Cars -----------------------
    # Filter dataset for cars from multiselect

    cars = data[data['Year'].isin(selected_years)]

        # Drop duplicates based on 'Car Model' and 'Price (in USD)'
    cars_unique = cars.drop_duplicates(subset=['Car Model', 'Price (in USD)'])

        # Sort the data by price in descending order and select the top 10 most expensive car models
    top_expensive_cars_unique = cars_unique.sort_values(by='Price (in USD)', ascending=False).head(10)

        # Create the bar chart for the top 10 most expensive cars
    fig_top10 = px.bar(top_expensive_cars_unique,
                        x='Car Model',
                        y='Price (in USD)',
                        title=f'Top 10 Most Expensive Car Models in Year(s): {", ".join(selected_years)}',
                        text='Price (in USD)',
                        color='Car Model',
                        hover_data={'Price (in USD)': ':,.2f'},  # Custom format for hover data
                        color_discrete_sequence=px.colors.qualitative.Vivid_r
                        )

        # Update the text template to format the text to two decimal places
    fig_top10.update_traces(texttemplate='%{text:,.2f}', textposition='outside')

    # Display the bar chart for the top 10 most expensive cars
    st.plotly_chart(fig_top10, width='stretch')