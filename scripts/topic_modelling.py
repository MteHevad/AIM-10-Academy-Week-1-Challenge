import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate SMA
def calculate_sma(data, window):
    return data.rolling(window=window).mean()

# Function to calculate RSI
def calculate_rsi(data, window=14):
    delta = data.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Function to calculate MACD
def calculate_macd(data, slow=26, fast=12, signal=9):
    exp1 = data.ewm(span=fast, adjust=False).mean()
    exp2 = data.ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

# List of stock file names
stock_files = [
    "AAPL_historical_data.csv", 
    "AMZN_historical_data.csv", 
    "GOOG_historical_data.csv", 
    "META_historical_data.csv", 
    "MSFT_historical_data.csv", 
    "NVDA_historical_data.csv", 
    "TSLA_historical_data.csv"
]

# File path
file_path = r"C:\yfinance_data"

# Loop through each stock file
for stock_file in stock_files:
    # Load the data
    full_path = os.path.join(file_path, stock_file)
    data = pd.read_csv(full_path, parse_dates=True, index_col='Date')
    
    # Calculate indicators
    data['SMA20'] = calculate_sma(data['Close'], 20)
    data['RSI'] = calculate_rsi(data['Close'])
    data['MACD'], data['Signal'] = calculate_macd(data['Close'])

    # Plotting
    plt.figure(figsize=(14, 10))
    
    # Plot the stock prices and SMA20
    plt.subplot(3, 1, 1)
    plt.plot(data.index, data['Close'], label='Close Price', color='black')
    plt.plot(data.index, data['SMA20'], label='SMA20', color='blue')
    plt.title(f"{stock_file.split('_')[0]} Stock Price with SMA20")
    plt.legend()
    
    # Plot the RSI
    plt.subplot(3, 1, 2)
    plt.plot(data.index, data['RSI'], label='RSI', color='green')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='blue')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()
    
    # Plot the MACD and Signal Line
    plt.subplot(3, 1, 3)
    plt.plot(data.index, data['MACD'], label='MACD', color='purple')
    plt.plot(data.index, data['Signal'], label='Signal Line', color='orange')
    plt.title('MACD and Signal Line')
    plt.legend()
    
    # Display the plots
    plt.tight_layout()
    plt.show()
