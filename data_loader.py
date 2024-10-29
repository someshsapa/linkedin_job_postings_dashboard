import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load job postings data from a CSV file."""
    return pd.read_csv('data/postings.csv')
