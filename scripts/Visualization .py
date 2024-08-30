import matplotlib.pyplot as plt

# Function to visualize data for each company
def visualize_data(df, company):
    # Plot stock price and moving averages
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['SMA_20'], label='20-Day SMA')
    plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA')
    plt.title(f'{company}: Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14, 5))
    plt.plot(df['Date'], df['RSI'], label='RSI')
    plt.title(f'{company}: Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.legend()
    plt.show()

    # Plot MACD
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['MACD'], label='MACD')
    plt.plot(df['Date'], df['MACD_Signal'], label='MACD Signal')
    plt.bar(df['Date'], df['MACD_Hist'], label='MACD Histogram', color='gray', alpha=0.5)
    plt.title(f'{company}: MACD and MACD Signal')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

# Visualize data for each company
for company, df in company_data.items():
    print(f"\nVisualizing data for {company}:")
    visualize_data(df, company)
