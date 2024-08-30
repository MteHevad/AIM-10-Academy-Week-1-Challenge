import talib

# Function to apply TA-Lib indicators to each company's data
def apply_ta_indicators(df):
    # Calculate moving averages
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    
    # Calculate RSI (Relative Strength Index)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    
    # Calculate MACD (Moving Average Convergence Divergence)
    macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist
    
    return df

# Apply the function to each company's data
for company, df in company_data.items():
    company_data[company] = apply_ta_indicators(df)
    print(f"Applied TA-Lib indicators for {company}.")
