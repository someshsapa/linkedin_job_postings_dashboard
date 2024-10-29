import streamlit as st
from data_loader import load_data
from data_cleaning import clean_data
from visualizations import create_visualizations
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    st.title("Job Postings Dashboard")
    
    # Load and clean data
    logging.info("Loading data...")
    data = load_data()
    
    logging.info("Cleaning data...")
    cleaned_data = clean_data(data)

    # Filters
    st.sidebar.header("Filters")
    selected_state = st.sidebar.selectbox("Select State:", options=['All'] + sorted(cleaned_data['state'].dropna().unique().tolist()))
    selected_exp_level = st.sidebar.multiselect("Select Experience Level:", options=['All'] + sorted(cleaned_data['formatted_experience_level'].dropna().unique().tolist()))

    # Apply filters to data
    filtered_data = data.copy()
    # deal with outliers
    filtered_data = filtered_data[filtered_data.normalized_salary < 1000000]
    if selected_state != 'All':
        filtered_data = filtered_data[filtered_data['state'] == selected_state]
    if selected_exp_level and 'All' not in selected_exp_level:
        filtered_data = filtered_data[filtered_data['formatted_experience_level'].isin(selected_exp_level)]

    # Create visualizations
    logging.info("Creating visualizations...")
    create_visualizations(filtered_data)

if __name__ == "__main__":
    main()
