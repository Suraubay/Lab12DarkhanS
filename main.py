import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('car_data.csv')

# Sidebar options
st.sidebar.header("Filter options")
car_name = st.sidebar.text_input("Car name")
transmission = st.sidebar.multiselect("Transmission", options=['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider("Selling price range", 0, 20, (0, 20))
year_range = st.sidebar.slider("Year range", 2000, 2024, (2000, 2024))
submit = st.sidebar.button("Submit")

# Filtering the data
if submit:
    filtered_data = df[df['Selling_Price'].between(*selling_price_range) & df['Year'].between(*year_range)]
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False)]
    if transmission:
        filtered_data = filtered_data[df['Transmission'].isin(transmission)]
    st.write(filtered_data)
else:
    st.write(df)