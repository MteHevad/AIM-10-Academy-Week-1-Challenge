import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure nltk dependencies are downloaded
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load news dataset (assuming news_data is already loaded)
news_data = pd.read_csv('C:/raw_analyst_ratings.csv')

# Convert news date to datetime and extract the date part
news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')
news_data['date'] = news_data['date'].dt.date

# Perform sentiment analysis on the news headlines
news_data['sentiment_score'] = news_data['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Classify sentiment into categories (Positive, Neutral, Negative)
news_data['sentiment_label'] = news_data['sentiment_score'].apply(lambda x: 'Positive' if x > 0 else ('Neutral' if x == 0 else 'Negative'))

# Compute the average daily sentiment scores by grouping by the date
average_daily_sentiment = news_data.groupby('date')['sentiment_score'].mean().reset_index()

# Display the aggregated daily sentiment scores
print("Average Daily Sentiment Scores:")
print(average_daily_sentiment.head())

# Save the aggregated daily sentiment scores to an Excel file
output_file = 'C:/yfinance_data/outputs/average_daily_sentiment_scores.xlsx'
average_daily_sentiment.to_excel(output_file, index=False)

print(f"Saved average daily sentiment scores to {output_file}")
