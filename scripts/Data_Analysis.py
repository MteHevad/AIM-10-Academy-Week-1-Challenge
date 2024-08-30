import pandas as pd
import os

# Set the folder path containing the CSV files
folder_path = r"C:\yfinance_data"

# List of company files
company_files = [
    "AAPL_historical_data.csv", 
    "AMZN_historical_data.csv", 
    "GOOG_historical_data.csv", 
    "META_historical_data.csv", 
    "MSFT_historical_data.csv", 
    "NVDA_historical_data.csv", 
    "TSLA_historical_data.csv"
]

# Dictionary to hold each company's DataFrame
company_data = {}

# Iterate over all CSV files in the folder and load them separately
for file_name in company_files:
    file_path = os.path.join(folder_path, file_name)
    company_name = file_name.split('_')[0]  # Extract company name from file name
    df_temp = pd.read_csv(file_path, parse_dates=['Date'])  # Ensure date is parsed correctly
    company_data[company_name] = df_temp
    print(f"Loaded data for {company_name}")

# Check loaded data for each company
for company, df in company_data.items():
    print(f"\nData for {company}:")
    print(df.head())
