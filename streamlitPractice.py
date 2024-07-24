"""
# This file used to demo data from dataCleaner.py to create a DataFrame and visualize it
"""

import streamlit as st
import pandas as pd
from dataCleaner import read_csv_to_hashtable

st.title("FDIC Failed Bank List Analysis")

file_path = "bank_failures.csv"
data_hashtable = read_csv_to_hashtable(file_path)

if data_hashtable:
    st.write("Data successfully loaded!")
    
    # Convert hashtable to DataFrame
    df = pd.DataFrame(data_hashtable)
    
    # Display the first few rows of the data
    st.subheader("Sample Data")
    st.write(df.head())
    
    # Display some basic statistics
    st.subheader("Data Statistics")
    st.write(df.describe())
    
    # Create a simple visualization
    st.subheader("Bank Failures Over Time")
    st.line_chart(df['Closing Date'].value_counts().sort_index())
else:
    st.error("Failed to load data. Please check the file path and try again.")