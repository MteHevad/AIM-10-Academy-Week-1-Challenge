# Calculate daily stock returns for each stock
for stock, df in stock_data.items():
    df['Daily_Return'] = df['Close'].pct_change()  # Calculate daily percentage change in closing price
    stock_data[stock] = df
