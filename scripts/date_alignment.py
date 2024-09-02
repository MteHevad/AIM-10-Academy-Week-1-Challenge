import pandas as pd
from datetime import datetime

# Load news dataset
news_data = pd.read_csv('C:/raw_analyst_ratings.csv')

# Convert news date to datetime
news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')
news_data['date'] = news_data['date'].dt.date

# Load stock datasets
stock_files = {
    'AAPL': 'C:/yfinance_data/AAPL_historical_data.csv',
    'AMZN': 'C:/yfinance_data/AMZN_historical_data.csv',
    'GOOG': 'C:/yfinance_data/GOOG_historical_data.csv',
    'META': 'C:/yfinance_data/META_historical_data.csv',
    'MSFT': 'C:/yfinance_data/MSFT_historical_data.csv',
    'NVDA': 'C:/yfinance_data/NVDA_historical_data.csv',
    'TSLA': 'C:/yfinance_data/TSLA_historical_data.csv'
}

# Dictionary to store stock dataframes
stock_data = {}

# Normalize timestamps in stock data
for stock, path in stock_files.items():
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Date'] = df['Date'].dt.date
    stock_data[stock] = df

# Align dates between news and stock datasets
aligned_data = {}
for stock, df in stock_data.items():
    merged_df = pd.merge(news_data, df, left_on='date', right_on='Date', how='inner')
    aligned_data[stock] = merged_df
