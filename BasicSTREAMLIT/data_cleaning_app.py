import numpy as np
import pandas as pd
import streamlit as st

# สร้างหัวข้อ
st.title('Data Cleaning with Streamlit')

# สร้าง DataFrame ตัวอย่าง
st.header('Raw Data')

raw_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan, 'Frank'],
    'Age': [25, 30, 35, 38, 45, 50],
    'Gender': ['F', 'M', np.nan, 'M', 'F', 'M'],
    'Score': [85, 90, 60, 75, 95, 88]
})

# Convert 'Score' and 'Age' columns from str to int
raw_data['Score'] = raw_data['Score'].astype(int)
raw_data['Age'] = raw_data['Age'].astype(int)

# Display the DataFrame with color formatting
st.header('Cleaned Data with Styling')

# Apply conditional formatting
def highlight_missing(s):
    return ['background-color: yellow' if pd.isnull(v) else '' for v in s]

#styled_data = raw_data.style.apply(highlight_missing, subset=['Name', 'Gender'])
raw_data.index = raw_data.index + 1
# Set width and height of the dataframe
st.dataframe(raw_data, width=700, height=400,hide_index=True)

# Create a line chart
st.line_chart(raw_data[['Score', 'Age']].set_index('Score'))
