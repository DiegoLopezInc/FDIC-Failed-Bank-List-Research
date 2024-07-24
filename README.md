# FDIC-Failed-Bank-List-Research

## Overview
This project analyzes the FDIC Failed Bank List to investigate potential correlations between bank failures and economic indicators.

## Setup and Installation
1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Data Source
The data is sourced from the FDIC Failed Bank List, available at: https://catalog.data.gov/dataset/fdic-failed-bank-list

## Project Structure
- `app.py`: Main Streamlit application
- `dataCleaner.py`: Data cleaning and processing functions
- `dataGetter.py`: Script to download the latest data
- `bank_failures.csv`: Raw data file

## Future Work
- Implement hypothesis testing to validate the correlation between bank failures and economic indicators
- Add more advanced visualizations and analysis
- Integrate real-time data updates

## Contributors
Diego Lopez

## License
[Still need to choose an appropriate license for this project]