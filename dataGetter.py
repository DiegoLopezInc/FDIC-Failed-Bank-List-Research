'''
This script downloads the data from the FDIC website and saves it as a CSV file.
Source of data: https://catalog.data.gov/dataset/fdic-failed-bank-list
'''
# from urllib.request import urlretrieve
import requests

url = "https://www.fdic.gov/bank/individual/failed/banklist.csv"

# Send a GET request to download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Save the content as a CSV file
  with open("bank_failures.csv", "wb") as f:
    f.write(response.content)
  print("Data downloaded successfully!")
else:
  print(f"Failed to download data. Error code: {response.status_code}")
