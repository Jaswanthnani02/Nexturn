import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and company logo
st.set_page_config(
    page_title="Interactive Company App",
    page_icon=":rocket:",
    layout="wide"
)

# Company logo
st.image("LOGO.png", use_container_width=True)

# Add a title and description
st.title("Welcome to Your Interactive Company App!")
st.write("Explore different cases and visualize data interactively.")

# Dropdown for selecting cases
selected_case = st.selectbox("Select a Case:", ["Case One", "Case Two", "Case Three"])

# Display specific content based on the selected case
if selected_case == "Case One":
    st.header("Case One Details")
    st.write("Details about Case One goes here.")
elif selected_case == "Case Two":
    st.header("Case Two Details")
    st.write("Details about Case Two goes here.")
else:
    st.header("Case Three Details")
    st.write("Details about Case Three goes here.")

# Interactive chart based on user input
st.header("Interactive Chart")
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [st.slider('A', 1, 100, 25),
               st.slider('B', 1, 100, 50),
               st.slider('C', 1, 100, 75),
               st.slider('D', 1, 100, 10)]
})
fig = px.bar(data, x='Category', y='Values', text='Values', title='Interactive Bar Chart')
st.plotly_chart(fig)

# Add a fun fact
st.sidebar.header("Fun Fact")
st.sidebar.write("Did you know? Streamlit is an amazing tool for creating interactive web applications with Python!")

# Footer
st.markdown("---")
st.write("© 2023 Your Company. All rights reserved.")

