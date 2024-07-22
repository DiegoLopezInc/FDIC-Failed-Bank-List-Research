import numpy as np
import pandas as pd
import streamlit as sl
import dataCleaner as dc

def main():
    sl.title("Data Cleaner")
    file_path = "./bank_failures.csv"
    data_hashtable = dc.read_csv_to_hashtable(file_path)
    sl.write(data_hashtable)
    
    sl.print(data_hashtable)
    
    # Display the data as a DataFrame
    # df = pd.DataFrame(data_hashtable)
    # sl.write(df)
    

