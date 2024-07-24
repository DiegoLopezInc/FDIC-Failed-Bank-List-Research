import pandas as pd
from collections import defaultdict

"""
Reads a CSV file into a hash table.

  Args:
    file_path: Path to the CSV file.

  Returns:
    A hash table (defaultdict) containing the CSV data.
  """
def read_csv_to_hashtable(file_path):
    try:
        df = pd.read_csv(file_path)
        hashtable = defaultdict(list)

        for _, row in df.iterrows():
            for col, value in row.items():
                hashtable[col].append(value)

        return hashtable
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

# Example usage:
file_path = "bank_failures.csv"
data_hashtable = read_csv_to_hashtable(file_path)
print(data_hashtable)