import streamlit as st
import pandas as pd
import dataCleaner as dc

def main():
    st.title("FDIC Failed Bank List Analysis")
    file_path = "./bank_failures.csv"
    
    data_hashtable = dc.read_csv_to_hashtable(file_path)
    
    if data_hashtable:
        df = pd.DataFrame(data_hashtable)
        
        st.subheader("Sample Data")
        st.write(df.head())
        
        st.subheader("Data Statistics")
        st.write(df.describe())
        
        st.subheader("Bank Failures Over Time")
        st.line_chart(df['Closing Date'].value_counts().sort_index())
        
        # Add more analysis and visualizations here
    else:
        st.error("Failed to load data. Please check the file path and try again.")

if __name__ == "__main__":
    main()