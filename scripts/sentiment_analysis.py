import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure nltk dependencies are downloaded
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Calculate sentiment scores
news_data['sentiment_score'] = news_data['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Classify sentiment into categories
news_data['sentiment_label'] = news_data['sentiment_score'].apply(lambda x: 'Positive' if x > 0 else ('Neutral' if x == 0 else 'Negative'))

# Display sentiment analysis result
print(news_data[['headline', 'sentiment_score', 'sentiment_label']].head())
