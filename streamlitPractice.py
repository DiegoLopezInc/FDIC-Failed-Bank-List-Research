"""
# This file used to demo data from dataCleaner.py to create a DataFrame and visualize it
"""

import streamlit as st
import pandas as pd
from dataCleaner import read_csv_to_hashtable

#TODO: Modify to use the read_csv_to_hashtable function from dataCleaner.py
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df