import matplotlib.pyplot as plt
import seaborn as sns

# Merge sentiment scores with stock returns for correlation analysis
correlation_results = {}
for stock, df in aligned_data.items():
    # Calculate correlation between sentiment score and stock return
    correlation = df['sentiment_score'].corr(df['Daily_Return'])
    correlation_results[stock] = correlation

    # Plot correlation
    sns.regplot(x='sentiment_score', y='Daily_Return', data=df)
    plt.title(f'Correlation between News Sentiment and {stock} Stock Returns')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Daily Stock Return')
    plt.show()

# Display correlation results
print("Correlation between news sentiment and stock returns:")
for stock, correlation in correlation_results.items():
    print(f"{stock}: {correlation:.2f}")
