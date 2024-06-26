import streamlit as st
import pandas as pd
from main import main

# Initialize the models
models = main()

# Streamlit app
st.title("Content-Based Recommendation System")

# User inputs
st.sidebar.header("User Input Features")
model_choice = st.sidebar.selectbox("Choose Recommendation Model", list(models.keys()))
item_id = st.sidebar.number_input("Enter Item ID", min_value=1, max_value=len(models[model_choice].data), step=1, value=1)
num_recommendations = st.sidebar.slider("Number of Recommendations", min_value=1, max_value=10, value=5)

# Get recommendations
recommendations = models[model_choice].get_recommendations(item_id, num_recommendations)

st.write(f"Recommendations for Item ID {item_id} using {model_choice} model:")
st.write(recommendations[['SHIP_ID', 'SHIP_NAME', 'VOYAGE_NAME', 'PORT_FROM', 'PORT_TO', 'MEDIAN_PRICE']])
